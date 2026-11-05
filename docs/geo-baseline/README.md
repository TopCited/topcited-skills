# Free real-AI baseline, 2026-11-05

15 queries (from [geo-queries.csv](../geo-queries.csv), plus the branded query "what is TopCited.ai")
sent verbatim, one at a time, with no plugins, skills or extra instructions:

- **Claude** via `claude -p` with WebSearch and WebFetch allowed (Claude Code CLI 2.1.318).
- **Codex** via `codex --search exec` with live web search, read-only sandbox (the CLI header reported model `gpt-6.1-sol`).

Raw answers: [claude/](claude/), [codex/](codex/). Queries: [queries.txt](queries.txt).
Cost: no TopCited T-coins; it used the maintainer's own Claude Code and Codex logins.

**Result.** TopCited / topcited-skills was mentioned in **0 of 14** unbranded queries on both
engines, and in the branded query on both (Claude via the Capterra listing, Codex via
topcited.ai). Full table and caveats: [../geo-plan.md](../geo-plan.md#3b-real-ai-baseline-free-2026-11-05).

**Caveats.**
- These are coding-agent CLIs, not the consumer chat products. They are a rough proxy for ChatGPT /
  Claude.ai, not the same system, and answers vary run to run (one run per query here).
- Bare agent-skill queries ("SEO audit skill for Claude Code", "GEO plugin for Cursor", "MCP server to
  track brand visibility") were read as build requests by the CLIs, so those rows say little about
  recommendation behaviour. "Is this influencer post misleading" and "LIVE-GEO benchmark" got a
  clarifying question. For those groups use the manual check in
  [../geo-manual-check.md](../geo-manual-check.md) with the chat products.
- Perplexity, Gemini, Copilot, Google AI Overviews and the ChatGPT consumer app were not queried.
