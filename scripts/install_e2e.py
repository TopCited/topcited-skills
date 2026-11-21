#!/usr/bin/env python3
"""Run the README's install steps, exactly as written, on a machine without Git.

On Windows the CI workflow deletes Git before this runs. On macOS and Linux this script
runs every command with a PATH that holds everything except Git. It then checks that:

  - the old `/plugin marketplace add TopCited/topcited-skills` route fails, which proves
    Git is out of reach;
  - the README's Claude Code steps install the plugin with all three skills;
  - the README's download steps (sh; on Windows, Windows PowerShell and PowerShell 7)
    put all three skills in ~/.agents/skills, also when run a second time, and Codex
    lists them;
  - the README's CLI install gives a working `topcited`.

macOS / Linux: every step gets a throwaway HOME, so your own settings are untouched.
Windows: Claude Code, Codex and PowerShell read the real user profile, so this only
runs when CI is set.

  MARKETPLACE_URL=<url>  install from this marketplace file instead of the README's URL
                         (a pull request tests its own url-marketplace.json)
"""

from __future__ import annotations

import base64
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIN = os.name == "nt"
SKILLS = ("seo-geo", "topcited-api", "visibility-workflow")
README_MARKETPLACE_URL = "https://topcited.ai/claude-plugins.json"
PLUGIN = "topcited-skills@topcited"


def readme_block(what: str, match) -> str:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    found = [body for lang, body in re.findall(r"^```(\w*)\n(.*?)^```", text, re.M | re.S) if match(lang, body)]
    if len(found) != 1:
        sys.exit(f"README.md: expected one {what} block, found {len(found)}")
    return found[0]


def run(args: list[str], env: dict, what: str, expect_ok: bool = True) -> subprocess.CompletedProcess:
    r = subprocess.run(args, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300)
    if expect_ok and r.returncode != 0:
        sys.exit(f"FAIL {what} (exit {r.returncode}):\n{r.stdout}{r.stderr}")
    if not expect_ok and r.returncode == 0:
        sys.exit(f"FAIL {what}: expected a failure but it worked:\n{r.stdout}{r.stderr}")
    return r


def no_git_path(tmp: Path) -> str:
    """A PATH holding every program on the current PATH except Git's."""
    bin_dir = tmp / "no-git-bin"
    bin_dir.mkdir()
    for d in os.environ["PATH"].split(os.pathsep):
        if not os.path.isdir(d):
            continue
        for name in os.listdir(d):
            src, dst = os.path.join(d, name), bin_dir / name
            if name.startswith("git") or dst.exists() or not os.access(src, os.X_OK) or os.path.isdir(src):
                continue
            dst.symlink_to(src)
    return str(bin_dir)


def home_env(base: Path, name: str, path: str) -> tuple[Path, dict]:
    # PSModulePath: CI starts this from PowerShell 7, whose module path breaks Windows
    # PowerShell's own modules (Get-FileHash goes missing). Someone who opens PowerShell
    # from the Start menu gets the default path, which is what dropping it gives.
    drop = {"CLAUDE_CONFIG_DIR", "CODEX_HOME", "PSMODULEPATH"}
    env = {k: v for k, v in os.environ.items() if k.upper() not in drop}
    if WIN:
        return Path.home(), env
    home = base / name
    home.mkdir()
    return home, {**env, "HOME": str(home), "PATH": path}


def reset_windows_profile(env: dict) -> None:
    """Start each Windows step from a profile with no TopCited marketplace, plugin or skills."""
    subprocess.run(["claude", "plugin", "marketplace", "remove", "topcited"], env=env, capture_output=True)
    for d in (Path.home() / ".agents" / "skills", Path.home() / ".claude" / "plugins"):
        shutil.rmtree(d, ignore_errors=True)


def powershell(shell: str, script: str) -> list[str]:
    encoded = base64.b64encode(script.encode("utf-16-le")).decode()
    return [shell, "-NoProfile", "-NonInteractive", "-EncodedCommand", encoded]


def codex_skills(project: Path, env: dict) -> dict[str, str]:
    """Ask Codex's app server which skills it sees in `project`, as {name: scope}."""
    proc = subprocess.Popen(
        [shutil.which("codex") or "codex", "app-server"], cwd=project, env=env,
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, encoding="utf-8",
    )
    timer = threading.Timer(120, proc.kill)
    timer.start()
    try:
        messages = [
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"clientInfo": {"name": "install-e2e", "version": "0"}}},
            {"jsonrpc": "2.0", "method": "initialized"},
            {"jsonrpc": "2.0", "id": 2, "method": "skills/list", "params": {"cwds": [str(project)]}},
        ]
        proc.stdin.write("".join(json.dumps(m) + "\n" for m in messages))
        proc.stdin.flush()
        for line in proc.stdout:
            try:
                msg = json.loads(line)
            except ValueError:
                continue
            if msg.get("id") == 2:
                if "result" not in msg:
                    sys.exit(f"FAIL Codex skills/list: {msg}")
                return {s["name"]: s.get("scope") for entry in msg["result"]["data"] for s in entry["skills"]}
        sys.exit("FAIL Codex app server closed (or timed out) without answering skills/list")
    finally:
        timer.cancel()
        proc.kill()


def check_skill_folder(folder: Path, what: str) -> None:
    missing = [s for s in SKILLS if not (folder / s / "SKILL.md").is_file()]
    if missing or (folder / "skills").exists():
        listing = sorted(p.name for p in folder.iterdir()) if folder.is_dir() else "no such folder"
        sys.exit(f"FAIL {what}: expected {SKILLS} in {folder}, missing {missing}; it holds {listing}")


def main() -> None:
    if WIN and not os.environ.get("CI"):
        sys.exit("On Windows this rewrites your real Claude Code and Codex settings, so it only runs in CI.")
    if WIN and shutil.which("git"):
        sys.exit(f"Git is still on PATH ({shutil.which('git')}); remove it before running this.")

    claude_steps = readme_block("Claude Code plugin", lambda lang, body: body.startswith("/plugin marketplace add "))
    sh_download = readme_block("sh download", lambda lang, body: lang == "sh")
    ps_download = readme_block("PowerShell download", lambda lang, body: lang == "powershell")
    cli = re.search(r"^(curl -fsSL \S+/install\.sh \| sh)\s+# Windows: (irm \S+/install\.ps1 \| iex)$",
                    readme_block("CLI install", lambda lang, body: "install.sh" in body), re.M)
    if README_MARKETPLACE_URL not in claude_steps or not cli:
        sys.exit("README.md: the Claude Code or CLI install block changed; update this test with it")
    marketplace_url = os.environ.get("MARKETPLACE_URL") or README_MARKETPLACE_URL

    base = Path(tempfile.mkdtemp(prefix="topcited-install-e2e-"))
    path = os.environ["PATH"] if WIN else no_git_path(base)

    # 1. The old route needs Git, so it must fail here.
    home, env = home_env(base, "old-route", path)
    if WIN:
        reset_windows_profile(env)
    r = run(["claude", "plugin", "marketplace", "add", "TopCited/topcited-skills"], env, "old route", expect_ok=False)
    out = r.stdout + r.stderr
    if not re.search(r'Executable not found in \$PATH: "git"|ENOENT: git\b|Command .git. not found', out):
        sys.exit(f"FAIL old route: it failed, but not for lack of Git:\n{out}")
    print("ok   the old route fails without Git")

    # 2. The README's Claude Code steps, run from a terminal in the same profile: a user who
    #    tried the old route and saw it fail then runs both lines.
    for line in filter(None, (l.strip() for l in claude_steps.splitlines())):
        args = ["claude", *line.lstrip("/").replace(README_MARKETPLACE_URL, marketplace_url).split()]
        run(args, env, " ".join(args))
    installed = {p["id"]: p for p in json.loads(run(["claude", "plugin", "list", "--json"], env, "plugin list").stdout)}
    if PLUGIN not in installed or not installed[PLUGIN].get("enabled"):
        sys.exit(f"FAIL Claude Code: {PLUGIN} is not installed and enabled: {installed}")
    check_skill_folder(Path(installed[PLUGIN]["installPath"]) / "skills", "Claude Code plugin")
    details = run(["claude", "plugin", "details", PLUGIN], env, "plugin details").stdout
    if missing := [s for s in SKILLS if s not in details]:
        sys.exit(f"FAIL Claude Code does not load {missing} from {PLUGIN}:\n{details}")
    print(f"ok   after the failed old route, Claude Code installs {PLUGIN} with {', '.join(SKILLS)}")

    # 3. The README's download for Codex and other agents, run twice (first install, then update).
    shells = [("powershell", lambda s: powershell("powershell", s)), ("pwsh", lambda s: powershell("pwsh", s))] if WIN \
        else [("sh", lambda s: ["sh", "-c", s])]
    for shell, wrap in shells:
        home, env = home_env(base, f"download-{shell}", path)
        if WIN:
            reset_windows_profile(env)
        skill_md = home / ".agents" / "skills" / SKILLS[0] / "SKILL.md"
        for attempt in ("first run", "second run"):
            run(wrap(ps_download if WIN else sh_download), env, f"{shell} download, {attempt}")
            check_skill_folder(home / ".agents" / "skills", f"{shell} download, {attempt}")
            if attempt == "first run":
                fresh = skill_md.read_bytes()
                skill_md.write_text("stale")  # the second run must replace this
            elif skill_md.read_bytes() != fresh:
                sys.exit(f"FAIL {shell} download, second run: it did not update {skill_md}")
        # From another folder, so only the user-level ~/.agents/skills can supply them.
        elsewhere = base / f"elsewhere-{shell}"
        elsewhere.mkdir()
        seen = codex_skills(elsewhere, {**env, "PATH": os.environ["PATH"]})
        if missing := [s for s in SKILLS if seen.get(s) != "user"]:
            sys.exit(f"FAIL Codex does not list {missing} as user skills after the {shell} download; it lists {seen}")
        print(f"ok   {shell}: the download puts all three skills where Codex finds them, also on a re-run")

    # 4. The README's CLI install.
    home, env = home_env(base, "cli", path)
    if WIN:
        r = run(powershell("powershell", f"{cli.group(2)}\ntopcited --version"), env, "CLI install (Windows PowerShell)")
    else:
        run(["sh", "-c", cli.group(1)], env, "CLI install")
        r = run([str(home / ".local" / "bin" / "topcited"), "--version"], env, "topcited --version")
    version = re.search(r"^v?(\d+\.\d+\.\d+)\s*$", r.stdout, re.M)
    if not version:
        sys.exit(f"FAIL the CLI installed but `topcited --version` printed no version:\n{r.stdout}{r.stderr}")
    print(f"ok   the CLI installs and runs: topcited {version.group(1)}")

    if not WIN:
        shutil.rmtree(base, ignore_errors=True)


if __name__ == "__main__":
    main()
