"""Offline tests for skills/seo-geo-audit/scripts/topcited_audit.py (stdlib unittest).

Run from the repo root:  python3 -m unittest discover -s tests -v
No network: the end-to-end test serves fixtures from a local HTTP server.
"""

import http.server
import importlib.util
import json
import pathlib
import threading
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parent.parent / "skills" / "seo-geo-audit" / "scripts" / "topcited_audit.py"
spec = importlib.util.spec_from_file_location("topcited_audit", SCRIPT)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class RobotsTests(unittest.TestCase):
    def test_specific_group_beats_star(self):
        txt = "User-agent: *\nAllow: /\n\nUser-agent: GPTBot\nDisallow: /\n"
        v = audit.parse_robots(txt)
        self.assertEqual(v["GPTBot"], "blocked")
        self.assertEqual(v["ClaudeBot"], "allowed (via *)")

    def test_star_block_is_inherited_and_labelled(self):
        v = audit.parse_robots("User-agent: *\nDisallow: /\n")
        self.assertEqual(v["PerplexityBot"], "blocked (via *)")

    def test_bot_group_can_reopen_a_star_block(self):
        v = audit.parse_robots("User-agent: *\nDisallow: /\n\nUser-agent: OAI-SearchBot\nAllow: /\n")
        self.assertEqual(v["OAI-SearchBot"], "allowed")
        self.assertEqual(v["GPTBot"], "blocked (via *)")

    def test_partial_block_is_not_reported_as_full_block(self):
        v = audit.parse_robots("User-agent: ClaudeBot\nDisallow: /\nAllow: /blog/\n")
        self.assertEqual(v["ClaudeBot"], "partly blocked")

    def test_path_rules_are_reported_but_not_as_a_block(self):
        v = audit.parse_robots("User-agent: GPTBot\nDisallow: /blog\n")
        self.assertEqual(v["GPTBot"], "allowed, but some paths disallowed")

    def test_empty_disallow_means_allowed(self):
        self.assertEqual(audit.parse_robots("User-agent: GPTBot\nDisallow:\n")["GPTBot"], "allowed")

    def test_shared_group_for_several_agents(self):
        v = audit.parse_robots("User-agent: GPTBot\nUser-agent: CCBot\nDisallow: /\n")
        self.assertEqual((v["GPTBot"], v["CCBot"]), ("blocked", "blocked"))

    def test_split_groups_for_one_agent_are_merged(self):
        txt = "User-agent: GPTBot\nDisallow: /private\n\nUser-agent: GPTBot\nDisallow: /\n"
        self.assertEqual(audit.parse_robots(txt)["GPTBot"], "blocked")

    def test_no_matching_group_is_unspecified(self):
        self.assertEqual(audit.parse_robots("User-agent: Googlebot\nDisallow: /x\n")["GPTBot"], "unspecified")

    def test_comments_and_case_are_ignored(self):
        v = audit.parse_robots("# hi\nUSER-AGENT: gptbot  # inline\nDISALLOW: /\n")
        self.assertEqual(v["GPTBot"], "blocked")


class NoindexTests(unittest.TestCase):
    def test_cases(self):
        yes = ["noindex", "NOINDEX, nofollow", "none", "googlebot: noindex", "max-snippet:-1, noindex"]
        no = ["", "index, follow", "max-image-preview:none", "nofollow", "max-snippet:0"]
        for s in yes:
            self.assertTrue(audit.is_noindex(s), s)
        for s in no:
            self.assertFalse(audit.is_noindex(s), s)


class ParsingTests(unittest.TestCase):
    def test_schema_types_nested_and_invalid(self):
        blocks = ['{"@graph":[{"@type":"Organization"},{"@type":["WebSite","Thing"]}]}', "{not json"]
        types, bad = audit.schema_types(blocks)
        self.assertEqual(types, ["Organization", "Thing", "WebSite"])
        self.assertEqual(bad, 1)

    def test_page_parser(self):
        html = ('<html lang="en"><head><title> Hi </title><meta name="description" content="d">'
                '<link rel="canonical" href="https://x/">'
                '<script type="application/ld+json">{"@type":"Organization"}</script></head>'
                '<body><h1>One</h1><h2>Two</h2><img src=a><img src=b alt="b"><a href="/p">p</a>'
                "<script>var hidden = 'not text';</script><p>Visible words here.</p></body></html>")
        p = audit.Page()
        p.feed(html)
        self.assertEqual((p.title.strip(), p.lang, p.canonical), ("Hi", "en", "https://x/"))
        self.assertEqual((p.h["h1"], p.h["h2"]), (["One"], ["Two"]))
        self.assertEqual((p.imgs, p.imgs_no_alt), (2, 1))
        self.assertNotIn("not text", " ".join(p.text))
        self.assertIn("Visible words here.", " ".join(p.text))


GOOD = """<!doctype html><html lang="en"><head><title>Acme Coffee Roasters: espresso beans, delivered</title>
<meta name="description" content="Acme roasts single-origin espresso beans weekly in Lisbon and ships them across Europe within two days of roasting.">
<meta name="viewport" content="width=device-width"><meta property="og:title" content="Acme">
<link rel="canonical" href="http://127.0.0.1/"><script type="application/ld+json">{"@type":"Organization","name":"Acme"}</script>
</head><body><h1>Acme Coffee</h1><a href="/about">About</a><p>%s</p></body></html>""" % ("coffee words " * 100)

NOINDEX = """<!doctype html><html lang="en"><head><title>Staging copy of the Acme site</title>
<meta name="robots" content="noindex,nofollow"></head><body><h1>Staging</h1><p>%s</p></body></html>""" % ("text " * 200)


class Handler(http.server.BaseHTTPRequestHandler):
    routes: dict = {}

    def do_GET(self):  # noqa: N802
        body, ctype, extra = self.routes.get(self.path, (None, None, {}))
        if body is None:
            self.send_response(404)
            self.end_headers()
            return
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        for k, v in extra.items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body.encode())

    def log_message(self, *a):
        pass


class EndToEnd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        port = cls.server.server_address[1]
        cls.base = f"http://127.0.0.1:{port}"
        sm_index = f"<sitemapindex><sitemap><loc>{cls.base}/sm-pages.xml</loc></sitemap></sitemapindex>"
        sm_pages = f"<urlset><url><loc>{cls.base}/about</loc></url><url><loc>{cls.base}/staging</loc></url></urlset>"
        Handler.routes = {
            "/": (GOOD, "text/html", {}),
            "/about": (GOOD, "text/html", {"X-Robots-Tag": "noindex"}),
            "/staging": (NOINDEX, "text/html", {}),
            "/robots.txt": (f"User-agent: GPTBot\nDisallow: /\n\nSitemap: {cls.base}/sitemap.xml\n", "text/plain", {}),
            "/sitemap.xml": (sm_index, "application/xml", {}),
            "/sm-pages.xml": (sm_pages, "application/xml", {}),
        }
        threading.Thread(target=cls.server.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def test_full_run(self):
        rep = audit.run(self.base, 5)
        self.assertEqual(rep["home"]["status"], 200)
        self.assertEqual(rep["home"]["schema_types"], ["Organization"])
        self.assertEqual(rep["robots_txt"]["ai_crawlers"]["GPTBot"], "blocked")
        self.assertTrue(any("GPTBot" in x for x in rep["site_level_issues"]))
        self.assertTrue(any("llms.txt" in x for x in rep["site_level_issues"]))  # none served
        # sitemap index was followed to its child, so page URLs came from it
        self.assertTrue(any(s.get("urls") == 2 for s in rep["sitemaps"]))
        by_url = {p["url"]: p for p in rep["sampled_pages"]}
        self.assertTrue(any("NOINDEX" in i for i in by_url[self.base + "/about"]["issues"]))  # header
        self.assertTrue(any("NOINDEX" in i for i in by_url[self.base + "/staging"]["issues"]))  # meta
        self.assertFalse(any("NOINDEX" in i for i in rep["home"]["issues"]))
        self.assertTrue(any(x.startswith("NOINDEX on 2 of 3") for x in rep["site_level_issues"]))
        text = audit.render(rep)
        self.assertIn("GPTBot=blocked", text)
        json.dumps(rep)  # serialisable for --json

    def test_sitemap_on_another_host_is_not_fetched(self):
        hits = []

        class Other(http.server.BaseHTTPRequestHandler):
            def do_GET(self):  # noqa: N802
                hits.append(self.path)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"<urlset></urlset>")

            def log_message(self, *a):
                pass

        other = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Other)
        threading.Thread(target=other.serve_forever, daemon=True).start()
        try:
            evil = f"http://localhost:{other.server_address[1]}/internal-sitemap.xml"  # different host from 127.0.0.1
            Handler.routes["/robots.txt"] = (f"User-agent: *\nAllow: /\nSitemap: {evil}\n", "text/plain", {})
            rep = audit.run(self.base, 2)
        finally:
            other.shutdown()
            other.server_close()
            Handler.routes["/robots.txt"] = (f"User-agent: GPTBot\nDisallow: /\n\nSitemap: {self.base}/sitemap.xml\n", "text/plain", {})
        self.assertEqual(hits, [])
        self.assertTrue(any(s.get("skipped") for s in rep["sitemaps"]))
        self.assertIn("not fetched", audit.render(rep))

    def test_unreachable_home_reports_error(self):
        rep = audit.run("http://127.0.0.1:9", 3)
        self.assertIn("error", rep["home"])
        self.assertIn("Could not fetch", audit.render(rep))


if __name__ == "__main__":
    unittest.main()
