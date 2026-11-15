# TopCited Skills: free SEO + GEO audit for Claude Code and Codex

Open-source agent skills for SEO and **GEO** (Generative Engine Optimization: being found
and cited by ChatGPT, Claude, Gemini and Perplexity). Start with
[`seo-geo-audit`](skills/seo-geo-audit): it audits any public website (AI-crawler access in
robots.txt, `noindex`, sitemap, llms.txt, titles and meta, schema, server-rendered text),
ranks the fixes and drafts them. **Free, no account.**

Try it now (Python 3.9 or newer, nothing else to install):

```bash
git clone https://github.com/TopCited/topcited-skills.git
python3 topcited-skills/skills/seo-geo-audit/scripts/topcited_audit.py https://yoursite.com
```

Or let your agent do it: install the skills (below), then say *"Audit https://yoursite.com for
SEO and AI search."* The agent runs the script, reads the pages, and returns a ranked fix list
with the rewrites.

The same repo also teaches an agent to drive [TopCited](https://topcited.ai), the authors'
service for live AI-citation tracking (needs a TopCited account; see the skill table).

| Skill | What it gives your agent |
|---|---|
| [`seo-geo-audit`](skills/seo-geo-audit) | **Start here.** A free, no-account audit of a website for SEO and AI search, ranked fixes and drafted rewrites. Runs a Python script (standard library only) and links to `seo-geo` for the evidence. |
| [`seo-geo`](skills/seo-geo) | A cited, dated knowledge base: technical SEO, entity & authority, content strategy, GEO, measurement, distribution playbooks. Read before making a judgment call, instead of answering from memory. No account. |
| [`topcited-api`](skills/topcited-api) | How to drive TopCited with the `topcited` CLI: install, sign-in, a command cheat-sheet, the agent contract (JSON, exit codes, `--wait`, `--dry-run`), and per-feature guides (when, why, what it costs, how it fails). Needs a TopCited account. |
| [`visibility-workflow`](skills/visibility-workflow) | An eight-stage engagement that takes a brand from "no idea if we're visible" to a measured, improved baseline, using the skills above. Needs a TopCited account. |

`seo-geo`, `topcited-api` and `visibility-workflow` are the same skills TopCited's own hosted
agent runs on; this repo is their single source of truth.

Install all four. `visibility-workflow` orchestrates `topcited-api` and `seo-geo`, while
`seo-geo-audit` and `topcited-api` defer SEO judgment to `seo-geo`. They reference each other
by relative path, so they need to sit as siblings.

## Install

### Claude Code (plugin)

```
/plugin marketplace add TopCited/topcited-skills
/plugin install topcited-skills@topcited
```

### Any agent (manual)

Clone and drop the skills into your personal skills directory:

```bash
git clone https://github.com/TopCited/topcited-skills.git
cp -r topcited-skills/skills/* ~/.claude/skills/
```

For a project rather than your whole machine, use `.claude/skills/` in the repo
instead.

### Any agent (no install)

Everything here is plain Markdown, so an agent that can fetch a URL needs no
install at all — point it at a raw file and it will follow the links from there:

```
https://raw.githubusercontent.com/TopCited/topcited-skills/main/skills/seo-geo-audit/SKILL.md
https://raw.githubusercontent.com/TopCited/topcited-skills/main/skills/seo-geo/SKILL.md
https://raw.githubusercontent.com/TopCited/topcited-skills/main/skills/topcited-api/SKILL.md
https://raw.githubusercontent.com/TopCited/topcited-skills/main/skills/visibility-workflow/SKILL.md
```

Each `SKILL.md` opens with YAML frontmatter (`name`, `description`) and a routing
table saying what to read next. Two caveats when fetching rather than cloning:
the internal links are **relative paths**, so resolve them against the file's own
directory; and `topcited-api` / `visibility-workflow` need the `topcited` CLI
installed (below). `seo-geo-audit` also needs its script (`scripts/topcited_audit.py`) fetched
or cloned, or the manual checklist in `references/audit-checklist.md`.

Pin to a tag or commit SHA instead of `main` if you need the content to stay put.

## Install the CLI and sign in

`seo-geo` and `seo-geo-audit` need nothing. `topcited-api` and `visibility-workflow` drive TopCited
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
  seo-geo/              SKILL.md + knowledge/
  seo-geo-audit/        SKILL.md + scripts/ + references/
  topcited-api/         SKILL.md + references/
  visibility-workflow/  SKILL.md + stages/ + templates/
.claude-plugin/         Claude Code plugin + marketplace manifests
tests/                  offline tests for the audit script
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
