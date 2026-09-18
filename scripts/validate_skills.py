#!/usr/bin/env python3
"""Validate every skill in skills/ and every relative link between them.

Checks, per skill:
  - skills/<dir>/SKILL.md exists
  - frontmatter parses, has `name` and `description`
  - `name` matches the directory name and is lowercase-kebab
  - `description` is non-empty and under 1024 characters

Then, repo-wide: every relative markdown link resolves to a file that exists.

No third-party dependencies, so it runs anywhere python3 does.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
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

    if errors:
        print(f"FAIL — {len(errors)} problem(s):", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    print(f"OK — {len(found)} skills valid, all relative links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
