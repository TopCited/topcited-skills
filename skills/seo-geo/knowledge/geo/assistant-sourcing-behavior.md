---
topic: How each AI assistant finds and cites sources (ChatGPT, Perplexity, Gemini, Claude, Grok, Copilot)
stage-relevance: [2]
last-verified: 2026-10-24
sources:
  - https://help.openai.com/en/articles/9237897-chatgpt-search (accessed 2026-10-24)
  - https://developers.openai.com/api/docs/bots (accessed 2026-10-24)
  - https://think.resoneo.com/chatgpt-retrieval/ (ChatGPT result sources, Jul–Aug 2026; accessed 2026-10-24)
  - https://docs.peec.ai/research/chatgpt-own-search-index-labrador (accessed 2026-10-24)
  - AirOps citation-rate study, via https://searchengineland.com/study-how-generative-engines-select-and-cite-sources-471606 (accessed 2026-10-24)
  - https://docs.perplexity.ai/docs/resources/perplexity-crawlers (accessed 2026-10-24)
  - Tinuiti Q1 2026 AI Citation Trends report, via https://everything-pr.com/perplexity-citation-source-index-2026 (accessed 2026-10-24)
  - https://developers.google.com/search/docs/appearance/ai-features (accessed 2026-10-24)
  - https://ahrefs.com/blog/ai-overview-citations-top-10/ (2026-03-02 update; accessed 2026-10-24)
  - https://seranking.com/blog/ai-mode-research/ (AI Mode vs organic overlap, 2025; accessed via search summary)
  - https://searchengineland.com/what-15-7-million-ai-mode-citations-reveal-about-getting-quoted-by-google-483393 (scroll-to-text links in AI Mode; accessed via search summary)
  - https://wicg.github.io/scroll-to-text-fragment/ (Text Fragments spec)
  - https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool (accessed 2026-10-24)
  - https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler (accessed 2026-10-24)
  - https://xponent21.com/insights/claude-web-search-brave-turbopuffer/ (Anthropic subprocessor re-check, 2026-07; accessed 2026-10-24)
  - https://docs.x.ai/docs/guides/tools/search-tools (accessed 2026-10-24)
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access (updated 2026-08-18; accessed 2026-10-24)
  - https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview (accessed 2026-10-24)
  - https://blogs.bing.com/webmaster/2026/10/introducing-topics-portfolio-beta-in-ai-performance/ (accessed 2026-10-24)
  - https://windowsreport.com/microsoft-copilot-seems-to-be-making-sign-in-mandatory-across-edge-bing-and-mobile-apps/ (2026-08-18; accessed via search summary)
  - TopCited internal research (LLM-monitoring industry study, 2026-08 — unpublished): assistant access paths, cross-engine citation overlap
  - heuristic
---

# Assistant sourcing behavior

## In plain words
Each AI assistant finds and picks its sources differently: ChatGPT blends its
own index with results from outside search providers, Perplexity and Google
run their own indexes, Copilot reads Bing, Grok leans on real-time posts from
X/Twitter, and Claude uses third-party search providers and can't be checked
while logged out at all. If you want your brand or page to get cited, you
have to know which underlying engine actually does the finding for the
assistant you care about — optimizing for "AI search" in general is too vague
to act on.

## What practitioners need to know

**No single mechanism covers all assistants.** Treat each one as its own retrieval
system with its own citation UI:

- **ChatGPT** retrieves from a mix of OpenAI's own index and third-party
  search providers — OpenAI documents "other search providers" and names
  Bing for some queries, and 2026 analyses of ChatGPT's result metadata found
  Google-derived results dominating (see
  `../foundations/how-llms-source-answers.md`). It fans the query out into
  sub-questions before citing. It is highly selective: an AirOps study
  (548,534 retrieved pages, 15,000 prompts) found it cites only **~15%** of
  pages it retrieves, and about a third of cited pages appeared only in
  fan-out sub-query results (industry-tier). Ranking on Google or Bing alone
  is a weak lever. Citations render as inline source chips/footnotes that
  expand to a sources panel. OpenAI's crawlers: `OAI-SearchBot` (search
  index — blocking it removes you from ChatGPT search answers), `GPTBot`
  (training), `ChatGPT-User` (user-initiated fetches), `OAI-AdsBot` (ad
  landing pages only) — documented; see
  `../technical-seo/ai-crawler-access.md`.
- **Perplexity** cites far more densely than ChatGPT or Gemini — reported ranges of
  roughly 8 to 22 citations per answer vary by study, so report it as "cites more
  densely," not a fixed number. Source mix skews heavily social: Tinuiti's Q1 2026
  AI Citation Trends report (industry-tier) put Reddit at roughly **24%** of
  Perplexity citations in Jan 2026 — the highest single-domain concentration of any
  engine — though other studies report anything from ~4% to ~47% depending on
  what they count, so cite the source with the number. Freshness appears to matter
  a lot; one analysis found content published in the last 30 days was cited at an
  **82%** rate (heuristic, single source, no traceable methodology). Format is
  numbered inline `[n]` on nearly every sentence — the tightest claim-to-source
  binding of the major assistants. `Perplexity-User` "generally ignores
  robots.txt rules" (documented).
- **Gemini / Google AI Overviews / AI Mode** use documented "grounding" in Google
  Search plus query fan-out into parallel sub-queries; Google says the features are
  "rooted in our core Search ranking and quality systems" (documented). Overlap
  with the top 10 for the original query is low and falling: Ahrefs' Mar 2026
  update found **37.9%** of AI Overview citations rank in the top 10 (industry,
  disclosed methodology), and SE Ranking's 2025 AI Mode study found only **14%**
  exact-URL overlap (21.9% at domain level) between AI Mode citations and the top
  10 (industry). Ranking #1 for the head term does not predict an AI citation.
  Many AI Mode citation links carry a scroll-to-text fragment (`#:~:text=`)
  highlighting the lifted passage — one vendor study of 15.7M AI Mode citations put
  it at ~48%, with a median highlighted passage of ~117 words (a paragraph, not a
  sentence). The Text Fragments spec is real; Google hasn't documented this usage
  (industry).
- **Claude** is the one major assistant with **no logged-out access path**
  (claude.ai has no guest mode; incognito chats still require an account —
  TopCited internal research, consistent with public sources) — this is why the
  industry sells Claude coverage as a paid API add-on rather than as UI-derived
  data. Anthropic runs three crawlers with distinct jobs: `ClaudeBot` (training),
  `Claude-User` (live per-prompt fetch), `Claude-SearchBot` (search indexing), all
  documented as honoring robots.txt. Claude's web search uses third-party
  providers — Anthropic's subprocessor list names Brave Search (since 2025-03) and
  turbopuffer (since 2026-05) for web search (industry, reported secondhand). The
  current tool version can filter results with code before citing ("dynamic
  filtering," documented); claims of a specific credibility filter that avoids a
  brand's own self-description are not documented by Anthropic (heuristic).
- **Grok** is structurally different: it searches the web *and* live X/Twitter posts
  as a first-class citation source — xAI's API exposes separate Web Search and X
  Search tools (documented); no other major assistant indexes real-time social
  posts this way. Consumer modes are now Auto / Fast / Expert / Heavy (Heavy on
  top paid tiers), with DeepSearch still offered as a feature (industry). Guest
  access appears to have closed — 2026 guides say Grok requires a free account
  (email or X login) — **re-test logged-out before assuming either way**
  (heuristic).
- **Copilot** is effectively gated on Bing SEO: Microsoft documents that Copilot
  generates search queries, sends them to "the Bing search service," and builds
  the answer from those results (documented, for Microsoft's work Copilot; the
  consumer app is industry consensus). Get indexed and ranking in Bing (Bing
  Webmaster Tools, IndexNow, backlinks). Bing Webmaster Tools' **AI Performance**
  report (public preview 2026-02-10, expanded 2026-06-16, Topics Portfolio beta
  2026-10-13) shows citations, cited pages, a sample of grounding queries, and
  topic-level "opportunity queries" across Copilot, Bing's AI summaries, and select
  partners — no click data (documented). Copilot's guest path has been tightening:
  Aug 2026 testing found a sign-in wall across Edge, Bing, and the mobile apps,
  with no official announcement (industry).

**Per-assistant citation format and density** (heuristic-tier unless noted —
consistent across multiple blogs, not independently verified against vendor UI
docs):

| Assistant | Format | Density |
|---|---|---|
| ChatGPT | inline source chips/footnotes → sources panel; since ~May 2026 can also add inline links without searching | not reliably quantified (an often-repeated "~8 per answer" figure has no traceable source) |
| Perplexity | numbered inline `[n]`, nearly every sentence | highest of any engine, range 8–22 |
| Gemini / AI Mode | inline links, often with passage-level text-fragment anchors | implicit/subtle, not always fully attributed |
| Claude | inline citations when web search is invoked | not quantified in sources found |
| Grok | inline citations (opt-in in the API), web + X split | not quantified in sources found |
| Copilot | inline citations, gated on Bing index presence | measurable per site in Bing's AI Performance report |

*(Table current as of 2026-10-24 — re-verify before relying on it more than a few
months out; assistant citation UIs change without notice.)*

Cross-engine overlap is low: only **11%** of cited domains are shared between
ChatGPT and Perplexity (TopCited internal research) — optimizing for one
assistant's sourcing behavior does not transfer cleanly to another.

## How this shows up in the workflow
Stage 2 (baseline monitoring) lists this file: use it when deciding which
assistants to track and how to interpret per-engine citation density and
access-path gaps (Claude, and increasingly Copilot and Grok, need logged-in or
API collection). It's also relevant to review/monitoring (stage 08) — explaining
why per-engine results diverge.
