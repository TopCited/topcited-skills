---
topic: How LLM/AI share-of-voice is computed, and where the metric breaks down
stage-relevance: [8]
last-verified: 2026-08-20
sources:
  - https://www.apollotechnical.com/ai-share-of-voice-best-tools-and-how-to-measure-it/
  - https://www.semrush.com/blog/how-to-measure-ai-share-of-voice/
  - https://searchengineland.com/ai-share-of-voice-metrics-that-matter-more-479611
  - TopCited internal research (LLM-monitoring industry study, 2026-08 — unpublished): vendor methodology (Peec, Profound, Ahrefs Brand Radar), cross-engine citation overlap, variance decomposition
  - heuristic
---

# LLM share of voice

## In plain words
Share of voice, applied to AI answers, is the percentage of brand mentions
in a category that belong to your brand — the same idea as traditional
media share of voice, just counted across chatbot responses instead of ad
impressions. Every AI-visibility vendor reports some version of it, but
there's no single, agreed "universe" of AI answers to measure against —
each vendor tests its own private set of prompts, so a share-of-voice
number really means "your share of that vendor's specific test," not a
comparable industry-wide score. Treat it as a trend inside one tool over
time, never as a number to compare across two different tools.

## What practitioners need to know

### The converged formula
Nearly every vendor uses the same base calculation:

> AI share of voice = (your brand's AI mentions ÷ total AI mentions across
> all brands in your category) × 100

*(I)*

### How the major vendors actually compute it
- **Semrush** (AI Visibility Toolkit / Brand Performance, updated
  2026-07-17) weights by both mention count *and* mention position, not
  just presence/absence; its Enterprise AIO product additionally factors in
  a topic's search volume for ChatGPT calculations (weighting by
  commercial importance, not a flat count). It does not disclose exactly
  how the competitive set/category boundary is chosen, and explicitly
  tracks share of voice **per platform** — ChatGPT, Google AI Mode,
  Perplexity, Gemini separately — because each builds answers differently.
  *(I)*
- **Peec AI** runs prompts once per 24h per model, logged out, and reports
  **Visibility** (share of chats mentioning the brand), **Position**
  (average rank of the mention within the response), and **Sentiment**,
  with visibility smoothed over a **rolling 7-day window** to cut day-to-day
  noise. Peec is also the vendor most transparent about splitting
  "Sources" (URLs the model's tool-use accessed) from "Citations" (URLs
  actually referenced in the visible text) as two distinct signals.
  *(I — TopCited internal research)*
- **Profound** captures via geo-distributed headless browsers, once per
  day per platform/config, across ~11 surfaces. Its own variance experiment
  found that sampling 10×/day vs. 1×/day changed measured visibility by
  ≤2 percentage points, because **platform response drift dominates
  sampling noise** — resampling more within a day buys little; a broader
  prompt portfolio buys more stability than deeper sampling per prompt.
  *(I — TopCited internal research)*
- **Ahrefs Brand Radar** runs prompts **monthly** (not daily) through free
  public web interfaces, ~14M queries/mo per chatbot, separately from its
  continuous AI Overviews crawl (~282M/mo). Its prompt universe is
  synthetic — derived from Ahrefs' own keyword database plus
  People-Also-Ask harvesting plus semantic "Fanout" expansion — not
  observed real user prompts. *(I — TopCited internal research)*

### Why the metric is contested
Search Engine Land's sharpest documented critique (Dan Taylor, 2026-06-08):
traditional share-of-voice math assumes a closed, enumerable keyword
universe — legacy SEO had exactly that (a defined keyword list as
denominator). AI prompts have no fixed universe; "the universe of possible
AI prompts is effectively infinite," so every vendor's number is actually
computed over a small, arbitrary, vendor-chosen subset of static prompts
presented as if it measured the open web. Concrete example: when OpenAI
shipped ChatGPT 5.0 (September 2025), platform-wide outbound-citation
volume dropped, and every vendor's visibility numbers cratered
simultaneously — for reasons having nothing to do with any brand's actual
standing, purely a UI change in how much the model links out. Proposed
replacements worth knowing about even if TopCited doesn't implement them:
**Share of Mentions** (organic brand frequency in the high-trust sources
models are trained on/retrieve from — a leading indicator upstream of any
one platform's UI quirks), **Share of Recommendations** (frequency of
appearing in AI-generated comparison/shortlist answers specifically —
closer to purchase intent), and **Share of Narrative** (qualitative: what
adjectives/positioning the AI associates with the brand — captures
perception drift a percentage can't). *(I)*

**Practical takeaways:** (1) a platform-level change (a model version bump)
can move everyone's share of voice simultaneously with zero connection to
brand quality — don't panic on a single-period drop without checking
whether the whole category moved; (2) the denominator/prompt-set is
vendor-chosen and largely undisclosed, so share-of-voice numbers are **not
comparable across vendors** and should be read as a self-consistent trend
within one tool only.

### Statistical honesty
The same variance findings that apply to raw visibility (see
`baselines-and-kpis.md`) apply directly to share-of-voice reporting: an
11% shared-cited-domain overlap between ChatGPT and Perplexity, and the
same brand named by 3+ engines only 21% of the time, mean a cross-engine
"blended" share-of-voice number is close to meaningless. Every credible
vendor reports **per-engine**, never pooled. *(I — TopCited internal research)*

## How this shows up in the workflow
Stage 8 (review & ongoing monitoring) uses this file when presenting
TopCited's own monitoring-run numbers as share of voice. TopCited's
`metrics/visibility` and `metrics/summary` endpoints (`monitoring.md`)
compute mention rate per brand per engine from query-set runs — that is
TopCited's implementation of the same formula above, and it should be
presented per-engine, matching vendor convention, never pooled across
engines into one blended number. When walking a user through Stage 8
numbers: frame share of voice as a trend inside TopCited over time, not as
something comparable to a number they may have seen from Semrush, Profound,
or another tool; and if a share-of-voice number drops sharply in one
period, check whether it's a category-wide/platform-wide move (a model
update) before treating it as brand-specific signal worth reacting to.
