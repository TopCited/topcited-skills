#!/usr/bin/env python3
"""Free, account-less SEO + GEO audit of a public website (stdlib only).

Usage:
    python3 audit.py https://example.com [--pages 5] [--json]

Fetches the home page, robots.txt, sitemap(s) and llms.txt, then samples up to
--pages URLs (from the sitemap, else internal links). Reports facts, not
opinions: every finding names the evidence. Read-only; sends plain GET
requests with an honest User-Agent.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser

UA = "topcited-skills-audit/0.2 (+https://github.com/TopCited/topcited-skills)"
TIMEOUT = 15
AI_BOTS = [
    "GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot",
    "Claude-User", "PerplexityBot", "Perplexity-User", "Google-Extended",
    "Applebot-Extended", "CCBot", "Bytespider",
]


def fetch(url: str, max_bytes: int = 2_000_000) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            body = r.read(max_bytes).decode(r.headers.get_content_charset() or "utf-8", "replace")
            return {"ok": True, "status": r.status, "final_url": r.geturl(),
                    "headers": {k.lower(): v for k, v in r.headers.items()}, "body": body}
    except urllib.error.HTTPError as e:
        return {"ok": False, "status": e.code, "final_url": url, "headers": {}, "body": ""}
    except Exception as e:  # DNS, TLS, timeout
        return {"ok": False, "status": None, "final_url": url, "headers": {}, "body": "", "error": str(e)}


class Page(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title = ""
        self._in_title = False
        self.meta: dict[str, str] = {}
        self.canonical = ""
        self.lang = ""
        self.h: dict[str, list[str]] = {"h1": [], "h2": [], "h3": []}
        self._h: str | None = None
        self.imgs = 0
        self.imgs_no_alt = 0
        self.links: list[str] = []
        self.jsonld: list[str] = []
        self._in_ld = False
        self.text: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang") or ""
        elif tag == "title":
            self._in_title = True
        elif tag == "meta":
            key = a.get("name") or a.get("property")
            if key and a.get("content") is not None:
                self.meta[key.lower()] = a["content"]
        elif tag == "link" and (a.get("rel") or "").lower() == "canonical":
            self.canonical = a.get("href") or ""
        elif tag in self.h:
            self._h = tag
            self.h[tag].append("")
        elif tag == "img":
            self.imgs += 1
            if not (a.get("alt") or "").strip():
                self.imgs_no_alt += 1
        elif tag == "a" and a.get("href"):
            self.links.append(a["href"])
        elif tag == "script":
            if (a.get("type") or "").lower() == "application/ld+json":
                self._in_ld = True
                self.jsonld.append("")
            else:
                self._skip += 1
        elif tag == "style":
            self._skip += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag == self._h:
            self._h = None
        elif tag == "script":
            if self._in_ld:
                self._in_ld = False
            elif self._skip:
                self._skip -= 1
        elif tag == "style" and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_ld and self.jsonld:
            self.jsonld[-1] += data
        elif self._h:
            self.h[self._h][-1] += data
        if not self._skip and not self._in_ld:
            self.text.append(data)


def schema_types(blocks: list[str]) -> tuple[list[str], int]:
    types: list[str] = []
    bad = 0

    def walk(o):
        if isinstance(o, dict):
            t = o.get("@type")
            if isinstance(t, str):
                types.append(t)
            elif isinstance(t, list):
                types.extend(x for x in t if isinstance(x, str))
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    for b in blocks:
        try:
            walk(json.loads(b))
        except ValueError:
            bad += 1
    return sorted(set(types)), bad


def parse_robots(txt: str) -> dict[str, str]:
    """Return {bot: 'blocked'|'allowed'|'unspecified'} using longest-prefix on '/'."""
    groups: list[tuple[list[str], list[tuple[str, str]]]] = []
    agents: list[str] = []
    rules: list[tuple[str, str]] = []
    last_was_agent = False
    for raw in txt.splitlines():
        line = raw.split("#", 1)[0].strip()
        if ":" not in line:
            continue
        k, v = (s.strip() for s in line.split(":", 1))
        k = k.lower()
        if k == "user-agent":
            if not last_was_agent and (agents or rules):
                groups.append((agents, rules))
                agents, rules = [], []
            agents.append(v.lower())
            last_was_agent = True
        else:
            last_was_agent = False
            if k in ("allow", "disallow"):
                rules.append((k, v))
    if agents or rules:
        groups.append((agents, rules))

    def verdict(bot: str) -> str:
        for want in (bot.lower(), "*"):
            for ags, rs in groups:
                if want in ags:
                    root = [(k, v) for k, v in rs if v == "/" or v == ""]
                    if any(k == "disallow" and v == "/" for k, v in root) and not any(
                        k == "allow" and v == "/" for k, v in root
                    ):
                        return "blocked" if want != "*" else "blocked (via *)"
                    return "allowed" if want != "*" else "allowed (via *)"
        return "unspecified"

    return {b: verdict(b) for b in AI_BOTS}


def audit_page(url: str) -> dict:
    r = fetch(url)
    out: dict = {"url": url, "status": r["status"], "final_url": r["final_url"]}
    if not r["ok"]:
        out["error"] = r.get("error") or f"HTTP {r['status']}"
        return out
    p = Page()
    try:
        p.feed(r["body"])
    except Exception:  # malformed HTML — report what we parsed
        pass
    words = len(re.findall(r"\w+", " ".join(p.text)))
    types, bad_ld = schema_types(p.jsonld)
    title, desc = p.title.strip(), p.meta.get("description", "").strip()
    issues: list[str] = []
    if not title:
        issues.append("missing <title>")
    elif not 15 <= len(title) <= 65:
        issues.append(f"title length {len(title)} (aim ~30-60)")
    if not desc:
        issues.append("missing meta description")
    elif not 70 <= len(desc) <= 165:
        issues.append(f"meta description length {len(desc)} (aim ~110-160)")
    if len(p.h["h1"]) != 1:
        issues.append(f"{len(p.h['h1'])} <h1> elements (want exactly 1)")
    if not p.canonical:
        issues.append("no canonical link")
    if not p.lang:
        issues.append("no <html lang>")
    if "viewport" not in p.meta:
        issues.append("no viewport meta")
    if not types:
        issues.append("no JSON-LD structured data (rich-result eligibility; studies show no AI-citation lift)")
    if bad_ld:
        issues.append(f"{bad_ld} JSON-LD block(s) fail to parse")
    if p.imgs and p.imgs_no_alt / p.imgs > 0.3:
        issues.append(f"{p.imgs_no_alt}/{p.imgs} images lack alt text")
    if words < 150:
        issues.append(f"thin server-rendered text ({words} words) — JS-only content is invisible to most AI crawlers")
    if not any(k.startswith("og:") for k in p.meta):
        issues.append("no Open Graph tags")
    out.update(
        title=title, title_len=len(title), meta_description=desc, canonical=p.canonical,
        lang=p.lang, h1=[x.strip() for x in p.h["h1"]], h2_count=len(p.h["h2"]),
        word_count=words, schema_types=types, images=p.imgs, images_missing_alt=p.imgs_no_alt,
        x_robots_tag=r["headers"].get("x-robots-tag", ""), issues=issues,
        _links=p.links,
    )
    return out


def run(site: str, pages: int) -> dict:
    if not re.match(r"^https?://", site):
        site = "https://" + site
    base = "{0.scheme}://{0.netloc}".format(urllib.parse.urlparse(site))
    rep: dict = {"site": base, "tool": UA}
    home = audit_page(site)
    rep["home"] = {k: v for k, v in home.items() if k != "_links"}
    if home.get("error"):
        return rep

    robots = fetch(base + "/robots.txt")
    rep["robots_txt"] = {"status": robots["status"]}
    sitemaps: list[str] = []
    if robots["ok"]:
        rep["robots_txt"]["ai_crawlers"] = parse_robots(robots["body"])
        sitemaps = re.findall(r"(?im)^\s*sitemap:\s*(\S+)", robots["body"])
    llms = fetch(base + "/llms.txt")
    rep["llms_txt"] = {"status": llms["status"], "bytes": len(llms["body"]) if llms["ok"] else 0}

    sm_urls: list[str] = []
    for sm in (sitemaps or [base + "/sitemap.xml"])[:3]:
        s = fetch(sm)
        if s["ok"]:
            locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", s["body"])
            rep.setdefault("sitemaps", []).append({"url": sm, "status": s["status"], "urls": len(locs)})
            sm_urls += [u for u in locs if not u.endswith(".xml")]
        else:
            rep.setdefault("sitemaps", []).append({"url": sm, "status": s["status"]})

    host = urllib.parse.urlparse(base).netloc
    cand = sm_urls or [urllib.parse.urljoin(site, h) for h in home["_links"]]
    seen, sample = {home["final_url"].rstrip("/"), site.rstrip("/")}, []
    for u in cand:
        u = u.split("#", 1)[0]
        if urllib.parse.urlparse(u).netloc == host and u.rstrip("/") not in seen and u.startswith("http"):
            seen.add(u.rstrip("/"))
            sample.append(u)
        if len(sample) >= max(pages - 1, 0):
            break
    rep["sampled_pages"] = [{k: v for k, v in audit_page(u).items() if k != "_links"} for u in sample]

    g: list[str] = []
    ai = rep["robots_txt"].get("ai_crawlers", {})
    if not robots["ok"]:
        g.append("no robots.txt")
    blocked = [b for b, v in ai.items() if v.startswith("blocked")]
    if blocked:
        g.append("AI crawlers blocked in robots.txt: " + ", ".join(blocked))
    if not llms["ok"]:
        g.append("no /llms.txt (optional hygiene; studies show no citation lift; see seo-geo/knowledge/technical-seo/llms-txt.md)")
    if not any(s.get("urls") for s in rep.get("sitemaps", [])):
        g.append("no readable sitemap")
    if not base.startswith("https"):
        g.append("site not served over HTTPS")
    rep["site_level_issues"] = g
    return rep


def render(rep: dict) -> str:
    L = [f"# Audit: {rep['site']}", ""]
    h = rep["home"]
    if h.get("error"):
        return "\n".join(L + [f"Could not fetch the home page: {h['error']}"])
    L += ["## Site level"] + [f"- {x}" for x in rep["site_level_issues"] or ["no site-level problems found"]]
    ai = rep["robots_txt"].get("ai_crawlers")
    if ai:
        L.append("- AI crawler access: " + "; ".join(f"{b}={v}" for b, v in ai.items()))
    L.append(f"- llms.txt: HTTP {rep['llms_txt']['status']}")
    for s in rep.get("sitemaps", []):
        L.append(f"- sitemap {s['url']}: HTTP {s['status']}, {s.get('urls', '?')} URLs")
    for pg in [h] + rep["sampled_pages"]:
        L += ["", f"## {pg['url']}"]
        if pg.get("error"):
            L.append(f"- fetch failed: {pg['error']}")
            continue
        L += [f"- title ({pg['title_len']}): {pg['title']!r}",
              f"- meta description: {pg['meta_description']!r}",
              f"- h1: {pg['h1']}  |  h2 count: {pg['h2_count']}  |  words: {pg['word_count']}",
              f"- structured data: {pg['schema_types'] or 'none'}"]
        L += [f"- ISSUE: {i}" for i in pg["issues"]] or ["- no on-page issues found by these checks"]
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url")
    ap.add_argument("--pages", type=int, default=5, help="max pages to sample, home included (default 5)")
    ap.add_argument("--json", action="store_true", help="emit JSON instead of a text report")
    a = ap.parse_args()
    rep = run(a.url, max(1, min(a.pages, 25)))
    print(json.dumps(rep, indent=2) if a.json else render(rep))
    return 1 if rep["home"].get("error") else 0


if __name__ == "__main__":
    sys.exit(main())
