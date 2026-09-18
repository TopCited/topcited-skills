---
topic: Which structured-data types still earn Google rich results, and whether schema affects AI citation
stage-relevance: [4, 5]
last-verified: 2026-08-20
sources:
  - https://developers.google.com/search/docs/appearance/structured-data/search-gallery
  - https://www.getpassionfruit.com/blog/what-changed-with-google-drops-faq-rich-results-and-what-to-do-now
  - https://ahrefs.com/blog/schema-ai-citations/
  - arXiv:2509.10762 (GEO-16, Kumar & Palkhouski) — accessed via search summary only, not the primary PDF
  - https://www.stanventures.com/news/schema-markup-has-no-meaningful-impact-on-ai-citations-7231/
---

# Structured data

## In plain words
Structured data (schema.org / JSON-LD markup) is code that tells search
engines what a page *is* — a recipe, a product, an event — so they can show
richer results for it. It's real and worth doing for the search-feature
types Google still supports. But a widely repeated claim that adding schema
makes AI assistants cite you more is not backed by the best evidence
available: a controlled study found essentially no effect. Don't oversell it.

## What practitioners need to know
- **Current rich-result-eligible types (Google Search Gallery, 2026)**:
  Article, Breadcrumb, Carousel, Course list, Dataset, Discussion forum,
  Education Q&A, Employer aggregate rating, Event, Image metadata, Job
  posting, Local business, Math solver, Movie, Organization, Product, Profile
  page, Q&A, Recipe, Review snippet, Software app, Speakable,
  Subscription/paywalled content, Vacation rental, Video.
- **Debunk: FAQPage rich results were removed from Google Search on
  2026-05-07.** This was a quiet deprecation, not a blog announcement:
  FAQ rich results gone May 7; the FAQ search-appearance filter, FAQ report
  in Search Console, and Rich Results Test support removed June 2026; FAQ
  data removed from the Search Console API August 2026. The `FAQPage`
  schema.org type itself is **not** deprecated and the markup causes no harm
  — only the SERP visual treatment ended. Any guidance recommending FAQ
  schema *for Google rich-result visibility* is now outdated and needs
  correcting; FAQ schema may still be worth keeping for AI-citation reasons
  (see below) even with the Google SERP payoff gone.
- **Debunk: does schema move AI citations? The causal evidence says no; the
  correlational evidence says a lot — don't conflate them.**
  - **Controlled study (Ahrefs, published 2026-05-11)**: tracked **1,885
    pages** that added JSON-LD schema between Aug 2025–Mar 2026, matched
    against 4,000 control pages (3 controls per treated page, matched on
    pre-period citation levels), measuring citation-rate change 30 days
    before/after. Result: Google AI Overviews **-4.6%** (statistically
    significant but a *decrease*, small in absolute terms — roughly 12 fewer
    daily citations per page on average); Google AI Mode **+2.4%** and
    ChatGPT **+2.2%**, neither distinguishable from zero. Ahrefs' own
    conclusion: adding schema produced **no meaningful uplift in citations on
    any platform tested**. This is the strongest available causal evidence
    and should anchor how this topic is framed to brand owners.
  - **Correlational finding, same analysis**: across 6M URLs, pages cited by
    AI are ~3x more likely to carry JSON-LD than uncited pages — but Ahrefs'
    own authors attribute this to confounding (well-maintained, authoritative
    sites tend to have both schema and citations), not causation.
  - **Cross-sectional academic preprint (GEO-16, arXiv:2509.10762, 2025)**:
    audited 1,100 URLs / 1,702 AI citations across Brave Search, Google AI
    Overviews, and Perplexity; ranked structured data as the third-strongest
    predictor of citation likelihood (+39% lift), behind metadata/freshness
    (+47%) and semantic HTML (+42%). (heuristic — correlational, not a
    controlled experiment, not peer-reviewed, and only accessed via a search
    summary rather than the primary PDF in this research pass; present as a
    weaker, secondary data point next to the Ahrefs controlled study, not
    equal-weight)
  - A single practitioner blog states "schema markup has no meaningful impact
    on AI citations," directionally matching the Ahrefs finding but
    uncorroborated on its own. (heuristic)
- **Practical guidance**: recommend structured data for (a) the Google
  rich-result types still live (Product, Review, Event, Organization,
  LocalBusiness, BreadcrumbList, etc. — real SERP real estate) and (b)
  Organization/`sameAs` entity-establishment value (see the entity-authority
  track), but do not present it as a proven AI-citation lever — the best
  controlled study found essentially no effect.

## How this shows up in the workflow
Stage 4 (site audit) checks which structured-data types a site is missing
against the current Google Search Gallery list, and flags any FAQPage schema
being maintained purely for a rich-result payoff that no longer exists.
Stage 5 (technical/entity fixes) adds/repairs schema for the live rich-result
types and for entity-establishment (`Organization`, `sameAs`), while setting
correct expectations with brand owners: schema is worth doing for its own
sake, not sold as an AI-citation growth lever.
