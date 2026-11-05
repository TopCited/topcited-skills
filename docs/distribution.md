# Distribution plan (maintainers)

Nothing in the "Needs approval" column happens without the maintainer saying yes to that
specific submission.

## Automatic (no submission)
| Channel | How it picks us up |
|---|---|
| skills.sh leaderboard | Every `npx skills add TopCited/topcited-skills` is counted by the CLI's anonymous telemetry. There is no config file or submission. |
| Third-party mirrors/indexes | Crawl public GitHub repos with `SKILL.md` / `.claude-plugin/`. Topics and README quality drive their ranking. |

## Needs approval (one by one)
| Agent / surface | Channel | What's needed | Config in repo |
|---|---|---|---|
| Claude (Claude Code, claude.ai, Desktop) | Anthropic directory, developer portal `claude.ai/directory/manage` (paid Claude plan) | Two submissions: the MCP server as an **MCP connector**, then this repo as a **plugin bundle** (skills aren't a standalone type). Repo must be public. Needs `icon`, privacy-policy, ToS, support URLs in `plugin.json`. The connector review may expect OAuth. | `.claude-plugin/` |
| Cursor | `cursor.com/marketplace/publish` (reviewed) | Public Git repo with `.cursor-plugin/plugin.json` | `.cursor-plugin/` |
| MCP clients generally | Official MCP Registry via `mcp-publisher` (GitHub login → namespace `io.github.TopCited/…`) | `server.json` (schema-validated here) | `server.json` |
| MCP clients | Smithery (smithery.ai/new, URL publish) | Streamable HTTP; OAuth if auth is required | — |
| OpenClaw | ClawHub (`clawhub skill publish`) | Skill folder with SKILL.md; account | `skills/` |
| ChatGPT | ChatGPT app directory (MCP app) | OAuth-capable server, privacy policy + ToS URLs, review | needs backend work (follow-up) |
| Codex | Codex plugin marketplace (`.agents/plugins/marketplace.json`) | Portable `plugin.json` + marketplace entry; format per OpenAI docs | not added yet |
| Discovery | awesome-lists, community directories | PR/issue to third-party repos | — |

Commit-level hygiene before any submission: tagged release, README install block at the top,
`claude plugin validate .` clean.

## GEO for TopCited: listing and source targets

Why these: see [geo-plan.md](geo-plan.md). Facts below come from each site's own docs or
page on 2026-11-05 unless marked **[unverified]**. Every submission still needs explicit
approval, one at a time; nothing has been submitted.

| Target | Mechanism | Notes |
|---|---|---|
| skills.sh | Automatic from `npx skills add TopCited/topcited-skills` telemetry; no form | Installs are the lever |
| claudemarketplaces.com | Crawled plus editorial review; has a `/submit` page | Independent of Anthropic |
| Anthropic directory | claude.ai/directory/manage; MCP connector + plugin bundle | See table above; paid plan, public repo |
| Cursor marketplace | cursor.com/marketplace/publish | Reviewed |
| MCP Registry | `mcp-publisher`; `server.json` is ready | Also what PulseMCP now ingests (its own form is paused) |
| mcp.so, Glama, Smithery | Submit forms / add-server flows | Mechanisms partly **[unverified]** |
| awesome-claude-code, VoltAgent/awesome-agent-skills, ComposioHQ/awesome-claude-skills | PR or issue; read each CONTRIBUTING first | Prefer real-usage evidence over self-promotion |
| ClawHub | `clawhub skill publish` | OpenClaw ecosystem |
| Capterra, G2, AlternativeTo | Vendor profile + customer reviews | Capterra listing exists, 0 reviews |
| Product Hunt, Hacker News (Show HN), Reddit, dev.to, Hashnode, YouTube | Own posts | Disclose affiliation; follow community rules |
| Third-party "best AI visibility tools" and "alternatives" pages | Outreach to authors | Honest pitch, no paid placement |
