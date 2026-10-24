---
topic: Tactics that measurably increase the odds an AI assistant cites a page (GEO)
stage-relevance: [4]
last-verified: 2026-10-24
sources:
  - arxiv.org/abs/2311.09735 (Aggarwal, Murahari, Rajpurohit, Kalyan, Narasimhan, Deshpande, "GEO: Generative Engine Optimization", KDD 2024, accessed 2026-10-24)
  - arxiv.org/abs/2607.14035 (Martinez, "Optimizing Visibility in Generative Engines: A Critical Survey of GEO 2023–2026", 2026-07-15, accessed 2026-10-24)
  - arxiv.org/abs/2603.29979 (Yu, Yang, Ding, Sato, GEO-SFE, "Structural Feature Engineering for GEO", 2026-03-31, accessed 2026-10-24)
  - arxiv.org/abs/2604.25707 v2 (Zhang, He, Yao, "From Citation Selection to Citation Absorption", 2026-04-29, accessed 2026-10-24)
  - arxiv.org/abs/2604.19113 (Liu & Xu, "Think Before Writing", 2026-04-21; abstract only, accessed 2026-10-24)
  - arxiv.org/abs/2603.09296 (Tian et al., "Diagnosing and Repairing Citation Failures in GEO", 2026-03-10; abstract only, accessed 2026-10-24)
  - AirOps ChatGPT citation-rate study, via https://searchengineland.com/study-how-generative-engines-select-and-cite-sources-471606 (accessed 2026-10-24)
  - https://docs.peec.ai/research/retrieval-vs-citation (Peec, Perplexity retrieved-vs-cited, Feb 2026, accessed 2026-10-24)
  - https://ahrefs.com/blog/schema-ai-citations/ (Ahrefs controlled schema study, 2026-05-11)
  - https://ahrefs.com/blog/llmstxt-study/ (Ahrefs llms.txt log study, 2026-06-15)
  - https://developers.google.com/search/docs/fundamentals/ai-optimization-guide (Google, updated 2026-07-10)
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
retrieved pool at all (crawlability, AI search bots allowed in robots.txt, and
presence in the indexes each assistant draws on — see the technical-seo
knowledge files, especially `../technical-seo/ai-crawler-access.md`), not just in polishing pages that already made the cut.
Peec's Feb 2026 data shows the same funnel on Perplexity: 64% of URLs it
retrieves are never cited (industry-tier).

**Measured tactics, ranked by evidence strength:**

- **[Documented, arxiv.org/abs/2607.14035]** Relevance and *position within the
  retrieved context* are the primary drivers of whether a source gets the *first*
  citation. Moving a source higher in the retrieved context set has a bigger
  effect than most on-page rewrites — but this is largely outside a content
  author's direct control; it's a retrieval/reranking effect, not a writing
  technique.
- **[Documented, arxiv.org/abs/2311.09735]** Citing reliable third-party sources
  within your own content, plus stylistic fluency/readability improvements,
  produced a measured **15–30%** visibility boost in the original GEO paper's
  benchmark (the 2026 survey restates these results rather than adding new
  measurements).
- **[Documented, arxiv.org/abs/2603.29979, GEO-SFE]** Structuring content across
  three levels — macro (document architecture), meso (information
  chunking/sectioning), micro (visual emphasis: bolding, lists) — produced a
  measured **17.3%** improvement in citation rate and **18.5%** improvement in
  subjective answer quality, across six generative engines. The abstract doesn't
  break out which of the three levels drove the most gain; treat "structure your
  content in sections with clear emphasis" as the actionable takeaway, not a
  specific one of the three sub-tactics.
- **[Documented, arxiv.org/abs/2603.09296]** Diagnosing *why* a page isn't cited
  and making targeted repairs ("AgentGEO") reported a 40%+ relative gain in
  citation rate while editing only ~5% of the content — evidence that small,
  diagnosed fixes can beat wholesale rewrites (preprint, abstract-level only).
- **[Documented, arxiv.org/abs/2604.25707]** A large empirical study (602 prompts,
  21,143 valid citations, 23,745 citation-level feature records across ChatGPT,
  Google AI Overviews/Gemini, and Perplexity) distinguishes **citation selection** (does the
  source appear at all) from **citation absorption** (how deeply the answer
  actually draws on it, vs. a shallow name-drop). Most citation metrics, including
  TopCited's, count selection only — keep in mind that "cited" and "actually used"
  are not the same thing.
- **[Heuristic, consistent cross-source consensus, no controlled measurement]**
  Direct-answer-in-the-first-third-of-content, FAQ-style structure, dense original
  data/statistics, named-expert quotes with authorship, and visible
  recently-updated timestamps are repeatedly named across ChatGPT/Claude/Copilot
  optimization guides as citation-correlated. Treat as reinforced consensus, not
  new evidence. For Google's AI features specifically, Google says there's "no
  requirement to break your content into tiny pieces" and no special markup or
  files are needed — so don't restructure pages *only* to chase AI Overviews.
- **[Heuristic]** "Liftable" passage writing — self-contained, factually specific
  paragraphs an assistant can quote wholesale — is a recurring theme, and
  plausible given that many AI Mode citation links carry a text-fragment anchor
  highlighting the quoted passage (median ~117 words in one vendor study — a
  paragraph, not a sentence). The causal writing advice is asserted, not
  measured, in every source found.

**Gaps — do not claim these are measured:**
- No controlled before/after study isolates FAQPage/HowTo markup specifically.
  The closest is Ahrefs' 2026 controlled study of adding JSON-LD in general,
  which found no meaningful citation uplift on any platform (see
  `../technical-seo/structured-data.md`).
- No study measures llms.txt's causal effect on citation. What exists is
  adoption data and server-log evidence that the major AI crawlers almost never
  request the file (see `../technical-seo/llms-txt.md`).

## How this shows up in the workflow
Referenced by **stage 04 (site audit)** — used when auditing existing content and
deciding which structural/citation-signal fixes to prioritize on a page before
recommending a rewrite. The "retrieval precedes citation" framing is the key
decision point: if a page fails a crawlability/indexing check (see
`technical-seo/crawlability-and-indexing.md`), fix that first — citation-tactic
rewrites on an unindexed page are wasted effort.
