# Audit checklist (manual fallback)

Use when `scripts/audit.py` cannot run. For each item record the evidence (URL, header
or snippet), not just pass/fail.

**Access & indexing**
- Home page returns 200 over HTTPS; one canonical host (www vs non-www, http → https redirect).
- `/robots.txt` exists; does it block `GPTBot`, `OAI-SearchBot`, `ChatGPT-User`, `ClaudeBot`,
  `Claude-SearchBot`, `PerplexityBot`, `Google-Extended`, or `*`? Blocking *training* bots is a
  legitimate choice; blocking *search/answer* bots removes you from those answers.
- Sitemap listed in robots.txt or at `/sitemap.xml`; URLs return 200 and are canonical.
- No stray `noindex` (meta robots or `X-Robots-Tag`) on pages that should rank.
- Important text is in the server-rendered HTML (view-source), not only injected by JavaScript.

**Per page**
- One `<title>` (~30–60 chars) naming the page's topic and brand; unique across pages.
- Meta description (~110–160 chars) that states what the reader gets.
- Exactly one `<h1>`; `<h2>`s that read like the questions people ask.
- `<link rel="canonical">`, `<html lang>`, viewport meta, Open Graph tags.
- JSON-LD that parses and matches visible content (Organization, WebSite, Article, Product, FAQ…).
- Images have meaningful alt text.

**GEO**
- The first paragraph answers the page's main question in plain words.
- Claims carry a number, a date and a named source; authorship and "last updated" are visible.
- Brand facts (what you are, where, who for) are stated identically on the site, About page and profiles.
- `/llms.txt` present and accurate (optional, cheap).

Knowledge-base files to read for each: see [seo-geo knowledge index](../../seo-geo/knowledge/INDEX.md).
