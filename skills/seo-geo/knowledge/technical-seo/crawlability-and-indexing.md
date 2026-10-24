---
topic: Diagnosing why pages don't get indexed and fixing the underlying crawl/indexing gap
stage-relevance: [4, 5]
last-verified: 2026-10-24
sources:
  - https://support.google.com/webmasters/answer/7440203 (Search Console Page indexing report)
  - https://support.google.com/webmasters/answer/9012289 (URL Inspection tool)
  - https://developers.google.com/search/docs/crawling-indexing/canonicalization-troubleshooting (updated 2026-08-21)
  - https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt (updated 2026-10-23)
  - https://www.onely.com/blog/how-to-fix-discovered-currently-not-indexed-in-google-search-console/
  - https://www.outrank.so/blog/how-to-fix-crawled-but-not-indexed
  - https://www.clickrank.ai/mueller-explains-indexing-errors/
  - heuristic
---

# Crawlability and indexing

## In plain words
If a page isn't showing up in Google at all, the first question isn't "why
don't we rank" — it's "does Google even know this page is worth storing."
Google applies a quality bar to what it keeps in its index, and a page can
be fully crawlable and still sit in limbo because Google has decided it
isn't worth prioritizing. Diagnosing this means working through Search
Console systematically rather than guessing.

## What practitioners need to know
- **"Discovered — currently not indexed"** — Google's own definition: "The
  page was found by Google, but not crawled yet. Typically, Google wanted to
  crawl the URL but this was expected to overload the site; therefore Google
  rescheduled the crawl." *(P)* Practitioners read it more broadly as a
  crawl-priority decision driven by site-wide crawl demand, not just server
  capacity. (heuristic — pattern converges across ~8 practitioner sources)
- Converging root causes practitioners point to: thin/duplicate/AI-mass-produced
  content lowering site-wide crawl demand, poor internal linking / orphaned
  pages, and slow server response or render timeouts that cause Googlebot to
  abandon a crawl before indexing is even evaluated. (heuristic)
- **Diagnosis order matters** — work top-down, not URL-by-URL first:
  1. **Search Console → Pages report ("Page indexing")** for the aggregate,
     site-wide breakdown (`Discovered — currently not indexed`, `Crawled —
     currently not indexed`, `Duplicate, Google chose different canonical
     than user`, `Excluded by 'noindex' tag`, etc.) before drilling into
     individual URLs. *(P for the report; heuristic for the ordering)*
  2. **URL Inspection tool**, per specific URL — shows the indexed version
     Google last saw, and "Test live URL" fetches the page now to catch a
     robots.txt block, a `noindex` tag, or a server error that differs from
     the indexed snapshot. *(P)*
  3. **robots.txt + sitemap validity** — confirm the URL isn't disallowed
     (Google reads only the first 500 KiB of robots.txt and caches it up to
     24h *(P)*) and appears in an error-free sitemap (see
     `sitemaps-and-indexnow.md`). AI-crawler rules belong in the same file —
     see `ai-crawler-access.md` before adding blanket bot blocks.
  4. **Crawl Stats report** — look for URL patterns generating high crawl
     volume but low indexing yield (parameterized/faceted URLs, thin
     paginated pages) and disallow them to free up crawl budget for pages
     that matter. (heuristic)
  5. **Request indexing** via URL Inspection — Google says only "there is a
     daily limit" and that indexing "typically takes only a day or so" after
     a request; it publishes no number. Practitioner reports put the cap
     around 10–50 per property per day (heuristic). Treat it as a nudge for
     high-value pages, not a bulk-indexing fix. Don't confuse it with the
     Indexing API (200 publish requests/day, and only for job-posting and
     livestream pages). *(P)*
- **Give fixes time before calling them failed.** Google's troubleshooting
  doc says "Google might hold pages in a duplicate cluster for up to two
  weeks" after a fix. *(P)* Applying a similar wait to other indexing-state
  changes is a reasonable inference, not a Google statement. (heuristic)
  Don't re-diagnose or escalate inside that window.
- **New domains carry a trust delay, not a penalty** — typically 3–6 months
  to rank consistently, which active indexing requests and backlinks can
  shorten but not eliminate. (heuristic, not independently re-verified)

## How this shows up in the workflow
Stage 4 (site audit) uses this as the diagnostic entry point whenever a site
looks invisible in search — work the Pages report, URL Inspection, robots/sitemap
checks, and Crawl Stats in that order before concluding a page is broken.
Stage 5 (technical/entity fixes) uses the root-cause list to prioritize what
to actually fix (thin content, internal linking, server response time,
crawl-budget waste) and uses the two-week re-evaluation window and the
3–6 month new-domain trust delay to set realistic expectations for when a fix
should show measurable movement.
