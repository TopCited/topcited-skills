---
topic: How ChatGPT, Perplexity, Gemini/AI Overviews, and Claude retrieve and choose citations
stage-relevance: [2, 3, 6]
last-verified: 2026-08-20
sources:
  - https://help.openai.com/en/articles/9237897-chatgpt-search — OpenAI Help Center, "ChatGPT Search" [documented]
  - https://searchengineland.com/chatgpt-retrieval-stack-index-cache-pages-485036 — Search Engine Land, ChatGPT retrieval-stack analysis [industry, single-outlet for the Bing-index and 6.8–7.8% overlap claims — flagged unverified]
  - https://algoblueprints.com/what-search-engine-does-chatgpt-use/ — corroborating industry analysis on ChatGPT/Bing [industry]
  - https://docs.perplexity.ai/docs/resources/perplexity-crawlers — Perplexity docs, "Perplexity Crawlers" [documented]
  - https://theaiengineer.substack.com/p/how-perplexity-built-their-search — secondary account of Perplexity's Vespa-based architecture [industry, not a Perplexity-published source — flagged for verification]
  - https://www.frase.io/blog/which-ai-engines-cite-which-sources — comparative citation-count study across engines [industry, single-source "3x" figure]
  - https://ai.google.dev/gemini-api/docs/google-search — Google AI for Developers, "Grounding with Google Search" [documented]
  - https://dejan.ai/blog/gemini-grounding/ — third-party technical writeup on Gemini query rewriting [industry]
  - https://www.wislr.com/articles/gemini-vs-ai-overviews-vs-ai-mode — comparison of Gemini app / API grounding / AI Overviews / AI Mode [industry, key AI Overviews claim not corroborated against a Google primary page]
  - https://rankry.ai/blog/how-claude-finds-and-cites-sources/ — vendor analysis of Claude's web-search architecture [industry]
  - https://mostailabs.com/field-guide/claude-and-brave-search — secondary report on Anthropic's Brave Search subprocessor listing and citation-overlap testing [industry, not directly verified against Anthropic's Trust Center]
  - https://developmentcorporate.com/saas/what-chatgpt-claude-gemini-grok-perplexity-are-actually-trained-on-and-why-it-matters-for-every-early-stage-saas-executive/ — aggregated knowledge-cutoff and live-search-trigger estimates [industry, directional not vendor-confirmed]
---

# How LLM assistants source and cite answers

## In plain words
Every major AI assistant is a hybrid: it mostly answers from what it learned
during training, but can decide on its own to search the live web when a
question needs current information. Crucially, each assistant searches a
*different* pool of web content — ChatGPT leans on Bing's index, Perplexity
built its own search engine from scratch, Google's Gemini and AI Overviews
draw on Google's own search results, and Claude uses Brave Search. That
means ranking well on Google doesn't automatically get a brand mentioned by
ChatGPT or Claude — each assistant is effectively a separate race to win.

## What practitioners need to know

### The cross-cutting mechanic
- Every assistant combines a frozen training snapshot (parametric knowledge)
  with an optional live-retrieval tool the model invokes when it judges the
  query needs current or external information. Perplexity is the exception —
  it's retrieval-first by design, not model-gated. (synthesized from
  vendor docs across engines, documented + industry)
- Reported estimate: roughly **34.5% of ChatGPT queries** trigger a live web
  search rather than answering from memory alone; knowledge cutoffs are
  roughly ChatGPT ~Dec 2025, Gemini ~Jan 2025, Grok ~Nov 2024. Treat these
  numbers as **directional, not vendor-confirmed** — no OpenAI page states
  the 34.5% figure. (industry, unverified)
- Cross-engine citation overlap is low even when two engines both retrieve
  live — only ~11% of cited domains are shared between ChatGPT and
  Perplexity (per the seed research doc). This confirms each engine's
  retrieval + reranking stack is a genuinely separate funnel to win, not
  just a proxy for training-data overlap.

### Per-assistant mechanics

**ChatGPT (OpenAI)**
- Official: "ChatGPT automatically searches the web if your question might
  benefit from information on the web," turning the request into one or
  more search queries, retrieving results, and generating an answer with
  inline citations. (OpenAI Help Center, documented)
- Its web index is reported to be **Bing-powered** — OAI-SearchBot and the
  browse feature pull from Bing's indexed content rather than an
  independent OpenAI crawl. **Flagged**: this is converging industry
  analysis from multiple outlets, but no OpenAI page explicitly names Bing
  — treat as industry consensus, not vendor-confirmed. (industry)
- Pipeline: query fan-out into sub-questions → per-sub-question candidate
  retrieval → chunking of fetched pages → citation selection.
- **Bing's own top-3 organic ranking only weakly predicts what ChatGPT
  cites** — one reported study found only 6.8–7.8% overlap. This is a
  single outlet's figure, not independently cross-verified here — spot-check
  before treating as settled, but directionally it means ranking well on
  Bing/Google is necessary but far from sufficient for a ChatGPT citation.
  (industry, single-source figure)
- OpenAI's crawler is reported to **not render JavaScript** (HTML-only
  parsing) — JS-only content is reportedly invisible to it regardless of
  how well it otherwise ranks. (industry, single experiment cited)

**Perplexity**
- Official: Perplexity crawls with its own bots (PerplexityBot,
  Perplexity-User) to "gather and index information from the internet."
  (Perplexity docs, documented)
- Reported to run its own crawler, index, retrieval pipeline, and ranking —
  not a licensed index. Rebuilt on **Vespa** (open-source retrieval+ranking+
  ML-inference engine) around April 2025, moving off third-party search
  APIs; the resulting index is described by Perplexity as covering "hundreds
  of billions of webpages." **Flagged**: this account comes from a secondary
  substack writeup, not a Perplexity-published source — verify before
  treating the scale claim as settled. (industry, unverified)
- Retrieval detail: multi-layered RAG — BM25 lexical + vector embeddings for
  broad candidate retrieval, then a cross-encoder reranking layer, inside a
  ~100ms latency budget. (industry)
- Cites roughly **3x more sources per response than ChatGPT** and tends to
  cite multiple sources per claim, consistent with being retrieval-first by
  design. Treat "3x" as one vendor's comparative study, not independently
  reproduced. (industry, single-source figure)

**Gemini app / Gemini API grounding / AI Overviews / AI Mode — four distinct
surfaces, do not conflate**
- Gemini API grounding (official): with the `google_search` tool enabled,
  "the model analyzes the prompt and determines if a Google Search can
  improve the answer," generates search queries, executes them, then
  synthesizes a response. (Google AI for Developers, documented)
- User prompts are rewritten into search-optimized queries before
  retrieval; a prediction classifier reportedly scores each candidate query
  0–1 to decide whether search would help before firing. (industry,
  consistent with the documented mechanism but not itself from the Google
  doc)
- **The single most important distinction in this file**: AI Overviews is
  **not** a fresh, independent retrieval call. It's reported to be
  synthesized from results Google's *existing* organic ranking pipeline
  already retrieved and ranked — meaning ranking well in classic Google
  Search is a near-precondition for AI Overview inclusion, unlike
  ChatGPT/Perplexity where ranking elsewhere is only weakly predictive.
  **Flagged**: this rests on one secondary source, not a fetched Google "About
  AI Overviews" primary page — corroborate before treating as fully settled,
  though it is the most load-bearing claim in this file for practitioner
  strategy. (industry, unverified against primary source)
- **What not to believe**: treating "Gemini," "AI Overviews," and "AI Mode"
  as one interchangeable thing is a common practitioner error — they are
  four separate products (the fourth being bare API grounding for
  third-party apps) with different retrieval mechanics, per above.

**Claude (Anthropic)**
- Reported mechanism: a server-side web-search tool inside Claude's tool-use
  loop queries an upstream search backend, receives passage-level chunks,
  and generates a grounded answer with inline citations. (industry, vendor
  analysis, not an Anthropic engineering post)
- Anthropic's Trust Center reportedly lists **Brave Search** as a Web Search
  subprocessor (added 2025-03-19, one day before web search launched).
  Brave runs an independent Western index (~40B+ pages) built without
  depending on Google/Bing. **Flagged**: the subprocessor listing is a
  primary Anthropic disclosure in principle, but this finding is reported
  secondhand here, not fetched directly from the Trust Center — verify
  directly before treating as settled. (industry, unverified)
- Independent testing reportedly found **86.7% overlap** between Claude's
  cited results and Brave's top organic results at web-search launch,
  dropping to **~79.2%** in a June 2026 re-run (~400 queries) — suggesting
  Claude's citation selection has grown more independent of raw Brave
  ranking over time, plausibly from added reranking/filtering logic tied to
  a reported Feb 9, 2026 tool update (`web_search_20260209`). **Flagged**:
  not independently corroborated against an Anthropic changelog. (industry,
  unverified)

### Summary table

| Assistant | Own crawl/index? | Index partnership | Live-search trigger | What predicts citation |
|---|---|---|---|---|
| ChatGPT | No | Bing (reported, unverified) | Model-decided, ~1/3 of queries (est.) | Weakly: post-retrieval LLM judgment; Bing rank only ~7% predictive |
| Perplexity | Yes (own crawler + Vespa index) | None — in-house since ~2025 | Near-always (retrieval-first) | Own BM25 + embedding + cross-encoder rerank |
| Gemini app / API grounding | No | Google Search index | Classifier-gated, model-decided | Google Search ranking as candidate pool |
| Google AI Overviews | No (reuses existing pipeline) | Google Search index, same pipeline | Always (built into SERP) | Classic organic ranking is the retrieval pool itself |
| Claude | No | Brave Search | Tool-use-decided by model | Brave ranking, increasingly filtered/reranked over time |

## How this shows up in the workflow
No workflow stage currently cites this file by name (grepped against
`.claude/skills/visibility-workflow/stages/*.md` — no match). It's
background material that underpins stage 2 (baseline monitoring — explains
why prompt-visibility results differ so much across engines) and stage 3/6
(competitor research and content — explains why winning classic SEO rank
doesn't guarantee AI-citation, especially outside Google's own AI Overviews
surface).
