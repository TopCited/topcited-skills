---
topic: Setting an SEO/GEO visibility baseline and choosing the right KPIs
stage-relevance: [2, 8]
last-verified: 2026-10-24
sources:
  - https://www.trysight.ai/blog/ai-visibility-audit-template
  - https://skyscale.com.au/blogs/prompt-testing-ai-visibility-diy
  - https://discoveredlabs.com/blog/free-ai-visibility-audit-checklist
  - https://www.fratzkemedia.com/insights/ai-visibility-audit
  - https://tajo.io/blog/the-6-best-seo-audit-tools/
  - https://seeklab.io/blog/best-free-seo-audit-tools-for-small-business-in-2026-tested-and-compared/
  - https://support.google.com/analytics/answer/9164320 (GA4 release notes, 2026-05-13 "New AI Assistant traffic measurement")
  - https://support.google.com/analytics/answer/9756891 (GA4 default channel group definitions)
  - https://www.searchenginejournal.com/google-analytics-adds-ai-assistant-as-default-channel-group/574974/
  - https://weekerp.com/en/blog/ga4-ai-assistant-channel-what-it-tracks-and-misses
  - https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports (Search Console generative AI performance reports, 2026-06)
  - https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview
  - https://clarity.microsoft.com/blog/citations-now-generally-available/ (Microsoft Clarity AI Citations, GA 2026-05-13)
  - https://ahrefs.com/benchmarks/ai-vs-search (AI share of web traffic, updated 2026-10-22)
  - https://seranking.com/blog/ai-traffic-research-study/ (AI referral traffic share by assistant, 2026-06-18)
  - https://writesonic.com/blog/geo-kpis-every-brand-should-track
  - https://analyticahouse.com/blogs/how-to-generative-engine-optimization-geo-kpi-reporting-model-for-ai-visibility
  - https://www.similarweb.com/blog/marketing/geo/what-is-geo/
  - https://www.searchpilot.com/resources/blog/what-is-seo-split-testing
  - https://www.searchpilot.com/resources/blog/the-math-behind-searchpilot-how-seo-a/b-testing-actually-works
  - https://arxiv.org/abs/2603.08924 (Sielinski, "Quantifying Uncertainty in AI Visibility", v3 2026-08-26)
  - https://arxiv.org/abs/2604.07585 (Schulte, Bleeker, Kaufmann, "Don't Measure Once: Measuring Visibility in AI Search", 2026-04-08)
  - https://arxiv.org/abs/2607.13304 (Żatuchin, variance-components decomposition of LLM brand answers, 2026-07-14)
  - TopCited internal research (LLM-monitoring industry study, 2026-08 — unpublished), itself citing petralabs.com (no public URL found for the specific figures)
  - heuristic
---

# Baselines and KPIs

## In plain words
A baseline is a snapshot of how visible a brand is today — in Google and in
AI answers — taken before anything changes, so later progress can be
measured against something real instead of a feeling. It doesn't require
expensive tools: a spreadsheet of 15–30 real customer questions, checked by
hand across a few AI assistants and Google Search Console, is essentially
the same method the paid vendors automate at scale. What gets tracked after
that differs by channel — SEO has hard, first-party numbers (rankings,
clicks, indexing), while GEO mostly has *directional* signals (mention
rate, citation rate) because AI answers rarely leave a trackable trail back
to the site.

## What practitioners need to know

### Setting a baseline cheaply
**GEO — manual prompt audit (no paid tool required):** build a spreadsheet
with one row per (prompt × engine): Query, Engine, Brand Mentioned (Y/N),
Brand Cited with Link (Y/N), Citation Position, Cited URL, Competitor
Mentioned, Competitor Cited, Intent Category. Run the prompts **logged
out/incognito** across at least 3 major platforms (ChatGPT, Claude,
Perplexity, Gemini are the commonly named four) to avoid personalization
bias. Use **15–30 prompts** spread across brand, category, comparison, and
problem-based question types for a first pass — enough to show a pattern
without becoming a chore; a 10–15-prompt × 3-platform manual audit takes
roughly 2–4 hours. Re-run on a fixed cadence (monthly or quarterly) and log
the visibility rate each time to turn a one-off audit into a trend. *(I)*
This is the correct low-cost entry point for a brand owner, and it's worth
saying explicitly: "this is what the $200+/mo tools do, just manual and
monthly instead of automated and daily" — that framing sets expectations
correctly without oversell.

**SEO — free-tool stack:** **Google Search Console** (indexing status,
query/impression/click/position data, Core Web Vitals, URL Inspection) is
the single best free baseline instrument because it's first-party Google
data, not an estimate. Add **Screaming Frog**'s free tier (up to 500 URLs)
for a technical/crawl-depth baseline, **Ahrefs Webmaster Tools** (free with
GSC-verified ownership) for backlink/site-health visibility, and
**PageSpeed Insights/Lighthouse** for Core Web Vitals detail. *(I)*

**GEO via first-party analytics (GA4):** GA4 added a native **"AI
Assistant" default channel group** on 2026-05-13 — sessions with a referrer
matching a recognized AI assistant are auto-tagged `medium = ai-assistant`
with no setup required. *(P)* Google's release note names "chatbots like
ChatGPT, Gemini, and Claude," and the channel-definition doc gives
"ChatGPT, Gemini, Deepseek, Copilot, or Grok" as examples — both are
examples, not a full list. *(P)* The same doc says the channel **excludes
Google's AI Overviews and AI Mode** — those clicks stay in Organic Search.
*(P)* **Important limitation for honest baselining:** GA4 only captures
traffic with a matching referrer header —
in-app AI browsers, copy-pasted links, and zero-click answers (the majority
of GEO's value) land in Direct or don't appear at all. It also processes
**forward-only**: AI traffic from before 2026-05-13 stays misclassified, so
GA4 cannot retroactively establish a historical AI-traffic baseline. *(I)*
For scale: AI assistants sent **~0.3–0.4%** of total web traffic in 2026
(Ahrefs: 0.43% across 115K sites in Sept 2026; SE Ranking: 0.32% across 101K
sites in Jan–Apr 2026), with ChatGPT ~75–81% of it. *(I)* A small AI-referral
number is normal, not a tracking failure.

**First-party AI-visibility data from the platforms themselves** *(P)*:
- **Google Search Console — generative AI performance reports** (all sites
  worldwide since 2026-08-31): impressions in AI Overviews, AI Mode, and
  Discover's AI features, by page, country, device, and date — no clicks or
  queries.
- **Bing Webmaster Tools — AI Performance** (preview 2026-02, expanded
  2026-06 and 2026-10): citations, cited pages, a sample of grounding
  queries, and topic clusters for Copilot and Bing's AI summaries.
- **Microsoft Clarity — AI Citations** (GA 2026-05-13): page citations and
  grounding queries alongside AI referral traffic, Copilot/Bing only.
No equivalent first-party report exists for ChatGPT, Perplexity, Claude, or
the Gemini app — for those, prompt-based monitoring is the only option.

### KPIs — SEO vs. GEO
**SEO KPIs** are established and unchanged by AI-search disruption: organic
sessions, keyword rankings, click-through rate by position, indexed-page
coverage, Core Web Vitals pass rate, backlink count/referring domains,
conversion rate from organic traffic — all directly measurable in GSC/GA4
with no vendor tool required. *(heuristic — standard, uncontroversial
practitioner consensus)*

**GEO KPIs** converge, across multiple 2026 sources, on roughly seven:
brand visibility (% of runs/prompts mentioning the brand), share of voice,
sentiment, domain/citation influence (cited as the source vs. just named),
topical visibility (breadth across a category, not just branded prompts),
prompt-level visibility (granular, not aggregated), and AI referral traffic
+ conversions. A tighter core set often used: citation rate, share of voice,
AI referral traffic, and conversion value from AI-sourced visitors. *(I)*

**The structural measurement gap:** an often-quoted "54% plan vs. 23%
measure" framing actually splices two different 2026 sources (a vendor
survey on GEO plans and an eMarketer figure on measurement investment), so
don't cite it as one survey — but the direction is consistent: far more
marketers say GEO is part of their strategy than say they can measure its
impact. (heuristic) Two structural reasons: most AI answers are zero-click
(no referral session to attribute), and the most valuable AI influence —
landing on a shortlist a user later acts on outside the chat — happens
*before* any trackable touchpoint exists. The platform reports above give
impressions and citations for Google's and Microsoft's AI surfaces, but none
reports the query-level, conversion-level picture SEO is used to.

**Recommendation:** state GEO KPIs as *leading/directional* indicators
(visibility, share of voice, citation rate), not *outcome* metrics — the
outcome metric (assisted conversion) is mostly invisible by construction.
Don't imply GEO tooling, including TopCited's, can deliver attribution it
structurally cannot.

### Attributing improvement honestly
**SEO:** the only rigorous, causal method in production use is split/holdout
testing, not before/after comparison. SEO split testing (pioneered by
SearchPilot) randomly assigns similar pages to treatment/control, models
what the treatment group's traffic *would have been* absent the change, and
compares that counterfactual to what actually happened — isolating the
change from seasonality, algorithm updates, and competitor moves. *(I)* The
underlying technique traces to Google's own **CausalImpact** (open-source
Bayesian structural time-series package); SearchPilot replaced it in 2019
with a purpose-built model because general CausalImpact under-modeled
organic search's layered (weekly + algorithm-update + competitive)
seasonality. *(P/I)* Without SearchPilot-scale infrastructure, the honest
fallback is correlational before/after reporting **with explicit caveats**
(note concurrent algorithm updates, seasonality, competitor activity in the
same window) — never a bare "traffic went up X%" claim. *(heuristic)*

**GEO:** honest attribution is currently unsolved industry-wide, not a
TopCited gap. A genuine 5-point visibility shift is detected only ~11% of
the time at 100 runs, and rank ordering stabilizes ~8x faster than
magnitudes (~80 runs for Spearman ≥0.90) *(I — TopCited internal research,
citing Petra Labs; no public URL for these figures)*. Public preprints make
the same point — single measurements of AI visibility carry wide
uncertainty and unstable ranks, so visibility should be measured repeatedly
with confidence intervals (arXiv:2603.08924, 2604.07585). One
variance-components study found within-prompt resampling (34.8%) and query
language (26.5%) dwarf brand identity (1.5%) — though it measured
*sentiment*, not visibility (arXiv:2607.13304). *(I)* Most of the "signal"
in a single before/after comparison is noise, not the brand's actual
standing. Never attribute a single-period visibility
delta to a specific content change without (a) a frozen, versioned prompt
set for both periods, (b) a stated sample size, and (c) a stated noise
floor below which deltas are suppressed. No major vendor publishes a causal
GEO-attribution methodology — every one frames visibility metrics as
"directional." Track the leading indicator over a rolling window long
enough to exceed the noise floor; correlate loosely with content changes;
never claim causation from one before/after comparison. *(I/heuristic)*

## How this shows up in the workflow
Stage 2 (baseline monitoring) uses this file when deriving the initial
query set and triggering the first run — the "before photo": freeze the
prompt set, record its size, and treat that first run's mention rate as the
baseline against which everything later is compared, per `monitoring.md`'s
create-query-set → add-queries → run flow. TopCited's own `metrics/summary`
and `metrics/visibility` endpoints are the automated version of the manual
spreadsheet audit above — one row per query per engine, aggregated —  so
the same honesty rules apply: don't read a single early run as definitive,
and don't promise attribution the underlying data can't support.

Stage 8 (review & ongoing monitoring) uses this file when comparing current
numbers against the Stage 2 baseline: apply the noise-floor and
frozen-prompt-set caveats before claiming any KPI moved, keep SEO KPIs
(GSC/GA4-based) and GEO KPIs (monitoring-run-based) in separate frames
rather than blending them, and when offering a `reports.md`-generated
snapshot, note explicitly that its visibility numbers are directional, not
causal proof of what changed.
