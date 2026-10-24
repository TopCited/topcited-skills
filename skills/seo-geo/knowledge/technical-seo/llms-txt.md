---
topic: llms.txt spec status, real-world adoption, and whether it actually affects AI citation
stage-relevance: [4, 5]
last-verified: 2026-10-24
sources:
  - https://llmstxt.org/ (spec; "Modified Aug 10, 2026")
  - https://github.com/w3c/strategy/issues/506 (the only W3C activity found — an open "Investigation"-stage strategy issue, no Community Group)
  - https://developers.google.com/search/docs/fundamentals/ai-optimization-guide (Google, updated 2026-07-10 — llms.txt mythbusting)
  - https://developers.google.com/search/updates (Google changelog, 2026-06-15 "Clarifying guidance on llms.txt files")
  - https://www.searchenginejournal.com/google-says-llms-txt-comparable-to-keywords-meta-tag/544804/ (Mueller, 2025-04)
  - https://www.searchenginejournal.com/googles-llms-txt-guidance-depends-on-which-product-you-ask (2026-05-20)
  - https://developer.chrome.com/docs/lighthouse/agentic-browsing/llms-txt (Lighthouse audit, updated 2026-05-05)
  - https://github.com/GoogleChrome/lighthouse/releases/tag/v13.2.0
  - https://www.rankability.com/data/llms-txt-adoption/ (scan of 2026-09-18)
  - https://ahrefs.com/blog/llmstxt-study/ (server-log study, 2026-06-15)
  - https://www.ezy.ai/research/do-ai-bots-read-llms-txt (server-log study, 2026-07-27; vendor sells llms.txt tooling)
  - https://arxiv.org/abs/2311.09735 (GEO paper — checked for the misattributed 23% claim)
---

# llms.txt

## In plain words
llms.txt is a proposed markdown file, hosted at `/llms.txt`, meant to give AI
tools a clean, curated summary of a site instead of making them parse full
HTML pages. It's cheap to add and roughly one in ten large sites now has one.
But Google says outright that it doesn't use it for Search, server logs show
the major AI crawlers almost never request it, and the most widely repeated
"it gets you cited more" statistic appears to be misattributed. Treat it as
low-cost hygiene for developer-facing sites, not a growth lever.

## What practitioners need to know
- **Spec status**: proposed by Jeremy Howard, published 2024-09-03, spec
  page last modified 2026-08-10. Format: a markdown file with a required H1
  (project/brand name), an optional blockquote summary, then H2-delimited
  sections of annotated links. It's deliberately positioned as
  **complementary** to robots.txt/sitemap.xml, not a replacement. It
  **remains a community proposal, not a ratified standard**, governed
  informally via GitHub and Discord. *(P)*
  - **No standards body has adopted it.** The only W3C activity is an open
    W3C strategy-repo issue (#506, opened 2025-04) still at the
    "Investigation" stage, with no Community Group or working draft. *(P)*
    A blog claim of a June 2026 W3C "working draft" could not be traced to
    any w3.org page — do not repeat it. No IETF Internet-Draft for llms.txt
    was found. (heuristic — absence of evidence)
- **Google Search does not use it.** Google's AI optimization guide and a
  2026-06-15 changelog entry state llms.txt files "aren't needed for Google
  Search (and won't negatively or positively impact your visibility or
  rankings)"; the same guide says you don't need "new machine readable files,
  AI text files, markup, or Markdown" to appear in AI Overviews or AI Mode.
  *(P)* This follows John Mueller's 2025-04 comparison of llms.txt to the
  keywords meta tag — "what a site-owner claims their site is about." *(I)*
- **Google is not consistent across products**, though: Chrome's Lighthouse
  added an llms.txt audit in v13.2.0 (May 2026), inside a new
  informational, unscored "Agentic Browsing" category; it calls llms.txt an
  "emerging convention," flags only server errors when fetching it, and
  treats a 404 as Not Applicable because the file is "optional at the
  moment." *(P)* So a Lighthouse llms.txt pass is an agent-readiness check,
  not an SEO signal.
- **No AI vendor has said its crawler or assistant reads third-party
  llms.txt files.** OpenAI, Anthropic and Google do *publish* llms.txt for
  their own developer docs (e.g. `docs.claude.com/llms.txt`,
  `platform.openai.com/docs/llms.txt`, `ai.google.dev/gemini-api/docs/llms.txt`
  all returned 200 on 2026-10-24), and Mintlify auto-generates one for hosted
  docs sites — consumption is mostly by IDE/coding agents a user points at
  the file, not by search crawlers. (heuristic for the consumption framing)
- **Server-log evidence: the big AI crawlers barely fetch it.**
  - Ahrefs (2026-06-15; 137,210 domains on Ahrefs Web Analytics, May 2026
    logs): 28% of those domains publish llms.txt (an upper bound — the
    customer base skews technical), and **97% of those files received zero
    requests** in the month. *(I)*
  - EZY.ai (2026-07-27; 83 sites, 12 weeks of verified-UA logs): llms.txt vs
    robots.txt fetches were OpenAI 7 vs 3,990, Anthropic 9 vs 3,120,
    Perplexity 0 vs 775, Googlebot 67 vs 5,125; only Meta-ExternalAgent
    fetched llms.txt more than robots.txt (193 vs 172). Small-business panel,
    and the vendor sells llms.txt tooling — directional only. *(I)*
- **Adoption data (Rankability tracker, scan of 2026-09-18, Tranco top
  sites)**: **9.3%** of the top 1,000 (93 sites) and **8.3%** of the top
  10,000 publish a valid llms.txt; 16 of the top 1,000 also publish
  `llms-full.txt`. Validation requires HTTP 200, a text type, recognizable
  markdown structure, and a fake-URL control to reject catch-all responses.
  The tracker publishes separate point-in-time observations, not a
  continuous monthly series (its earlier scanner measured 8.7% in June 2026
  and 0.3% in June 2025). *(I)*
- **Debunk: the "23% more AI citations" / "Princeton GEO-bench" claim is
  a misattribution.** Some industry summaries attribute a finding that
  llms.txt sites earn 23% more AI citations to "Princeton's GEO-bench." The
  actual GEO paper (Aggarwal, Murahari, Rajpurohit, Kalyan, Narasimhan,
  Deshpande, KDD 2024) evaluated nine *content* optimization methods
  (statistics, quotations, fluency, etc.) and **does not study llms.txt at
  all**. *(P)* Do not cite the 23% figure to Princeton/GEO-bench in any
  downstream material.
- **Honest framing**: llms.txt is a low-cost, low-yield bet — roughly half
  a day to implement, and worth shipping for dev-tool/SaaS/docs sites whose
  users point coding agents at documentation. (heuristic) Do not promise a
  citation or ranking lift from adding it: Google says it has no effect on
  Search, no AI vendor documents reading it, and log data shows the major AI
  crawlers rarely request it.

## How this shows up in the workflow
Stage 4 (site audit) checks whether `/llms.txt` exists and is well-formed
(and, for developer-facing sites, whether it's missing). Stage 5 (technical/
entity fixes) adds it as a low-cost hygiene item alongside other technical
fixes — framed to brand owners as "useful for agents reading your docs,"
explicitly not as a Google or AI-citation lever, given Google's on-record
statement and the fetch-log data above.
