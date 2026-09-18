---
topic: Setting an SEO/GEO visibility baseline and choosing the right KPIs
stage-relevance: [2, 8]
last-verified: 2026-08-20
sources:
  - https://www.trysight.ai/blog/ai-visibility-audit-template
  - https://skyscale.com.au/blogs/prompt-testing-ai-visibility-diy
  - https://discoveredlabs.com/blog/free-ai-visibility-audit-checklist
  - https://www.fratzkemedia.com/insights/ai-visibility-audit
  - https://tajo.io/blog/the-6-best-seo-audit-tools/
  - https://seeklab.io/blog/best-free-seo-audit-tools-for-small-business-in-2026-tested-and-compared/
  - https://www.searchenginejournal.com/google-analytics-adds-ai-assistant-as-default-channel-group/574974/
  - https://www.digitalapplied.com/blog/ga4-ai-assistant-channel-2026-measure-ai-traffic-playbook
  - https://www.tryaivo.com/blog/ga4-ai-assistant-channel
  - https://weekerp.com/en/blog/ga4-ai-assistant-channel-what-it-tracks-and-misses
  - https://writesonic.com/blog/geo-kpis-every-brand-should-track
  - https://analyticahouse.com/blogs/how-to-generative-engine-optimization-geo-kpi-reporting-model-for-ai-visibility
  - https://www.similarweb.com/blog/marketing/geo/what-is-geo/
  - https://www.searchpilot.com/resources/blog/what-is-seo-split-testing
  - https://www.searchpilot.com/resources/blog/the-math-behind-searchpilot-how-seo-a/b-testing-actually-works
  - TopCited internal research (LLM-monitoring industry study, 2026-08 — unpublished), itself citing petralabs.com and arXiv:2603.08924 / 2604.07585
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
with no setup required. *(P)* Treat the exact recognized-assistant list
with caution: secondary reporting on the live 2026-06 documentation lists
ChatGPT, Gemini, DeepSeek, Copilot, and Grok, while the original 2026-05-13
launch post named only ChatGPT/Gemini/Claude — Claude's presence is
unconfirmed in this pass and should be checked against Google's own
changelog before stating it as fact. **Important limitation for honest
baselining:** GA4 only captures traffic with a matching referrer header —
in-app AI browsers, copy-pasted links, and zero-click answers (the majority
of GEO's value) land in Direct or don't appear at all. It also processes
**forward-only**: AI traffic from before 2026-05-13 stays misclassified, so
GA4 cannot retroactively establish a historical AI-traffic baseline. *(I)*

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

**The structural measurement gap:** one 2026 industry survey frames it as
**"54% plan vs. 23% measurement"** — over half of marketers say GEO is part
of their strategy, but fewer than a quarter say they can actually measure
its impact. Two structural reasons: most AI answers are zero-click (no
referral session to attribute), and the most valuable AI influence —
landing on a shortlist a user later acts on outside the chat — happens
*before* any trackable touchpoint exists. *(I)* This matches TopCited's own
internal monitoring research, which independently found that Bing Webmaster
Tools' "grounding queries" report is the only first-party ground truth GEO has
today, and only for Copilot/Bing-grounded answers.

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
the time at 100 runs (Petra Labs, 7,200 trials); rank ordering stabilizes
~8x faster than magnitudes (~80 runs for Spearman ≥0.90); within-prompt
resampling variance (34.8%) and prompt-phrasing variance (26.5%) dwarf
brand-identity variance (1.5%) — most of the "signal" in a before/after
comparison is noise from the prompt portfolio, not the brand's actual
standing. *(I — TopCited internal research)* Never attribute a single-period visibility
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
