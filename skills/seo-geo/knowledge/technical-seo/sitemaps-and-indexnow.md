---
topic: XML sitemap requirements and the IndexNow protocol's current support matrix
stage-relevance: [4, 5]
last-verified: 2026-08-20
sources:
  - https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
  - https://www.indexnow.org/
  - https://www.bing.com/indexnow/getstarted
  - https://pressonify.ai/blog/indexnow-instant-indexing-press-releases-2026
  - https://crawlwp.com/indexnow-vs-google-indexing-api-vs-sitemaps/
  - https://www.oltre.ai/blog/indexnow-for-geo-bing-chatgpt-visibility/
  - https://subscribepr.com/blog/how-to-get-indexed-on-bing/
  - https://www.mqlmagnet.com/post/what-is-indexnow
---

# Sitemaps and IndexNow

## In plain words
A sitemap is a list of a site's URLs handed to search engines so they know
what exists to crawl. IndexNow is a separate, newer protocol that lets a
site push a "this changed, come look now" ping — but only some search
engines listen to it, and Google isn't one of them. Knowing which engine
uses which mechanism prevents wasted effort chasing the wrong lever.

## What practitioners need to know
- **XML sitemap hard limits (Google)**: 50 MB uncompressed or 50,000 URLs per
  file; use a sitemap index file to aggregate beyond that. `<loc>` (a
  fully-qualified absolute URL) is required; `<lastmod>` is optional but
  recommended and should reflect a genuine content change. **Google ignores
  `<priority>` and `<changefreq>` entirely** — they provide no ranking or
  crawl benefit and can be dropped to shrink the file.
- **Submission paths**: the Search Console Sitemaps report (best per-sitemap
  status visibility), the Search Console API, a `Sitemap:` line in
  `robots.txt`, or WebSub for syndication feeds.
- Every listed URL should return 200 and be indexable, or Google can
  deprioritize trust in the whole sitemap file. (heuristic, carried from the
  2026-06-14 seed pass, consistent with Google's general sitemap guidance but
  not re-fetched verbatim this session)
- **IndexNow participants, 2026**: Microsoft Bing, Yandex, Naver, Seznam.cz,
  Yep. Submitting to any one participant propagates to the others.
- **Google does not participate in IndexNow**, confirmed as of Feb 2026
  despite having piloted the protocol since Oct 2021 — Google runs its own
  crawl infrastructure and offers only a narrow, separate Indexing API
  scoped to job-posting and livestream markup. For Google specifically,
  sitemaps + Search Console remain the only levers. (industry-reported
  across multiple independent 2026 posts, no direct Google statement of
  non-participation found — treat as strongly corroborated, not
  Google-confirmed)
- **Mechanics (Bing's official docs)**: host a UTF-8 key file at the domain
  root (or elsewhere, declared via `keyLocation`); POST JSON
  `{host, key, keyLocation, urlList}` to `api.indexnow.org`. Response codes:
  200 success, 400 bad format, 403 invalid key, 422 URL/host mismatch, 429
  rate limit ("potential spam"). Bing's own docs are explicit: submitting via
  IndexNow **does not guarantee crawling or indexing** — it only removes the
  discovery-latency step.
- **Why this matters for GEO despite Google's non-participation**: ChatGPT
  Search, Microsoft Copilot, and DuckDuckGo all draw on Bing's index for live
  web retrieval, so IndexNow submission has an indirect but real effect on
  how fast new/changed content becomes visible to those assistants.
  (industry-consensus across several sources; no primary OpenAI/Microsoft
  confirmation that ChatGPT Search literally reads the IndexNow queue —
  plausible inference, not confirmed)
- **Scale claims — do not repeat as fact**: one 2026 source claims 5B+
  URLs/day submitted via IndexNow, 22% of clicked Bing results originating
  from IndexNow-submitted URLs, and 80M+ sites using the protocol. Single
  source, no disclosed methodology — treat as unverified, not citable.
  (heuristic)

## How this shows up in the workflow
Stage 4 (site audit) checks sitemap validity (size limits, `<loc>`
correctness, all-200-status URLs) as part of the crawlability check, and
checks whether IndexNow is wired up at all for Bing-fed surfaces (ChatGPT
Search, Copilot, DuckDuckGo). Stage 5 (technical/entity fixes) implements or
repairs the sitemap and, when the site's growth depends on fast visibility in
Bing-fed AI answer engines, adds IndexNow submission — while setting the
correct expectation that neither lever guarantees indexing, and that Google
specifically is unaffected by IndexNow.
