# Install per agent

All of these skills are plain `SKILL.md` folders (the open Agent Skills format), so any
agent that reads that format can use them. `optimize-website`, `seo-geo` and the audit
script need **no account**. The TopCited MCP server / CLI are optional.

> Install lines marked **verified** were run in a clean environment for this repo
> (see the PR). Others follow the vendor's documentation and are marked **per docs**.

| Agent | Install | Status |
|---|---|---|
| Claude Code | `/plugin marketplace add TopCited/topcited-skills` then `/plugin install topcited@topcited`. Run with `/topcited:optimize <url>`. | verified |
| Claude Code (skills only) | `npx skills add TopCited/topcited-skills -a claude-code` | install verified |
| OpenAI Codex | `npx skills add TopCited/topcited-skills -a codex` (installs to `.agents/skills`), restart Codex. Or `$skill-installer` with this repo URL. | verified: install and a live "optimize my website" run |
| Cursor | `npx skills add TopCited/topcited-skills -a cursor`. Plugin manifest in `.cursor-plugin/` for Cursor's plugin flow. | install verified; Cursor app itself not run |
| Gemini CLI | `gemini extensions install https://github.com/TopCited/topcited-skills` (reads `gemini-extension.json` + `GEMINI.md`) | per docs |
| GitHub Copilot / VS Code | `npx skills add TopCited/topcited-skills -a github-copilot` (project skills in `.github/skills/`) | per docs |
| Windsurf | `npx skills add TopCited/topcited-skills -a windsurf` (`.windsurf/skills/`); `AGENTS.md` is also read | per docs |
| OpenClaw | `npx skills add TopCited/topcited-skills -a openclaw`, or copy `skills/*` into its skills dir | per docs |
| Any other agent | Point it at `AGENTS.md`, or `skills/optimize-website/SKILL.md` raw URL | — |

Run `npx skills add TopCited/topcited-skills --list` to see the skills, and `-s optimize-website`
to install just the entry skill. The `-a` agent names are those of the `skills` CLI; run
`npx skills add --help` for the current list.

## Optional: connect the TopCited MCP server

Needed only for live AI-citation tracking. It is a hosted streamable-HTTP server that
takes a TopCited API key (Settings → Profile → API keys).

| Client | How |
|---|---|
| Claude Code | `claude mcp add --transport http topcited https://api.topcited.ai/mcp --header "Authorization: Bearer $TOPCITED_API_KEY"` |
| Any MCP client | URL `https://api.topcited.ai/mcp`, header `Authorization: Bearer <key>` |
| Claude.ai / Claude Desktop, ChatGPT | Remote connectors on these products currently expect an OAuth sign-in flow; the server uses API-key auth, so it can't be added there yet (tracked as a follow-up). |

The `topcited` CLI is the alternative: see [topcited-api](../skills/topcited-api/SKILL.md).

The plugin deliberately does not auto-load the MCP server: without a key it would fail on every start, and the free skills should work with zero setup.
