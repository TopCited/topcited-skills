---
topic: XML sitemap requirements and the IndexNow protocol's current support matrix
stage-relevance: [4, 5]
last-verified: 2026-10-24
sources:
  - https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap (updated 2026-07-08)
  - https://developers.google.com/search/blog/2023/06/sitemaps-lastmod-ping (sitemap ping endpoint retired)
  - https://developers.google.com/search/apis/indexing-api/v3/quickstart (updated 2026-10-16)
  - https://www.indexnow.org/faq
  - https://www.indexnow.org/searchengines.json
  - https://www.indexnow.org/documentation
  - https://www.bing.com/indexnow/getstarted
  - https://www.oltre.ai/blog/indexnow-for-geo-bing-chatgpt-visibility/
  - https://pressonify.ai/blog/indexnow-instant-indexing-press-releases-2026
---

# Sitemaps and IndexNow

## In plain words
A sitemap is a list of a site's URLs handed to search engines so they know
what exists to crawl. IndexNow is a separate, newer protocol that lets a
site push a "this changed, come look now" ping — but only some search
engines listen to it, and Google isn't one of them. Knowing which engine
uses which mechanism prevents wasted effort chasing the wrong lever.

## What practitioners need to know
- **XML sitemap hard limits (Google)**: "All formats limit a single sitemap
  to 50MB (uncompressed) or 50,000 URLs"; use a sitemap index file to
  aggregate beyond that. `<loc>` (a fully-qualified absolute URL) is
  required. `<lastmod>` is optional but useful: Google uses it only "if
  it's consistently and verifiably" accurate, and it should reflect "the
  last significant update." **"Google ignores `<priority>` and
  `<changefreq>` values"** — they can be dropped to shrink the file. *(P)*
- **Submission paths**: the Search Console Sitemaps report (best per-sitemap
  status visibility), the Search Console API, a `Sitemap:` line in
  `robots.txt`, or WebSub for syndication feeds. *(P)* The old
  `google.com/ping?sitemap=` endpoint was retired in 2023 — don't wire it
  into a deploy hook. *(P)*
- Every listed URL should return 200 and be indexable; a sitemap full of
  redirects, 404s, or noindexed URLs wastes crawl and muddies the canonical
  signal. (heuristic — consistent with Google's guidance to list only
  canonical URLs, but Google doesn't document a "whole-file distrust"
  penalty)
- **IndexNow participants (indexnow.org, 2026-10)**: Microsoft Bing,
  Yandex, Naver, Seznam.cz, Yep, and **Amazon** (joined 2025); the
  protocol's `searchengines.json` also lists an Internet Archive endpoint.
  Submitting to any one participant shares the URLs with all the others.
  *(P)*
- **Google does not participate in IndexNow** — it isn't on indexnow.org's
  list as of 2026-10. Google said in Nov 2021 that it would test the
  protocol, and nothing came of it. (heuristic for the 2021 history; *(P)*
  for the current list) Google's Indexing API is not a substitute: it "can
  only be used to crawl pages with either `JobPosting` or `BroadcastEvent`
  embedded in a `VideoObject`." *(P)* For Google, sitemaps + Search Console
  remain the levers.
- **Mechanics (IndexNow/Bing docs)**: host a UTF-8 key file at the domain
  root (or elsewhere, declared via `keyLocation`); POST JSON `{host, key,
  keyLocation, urlList}` (up to 10,000 URLs per POST) to `api.indexnow.org`
  or any participant. Response codes: 200 success, **202 accepted (key
  validation pending)**, 400 bad format, 403 invalid key, 422 URL/host
  mismatch, 429 too many requests. Bing is explicit: "Using IndexNow does
  not guarantee that web pages will be crawled or indexed" — it only
  removes the discovery-latency step. *(P)*
- **Why this matters for GEO despite Google's non-participation**: Microsoft
  Copilot grounds on Bing's index, and DuckDuckGo's results lean on Bing, so
  IndexNow speeds up how fast new/changed content can surface there. *(P for
  Copilot/Bing; I for DuckDuckGo)* OpenAI names Bing as one of ChatGPT
  search's providers, though 2026 measurements show Google-derived results
  and OpenAI's own index carrying most of the load (see
  `../foundations/how-llms-source-answers.md`) — so faster Bing indexing may
  help ChatGPT at the margin, but don't sell IndexNow as a ChatGPT lever.
  (heuristic)
- **Scale claims — do not repeat as fact**: one 2026 source claims 5B+
  URLs/day submitted via IndexNow, 22% of clicked Bing results originating
  from IndexNow-submitted URLs, and 80M+ sites using the protocol. Single
  source, no disclosed methodology — treat as unverified, not citable.
  (heuristic)

## How this shows up in the workflow
Stage 4 (site audit) checks sitemap validity (size limits, `<loc>`
correctness, all-200-status URLs) as part of the crawlability check, and
checks whether IndexNow is wired up at all for Bing-fed surfaces (Copilot,
Bing's AI summaries, DuckDuckGo). Stage 5 (technical/entity fixes)
implements or repairs the sitemap and, when the site's growth depends on fast
visibility in Bing-fed AI answer engines, adds IndexNow submission — while
setting the correct expectation that neither lever guarantees indexing, and
that Google specifically is unaffected by IndexNow.
