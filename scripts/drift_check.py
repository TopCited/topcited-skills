#!/usr/bin/env python3
"""Detect drift between the skills and the real TopCited product.

Three checks, each reported in one deterministic Markdown report:

  (a) spec      — the live public OpenAPI spec vs the committed snapshot
                  (scripts/drift/openapi-public-ops.json), and vs what the
                  topcited-api skill documents: public operations the skill
                  doesn't cover, and operations the skill documents that are
                  neither public nor on the known-internal list.
  (b) cli       — the `## Commands` block of the CLI README (latest release,
                  falling back to the default branch) vs the `topcited …`
                  commands the topcited-api skill mentions.
  (c) freshness — seo-geo knowledge files whose `last-verified` is older than
                  --max-age-days (default 90).

A source that can't be fetched (404, private repo, network) is reported as
"source unavailable" and is not drift. No third-party dependencies.

Exit codes: 0 = ran (drift or not, unless --exit-code); 1 = drift found and
--exit-code given; 2 = usage or internal error.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterable

ROOT = Path(__file__).resolve().parent.parent
DRIFT_DIR = ROOT / "scripts" / "drift"
SNAPSHOT = DRIFT_DIR / "openapi-public-ops.json"
CLI_OPERATIONS = DRIFT_DIR / "cli-operations.json"
INTERNAL_OPS = DRIFT_DIR / "internal-ops.txt"
API_SKILL = ROOT / "skills" / "topcited-api"
KNOWLEDGE = ROOT / "skills" / "seo-geo" / "knowledge"

SPEC_URL = "https://api.topcited.ai/api/v1/openapi.public.json"
CLI_REPO = "TopCited/topcited-cli"
HTTP_METHODS = ("GET", "POST", "PUT", "PATCH", "DELETE")

# An operation is "METHOD /normalized/path", e.g. "POST /brands/{}/keywords:recommend".
Op = str


# ---------------------------------------------------------------- normalizing

PARAM_RE = re.compile(r"\{[^}/]*\}|<[^>/]*>")


def normalize_path(path: str) -> str:
    """Drop the /api/v1 prefix, query string and trailing slash; params -> {}."""
    path = path.split("?", 1)[0].split("#", 1)[0].strip()
    if path.startswith("/api/v1"):
        path = path[len("/api/v1"):]
    path = PARAM_RE.sub("{}", path)
    if len(path) > 1:
        path = path.rstrip("/")
    return path or "/"


def op(method: str, path: str) -> Op:
    return f"{method.upper()} {normalize_path(path)}"


# ------------------------------------------------------------------ (a) spec

def spec_operations(spec: dict) -> dict[Op, str]:
    """{operation: operationId} for every operation in an OpenAPI document."""
    out: dict[Op, str] = {}
    for path, item in spec.get("paths", {}).items():
        for method, detail in item.items():
            if method.upper() in HTTP_METHODS:
                out[op(method, path)] = (detail or {}).get("operationId", "")
    return out


# `GET /brands/<id>/keywords`, `DELETE /monitoring/query-sets/<id>`, …
VERB_PATH_RE = re.compile(r"\b(GET|POST|PUT|PATCH|DELETE)\s+(/[^\s`'\"|,;)]*)")
# `topcited api [flags] /path [flags]` inside one code span or line.
API_CALL_RE = re.compile(r"topcited api\b([^`\n]*)")


def _clean_path(raw: str) -> str | None:
    raw = raw.strip().strip("\"'").rstrip(".:")
    if not raw.startswith("/") or "…" in raw or "..." in raw:
        return None
    return raw


def documented_operations(texts: Iterable[str]) -> set[Op]:
    """Operations the skill text names, as `METHOD /path` or `topcited api …`."""
    found: set[Op] = set()
    for text in texts:
        for method, raw in VERB_PATH_RE.findall(text):
            path = _clean_path(raw)
            if path:
                found.add(op(method, path))
        for args in API_CALL_RE.findall(text):
            tokens = args.split()
            method, path, has_body = None, None, False
            for i, tok in enumerate(tokens):
                if tok in ("-X", "--method") and i + 1 < len(tokens):
                    method = tokens[i + 1].upper()
                elif tok in ("-d", "--data"):
                    has_body = True
                elif path is None:
                    candidate = _clean_path(tok)
                    if candidate:
                        path = candidate
            if path:
                found.add(op(method or ("POST" if has_body else "GET"), path))
    return found


@dataclass
class SpecResult:
    available: bool
    source: str
    added: list[Op] = field(default_factory=list)      # live, not in snapshot
    removed: list[Op] = field(default_factory=list)    # snapshot, not live
    undocumented: list[Op] = field(default_factory=list)  # public, skill silent
    unknown: list[Op] = field(default_factory=list)    # documented, not public/internal
    now_public: list[Op] = field(default_factory=list)  # on internal list, now public

    @property
    def drift(self) -> bool:
        return bool(self.added or self.removed or self.undocumented or self.unknown or self.now_public)


def check_spec(
    live: dict[Op, str] | None,
    snapshot: set[Op],
    documented: set[Op],
    cli_covered: set[Op],
    internal: set[Op],
    source: str,
) -> SpecResult:
    """Compare live spec, snapshot, and skill. With no live spec, use the snapshot."""
    public = set(live) if live is not None else set(snapshot)
    res = SpecResult(available=live is not None, source=source)
    if live is not None:
        res.added = sorted(public - snapshot)
        res.removed = sorted(snapshot - public)
    covered = documented | cli_covered
    res.undocumented = sorted(public - covered)
    res.unknown = sorted(documented - public - internal)
    res.now_public = sorted(internal & public)
    return res


# ------------------------------------------------------------------- (b) cli

FENCE_RE = re.compile(r"```[^\n]*\n(.*?)```", re.S)
CODE_SPAN_RE = re.compile(r"`([^`\n]+)`")
WORD_RE = re.compile(r"^[a-z][a-z-]*$")


def cli_commands_from_readme(readme: str) -> set[str] | None:
    """Commands in the README's `## Commands` fenced block, e.g. 'monitor sets list'."""
    m = re.search(r"^## Commands\s*$(.*?)(?=^## )", readme + "\n## ", re.M | re.S)
    if not m:
        return None
    block = FENCE_RE.search(m.group(1))
    if not block:
        return None
    commands: set[str] = set()
    for line in block.group(1).splitlines():
        line = line.split("#", 1)[0].strip()
        if not line.startswith("topcited "):
            continue
        segments = line[len("topcited "):].split(" | ")
        first = _leading_words(segments[0])
        if not first:
            continue
        commands.add(" ".join(first))
        prefix = first[:-1]
        for seg in segments[1:]:
            words = _leading_words(seg)
            if words:
                commands.add(" ".join(prefix + words[:1]))
    return commands


def _leading_words(segment: str) -> list[str]:
    words: list[str] = []
    for tok in segment.split():
        if not WORD_RE.match(tok):
            break
        words.append(tok)
    return words


def skill_commands(texts: Iterable[str]) -> set[str]:
    """`topcited …` command words used in code spans and fenced blocks."""
    found: set[str] = set()
    for text in texts:
        chunks = FENCE_RE.findall(text) + CODE_SPAN_RE.findall(text)
        for chunk in chunks:
            for m in re.finditer(r"(?<![\w./-])topcited((?:[ \t]+[a-z][a-z-]*)+)", chunk):
                words = m.group(1).split()
                if words:
                    found.add(" ".join(words))
    return found


def resolve(mention: str, commands: set[str]) -> str | None:
    """Longest real command that `mention` starts with ('recommend prompts' -> 'recommend')."""
    words = mention.split()
    for n in range(len(words), 0, -1):
        candidate = " ".join(words[:n])
        if candidate in commands:
            return candidate
    return None


@dataclass
class CliResult:
    available: bool
    source: str
    missing: list[str] = field(default_factory=list)  # CLI has it, skill silent
    stale: list[str] = field(default_factory=list)    # skill uses it, CLI doesn't

    @property
    def drift(self) -> bool:
        return bool(self.missing or self.stale)


def check_cli(commands: set[str] | None, mentions: set[str], source: str) -> CliResult:
    if commands is None:
        return CliResult(available=False, source=source)
    used = {resolve(m, commands) for m in mentions} - {None}
    groups = {" ".join(c.split()[:n]) for c in commands for n in range(1, len(c.split()))}
    stale = {m for m in mentions if resolve(m, commands) is None and m not in groups}
    return CliResult(
        available=True,
        source=source,
        missing=sorted(commands - used),
        stale=sorted(stale),
    )


# ------------------------------------------------------------- (c) freshness

LAST_VERIFIED_RE = re.compile(r"^last-verified:\s*(\S+)\s*$", re.M)


@dataclass
class FreshnessResult:
    max_age_days: int
    stale: list[tuple[str, str, int]] = field(default_factory=list)  # (file, date, age)
    undated: list[str] = field(default_factory=list)

    @property
    def drift(self) -> bool:
        return bool(self.stale or self.undated)


def check_freshness(files: dict[str, str], today: dt.date, max_age_days: int) -> FreshnessResult:
    """`files` maps a repo-relative path to its text."""
    res = FreshnessResult(max_age_days=max_age_days)
    for name in sorted(files):
        m = LAST_VERIFIED_RE.search(files[name].split("\n---\n", 1)[0])
        try:
            verified = dt.date.fromisoformat(m.group(1)) if m else None
        except ValueError:
            verified = None
        if verified is None:
            res.undated.append(name)
            continue
        age = (today - verified).days
        if age > max_age_days:
            res.stale.append((name, verified.isoformat(), age))
    return res


# ---------------------------------------------------------------- fetching

Fetcher = Callable[[str], "tuple[int, bytes]"]


def http_fetch(url: str) -> tuple[int, bytes]:
    """(status, body); status 0 on a network error. Uses GH_TOKEN for GitHub URLs."""
    headers = {"User-Agent": "topcited-skills-drift-check"}
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token and ("api.github.com" in url or "raw.githubusercontent.com" in url):
        headers["Authorization"] = f"Bearer {token}"
    if "api.github.com" in url:
        headers["Accept"] = "application/vnd.github+json"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, b""
    except (urllib.error.URLError, TimeoutError, OSError):
        return 0, b""


def _unavailable(url: str, status: int) -> str:
    why = f"HTTP {status}" if status else "network error"
    return f"source unavailable ({why}): {url}"


def fetch_spec(url: str, fetch: Fetcher) -> tuple[dict | None, str]:
    status, body = fetch(url)
    if status != 200:
        return None, _unavailable(url, status)
    try:
        return json.loads(body), url
    except ValueError:
        return None, f"source unavailable (not JSON): {url}"


def fetch_cli_readme(repo: str, fetch: Fetcher) -> tuple[str | None, str]:
    """README of the latest release, else of the default branch."""
    status, body = fetch(f"https://api.github.com/repos/{repo}/releases/latest")
    ref = None
    if status == 200:
        try:
            ref = json.loads(body).get("tag_name")
        except ValueError:
            ref = None
    attempts = [(ref, f"release {ref}")] if ref else []
    attempts.append(("HEAD", "default branch"))
    last = ""
    for r, label in attempts:
        url = f"https://raw.githubusercontent.com/{repo}/{r}/README.md"
        s, b = fetch(url)
        if s == 200:
            return b.decode("utf-8", "replace"), f"{repo} README ({label})"
        last = _unavailable(url, s)
    return None, last


# ----------------------------------------------------------------- report

def render_report(spec: SpecResult, cli: CliResult, fresh: FreshnessResult, today: dt.date) -> str:
    def bullets(items: Iterable[str]) -> list[str]:
        items = list(items)
        return [f"- `{i}`" for i in items] if items else ["- none"]

    drift = spec.drift or cli.drift or fresh.drift
    lines = [
        "# Skills drift report",
        "",
        f"Checked {today.isoformat()}. **{'Drift found' if drift else 'No drift'}.**",
        "",
        "## (a) Public API spec",
        "",
        f"Source: {spec.source}",
    ]
    if not spec.available:
        lines += ["", "Live spec not checked; coverage below is against the committed snapshot."]
    if spec.available:
        lines += ["", "### New in the live spec (not in the snapshot)", *bullets(spec.added)]
        lines += ["", "### Removed from the live spec (still in the snapshot)", *bullets(spec.removed)]
    lines += ["", "### Public operations the topcited-api skill doesn't cover", *bullets(spec.undocumented)]
    lines += ["", "### Documented in the skill, but neither public nor on the internal list", *bullets(spec.unknown)]
    lines += ["", "### On the internal list, but now public (drop the *internal* label)", *bullets(spec.now_public)]
    lines += ["", "## (b) CLI commands", "", f"Source: {cli.source}"]
    if cli.available:
        lines += ["", "### CLI commands the skill never mentions", *bullets(cli.missing)]
        lines += ["", "### Commands the skill uses that the CLI doesn't have", *bullets(cli.stale)]
    lines += [
        "",
        f"## (c) seo-geo knowledge freshness (older than {fresh.max_age_days} days)",
        "",
    ]
    if fresh.stale:
        lines += [f"- `{n}` — last verified {d} ({a} days)" for n, d, a in fresh.stale]
    if fresh.undated:
        lines += [f"- `{n}` — no valid `last-verified` date" for n in fresh.undated]
    if not (fresh.stale or fresh.undated):
        lines.append("- none")
    lines += [
        "",
        "---",
        "To clear spec drift after review: `python3 scripts/drift_check.py --update-snapshot`,",
        "add any newly internal operations to `scripts/drift/internal-ops.txt`, and update",
        "`scripts/drift/cli-operations.json` when a CLI verb starts using a new operation.",
        "",
    ]
    return "\n".join(lines)


# ------------------------------------------------------------------- main

def read_texts(root: Path) -> list[str]:
    return [p.read_text(encoding="utf-8") for p in sorted(root.rglob("*.md"))]


def load_snapshot() -> set[Op]:
    return {e["op"] for e in json.loads(SNAPSHOT.read_text(encoding="utf-8"))}


def write_snapshot(ops: dict[Op, str]) -> None:
    data = [{"op": o, "operationId": ops[o]} for o in sorted(ops)]
    SNAPSHOT.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def load_cli_covered() -> set[Op]:
    data = json.loads(CLI_OPERATIONS.read_text(encoding="utf-8"))
    return {op(*o.split(" ", 1)) for cmd, ops in data.items() if not cmd.startswith("_") for o in ops}


def load_internal() -> set[Op]:
    out = set()
    for line in INTERNAL_OPS.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            method, path = line.split(None, 1)
            out.add(op(method, path))
    return out


def knowledge_files() -> dict[str, str]:
    out = {}
    for p in sorted(KNOWLEDGE.rglob("*.md")):
        if p.name in ("INDEX.md", "_template.md"):
            continue
        out[str(p.relative_to(ROOT))] = p.read_text(encoding="utf-8")
    return out


def main(argv: list[str] | None = None, fetch: Fetcher = http_fetch) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--spec-url", default=SPEC_URL)
    ap.add_argument("--spec-file", help="read the spec from a file instead of --spec-url")
    ap.add_argument("--cli-repo", default=CLI_REPO)
    ap.add_argument("--cli-readme-file", help="read the CLI README from a file instead of GitHub")
    ap.add_argument("--max-age-days", type=int, default=90)
    ap.add_argument("--today", type=dt.date.fromisoformat, default=dt.datetime.now(dt.timezone.utc).date())
    ap.add_argument("--report", help="write the Markdown report here (default: stdout)")
    ap.add_argument("--github-output", default=os.environ.get("GITHUB_OUTPUT"),
                    help="append drift=true|false here (set automatically in Actions)")
    ap.add_argument("--exit-code", action="store_true", help="exit 1 when drift is found")
    ap.add_argument("--update-snapshot", action="store_true",
                    help="rewrite the committed spec snapshot from the live spec, then exit")
    args = ap.parse_args(argv)

    if args.spec_file:
        live_spec, spec_source = json.loads(Path(args.spec_file).read_text(encoding="utf-8")), args.spec_file
    else:
        live_spec, spec_source = fetch_spec(args.spec_url, fetch)
    live_ops = spec_operations(live_spec) if live_spec is not None else None

    if args.update_snapshot:
        if live_ops is None:
            print(f"error: {spec_source}", file=sys.stderr)
            return 2
        write_snapshot(live_ops)
        print(f"wrote {SNAPSHOT.relative_to(ROOT)} ({len(live_ops)} operations)")
        return 0

    skill_texts = read_texts(API_SKILL)
    spec = check_spec(live_ops, load_snapshot(), documented_operations(skill_texts),
                      load_cli_covered(), load_internal(), spec_source)

    if args.cli_readme_file:
        readme, cli_source = Path(args.cli_readme_file).read_text(encoding="utf-8"), args.cli_readme_file
    else:
        readme, cli_source = fetch_cli_readme(args.cli_repo, fetch)
    commands = cli_commands_from_readme(readme) if readme is not None else None
    if readme is not None and commands is None:
        cli_source = f"source unavailable (no `## Commands` block): {cli_source}"
    cli = check_cli(commands, skill_commands(skill_texts), cli_source)

    fresh = check_freshness(knowledge_files(), args.today, args.max_age_days)

    report = render_report(spec, cli, fresh, args.today)
    drift = spec.drift or cli.drift or fresh.drift
    if args.report:
        Path(args.report).write_text(report, encoding="utf-8")
    else:
        sys.stdout.write(report)
    if args.github_output:
        with open(args.github_output, "a", encoding="utf-8") as fh:
            fh.write(f"drift={'true' if drift else 'false'}\n")
    print(f"drift={'true' if drift else 'false'}", file=sys.stderr)
    return 1 if (drift and args.exit_code) else 0


if __name__ == "__main__":
    sys.exit(main())
