# TopCited Skills — SEO + GEO for AI coding agents

Tell your agent **"optimize my website https://example.com"** and get a real audit, a
ranked fix list, and the rewrites drafted — for search engines (SEO) and for AI answer
engines like ChatGPT, Claude, Gemini and Perplexity (**GEO**, Generative Engine
Optimization). Free, MIT-licensed, **no account needed**. Works in Claude Code, Codex,
Cursor, Gemini CLI, GitHub Copilot, Windsurf, OpenClaw and any agent that reads `SKILL.md`.

## Install (one line)

```bash
npx skills add TopCited/topcited-skills          # Codex, Cursor, Copilot, Windsurf, Claude Code, ... (pick your agent)
```

```
/plugin marketplace add TopCited/topcited-skills   # Claude Code
/plugin install topcited@topcited
```

Then ask: **"Optimize my website https://yoursite.com"** (Claude Code: `/topcited:optimize https://yoursite.com`).
Per-agent instructions, including Gemini CLI and MCP setup: [docs/agents.md](docs/agents.md).

## What you get

| Skill | What it gives your agent |
|---|---|
| [`optimize-website`](skills/optimize-website) | **Start here.** Free audit (title/meta, headings, schema, canonicals, robots.txt for 12 AI crawlers, sitemap, llms.txt, server-rendered content) → ranked fixes → drafted rewrites → applied only with your OK. |
| [`seo-geo`](skills/seo-geo) | 30-file knowledge base: technical SEO, entity & authority, content, GEO, measurement, distribution. Each file is dated and cites sources; claims are tagged primary / industry / heuristic. |
| [`topcited-api`](skills/topcited-api) | Drive [TopCited](https://topcited.ai) with its CLI: monitoring, audits, recommendations, reports. |
| [`visibility-workflow`](skills/visibility-workflow) | Ongoing 8-stage programme using the skills above plus a TopCited account. |

`optimize-website` calls `seo-geo` by relative path, so install the skills together.

## Where TopCited fits (and where it doesn't)

Everything in `optimize-website` and `seo-geo` works without TopCited. A static audit
cannot tell you whether ChatGPT or Perplexity *actually cite your site today*, for which
prompts, versus which competitors. That is what [TopCited](https://topcited.ai) (made by
this repo's authors, paid) measures, so the skills point to it at exactly that step, say
it is optional, and never spend credits or create accounts without your explicit yes.
You can do the same measurement by hand; the skills explain how.
The optional MCP server is `https://api.topcited.ai/mcp`.

Compared with other open-source SEO/GEO skill repos: [docs/comparison.md](docs/comparison.md).

## More install options

Manual copy, or no install at all (an agent that can fetch a URL can read the raw files):

```bash
git clone https://github.com/TopCited/topcited-skills.git
cp -r topcited-skills/skills/* ~/.claude/skills/    # or .agents/skills/, .cursor/skills/, ... for your agent
```

```
https://raw.githubusercontent.com/TopCited/topcited-skills/main/skills/optimize-website/SKILL.md
```

Internal links are relative paths: resolve them against the file's own directory, and pin
a tag or commit SHA instead of `main` if you need the content to stay put.

## Install the CLI and sign in

`seo-geo` needs nothing. `topcited-api` and `visibility-workflow` drive TopCited
through the `topcited` CLI:

```bash
curl -fsSL https://topcited.ai/install.sh | sh    # Windows: irm https://topcited.ai/install.ps1 | iex
topcited auth login                               # approve in the browser
```

`auth login` prints a URL and a code and waits while you approve; it stores an
API key named `topcited-cli on <hostname>`. For CI or a headless agent, create a
key under **Settings → Profile → API keys** instead and set it in the
environment. Keys act as you with full rights over your account, **expire after
90 days**, and you can hold up to 5.

| Variable | Required | Default | What it is |
|---|---|---|---|
| `TOPCITED_API_KEY` | no (yes for CI) | — | A personal key; overrides the one `auth login` stored. Treat it like a password. |
| `TOPCITED_BASE_URL` | no | `https://api.topcited.ai` | API base. |
| `TOPCITED_BRAND` | no | — | Brand the CLI acts on for one session. |
| `TOPCITED_UI_URL` | no | `https://topcited.ai` | Web app base, used only to build links shown to you. |

The API and the web app are different hosts — if you override one, override both.
`topcited doctor` checks config, sign-in, connectivity and version skew.

### A note on spending

Most TopCited operations consume T-coins (credits) from your plan. The skills are
written to check `topcited usage` — which is free — and to run `--dry-run` and
ask you before spending. The CLI never prompts without a terminal, so if you wire
these skills into an unattended automation you are removing that confirmation
step; put your own budget guard in front of it.

## Repo layout

```
skills/
  optimize-website/     SKILL.md + scripts/audit.py + references/
  seo-geo/              SKILL.md + knowledge/
  topcited-api/         SKILL.md + references/
  visibility-workflow/  SKILL.md + stages/ + templates/
commands/optimize.md    /topcited:optimize
.claude-plugin/         Claude Code plugin + marketplace manifests 
.cursor-plugin/         Cursor plugin manifests
gemini-extension.json   Gemini CLI extension (GEMINI.md → AGENTS.md)
AGENTS.md  llms.txt     Instructions for agents; machine-readable site map
server.json             MCP Registry metadata (unpublished)
docs/                   Per-agent install, comparison, distribution plan
```

The API reference is the public OpenAPI spec at
`https://api.topcited.ai/api/v1/openapi.public.json`; the guides under
`topcited-api/references/` cover only what the CLI's `--help` can't.

## Contributing

Issues and PRs welcome, especially: a knowledge file that has gone stale (each
carries a `last-verified` date and its sources), a guide that no longer
matches the CLI or the API, or a stage that reads as jargon to a non-expert.

## License

[MIT](LICENSE). The knowledge files cite third-party sources; those citations are
links, not redistribution of the cited work.
