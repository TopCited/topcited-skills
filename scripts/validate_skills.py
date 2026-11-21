#!/usr/bin/env python3
"""Validate every skill in skills/ and every relative link between them.

Checks, per skill:
  - skills/<dir>/SKILL.md exists
  - frontmatter parses, has `name` and `description`
  - `name` matches the directory name and is lowercase-kebab
  - `description` is non-empty and under 1024 characters

Then, repo-wide: every relative markdown link resolves to a file that exists,
and the two marketplace files and plugin.json agree.

No third-party dependencies, so it runs anywhere python3 does.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
PLUGIN_DIR = ROOT / ".claude-plugin"
# What url-marketplace.json installs: this repo's main branch as a zip, so no Git is needed.
ARCHIVE_SOURCE = {
    "source": "archive",
    "url": "https://github.com/TopCited/topcited-skills/archive/refs/heads/main.zip",
}
EXPECTED_SKILLS = {"seo-geo", "topcited-api", "visibility-workflow"}

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
# Markdown links that are relative paths (not http(s):, mailto:, or #anchors).
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")

errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def parse_frontmatter(text: str, path: Path) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        fail(f"{path}: no YAML frontmatter (file must start with '---')")
        return None
    end = text.find("\n---\n", 3)
    if end == -1:
        fail(f"{path}: frontmatter is not terminated by '---'")
        return None
    block, out, key = text[4:end], {}, None
    for line in block.splitlines():
        if not line.strip():
            continue
        if line.startswith((" ", "\t")) and key:  # folded continuation
            out[key] += " " + line.strip()
            continue
        if ":" not in line:
            fail(f"{path}: cannot parse frontmatter line {line!r}")
            return None
        key, value = line.split(":", 1)
        key = key.strip()
        out[key] = value.strip()
    return out


def check_skill(skill_dir: Path) -> None:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        fail(f"{skill_dir}: missing SKILL.md")
        return
    fm = parse_frontmatter(skill_md.read_text(encoding="utf-8"), skill_md)
    if fm is None:
        return
    name = fm.get("name", "")
    desc = fm.get("description", "")
    if not name:
        fail(f"{skill_md}: frontmatter has no `name`")
    elif name != skill_dir.name:
        fail(f"{skill_md}: name {name!r} != directory {skill_dir.name!r}")
    elif not NAME_RE.match(name):
        fail(f"{skill_md}: name {name!r} is not lowercase-kebab-case")
    if not desc:
        fail(f"{skill_md}: frontmatter has no `description`")
    elif len(desc) > 1024:
        fail(f"{skill_md}: description is {len(desc)} chars (max 1024)")


def check_links() -> None:
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts:
            continue
        for target in LINK_RE.findall(md.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path = target.split("#", 1)[0]
            if not path:
                continue
            if not (md.parent / path).resolve().exists():
                fail(f"{md.relative_to(ROOT)}: broken relative link -> {target}")


def check_marketplaces() -> None:
    """url-marketplace.json is marketplace.json for installs by URL (Claude Code downloads
    the plugin as a zip instead of cloning the repo). Apart from each plugin's source the
    two must match, and their versions must match plugin.json."""
    try:
        repo, by_url, plugin = (
            json.loads((PLUGIN_DIR / name).read_text(encoding="utf-8"))
            for name in ("marketplace.json", "url-marketplace.json", "plugin.json")
        )
    except (OSError, ValueError) as e:
        fail(f".claude-plugin: {e}")
        return

    def without_sources(m: dict) -> dict:
        return {**m, "plugins": [{k: v for k, v in p.items() if k != "source"} for p in m.get("plugins", [])]}

    if without_sources(repo) != without_sources(by_url):
        fail(".claude-plugin/url-marketplace.json differs from marketplace.json in more than the plugin source")
    for p in by_url.get("plugins", []):
        if p.get("source") != ARCHIVE_SOURCE:
            fail(f".claude-plugin/url-marketplace.json: {p.get('name')!r} must use the source {ARCHIVE_SOURCE}")
    for name, m in (("marketplace.json", repo), ("url-marketplace.json", by_url)):
        for p in m.get("plugins", []):
            if p.get("name") == plugin.get("name") and p.get("version") != plugin.get("version"):
                fail(f".claude-plugin/{name}: version {p.get('version')!r} != plugin.json {plugin.get('version')!r}")


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print("no skills/ directory", file=sys.stderr)
        return 1
    found = {d.name for d in SKILLS_DIR.iterdir() if d.is_dir()}
    if missing := EXPECTED_SKILLS - found:
        fail(f"skills/ is missing expected skill(s): {sorted(missing)}")
    for d in sorted(SKILLS_DIR.iterdir()):
        if d.is_dir():
            check_skill(d)
    check_links()
    check_marketplaces()

    if errors:
        print(f"FAIL — {len(errors)} problem(s):", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    print(f"OK — {len(found)} skills valid, all relative links resolve, marketplaces agree.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
