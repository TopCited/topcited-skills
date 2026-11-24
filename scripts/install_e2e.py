#!/usr/bin/env python3
"""Run the README's install steps, exactly as written, on a machine without Git.

On Windows the CI workflow deletes Git before this runs. On macOS and Linux this script
runs every command with a PATH that holds everything except Git. It then checks that:

  - the old `/plugin marketplace add TopCited/topcited-skills` route fails, which proves
    Git is out of reach;
  - the README's two Claude Code terminal commands install the plugin with all three skills;
  - the README's download steps (sh; on Windows, Windows PowerShell and PowerShell 7)
    put all three skills in ~/.agents/skills, also when run a second time, and Codex
    lists them;
  - the README's CLI install gives a working `topcited`;
  - Codex, given an `[mcp_servers.topcited]` block like the one on topcited.ai/developers
    (keep CODEX_MCP_TOML in step with it), connects to an MCP server and sends the
    Authorization header from that block.

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
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIN = os.name == "nt"
SKILLS = ("seo-geo", "topcited-api", "visibility-workflow")
README_MARKETPLACE_URL = "https://topcited.ai/claude-plugins.json"
PLUGIN = "topcited-skills@topcited"
# The Codex MCP block on topcited.ai/developers, with the real URL swapped for a local one.
CODEX_MCP_TOML = """[mcp_servers.topcited]
url = "{url}"
http_headers = {{ Authorization = "Bearer tc_your_api_key" }}
"""


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


def codex_request(project: Path, env: dict, method: str, params: dict) -> dict:
    """Send one request to Codex's app server, started in `project`, and return its result."""
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
            {"jsonrpc": "2.0", "id": 2, "method": method, "params": params},
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
                    sys.exit(f"FAIL Codex {method}: {msg}")
                return msg["result"]
        sys.exit(f"FAIL Codex app server closed (or timed out) without answering {method}")
    finally:
        timer.cancel()
        proc.kill()


def codex_skills(project: Path, env: dict) -> dict[str, str]:
    """Ask Codex's app server which skills it sees in `project`, as {name: scope}."""
    result = codex_request(project, env, "skills/list", {"cwds": [str(project)]})
    return {s["name"]: s.get("scope") for entry in result["data"] for s in entry["skills"]}


def codex_mcp_headers(home: Path, env: dict) -> tuple[list[str | None], list[dict]]:
    """Point Codex's config at a local MCP server, ask Codex for its MCP status, and return
    the Authorization headers the server received plus Codex's status for each server."""
    seen: list[str | None] = []

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def do_POST(self):
            request = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            seen.append(self.headers.get("Authorization"))
            if "id" not in request:  # a notification
                self.send_response(202)
                self.end_headers()
                return
            if request["method"] == "initialize":
                result = {"protocolVersion": request["params"].get("protocolVersion", "2025-03-26"),
                          "capabilities": {"tools": {}}, "serverInfo": {"name": "fake-topcited", "version": "1"}}
            elif request["method"] == "tools/list":
                result = {"tools": [{"name": "ping", "description": "ping", "inputSchema": {"type": "object"}}]}
            else:
                result = {}
            body = json.dumps({"jsonrpc": "2.0", "id": request["id"], "result": result}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):  # no server-to-client stream
            self.send_response(405)
            self.end_headers()

        def do_DELETE(self):
            self.send_response(200)
            self.end_headers()

    server = HTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    config = home / ".codex" / "config.toml"
    config.parent.mkdir(exist_ok=True)
    try:
        config.write_text(CODEX_MCP_TOML.format(url=f"http://127.0.0.1:{server.server_port}/mcp"), encoding="utf-8")
        elsewhere = home / "codex-mcp-project"
        elsewhere.mkdir(exist_ok=True)
        status = codex_request(elsewhere, env, "mcpServerStatus/list", {})["data"]
        return seen, status
    finally:
        server.shutdown()
        config.unlink(missing_ok=True)


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

    claude_steps = [
        readme_block("Claude Code marketplace add", lambda lang, body: body.startswith("claude plugin marketplace add ")),
        readme_block("Claude Code plugin install", lambda lang, body: body.startswith("claude plugin install ")),
    ]
    sh_download = readme_block("sh download", lambda lang, body: "main.tar.gz" in body)
    ps_download = readme_block("PowerShell download", lambda lang, body: lang == "powershell" and "main.zip" in body)
    cli_sh = readme_block("CLI install (sh)", lambda lang, body: "install.sh" in body).strip()
    cli_ps = readme_block("CLI install (PowerShell)", lambda lang, body: "install.ps1" in body).strip()
    if README_MARKETPLACE_URL not in claude_steps[0] or any("\n" in b.strip() for b in claude_steps):
        sys.exit("README.md: the Claude Code install blocks changed; update this test with them")
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

    # 2. The README's two Claude Code commands, run as written in the same profile: a user who
    #    tried the old route and saw it fail then runs both.
    for block in claude_steps:
        args = block.strip().replace(README_MARKETPLACE_URL, marketplace_url).split()
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
        r = run(powershell("powershell", f"{cli_ps}\ntopcited --version"), env, "CLI install (Windows PowerShell)")
    else:
        run(["sh", "-c", cli_sh], env, "CLI install")
        r = run([str(home / ".local" / "bin" / "topcited"), "--version"], env, "topcited --version")
    version = re.search(r"^v?(\d+\.\d+\.\d+)\s*$", r.stdout, re.M)
    if not version:
        sys.exit(f"FAIL the CLI installed but `topcited --version` printed no version:\n{r.stdout}{r.stderr}")
    print(f"ok   the CLI installs and runs: topcited {version.group(1)}")

    # 5. Codex with the MCP block from topcited.ai/developers.
    home, env = home_env(base, "codex-mcp", path)
    seen, status = codex_mcp_headers(home, {**env, "PATH": os.environ["PATH"]})
    topcited = [s for s in status if s["name"] == "topcited"]
    if not topcited or topcited[0].get("toolsError") or "ping" not in (topcited[0].get("tools") or {}):
        sys.exit(f"FAIL Codex could not use the MCP block: {topcited or status}")
    if not seen or set(seen) != {"Bearer tc_your_api_key"}:
        sys.exit(f"FAIL Codex sent the wrong Authorization header(s): {seen}")
    print("ok   Codex reads the MCP block, connects, and sends its Authorization header")

    if not WIN:
        shutil.rmtree(base, ignore_errors=True)


if __name__ == "__main__":
    main()
