---
topic: What content properties actually correlate with being cited by AI assistants
stage-relevance: [6]
last-verified: 2026-10-24
sources:
  - https://ahrefs.com/blog/ai-overview-citations-top-10/ (2026-03-02 update, accessed 2026-10-24) [industry, disclosed methodology]
  - https://ahrefs.com/blog/search-rankings-ai-citations/ (2025-07-21 original, accessed 2026-10-24) [industry, disclosed methodology]
  - https://ahrefs.com/blog/short-vs-long-content-in-ai-overviews/ (accessed 2026-10-24) [industry, disclosed methodology]
  - https://developers.google.com/search/docs/fundamentals/ai-optimization-guide (Google, updated 2026-07-10) [primary]
  - https://arxiv.org/abs/2311.09735 (Aggarwal et al., "GEO: Generative Engine Optimization," KDD 2024) (accessed 2026-10-24) [primary, peer-reviewed]
  - https://arxiv.org/abs/2506.11097 ("C-SEO Bench: Does Conversational SEO Work?", NeurIPS 2025 Datasets & Benchmarks) (accessed 2026-10-24) [primary, peer-reviewed]
  - https://arxiv.org/abs/2604.19113 ("Think Before Writing", Liu & Xu, 2026-04) (accessed 2026-10-24) [primary preprint, figures not extracted]
  - heuristic
---

# AI citation signals: what actually correlates with getting cited

## In plain words
Ranking well in regular Google search is still the strongest predictor of
being cited in Google's AI answers — but it now means ranking for the many
related sub-questions Google's AI searches behind the scenes, not just the
main query. One large, disclosed-methodology study found AI-Overview
citations from the traditional top 10 fell from about three-quarters in 2025
to under 40% by early 2026. Beyond that, a peer-reviewed study found that adding concrete statistics, direct quotes,
and citations to credible sources measurably helps get you cited more
prominently — while classic keyword-stuffing SEO tricks measurably hurt.
Page length barely matters either way. Treat all of this as "SEO plus a few
extra content moves," not a separate discipline that can substitute for
ranking well in the first place.

## What practitioners need to know

### Lead finding: ranking still matters, but across the topic, not one query (industry, disclosed methodology)
**Ahrefs, "Update: 38% of AI Overview Citations Pull From The Top 10"**
(published 2026-03-02; 863K keyword SERPs, ~4M AI Overview URLs):
- **37.9%** of AI-Overview-cited pages rank in Google's top 10 for the
  original query; 31.2% rank 11–100; **31.0%** rank beyond 100 (counting
  blue links only: 37.1% / 26.2% / 36.7%).
- That's down from **76.1%** top-10 in Ahrefs' July 2025 study (1.9M
  citations from 1M AI Overviews). Ahrefs' suggested explanation is query
  fan-out — Google's AI runs related sub-searches and cites pages ranking
  for those — and it warns the comparison is confounded by a parser change
  and AI Overviews moving to Gemini 3 in Jan 2026. Other vendors report even
  lower overlap (BrightEdge ~17%, via SEJ). (industry)
- Google's own framing matches: AI Overviews and AI Mode are "rooted in our
  core Search ranking and quality systems" and use query fan-out. (primary)
- **Practical reading**: GEO is still an addition to SEO fundamentals, not
  a substitute — the citations still come from Google's index and quality
  systems — but the target is ranking across a topic's sub-questions (the
  pillar-cluster logic in `pillar-cluster-model.md`), not winning one head
  term.

**Ahrefs, "Short vs. Long Content in AI Overviews"** (published 2025-12-03;
methodology: 174,048 cited pages, 560,346 AI Overviews, 1,677,876 citations
after filtering):
- Average cited-page word count: **1,282 words**. 53.4% of citations go to
  pages under 1,000 words; only 16% exceed 2,000 words.
- **Spearman correlation between word count and citation position: 0.04** —
  effectively zero. Content under 350 words appears in the top-3 citation
  slots over 95% of the time, the same distribution as longer content.
- Ahrefs' own conclusion: "Stop obsessing over word count and focus on
  actually answering the query instead." Google's AI optimization guide
  likewise says there's "no requirement to break your content into tiny
  pieces" for its AI features. (primary for Google)
- This directly contradicts unverifiable claims in circulation (e.g. a
  "3,000–4,999 word sweet spot," "sections of 120–180 words earn 70% more
  citations") that could not be corroborated to any real study and are
  deliberately excluded from this file — do not import them.

### The GEO paper: which content tweaks help, and by how much (primary, peer-reviewed)
Aggarwal, Murahari, Rajpurohit, Kalyan, Narasimhan, Deshpande, "GEO:
Generative Engine Optimization" (arXiv:2311.09735, KDD 2024). Methodology:
GEO-bench, ~10,000 queries drawn from 9 datasets across 25 domains, each paired with the web
sources a Bing-Chat-mimicking generative engine would draw on; top findings
also validated on Perplexity. Nine content-modification strategies tested
against a no-modification control, scored on cited-word-count (position-
weighted) and an LLM-judged "how good does this citation look" score.

- Best strategies achieved up to **40% relative improvement** (41% in the
  paper's Table 1) on the position-weighted word-count metric and **15–30%** on the subjective-
  impression metric.
- **Quotation Addition**: 30–40% range on the word-count metric generally,
  with **22%** specifically validated on Perplexity.
- **Statistics Addition**: **+37%** on the subjective-impression metric
  (validated on Perplexity); on sites already top-ranked this effect
  reverses to about **−20.6%**.
- **Cite Sources**: weak on its own, but ~31% on average when combined with
  other methods (domain-dependent).
- **Fluency Optimization** (grouped in the paper with "Easy-to-Understand"):
  +15–30%.
- **Keyword Stuffing**: the one tactic that reliably backfires — about
  **10% worse than baseline** on Perplexity. Classic on-page keyword-
  stuffing does not transfer to GEO and actively hurts rather than helps.
- **No single tactic wins everywhere** (domain-dependent effectiveness):
  Authoritative tone works best for debate/history queries; Cite Sources
  for factual questions; Statistics Addition for law/government/opinion;
  Quotation Addition for people/society, explanation, and history; Fluency
  Optimization for business, science, and health content.
- **Position-5 sources gain far more than position-1 sources**: Cite
  Sources produced +115.1% for a position-5-ranked source vs. −30.3% for an
  already position-1 source. The paper frames GEO as "democratizing"
  citation visibility — optimization has the most leverage for sources that
  aren't already dominant, and can hurt one that already is (a ceiling
  effect).

**Practical synthesis**: adding concrete statistics, direct quotes from
credible sources, and citations to credible external sources are the three
highest-leverage, lowest-risk content changes; avoid keyword stuffing; a
brand's marginal ROI from these tactics is highest when it is *not already*
the top-ranked/most-cited source for a topic — GEO reads as more of a
challenger-brand tool than an incumbent-defense tool.

**Caveat on all figures above**: these percentages are validated against a
Bing-Chat-mimicking benchmark and, for top strategies, Perplexity — not
against ChatGPT, Gemini, Claude, or Google AI Overviews directly. Treat the
exact numbers as Bing/Perplexity-specific; the directional lessons (avoid
keyword stuffing; add stats/quotes/citations; expect more ROI when not
already dominant) are the transferable part.

### A tempering finding: these gains are not stable once tactics become common (primary, peer-reviewed)
"C-SEO Bench: Does Conversational SEO Work?" (Puerto, Gubri, Green, Oh, Yun;
arXiv:2506.11097; NeurIPS 2025 Datasets & Benchmarks Track) found that most
current C-SEO/GEO-style methods are largely ineffective and frequently
*hurt* document ranking in a conversational-search context; traditional SEO
— improving a source's rank so it enters the LLM's retrieved context at all
— was significantly more effective than post-hoc content tweaks. It also
documents a **zero-sum/congestion effect**: as more competitors adopt the
same tactic, the aggregate benefit shrinks. Read the GEO-paper percentages
above as directionally useful, not as a stable, permanent edge — and weight
"get retrieved/ranked at all" above "phrase the page a specific way."

### What I could not verify (flagged, not silently dropped)
- "Think Before Writing: Feature-Level Multi-Objective Optimization for
  Generative Citation Visibility" (Liu & Xu, arXiv:2604.19113, 2026-04) confirms feature-level
  content optimization is a real, measurable lever, but precise percentage
  figures could not be extracted from the PDF in this research pass.
- No primary source quantifies AI-citation content properties **per
  specific assistant** (ChatGPT vs. Claude vs. Gemini vs. Perplexity
  individually) with disclosed methodology. The Ahrefs data above is
  Google-AI-Overviews-specific — don't over-generalize it to other
  assistants; for ChatGPT the link to Google/Bing ranking is far weaker
  (see `../foundations/how-llms-source-answers.md`).
- Visibility-measurement itself is noisy (a separate measurement-track
  finding); read any single "content property X caused Y% more citations"
  claim with wide error bars.

## How this shows up in the workflow
Stage 6 (content) uses this file to prioritize content-editing effort: check
traditional ranking first — for the main query *and* its obvious
sub-questions — then add concrete
statistics, direct quotes, and citations to credible sources where relevant
to the domain, and never resort to keyword stuffing. It also sets
expectations — these are incremental, domain-dependent, and most valuable
for content that isn't already winning, not a guaranteed or permanent
citation boost.
