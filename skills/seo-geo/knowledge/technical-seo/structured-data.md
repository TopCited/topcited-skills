---
topic: Which structured-data types still earn Google rich results, and whether schema affects AI citation
stage-relevance: [4, 5]
last-verified: 2026-10-24
sources:
  - https://developers.google.com/search/docs/appearance/structured-data/search-gallery (updated 2026-10-16)
  - https://developers.google.com/search/updates (Search Central documentation changelog — FAQ, Practice problems, Dataset, Book Actions entries)
  - https://developers.google.com/search/blog/2025/06/simplifying-search-results (2025-06-12)
  - https://developers.google.com/search/blog/2023/08/howto-faq-changes
  - https://www.searchenginejournal.com/google-drops-faq-rich-results-from-search/574429/ (2026-05-10)
  - https://developers.google.com/search/docs/fundamentals/ai-optimization-guide (updated 2026-07-10)
  - https://developers.google.com/search/docs/appearance/ai-features (updated 2025-12-10)
  - https://ahrefs.com/blog/schema-ai-citations/ (2026-05-11)
  - https://arxiv.org/html/2509.10762v1 (GEO-16, Kumar & Palkhouski, 2025-09 preprint)
  - https://www.stanventures.com/news/schema-markup-has-no-meaningful-impact-on-ai-citations-7231/
---

# Structured data

## In plain words
Structured data (schema.org / JSON-LD markup) is code that tells search
engines what a page *is* — a recipe, a product, an event — so they can show
richer results for it. It's real and worth doing for the search-feature
types Google still supports, and Google has been steadily retiring the rest.
But a widely repeated claim that adding schema makes AI assistants cite you
more is not backed by the best evidence available: Google says no special
markup is needed for its AI features, and a controlled study found
essentially no effect. Don't oversell it.

## What practitioners need to know
- **Current rich-result-eligible types (Google Search Gallery, updated
  2026-10-16)**: Article, Breadcrumb, Carousel, Course list, Dataset,
  Discussion forum, Education Q&A, Employer aggregate rating, Event, Image
  metadata, Job posting, Local business, Math solver, Movie, Organization,
  Product, Profile page, Q&A, Recipe, Review snippet, Software app,
  Speakable, Subscription/paywalled content, Vacation rental, Video. *(P)*
  - Caveat: since 2025-11-05 Google says Dataset markup "is only used by
    Dataset Search, and not Google Search" — it's still listed, but it won't
    produce a Google Search rich result. *(P)*
- **What Google has retired, in order** *(P, Search Central blog/changelog)*:
  - HowTo rich results — limited then fully deprecated (Aug–Sep 2023); FAQ
    limited to well-known government and health sites at the same time.
  - Sitelinks search box — stopped showing 2024-11-21.
  - 2025-06-12 "simplifying search results": Course Info, ClaimReview,
    Estimated Salary, Learning Video, Special Announcement, Vehicle Listing
    phased out (docs removed by 2025-09). **Book Actions was announced too,
    but the deprecation was reversed on 2025-11-05** because a feature still
    uses the markup — don't list it as retired.
  - Practice problems — phased out (announced 2025-11; docs and Search
    Console support removed 2026-01).
  - **FAQ rich results — removed from Google Search on 2026-05-07.** This
    was a changelog entry, not a blog announcement: FAQ results stopped
    showing May 7; the FAQ search-appearance filter, FAQ report, and Rich
    Results Test support were scheduled to go in June 2026 (FAQ docs removed
    2026-06-15); Search Console API support scheduled for removal in August
    2026. The `FAQPage` schema.org type itself is **not** deprecated and the
    markup causes no harm — only the SERP treatment ended. Any guidance
    recommending FAQ schema *for Google rich-result visibility* is outdated.
  - No 2026 deprecation of Q&A, Course list, or Math solver was found; Google
    actually added new Discussion forum / QAPage properties on 2026-03-24.
- **Google on structured data and its AI features**: "There are no additional
  technical requirements" to appear in AI Overviews or AI Mode, and "no
  special schema.org structured data that you need to add"; the AI
  optimization guide repeats that structured data "isn't required for
  generative AI search," while still recommending it for rich-result
  eligibility. *(P)*
- **Debunk: does schema move AI citations? The causal evidence says no; the
  correlational evidence says a lot — don't conflate them.**
  - **Controlled study (Ahrefs, published 2026-05-11)**: tracked **1,885
    pages** that added JSON-LD schema between Aug 2025–Mar 2026 against a
    matched control group (Ahrefs reports "4,000" controls described as
    three per treated page — the counts don't reconcile in the article
    itself), using difference-in-differences over a ±30-day window. Result:
    Google AI Overviews **-4.6%** (statistically significant but a
    *decrease*, roughly 12 fewer daily citations per page on average);
    Google AI Mode **+2.4%** and ChatGPT **+2.2%**, neither distinguishable
    from zero. Ahrefs' own conclusion: adding schema produced **no
    meaningful uplift in citations on any platform tested**. *(I)* Caveats
    worth stating: every treated page already had 100+ AI Overview
    citations, both groups were declining before treatment, and only JSON-LD
    (not microdata/RDFa) was studied. It is still the strongest available
    causal evidence and should anchor how this topic is framed to brand
    owners.
  - **Correlational finding, same analysis**: across 6M URLs, pages cited by
    AI are "almost three times" more likely to carry JSON-LD than uncited
    pages — but Ahrefs' own authors attribute this to confounding
    (well-maintained, authoritative sites tend to have both schema and
    citations), not causation. *(I)*
  - **Cross-sectional academic preprint (GEO-16, arXiv:2509.10762, Kumar &
    Palkhouski, 2025-09)**: 70 product-intent prompts, 1,702 citations,
    1,100 unique URLs across Brave Summary, Google AI Overviews, and
    Perplexity; structured data correlated with citation at r=0.63 (a
    reported "+39%" citation impact), behind metadata/freshness (r=0.68,
    "+47%") and semantic HTML (r=0.65, "+42%"). The paper does not explain
    how those percentages are computed, so don't call them "lift."
    (heuristic — correlational, not peer-reviewed, data not released; a
    weaker, secondary data point next to the Ahrefs controlled study)
  - A single practitioner blog states "schema markup has no meaningful impact
    on AI citations," directionally matching the Ahrefs finding but
    uncorroborated on its own. (heuristic)
- **Practical guidance**: recommend structured data for (a) the Google
  rich-result types still live (Product, Review snippet, Event,
  Organization, Local business, Breadcrumb, etc. — real SERP real estate)
  and (b) Organization/`sameAs` entity-establishment value (see the
  entity-authority track), but do not present it as a proven AI-citation
  lever — Google says it isn't required for its AI features and the best
  controlled study found essentially no effect.

## How this shows up in the workflow
Stage 4 (site audit) checks which structured-data types a site is missing
against the current Google Search Gallery list, and flags any markup being
maintained purely for a rich-result payoff that no longer exists (FAQPage,
HowTo, Practice problem, and the 2025 retired types). Stage 5
(technical/entity fixes) adds/repairs schema for the live rich-result types
and for entity-establishment (`Organization`, `sameAs`), while setting
correct expectations with brand owners: schema is worth doing for its own
sake, not sold as an AI-citation growth lever.
