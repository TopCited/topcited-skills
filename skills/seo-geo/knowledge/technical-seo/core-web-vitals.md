---
topic: Core Web Vitals current thresholds and their actual (unquantified) ranking weight
stage-relevance: [4, 5]
last-verified: 2026-10-24
sources:
  - https://web.dev/articles/vitals
  - https://developers.google.com/search/docs/appearance/core-web-vitals (updated 2025-12-10)
  - https://developers.google.com/search/docs/appearance/page-experience (updated 2026-09-22)
  - https://web.dev/blog/crux-experimental-soft-navs/ (2026-10-13)
  - https://developer.chrome.com/docs/crux/release-notes (September 2026 dataset, published 2026-10-13)
  - https://almanac.httparchive.org/en/2025/performance (Web Almanac 2025, July 2025 data)
  - https://www.searchenginejournal.com/google-core-web-vitals-ranking-factor/415533/ (Mueller, 2021)
  - https://www.seroundtable.com/google-page-experience-update-tiebreaker-31880.html
---

# Core Web Vitals

## In plain words
Core Web Vitals measure how fast a page loads, how quickly it responds to a
click or tap, and how much its layout jumps around while loading. Google
says they are used by its ranking systems, but not as a hard gate and not
with a published weight — good scores help, bad scores don't automatically
sink a page that's otherwise the best answer. They're worth fixing mainly
because, unlike backlinks or competitor quality, a site fully controls them.

## What practitioners need to know
- **Current thresholds (unchanged in 2026)**: **LCP (Largest Contentful
  Paint) <= 2.5s**, **INP (Interaction to Next Paint) <= 200ms**, **CLS
  (Cumulative Layout Shift) <= 0.1**, all measured at the **75th percentile
  of page loads**. A page needs a "good" score on **all three
  simultaneously** to pass — there's no averaging across metrics. *(P)*
  - INP replaced FID (First Input Delay) as the responsiveness metric in
    March 2024. *(P)* Some 2026 industry posts claim INP was "confirmed as a
    primary ranking signal with equal weight to LCP and CLS" in a "March
    2026 core update" — **no Google source says this** (the March 2026 core
    update shipped without any CWV-specific statement); do not repeat it.
    (heuristic)
  - **Coming change to watch — soft navigations**: on 2026-10-13 Chrome
    added *experimental* CrUX versions of LCP, INP, and CLS that include
    soft (single-page-app) navigations. Google states "stable Core Web
    Vitals scores remain unchanged while these experimental versions are
    evaluated"; the target for graduating them is May 2027, after which
    Search Console switches to the new data. SPA-heavy sites should check
    the experimental numbers now. *(P)*
- **Actual ranking weight — the honest answer**: Google's page-experience
  doc (updated 2026-09-22) says plainly "Core Web Vitals are used by our
  ranking systems," but also that "there is no single signal" and that
  beyond Core Web Vitals, "other page experience aspects don't directly
  help your website rank higher." *(P)* Google has **never published a
  quantified weight**.
- The most concrete on-record Google statement on magnitude remains **John
  Mueller's 2021 comment**: CWV "is a ranking factor, and it's more than a
  tie-breaker, but it also doesn't replace relevance" — it can matter
  directly, but relevance dominates. *(I, quoting Google)*
- **Debunk: no DOJ antitrust testimony on Core Web Vitals weighting was
  found.** Coverage suggesting otherwise (seroundtable.com,
  searchenginejournal.com) traces back to the same 2021 Mueller comment,
  not trial testimony. Do not cite a DOJ-trial CWV admission. (heuristic —
  absence of evidence)
- **Pass-rate reality check**: **55.9% of origins** had good Core Web
  Vitals in Chrome's September 2026 CrUX dataset (range 55.3–56.4% across
  Apr–Sep 2026; 59.5% under the experimental soft-navigation metrics).
  *(P)* By device, the HTTP Archive Web Almanac 2025 (July 2025 data) put
  passing sites at **48% on mobile and 56% on desktop** — mobile is still
  where most sites fail. *(I)*

## How this shows up in the workflow
Stage 4 (site audit) measures LCP/INP/CLS at the 75th percentile against the
2.5s/200ms/0.1 thresholds and treats a failing metric as a real, fixable
issue rather than a hard ranking blocker; for single-page apps it also
checks the experimental soft-navigation numbers. Stage 5 (technical/entity
fixes) prioritizes CWV fixes as a known, fully-controllable lever — worth
doing precisely because, unlike backlinks or competitor content quality, a
site owns the whole fix — while keeping the framing honest with brand
owners: Google uses it, but doesn't weight it publicly, and it won't
override a fundamentally weaker page's lack of relevance.
