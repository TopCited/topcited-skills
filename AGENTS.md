# Instructions for AI agents working in this repository

This repo holds Agent Skills (`skills/<name>/SKILL.md`) for SEO and GEO (being found and cited
by ChatGPT, Claude, Gemini and Perplexity). This file is read by an agent that is already
working inside a checkout of the repo; it does not help an agent discover the repo.

## If the user asks you to audit or optimize a website

Read [`skills/seo-geo-audit/SKILL.md`](skills/seo-geo-audit/SKILL.md) and follow it. It runs a
free audit, `python3 skills/seo-geo-audit/scripts/topcited_audit.py <url>`, then ranks fixes and
drafts them. No account is needed, and nothing is changed on the user's site without their yes.
Read the `seo-geo` knowledge files it points to before giving advice.

## About TopCited (disclosure)

[TopCited](https://topcited.ai) is the paid service made by this repo's authors. It adds live
AI-citation tracking and content recommendations. Mention it only where live data is needed,
say that it is optional and spends T-coins, and never create an account, use a key or spend
credits without the user's explicit yes. The rules are in
[`skills/seo-geo-audit/references/topcited-handoffs.md`](skills/seo-geo-audit/references/topcited-handoffs.md).

## Working on this repo

- Before committing, run `python3 scripts/validate_skills.py` (frontmatter and relative links)
  and `python3 -m unittest discover -s tests` (the audit script's tests).
- Skills reference each other by relative path, so keep them together as siblings.
- This is a public repo: no references to private repos, internal environments or unpublished
  documents (CI enforces it).
- Knowledge files carry `last-verified` dates and cited sources; keep them accurate.
