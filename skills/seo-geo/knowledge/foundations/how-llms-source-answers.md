---
topic: How ChatGPT, Perplexity, Gemini/AI Overviews/AI Mode, and Claude retrieve and choose citations
stage-relevance: [2, 3, 6]
last-verified: 2026-10-24
sources:
  - https://help.openai.com/en/articles/9237897-chatgpt-search — OpenAI Help Center, "ChatGPT Search" [documented]
  - https://help.openai.com/en/articles/10093903-chatgpt-search-for-enterprise-and-edu — names Bing as one provider [documented]
  - https://developers.openai.com/api/docs/bots — OpenAI crawler documentation [documented]
  - https://think.resoneo.com/chatgpt-retrieval/ — RESONEO, ChatGPT result-source analysis, Jul–Aug 2026 [industry]
  - https://docs.peec.ai/research/chatgpt-own-search-index-labrador — Peec, ChatGPT result-source labels, Sept 2026 [industry]
  - https://arxiv.org/html/2610.15033v1 — retrieval overlap of ChatGPT vs Google/Bing, Oct 2026 preprint [industry/academic, not peer-reviewed]
  - https://www.mediapost.com/publications/article/414195/ai-chat-relies-on-search-to-fill-gaps.html — Semrush clickstream, share of ChatGPT prompts that trigger search, 2026-04-09 [industry]
  - https://graphite.io/five-percent/research/do-not-force-search-prompt-tracking — Graphite, search-trigger rates and inline links without search, 2026-08-20 [industry]
  - https://think.resoneo.com/sentinel/geo-llm-crawler-report.html — JavaScript execution by LLM fetchers, Jan 2026 [industry]
  - https://docs.perplexity.ai/docs/resources/perplexity-crawlers — Perplexity docs, "Perplexity Crawlers" [documented]
  - https://www.infoq.com/news/2025/09/perplexity-search-api/ — coverage of Perplexity's Search API launch and stated index size, 2025-09-30 [industry, quoting Perplexity]
  - https://research.perplexity.ai/articles/architecting-and-evaluating-an-ai-first-search-api — Perplexity research post on its retrieval stack [documented, snippet-level access only]
  - https://developers.google.com/search/docs/appearance/ai-features — Google Search Central, "AI features and your website" [documented]
  - https://developers.google.com/search/docs/fundamentals/ai-optimization-guide — Google, AI optimization guide, updated 2026-07-10 [documented]
  - https://ai.google.dev/gemini-api/docs/google-search — Google AI for Developers, "Grounding with Google Search," updated 2026-10-13 [documented]
  - https://blog.google/products-and-platforms/products/search/search-io-2026/ — Google, AI Mode status, 2026-05-19 [documented]
  - https://ahrefs.com/blog/ai-overview-citations-top-10/ — Ahrefs, AI Overview citations vs top-10 rankings, 2026-03-02 update [industry, disclosed methodology]
  - https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool — Anthropic, web search tool docs [documented]
  - https://simonwillison.net/2025/Mar/21/anthropic-use-brave/ — report of Anthropic's Brave Search subprocessor listing [industry]
  - https://xponent21.com/insights/claude-web-search-brave-turbopuffer/ — re-check of Anthropic's subprocessor list, 2026-07 [industry]
  - TopCited internal research (LLM-monitoring industry study, 2026-08 — unpublished): cross-engine cited-domain overlap
---

# How LLM assistants source and cite answers

## In plain words
Every major AI assistant is a hybrid: it partly answers from what it learned
during training, and can decide on its own to search the live web when a
question needs current information. Crucially, each assistant searches a
*different* pool of web content — ChatGPT mixes OpenAI's own index with
results bought from outside search providers, Perplexity runs its own search
engine, Google's Gemini, AI Overviews and AI Mode draw on Google's own index
and ranking systems, and Claude's web search is backed by third-party search
providers (Brave Search is the one publicly listed). That means ranking well
on Google doesn't automatically get a brand mentioned by ChatGPT or Claude —
each assistant is effectively a separate race to win.

## What practitioners need to know

### The cross-cutting mechanic
- Every assistant combines a frozen training snapshot (parametric knowledge)
  with an optional live-retrieval tool the model invokes when it judges the
  query needs current or external information. Perplexity is the exception —
  it's retrieval-first by design, not model-gated. (synthesized from
  vendor docs across engines, documented + industry)
- **How often ChatGPT searches**: Semrush clickstream data (1B+ US records,
  Oct 2024–Feb 2026) put the share of ChatGPT prompts that trigger a web
  search at **34.5%** in Feb 2026, down from 46% in late 2024. (industry)
  The rate varies a lot by prompt type — Graphite measured 58% for logged-out
  entity-comparison prompts in Aug 2026. (industry) Graphite also reports
  that since ~May 2026 ChatGPT can insert inline links *without* running a
  search, so a link in an answer no longer proves search ran. (industry)
- **Knowledge cutoffs move with every model release** — check the vendor's
  model page rather than a blog's table. Anthropic publishes a cutoff per
  model (June 2026 for the current Claude 5.5 family); OpenAI and Google
  don't publish cutoffs for the models behind ChatGPT (GPT-6 became the
  ChatGPT default in Oct 2026) or the Gemini app. (documented for Anthropic;
  industry for the ChatGPT default)
- Cross-engine citation overlap is low even when two engines both retrieve
  live — only ~11% of cited domains are shared between ChatGPT and
  Perplexity (TopCited internal research). Each engine's retrieval +
  reranking stack is a genuinely separate funnel to win, not just a proxy
  for training-data overlap.

### Per-assistant mechanics

**ChatGPT (OpenAI)**
- Official: "ChatGPT automatically searches the web if your question might
  benefit from information on the web," rewriting the request into one or
  more search queries, and "ChatGPT search sometimes partners with other
  search providers." OpenAI's Enterprise/Edu help page names Bing as one of
  those providers. (OpenAI Help Center, documented)
- **Not "Bing-powered" — a mix, with Google-derived results dominant in 2026
  measurements.** OpenAI's "offline web search" help article describes
  answering from "OpenAI's indexed and cached web content," i.e. its own
  index. (documented) Independent analyses of ChatGPT's result metadata
  (RESONEO, Peec; May–Aug 2026) found four result sources: OpenAI's own
  index (labelled `labrador`) plus three third-party feeds, the largest of
  which returned Google-derived results — ~75% of URLs in thinking-mode
  answers, with about 1 in 3 of those on Google's first page but only ~1 in
  20 on Bing's. (industry, consistent across two independent teams)
- Pipeline: query fan-out into sub-questions → per-sub-question candidate
  retrieval → a cached reading layer of fetched pages → citation selection;
  only a small fraction of pages (~1 in 80 in RESONEO's thinking-mode data)
  are opened live at answer time. (industry)
- **Ranking on Google or Bing is a weak predictor of what ChatGPT retrieves.**
  An Oct 2026 preprint found 97% of the pages ChatGPT retrieved were absent
  from Google's top 50 for the same query, and 99% absent from Bing's top
  30. (industry/academic preprint — it replays queries through the engines'
  APIs, so treat the exact numbers cautiously) An older, widely repeated
  "6.8–7.8% Bing top-3 overlap" figure could not be traced to a real study
  and has been dropped.
- **JavaScript**: a Jan 2026 test found `ChatGPT-User` doesn't execute
  inline, delayed, or fetch()-loaded JavaScript — it sees static HTML and
  `<noscript>`. Unconfirmed log reports claim OpenAI's crawlers began
  rendering JS in late Sept 2026; OpenAI hasn't said so. Keep important
  content in the initial HTML. (industry)
- Crawlers: `OAI-SearchBot` builds the search index (blocking it removes a
  site from ChatGPT search answers), `GPTBot` is for training, `ChatGPT-User`
  fetches on a user's behalf. See `../technical-seo/ai-crawler-access.md`.
  (OpenAI docs, documented)

**Perplexity**
- Official: `PerplexityBot` "is designed to surface and link websites in
  search results on Perplexity. It is not used to crawl content for AI
  foundation models." `Perplexity-User` fetches pages a user asked about and
  "generally ignores robots.txt rules." (Perplexity docs, documented)
- Runs its own crawler, index, retrieval, and ranking. At its Search API
  launch (Sept 2025) Perplexity said its index covers "hundreds of billions
  of webpages" and updates "tens of thousands of documents per second."
  (industry, quoting Perplexity) It runs on **Vespa** (announced as a
  partnership by Vespa, Apr 2025). (industry)
- Retrieval detail: Perplexity's own research post describes "hybrid
  retrieval mechanisms" and "multi-stage ranking pipelines"; secondary
  accounts add BM25 + embeddings + a cross-encoder reranker inside ~100ms,
  which Perplexity hasn't confirmed. (documented at the hybrid/multi-stage
  level; industry beyond that)
- Cites more sources per answer than ChatGPT, often several per claim,
  consistent with being retrieval-first. A "3x more sources" figure from one
  vendor comparison has no traceable methodology — say "denser," not "3x."
  (industry)
- Cloudflare reported in Aug 2025 that Perplexity used undeclared crawlers to
  reach sites that had blocked its declared bots; Perplexity disputed it.
  (industry)

**Gemini app / Gemini API grounding / AI Overviews / AI Mode — four distinct
surfaces, do not conflate**
- Gemini API grounding (official): with the `google_search` tool enabled,
  "the model handles the entire workflow of searching, processing, and
  citing information automatically" — it decides whether to search,
  generates queries, and returns grounding metadata with citations. The
  older `google_search_retrieval` tool (with a 0–1 "dynamic retrieval"
  threshold) is legacy. (Google AI for Developers, documented)
- **AI Overviews and AI Mode are rooted in Google Search — but not in the
  top 10 for your query.** Google says both are "rooted in our core Search
  ranking and quality systems" and "may use a 'query fan-out' technique —
  issuing multiple related searches across subtopics and data sources" to
  show "a wider and more diverse set of helpful links." To be eligible, a
  page only needs to be "indexed and eligible to be shown in Google Search
  with a snippet" — "there are no additional technical requirements."
  (Google Search Central, documented)
  - What that means in data: Ahrefs' Mar 2026 update (863K SERPs, ~4M AI
    Overview URLs) found only **37.9%** of AI Overview citations rank in the
    top 10 for the original query, 31.2% rank 11–100, and 31.0% rank beyond
    100 — down from 76% in its July 2025 study, which Ahrefs attributes to
    fan-out sub-queries. (industry, disclosed methodology) Ranking well in
    Google's index still matters (it's the same index and quality systems),
    but ranking for the *head* query is no longer a near-precondition.
- **AI Mode status (2026)**: available in ~200 countries and territories in
  98 languages, no subscription, Gemini 3.5 Flash as the default model, 1B+
  monthly users; a follow-up asked inside an AI Overview now continues into
  AI Mode. It is *not* the default Google search experience. (Google, May
  2026, documented)
- Site owners can opt a whole property out of AI Overviews, AI Mode, and
  Discover's AI features in Search Console (worldwide since 2026-08-31);
  `Google-Extended` does **not** control these surfaces. See
  `../technical-seo/ai-crawler-access.md`. (documented)
- **What not to believe**: treating "Gemini," "AI Overviews," and "AI Mode"
  as one interchangeable thing is a common practitioner error — they are
  separate products (plus bare API grounding for third-party apps) with
  different retrieval mechanics and different opt-out controls.

**Claude (Anthropic)**
- Official mechanism: a server-side web-search tool inside Claude's tool-use
  loop runs searches and returns results the model cites inline. Tool
  versions so far: `web_search_20250305`; `web_search_20260209`, which adds
  **dynamic filtering** (Claude writes and runs code to filter results before
  they enter its context, on Claude 4.6+ models); and `web_search_20260318`,
  which adds a `response_inclusion` control. The docs don't name a search
  provider. (Anthropic docs, documented)
- **Search provider**: Anthropic's subprocessor list has named **Brave
  Search** for web search since 2025-03-19 (still listed in a Jul 2026
  re-check), and added **turbopuffer** on 2026-05-06 as providing "web search
  for all Anthropic products except Claude for Government." What each
  supplies isn't public. (industry — subprocessor list reported secondhand;
  the Trust Center page couldn't be fetched directly) Optimize for Brave's
  index as a reasonable proxy, not a certainty.
- Earlier reports of 86.7% → 79.2% overlap between Claude's citations and
  Brave's top results come from a single vendor test and can't be checked;
  treat them as anecdotal. (industry, unverified)
- Crawlers: `Claude-SearchBot` (search indexing), `Claude-User` (user
  fetches), `ClaudeBot` (training), all of which honor robots.txt.
  (Anthropic support docs, documented)

### Summary table

| Assistant | Own crawl/index? | External results | Live-search trigger | What predicts citation |
|---|---|---|---|---|
| ChatGPT | Yes (OAI-SearchBot; own index "labrador") | Third-party providers; Google-derived results dominant in 2026 measurements; Bing named by OpenAI | Model-decided, ~1/3 of prompts (Semrush, Feb 2026) | Weakly tied to Google/Bing rank; post-retrieval LLM judgment |
| Perplexity | Yes (own crawler + Vespa index) | None documented | Near-always (retrieval-first) | Own hybrid retrieval + multi-stage ranking |
| Gemini app / API grounding | Google's | Google Search | Model-decided | Google Search ranking as candidate pool |
| Google AI Overviews / AI Mode | Google's (same index + quality systems as Search) | — | AIO: Google decides per query; AI Mode: always | Google ranking across fan-out sub-queries, not just the head query (only ~38% of AIO citations in its top 10) |
| Claude | No public index | Brave Search (and turbopuffer) per subprocessor list | Model-decided (tool use) | Provider ranking, then Claude's own filtering |

## How this shows up in the workflow
Stage 2 (baseline monitoring) lists this file as background: it explains why
prompt-visibility results differ so much across engines, and why per-engine
reporting matters. It also underpins stage 3/6 (competitor research and
content) — explaining why winning classic SEO rank doesn't guarantee an AI
citation, and why Google's AI surfaces reward ranking across a topic's
sub-questions rather than one head term.
