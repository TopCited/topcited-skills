---
topic: How each AI assistant finds and cites sources (ChatGPT, Perplexity, Gemini, Claude, Grok, Copilot)
stage-relevance: [2]
last-verified: 2026-08-20
sources:
  - https://www.conbersa.ai/learn/bing-indexing-optimization-for-chatgpt (accessed 2026-08-20)
  - https://lemniscategrowth.com/blogs/how-chatgpt-search-works.html (accessed 2026-08-20)
  - AirOps study on ChatGPT citation rate, via https://www.conbersa.ai/learn/bing-indexing-optimization-for-chatgpt (accessed 2026-08-20)
  - https://medium.com/@aivsrank/how-ai-engines-cite-sources-patterns-across-chatgpt-claude-perplexity-and-sge-8c317777c71d (accessed 2026-08-20)
  - https://platform.openai.com/docs/bots (bot-name split; not directly re-fetched this pass — verify before relying on exact bot names)
  - https://everything-pr.com/perplexity-citation-source-index-2026 (accessed 2026-08-20)
  - https://topify.ai/blog/chatgpt-perplexity-gemini-cite-differently (accessed 2026-08-20)
  - Tinuiti (named research firm), Jan 2026, via https://everything-pr.com/perplexity-citation-source-index-2026 (accessed 2026-08-20)
  - https://www.stackmatix.com/blog/perplexity-optimization-multi-source-citation (accessed 2026-08-20)
  - https://firstmotion.com/insights/how-google-ai-mode-and-ai-overviews-select-sources (accessed 2026-08-20)
  - https://www.clickrank.ai/how-ai-overviews-select-the-source/ (accessed 2026-08-20)
  - https://wicg.github.io/scroll-to-text-fragment/ (Text Fragments spec — mechanism is documented web-platform tech; Google's use of it for AI Mode citations is unverified)
  - https://stridec.com/blog/how-to-get-cited-in-claude/ (accessed 2026-08-20)
  - https://www.searchcans.com/blog/anthropic-claude-web-search-2026/ (accessed 2026-08-20)
  - https://www.oltre.ai/blog/how-claude-picks-sources-technical-breakdown-claude-citations/ (accessed 2026-08-20)
  - https://www.datastudios.org/post/grok-real-time-search-how-x-integration-live-web-retrieval-citations-and-agent-tools-turn-xai-s (accessed 2026-08-20)
  - https://www.winstondigitalmarketing.com/playbooks/bing-copilot-optimization/ (accessed 2026-08-20)
  - TopCited internal research (LLM-monitoring industry study, 2026-08 — unpublished): assistant access paths, cross-engine citation overlap
  - heuristic
---

# Assistant sourcing behavior

## In plain words
Each AI assistant finds and picks its sources differently: some read from Bing's
search index, some crawl the web themselves, one leans on real-time posts from
X/Twitter, and one (Claude) can't be checked while logged out at all. If you want
your brand or page to get cited, you have to know which underlying engine actually
does the finding for the assistant you care about — optimizing for "AI search" in
general is too vague to act on.

## What practitioners need to know

**No single mechanism covers all assistants.** Treat each one as its own retrieval
system with its own citation UI:

- **ChatGPT** retrieves from Bing's index, then fans out the query into
  sub-questions and re-ranks before citing (heuristic; no OpenAI doc confirms the
  re-ranking layer). It is highly selective: an AirOps study found it cites only
  **~15%** of pages it actually retrieves, and Bing's top-3 rank predicts an actual
  ChatGPT citation only **6.8–7.8%** of the time (industry-tier, methodology not
  independently verified) — meaning Bing rank alone is a weak lever. Citations
  render as superscript `[1][2][3]` footnotes that expand to a sources sidebar.
  OpenAI runs distinct crawlers for training (`GPTBot`) vs. live search
  (`OAI-SearchBot`) — documented, but verify current bot names directly before
  publishing anything bot-name-specific.
- **Perplexity** cites far more densely than ChatGPT or Gemini — reported ranges of
  roughly 8 to 22 citations per answer vary by study, so report it as "cites more
  densely," not a fixed number. Source mix skews heavily social: a named Tinuiti
  study (industry-tier) found **31%** of Perplexity citations come from social
  media, with Reddit alone at **20–24%** — the highest single-domain concentration
  of any engine. Freshness appears to matter a lot: one analysis found content
  published in the last 30 days was cited at an **82%** rate (heuristic, single
  source). Format is numbered inline `[n]` on nearly every sentence — the tightest
  claim-to-source binding of the major assistants.
- **Gemini / Google AI Overviews / AI Mode** use documented "grounding" — retrieval
  anchored in Google's live index, Knowledge Graph, and Shopping Graph — plus query
  fan-out into parallel sub-queries. Only about **14%** overlap exists between
  AI-cited URLs and top-10 organic results for the same query (heuristic, single
  source) — ranking #1 organically does not predict an AI citation. There's a
  plausible (but unverified) claim that citation URLs carry a hidden text-fragment
  anchor pointing at the exact sentence lifted — the Text Fragments web spec is
  real; Google's specific use of it for AI Mode citations is not confirmed.
- **Claude** is the one major assistant with **no logged-out access path**
  (claude.ai has no guest mode and is Cloudflare-protected — TopCited internal
  research) — this is why the industry sells Claude coverage as a paid API
  add-on rather than as UI-derived data. Anthropic runs three crawlers with distinct
  jobs: `ClaudeBot` (training), `Claude-User` (live per-prompt fetch),
  `Claude-SearchBot` (search indexing) — worth verifying directly before citing bot
  names externally. Claude's live web search is reported to be Brave-powered with
  ~87% citation overlap vs. raw Brave results (heuristic, single source), with an
  added credibility-filtering layer that reportedly avoids citing a brand's own
  self-description without third-party corroboration.
- **Grok** is structurally different: it searches the indexed web *and* live
  X/Twitter posts as a first-class citation source — no other major assistant
  indexes real-time social posts this way. Two modes are reported: fast indexed
  **WebSearch** vs. multi-step autonomous **DeepSearch**. Guest access exists
  (~10 prompts/2h, mini-tier model per TopCited internal research) — worth
  retesting before assuming Grok requires a login.
- **Copilot / Bing Chat** is effectively gated on Bing SEO: get indexed and ranking
  in Bing (classic techniques — Bing Webmaster Tools, IndexNow, backlinks), because
  Copilot mostly reads what Bing already crawled rather than browsing live.
  Bing Webmaster's "AI Performance" report is a real, dated integration point
  (TopCited internal research cites public preview 2026-02-11, expanded 2026-06-16) — **this
  pass could not independently re-verify that launch-date/report-name claim
  against a primary Bing source**, so treat it as unconfirmed until checked
  against Bing's own documentation. Copilot's guest path is reported to be
  tightening through 2025–2026, unconfirmed either way as of this research date.

**Per-assistant citation format and density** (all heuristic-tier — consistent
across multiple blogs, not independently verified against vendor UI docs):

| Assistant | Format | Density |
|---|---|---|
| ChatGPT | superscript `[n]` → popover → sidebar | ~8 sources/answer (range 7.9–8.2) |
| Perplexity | numbered inline `[n]`, nearly every sentence | highest of any engine, range 8–22 |
| Gemini / AI Mode | inline links, sentence-level text-fragment anchors | implicit/subtle, not always fully attributed |
| Claude | inline citations when web search is invoked | not quantified in sources found |
| Grok | inline citations via agent-tools API, web + X split | not quantified in sources found |
| Copilot | inline citations, gated on Bing index presence | not quantified in sources found |

*(Table current as of 2026-08-20 — re-verify before relying on it more than a few
months out; assistant citation UIs change without notice.)*

Cross-engine overlap is low: only **11%** of cited domains are shared between
ChatGPT and Perplexity (TopCited internal research) — optimizing for one
assistant's sourcing behavior does not transfer cleanly to another.

## How this shows up in the workflow
Not currently referenced by any stage file in `visibility-workflow/stages/` (grep
run 2026-08-20 found no hits). It's most relevant in practice to **baseline
monitoring (stage 02)** — deciding which assistants to track and how to interpret
per-engine citation density — and to **review/monitoring (stage 08)** — explaining
why per-engine results diverge. Flag to the workflow maintainer as a candidate
knowledge-ref addition rather than adding an unrequested stage link here.
