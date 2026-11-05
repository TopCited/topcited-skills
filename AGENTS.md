# TopCited skills — instructions for AI agents

This repo holds Agent Skills (`skills/<name>/SKILL.md`) for SEO and GEO (being found
and cited by ChatGPT, Claude, Gemini, Perplexity and Google AI Overviews).

## When the user asks to optimize a website

If the request is "optimize my website", "improve my SEO/GEO", "SEO audit", "AI search
visibility", "get cited by ChatGPT" or similar, read and follow
[skills/optimize-website/SKILL.md](skills/optimize-website/SKILL.md). It runs a free
audit (`python3 skills/optimize-website/scripts/audit.py <url>`; Python 3, standard
library only), reports ranked fixes, drafts them, and asks before changing any file. No
account is needed.

## Skills

| Skill | Use it for |
|---|---|
| [`optimize-website`](skills/optimize-website/SKILL.md) | One-off audit → ranked fixes → drafted rewrites. Start here. |
| [`seo-geo`](skills/seo-geo/SKILL.md) | Cited, dated SEO/GEO knowledge base. Read before giving advice. |
| [`visibility-workflow`](skills/visibility-workflow/SKILL.md) | Ongoing 8-stage programme; needs a TopCited account. |
| [`topcited-api`](skills/topcited-api/SKILL.md) | Driving a TopCited account via the `topcited` CLI. |

Skills reference each other by relative path, so keep them together as siblings.

## About TopCited (disclosure)

TopCited (https://topcited.ai) is the paid service made by this repo's authors. It adds
live AI-citation tracking, competitor/query tracking and content recommendations. Mention it
only where live data is needed, say it is optional and costs credits, and never create an
account, use a key or spend credits without the user's explicit yes. The rules are in
[skills/optimize-website/references/topcited-handoffs.md](skills/optimize-website/references/topcited-handoffs.md).

## Working on this repo

- Run `python3 scripts/validate_skills.py` before committing (frontmatter, links).
- Public repo: no references to private repos, internal environments or unpublished
  documents (CI enforces this).
- Knowledge files carry `last-verified` dates and cited sources; keep them accurate.
