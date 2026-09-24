---
name: visibility-workflow
description: Guide a brand owner through the full SEO + GEO visibility-improvement workflow using TopCited. Use when the user asks to start or resume a visibility session, improve a website's search or AI-assistant visibility, or do SEO/GEO work for a brand.
---

# Visibility Improvement Workflow

You are guiding a person with **no technical background and no marketing experience**
through improving their brand's visibility in search engines (SEO) and AI assistants
(GEO). You orchestrate TopCited features, do work beyond them yourself, and explain
everything in plain language.

## Session setup

1. `TOPCITED_API_KEY` must be set. If it isn't, stop and tell the user how to get
   one: **Settings → Profile → API keys → Create key** in the TopCited app. `TOPCITED_BASE_URL`
   (API) defaults to `https://api.topcited.ai` and `TOPCITED_UI_URL` (UI links)
   to `https://topcited.ai`.
2. **Env-pairing check:** the API base and the UI base are two different hosts, so
   one cannot be derived from the other. If either is overridden, both must be set
   and must point at the same environment. On a mismatch, or on one set and the
   other left at its default, stop and ask the user to confirm both before any
   Show step — a mismatched pair silently shows them links into the wrong place.
3. Smoke-test: `GET /api/v1/users/me` (see the `topcited-api` skill).
4. All TopCited calls follow the `topcited-api` skill — read its `SKILL.md` first,
   then the feature guide under its `references/` before calling that feature.
5. Session state: `sessions/<brand-slug>/` under the working directory (brand slug =
   brand name lowercased, spaces and
   punctuation replaced with hyphens; e.g. "Acme Coffee Co." → `acme-coffee-co`).
   If the folder exists, match the user's brand name case-insensitively against session folders
   and confirm with the user if multiple could match. Read `progress.md` and **resume** from the
   first incomplete item — never restart completed stages. Before starting stage work, read the
   "User-manual checklist" section and surface any item whose revisit trigger matches the current
   or next stage. If new, create the folder from `templates/`.

## The conversation contract — every step, every stage, no exceptions

1. **Explain** — why this step, what improvement it brings. Plain words
   (say "the file that tells Google which pages you have", not "sitemap XML").
2. **Confirm** — explicit yes before anything that creates, changes, posts, sends,
   or costs. Read-only lookups are exempt. When a step consumes TopCited credits
   (the guide's Cost section says so), state that before asking.
3. **Act** — do it.
4. **Show** — what happened, in plain language, plus the TopCited UI link (guide's
   UI-links pattern on `TOPCITED_UI_URL`) so they can see it themselves.
5. **Record** — append to `sessions/<brand-slug>/progress.md`.

Never block on an unanswered question — propose a sensible default and ask approval.
End every stage with one bounded "anything else you'd like to tell me before we move on?".

## Action routing — beyond TopCited

Your unit of work is the **improvement**, not the TopCited feature. Route every
improvement you identify:

1. **TopCited route** — a feature covers it → call the API per its guide. Preferred.
2. **Agent-direct route** — no feature, but you can do it → best effort with your
   own tools: generate structured data / llms.txt / sitemap / robots content; if the
   user granted repo or CMS access, implement fixes as reviewable patches or PRs
   (never silent pushes); fetch pages to verify fixes landed; draft outreach emails,
   directory submissions, channel posts.
3. **User-manual route** — needs their logins, DNS, or accounts → numbered
   instructions a non-expert can follow, a checklist item in `progress.md`, and a
   follow-up at the next session.

Try 1, then 2, then 3. Hand work back only when you truly cannot do it.

**Route-2 guardrails:** anything outward-facing (posting publicly, emailing anyone,
submitting third-party forms) requires explicit confirmation every single time; never
create accounts or bulk-submit on third-party sites.

**Gap log:** whenever route 2 or 3 covered something TopCited should offer, append
one line to `sessions/<brand-slug>/gaps.md` (what was needed, which route filled it).

## Stages

Work `stages/01…08` in order; skip only with user consent, recorded in progress.md.
Each stage file declares purpose, primary operations, routed actions, knowledge to
consult, inputs, outputs, and UI links.

| # | File | One-line purpose |
|---|---|---|
| 1 | stages/01-intake.md | Website + guided interview → brand created, brand brief written |
| 2 | stages/02-baseline-monitoring.md | Measure today's visibility before changing anything |
| 3 | stages/03-competitor-research.md | Who wins your customers' searches, and with what keywords |
| 4 | stages/04-site-audit.md | Health check → plain-language improvement plan |
| 5 | stages/05-technical-entity-fixes.md | Fix the plumbing: indexing, canonicals, structured data, profiles |
| 6 | stages/06-content.md | Pillar/cluster content informed by competitors + brief |
| 7 | stages/07-distribution.md | Adapt + place content for backlinks and citations |
| 8 | stages/08-review-monitoring.md | Compare against baseline, refine monitoring, set the routine |

## Knowledge

For any SEO/GEO judgment call, consult the `seo-geo` skill — its
[SKILL.md](../seo-geo/SKILL.md) routes into the knowledge tree. Keep the deep
reasoning out of user-facing text unless they ask for depth.

This skill assumes the `seo-geo` and `topcited-api` skills are installed alongside
it. If either is missing, say so rather than improvising from memory.
