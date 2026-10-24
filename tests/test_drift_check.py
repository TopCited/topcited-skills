"""Tests for scripts/drift_check.py. Run: python3 -m unittest discover -s tests"""

from __future__ import annotations

import datetime as dt
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import drift_check as d  # noqa: E402

TODAY = dt.date(2026, 10, 24)

README = """# topcited

## Install
`curl … | sh`

## Commands

```
topcited auth login | logout | status | token [--show]
topcited brand list | use <id|name> | show [brand]
topcited monitor sets list | create | show
topcited monitor run <set> [--wait] [--dry-run] [--yes]
topcited audit run <url> [--wait] | show <id> | list
topcited recommend [keywords|prompts|content] [--wait] [--list]
topcited wait <job>                             # resume any --wait
topcited api <path> [-X M] [-d json|@file] [-f k=v]
```

## For agents
- `topcited not-a-command` here is outside the block
"""


def fake_fetch(responses: dict[str, tuple[int, bytes]]):
    def fetch(url: str) -> tuple[int, bytes]:
        return responses.get(url, (404, b""))
    return fetch


class NormalizeTest(unittest.TestCase):
    def test_prefix_params_query_and_slash(self):
        self.assertEqual(d.normalize_path("/api/v1/reports/"), "/reports")
        self.assertEqual(d.normalize_path("/api/v1/brands/{brand_id}/keywords:recommend"), "/brands/{}/keywords:recommend")
        self.assertEqual(d.normalize_path("/brands/<id>/keywords/<kid>:accept"), "/brands/{}/keywords/{}:accept")
        self.assertEqual(d.normalize_path("/reports/<id>/download/pdf?theme=light"), "/reports/{}/download/pdf")

    def test_spec_operations(self):
        spec = {"paths": {
            "/api/v1/brands": {"get": {"operationId": "listBrands"}, "post": {"operationId": "createBrand"}, "parameters": []},
            "/api/v1/brands/{brand_id}": {"patch": {"operationId": "updateBrand"}},
        }}
        self.assertEqual(d.spec_operations(spec), {
            "GET /brands": "listBrands", "POST /brands": "createBrand", "PATCH /brands/{}": "updateBrand",
        })


class DocumentedOperationsTest(unittest.TestCase):
    def test_verb_path_and_api_calls(self):
        text = """
- `GET /brands/<id>/competitor-keywords/dashboard` and `DELETE /brands/<id>`
- `topcited api /users/me`
- `topcited api /monitoring/runs -f query_set_id=<id> --paginate`
- `topcited api -X PATCH /monitoring/query-sets/<id> -d '{"paused": true}'`
- `topcited api -X POST /brands -d '{"name": "Acme"}'`
- `topcited api /brands -d '{"name": "Acme"}'`
- skipped: `DELETE …/runs` and `topcited api …/prompts/<pid>:accept`
"""
        self.assertEqual(d.documented_operations([text]), {
            "GET /brands/{}/competitor-keywords/dashboard",
            "DELETE /brands/{}",
            "GET /users/me",
            "GET /monitoring/runs",
            "PATCH /monitoring/query-sets/{}",
            "POST /brands",
        })


class CheckSpecTest(unittest.TestCase):
    def test_all_categories(self):
        live = {"GET /a": "", "GET /b": "", "GET /new": "", "POST /internal-now-public": ""}
        snapshot = {"GET /a", "GET /b", "GET /gone", "POST /internal-now-public"}
        documented = {"GET /a", "POST /secret", "POST /mystery", "GET /gone"}
        res = d.check_spec(live, snapshot, documented, cli_covered={"GET /b"},
                           internal={"POST /secret", "POST /internal-now-public"}, source="live")
        self.assertTrue(res.available)
        self.assertEqual(res.added, ["GET /new"])
        self.assertEqual(res.removed, ["GET /gone"])
        self.assertEqual(res.undocumented, ["GET /new", "POST /internal-now-public"])
        self.assertEqual(res.unknown, ["GET /gone", "POST /mystery"])
        self.assertEqual(res.now_public, ["POST /internal-now-public"])
        self.assertTrue(res.drift)

    def test_unavailable_falls_back_to_snapshot(self):
        res = d.check_spec(None, {"GET /a", "GET /b"}, {"GET /a"}, set(), set(), "source unavailable (HTTP 404): x")
        self.assertFalse(res.available)
        self.assertEqual((res.added, res.removed), ([], []))
        self.assertEqual(res.undocumented, ["GET /b"])

    def test_clean(self):
        res = d.check_spec({"GET /a": ""}, {"GET /a"}, {"GET /a"}, set(), set(), "live")
        self.assertFalse(res.drift)


class CliTest(unittest.TestCase):
    def test_readme_commands(self):
        self.assertEqual(d.cli_commands_from_readme(README), {
            "auth login", "auth logout", "auth status", "auth token",
            "brand list", "brand use", "brand show",
            "monitor sets list", "monitor sets create", "monitor sets show",
            "monitor run", "audit run", "audit show", "audit list",
            "recommend", "wait", "api",
        })

    def test_readme_without_block(self):
        self.assertIsNone(d.cli_commands_from_readme("# topcited\n\nno commands here\n"))

    def test_skill_commands_only_in_code(self):
        text = """Run `topcited auth login` then `topcited recommend prompts --wait`.
The `topcited-cli on <hostname>` key and topcited.ai are not commands; nor is topcited brand list in prose.

```bash
topcited monitor run Core --dry-run
topcited api /users/me
```
"""
        self.assertEqual(d.skill_commands([text]), {"auth login", "recommend prompts", "monitor run", "api"})

    def test_check_cli(self):
        commands = d.cli_commands_from_readme(README)
        mentions = {"auth login", "recommend prompts", "monitor", "monitor sets list", "brand delete", "doctor"}
        res = d.check_cli(commands, mentions, "readme")
        self.assertIn("auth logout", res.missing)
        self.assertNotIn("recommend", res.missing)  # covered via "recommend prompts"
        self.assertEqual(res.stale, ["brand delete", "doctor"])  # "monitor" is a group, not stale
        self.assertTrue(res.drift)

    def test_check_cli_unavailable(self):
        res = d.check_cli(None, {"auth login"}, "source unavailable (HTTP 404): x")
        self.assertFalse(res.available)
        self.assertFalse(res.drift)


class CheckCliStaleTest(unittest.TestCase):
    def test_unknown_subcommand_of_known_group_is_stale(self):
        res = d.check_cli({"brand list", "brand use"}, {"brand delete", "brand"}, "readme")
        self.assertEqual(res.stale, ["brand delete"])  # "brand" alone is a group, not stale


class FreshnessTest(unittest.TestCase):
    def fm(self, date: str) -> str:
        return f"---\ntopic: x\nlast-verified: {date}\nsources:\n  - y\n---\n\nbody last-verified: 1999-01-01\n"

    def test_boundaries(self):
        files = {
            "b.md": self.fm("2026-07-26"),  # exactly 90 days: fresh
            "a.md": self.fm("2026-07-25"),  # 91 days: stale
            "c.md": "---\ntopic: x\n---\n",
            "d.md": self.fm("2026-13-40"),
        }
        res = d.check_freshness(files, TODAY, 90)
        self.assertEqual(res.stale, [("a.md", "2026-07-25", 91)])
        self.assertEqual(res.undated, ["c.md", "d.md"])
        self.assertTrue(res.drift)

    def test_all_fresh(self):
        self.assertFalse(d.check_freshness({"a.md": self.fm("2026-10-01")}, TODAY, 90).drift)


class FetchTest(unittest.TestCase):
    def test_spec_404_and_bad_json(self):
        spec, src = d.fetch_spec("https://x/spec.json", fake_fetch({}))
        self.assertIsNone(spec)
        self.assertEqual(src, "source unavailable (HTTP 404): https://x/spec.json")
        spec, src = d.fetch_spec("https://x/spec.json", fake_fetch({"https://x/spec.json": (200, b"<html>")}))
        self.assertIsNone(spec)
        self.assertIn("not JSON", src)

    def test_network_error_label(self):
        _, src = d.fetch_spec("https://x/s", fake_fetch({"https://x/s": (0, b"")}))
        self.assertEqual(src, "source unavailable (network error): https://x/s")

    def test_cli_readme_prefers_release(self):
        fetch = fake_fetch({
            "https://api.github.com/repos/o/r/releases/latest": (200, json.dumps({"tag_name": "v1.2.0"}).encode()),
            "https://raw.githubusercontent.com/o/r/v1.2.0/README.md": (200, b"release readme"),
            "https://raw.githubusercontent.com/o/r/HEAD/README.md": (200, b"head readme"),
        })
        self.assertEqual(d.fetch_cli_readme("o/r", fetch), ("release readme", "o/r README (release v1.2.0)"))

    def test_cli_readme_falls_back_then_unavailable(self):
        fetch = fake_fetch({"https://raw.githubusercontent.com/o/r/HEAD/README.md": (200, b"head")})
        self.assertEqual(d.fetch_cli_readme("o/r", fetch), ("head", "o/r README (default branch)"))
        readme, src = d.fetch_cli_readme("o/r", fake_fetch({}))
        self.assertIsNone(readme)
        self.assertIn("source unavailable (HTTP 404)", src)


class ReportTest(unittest.TestCase):
    def test_deterministic_and_flags(self):
        spec = d.check_spec({"GET /a": ""}, {"GET /a"}, set(), set(), set(), "live")
        cli = d.check_cli(None, set(), "source unavailable (HTTP 404): x")
        fresh = d.check_freshness({}, TODAY, 90)
        one = d.render_report(spec, cli, fresh, TODAY)
        self.assertEqual(one, d.render_report(spec, cli, fresh, TODAY))
        self.assertIn("**Drift found.**", one)
        self.assertIn("- `GET /a`", one)
        self.assertIn("Source: source unavailable (HTTP 404): x", one)


class MainTest(unittest.TestCase):
    """End to end against the real repo files, with every remote source unavailable."""

    def run_main(self, *argv: str) -> tuple[int, str]:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "out.txt"
            report = Path(tmp) / "report.md"
            with redirect_stderr(io.StringIO()), redirect_stdout(io.StringIO()):
                code = d.main(["--today", "2026-10-24", "--report", str(report), "--github-output", str(out), *argv],
                              fetch=fake_fetch({}))
            return code, out.read_text() + report.read_text()

    def test_unavailable_sources_are_not_drift(self):
        code, text = self.run_main("--max-age-days", "100000", "--exit-code")
        self.assertEqual(code, 0)
        self.assertIn("drift=false", text)
        self.assertIn("source unavailable (HTTP 404)", text)

    def test_exit_code_on_drift(self):
        code, text = self.run_main("--max-age-days", "0", "--exit-code")
        self.assertEqual(code, 1)
        self.assertIn("drift=true", text)

    def test_drift_without_exit_code_still_exits_zero(self):
        code, _ = self.run_main("--max-age-days", "0")
        self.assertEqual(code, 0)


if __name__ == "__main__":
    unittest.main()
