---
topic: Tactics that measurably increase the odds an AI assistant cites a page (GEO)
stage-relevance: [4]
last-verified: 2026-08-20
sources:
  - arxiv.org/abs/2311.09735 (Aggarwal, Nagpure et al., "GEO: Generative Engine Optimization", accessed 2026-08-20)
  - arxiv.org/abs/2607.14035 ("Optimizing Visibility in Generative Engines: A Critical Survey of GEO 2023–2026", accessed 2026-08-20)
  - arxiv.org/abs/2603.29979 (GEO-SFE, "Structural Feature Engineering for GEO", submitted 2026-03-31, accessed 2026-08-20)
  - arxiv.org/pdf/2604.25707 v2 ("From Citation Selection to Citation Absorption", dated 2026-04-30, accessed 2026-08-20)
  - arxiv.org/pdf/2604.19113 (title/abstract only, not read in depth, accessed 2026-08-20)
  - arxiv.org/pdf/2603.09296 (title/abstract only, not read in depth, accessed 2026-08-20)
  - AirOps ChatGPT citation-rate study, via https://www.conbersa.ai/learn/bing-indexing-optimization-for-chatgpt (accessed 2026-08-20)
  - Tinuiti, Jan 2026, via https://everything-pr.com/perplexity-citation-source-index-2026 (accessed 2026-08-20)
  - heuristic
---

# Citation optimization (GEO tactics)

## In plain words
Getting an AI assistant to cite your page happens in two separate steps: first the
assistant has to find and consider your page at all, then it has to pick your page
over the others it found. Most "GEO tips" you'll read online only address the
second step — and they only work if the first step already happened. If your page
isn't being crawled or indexed, no amount of rewriting will get it cited.

## What practitioners need to know

**Being retrieved is the precondition; being cited is a downstream, conditional
win.** The foundational GEO paper (documented, arxiv.org/abs/2311.09735) showed
citing reliable sources and improving fluency/readability measurably raises
citation likelihood — but a 2026 critical survey of the field (documented,
arxiv.org/abs/2607.14035) reframes this: those gains are **conditional on the
source already being present in the model's retrieved context**. GEO reframes the
whole pipeline as "stochastic and partially observable," spanning search
activation → crawling/indexing → retrieval → reranking → context allocation →
citation → prominence → factual absorption → fidelity → user behavior — not a
single ranking task. Practical implication: content restructuring cannot fix a
retrieval-stage failure. If a page never gets fetched at all, on-page GEO tactics
have nothing to act on. This matches the AirOps finding that ChatGPT cites only
**~15%** of pages it retrieves (industry-tier) — the leverage is in being in that
retrieved pool at all (crawlability, Bing index presence — see the technical-seo
knowledge files), not just in polishing pages that already made the cut.

**Measured tactics, ranked by evidence strength:**

- **[Documented, arxiv.org/abs/2607.14035]** Relevance and *position within the
  retrieved context* are the primary drivers of whether a source gets the *first*
  citation. Moving a source higher in the retrieved context set has a bigger
  effect than most on-page rewrites — but this is largely outside a content
  author's direct control; it's a retrieval/reranking effect, not a writing
  technique.
- **[Documented, arxiv.org/abs/2607.14035]** Citing reliable third-party sources
  within your own content, plus stylistic fluency/readability improvements,
  produced a measured **15–30%** visibility boost across the studies the survey
  reviewed.
- **[Documented, arxiv.org/abs/2603.29979, GEO-SFE]** Structuring content across
  three levels — macro (document architecture), meso (information
  chunking/sectioning), micro (visual emphasis: bolding, lists) — produced a
  measured **17.3%** improvement in citation rate and **18.5%** improvement in
  subjective answer quality, across six generative engines. The abstract doesn't
  break out which of the three levels drove the most gain; treat "structure your
  content in sections with clear emphasis" as the actionable takeaway, not a
  specific one of the three sub-tactics.
- **[Documented, arxiv.org/pdf/2604.25707]** A large empirical study (602 prompts,
  21,143 valid citations, 23,745 citation-level features across ChatGPT,
  Perplexity, Gemini and others) distinguishes **citation selection** (does the
  source appear at all) from **citation absorption** (how deeply the answer
  actually draws on it, vs. a shallow name-drop). This distinction isn't currently
  captured by TopCited's own citation metrics — worth flagging to the measurement
  track as a gap, since "cited" and "actually used" are not the same thing.
- **[Heuristic, consistent cross-source consensus, no controlled measurement]**
  Direct-answer-in-the-first-third-of-content, FAQ-style structure, dense original
  data/statistics, named-expert quotes with authorship, and visible
  recently-updated timestamps are repeatedly named across ChatGPT/Claude/Copilot
  optimization guides as citation-correlated. Treat as reinforced consensus, not
  new evidence.
- **[Heuristic]** "Liftable" sentence writing — short, self-contained, factually
  specific sentences an assistant can lift wholesale — is a recurring theme, and
  plausible given that Gemini's citation URLs reportedly carry sentence-level
  text-fragment anchors (the anchor mechanism itself is real web-platform tech;
  the causal writing advice is asserted, not measured, in every source found).

**Gaps — do not claim these are measured:**
- No controlled before/after study was found isolating schema.org
  FAQPage/HowTo markup's *causal* effect on citation rate specifically, separate
  from "structured content" generally. That evidence, if it exists, belongs to the
  technical-seo track.
- No hard numbers were found on llms.txt's causal effect on citation — only
  adoption evidence.

## How this shows up in the workflow
Referenced by **stage 04 (site audit)** — used when auditing existing content and
deciding which structural/citation-signal fixes to prioritize on a page before
recommending a rewrite. The "retrieval precedes citation" framing is the key
decision point: if a page fails a crawlability/indexing check (see
`technical-seo/crawlability-and-indexing.md`), fix that first — citation-tactic
rewrites on an unindexed page are wasted effort.
