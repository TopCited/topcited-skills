---
topic: Core Web Vitals current thresholds and their actual (unquantified) ranking weight
stage-relevance: [4, 5]
last-verified: 2026-08-20
sources:
  - https://web.dev/articles/vitals
  - https://developers.google.com/search/docs/appearance/core-web-vitals
  - https://tworowstudio.com/core-web-vitals-q2-2026/
  - https://www.seroundtable.com/google-page-experience-update-tiebreaker-31880.html
  - https://www.searchenginejournal.com/google-core-web-vitals-ranking-factor/415533/
  - heuristic (2026-06-14 seed research pass, ~55% pass-rate figure, not re-verified)
---

# Core Web Vitals

## In plain words
Core Web Vitals measure how fast a page loads, how quickly it responds to a
click or tap, and how much its layout jumps around while loading. Google
uses them as one input into ranking, but not a hard gate and not a
publicly weighted one — good scores help, bad scores don't automatically
sink a page that's otherwise the best answer. They're worth fixing mainly
because, unlike backlinks or competitor quality, a site fully controls them.

## What practitioners need to know
- **Current thresholds (unchanged at the metric-definition level)**:
  **LCP (Largest Contentful Paint) <= 2.5s**, **INP (Interaction to Next
  Paint) <= 200ms**, **CLS (Cumulative Layout Shift) <= 0.1**, all measured
  at the **75th percentile of page loads**. A page needs a "good" score on
  **all three simultaneously** to pass — there's no averaging across
  metrics.
  - INP replaced FID (First Input Delay) as the responsiveness metric back
    in March 2024. Multiple 2026 sources describe INP as having been
    "confirmed as a primary ranking signal with equal weight to LCP and CLS"
    following a "March 2026 core update" — **this specific characterization
    is industry-sourced, not found in a primary Google announcement in this
    research pass; do not state it as confirmed fact.** (heuristic)
- **Actual ranking weight — the honest answer**: Google's own current
  developer docs describe page experience (of which CWV is a part) as
  something that "aligns with what our core ranking systems seek to
  reward" — notably *not* phrased as "is a ranking factor" in isolation —
  and Google has **never published a quantified weight**.
- The most concrete on-record Google statement on magnitude remains **John
  Mueller's 2021 Reddit comment**: CWV "is a ranking factor, and it's more
  than a tie-breaker, but it also doesn't replace relevance" — it can matter
  directly, but relevance dominates.
- **Debunk: no DOJ antitrust testimony on Core Web Vitals weighting was
  found.** Coverage suggesting otherwise (seroundtable.com,
  searchenginejournal.com) all traces back to the same 2021 Mueller comment,
  not trial testimony. Do not cite a DOJ-trial CWV admission — it wasn't
  found in this research pass and may not exist. Correct this if it's
  assumed anywhere downstream.
- **Pass-rate reality check**: roughly **55%** of sites pass Core Web Vitals
  overall. (heuristic, carried from the 2026-06-14 seed pass, not
  independently re-verified this session — a fresh CrUX-based or HTTP
  Archive Almanac number would be the primary source to pull if a precise
  current figure is needed)

## How this shows up in the workflow
Stage 4 (site audit) measures LCP/INP/CLS at the 75th percentile against the
2.5s/200ms/0.1 thresholds and treats a failing metric as a real, fixable
issue rather than a hard ranking blocker. Stage 5 (technical/entity fixes)
prioritizes CWV fixes as a known, fully-controllable lever — worth doing
precisely because, unlike backlinks or competitor content quality, a site
owns the whole fix — while keeping the framing honest with brand owners:
it supports ranking outcomes, it isn't a scored, publicly-weighted input, and
it won't override a fundamentally weaker page's lack of relevance.
