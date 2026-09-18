---
topic: Diagnosing why pages don't get indexed and fixing the underlying crawl/indexing gap
stage-relevance: [4, 5]
last-verified: 2026-08-20
sources:
  - https://developers.google.com/search/docs/crawling-indexing/canonicalization-troubleshooting
  - https://www.onely.com/blog/how-to-fix-discovered-currently-not-indexed-in-google-search-console/
  - https://www.outrank.so/blog/how-to-fix-crawled-but-not-indexed
  - https://www.clickrank.ai/mueller-explains-indexing-errors/
  - heuristic (2026-06-14 seed research pass, not re-verified)
---

# Crawlability and indexing

## In plain words
If a page isn't showing up in Google at all, the first question isn't "why
don't we rank" — it's "does Google even know this page is worth storing."
Google now applies a higher bar for what it keeps in its main index, and a
page can be fully crawlable and still sit in limbo because Google has decided
it isn't worth prioritizing. Diagnosing this means working through Search
Console systematically rather than guessing.

## What practitioners need to know
- **"Discovered — currently not indexed"** means Googlebot knows the URL
  exists but has deprioritized crawling it — a crawl-priority decision, not a
  block. (heuristic — pattern converges across ~8 practitioner sources, not
  Google-primary-sourced, but consistent with Google's own crawl-budget
  documentation)
- Converging root causes practitioners point to: thin/duplicate/AI-mass-produced
  content lowering site-wide crawl demand, missing E-E-A-T signals, poor
  internal linking / orphaned pages, and slow server response or render
  timeouts that cause Googlebot to abandon a crawl before indexing is even
  evaluated. (heuristic)
- **Diagnosis order matters** — work top-down, not URL-by-URL first:
  1. **Search Console → Pages report ("Page indexing")** for the aggregate,
     site-wide breakdown (`Discovered — not indexed`, `Crawled — not
     indexed`, `Duplicate, Google chose different canonical`, `Excluded by
     noindex`, etc.) before drilling into individual URLs. (heuristic)
  2. **URL Inspection tool**, per specific URL — shows Google's last crawled
     snapshot, and a separate "Test Live URL" action does a real-time fetch
     to catch a robots.txt block, a `noindex` tag, or a server error *right
     now* (state can differ from the indexed snapshot). (heuristic, adjacent
     to documented tool behavior — not independently confirmed against a
     primary Search Central page describing this exact workflow)
  3. **robots.txt tester + sitemap validity** — confirm the URL isn't
     disallowed and appears in an error-free sitemap; every listed sitemap
     URL should return 200 and be indexable, or Google can deprioritize trust
     in the whole file (see `sitemaps-and-indexnow.md`). (heuristic, carried
     from seed research, not re-verified this pass)
  4. **Crawl Stats report** — look for URL patterns generating high crawl
     volume but low indexing yield (parameterized/faceted URLs, thin
     paginated pages) and disallow them to free up crawl budget for pages
     that matter. (heuristic)
  5. **Request indexing** via URL Inspection — a limited, roughly
     10–50-requests/day lever; treat it as a last-resort nudge for
     high-value pages, not a bulk-indexing fix. (heuristic)
- **Give fixes time before calling them failed.** Google's own troubleshooting
  docs state pages can sit in a duplicate/canonical cluster for up to **two
  weeks** after a fix before re-evaluation completes, and the same lag applies
  broadly to indexing-decision changes. Don't re-diagnose or escalate inside
  that window.
- **New domains carry a trust delay, not a penalty** — typically 3–6 months
  to rank consistently, which active indexing requests and backlinks can
  shorten but not eliminate. (heuristic, carried from the 2026-06-14 seed
  pass, not independently re-verified this session)

## How this shows up in the workflow
Stage 4 (site audit) uses this as the diagnostic entry point whenever a site
looks invisible in search — work the Pages report, URL Inspection, robots/sitemap
checks, and Crawl Stats in that order before concluding a page is broken.
Stage 5 (technical/entity fixes) uses the root-cause list to prioritize what
to actually fix (thin content, internal linking, server response time,
crawl-budget waste) and uses the two-week re-evaluation window and the
3–6 month new-domain trust delay to set realistic expectations for when a fix
should show measurable movement.
