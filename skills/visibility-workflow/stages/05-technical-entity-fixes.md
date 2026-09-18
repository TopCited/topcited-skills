# Stage 5 — Technical & entity fixes

## Purpose (tell the user)
"Now we fix the plumbing. None of this is visible to your customers, but it
decides whether Google and AI assistants can find and trust you at all."

## Primary TopCited operations
None — this stage is almost entirely agent-direct and user-manual work; the
plan rows it's working through came out of Stage 4.

## Flow
Work through `improvement-plan.md` rows tagged for this stage, one at a time,
following the conversation contract (Explain → Confirm → Act → Show → Record)
for each.

**Routed action (agent-direct):** generate structured data (JSON-LD), an
`llms.txt` file, and sitemap/robots corrections yourself. If the user granted
repo or CMS access in Stage 1, apply these as reviewable patches or pull
requests — never a silent push. After applying a fix, verify it landed by
re-fetching the page (or re-running the relevant Stage 4 check) rather than
assuming it worked.

**Routed action (user-manual):** anything that needs the user's own logins or
accounts — Google Search Console / Bing Webmaster verification, DNS records,
claiming social profiles, directory submissions. Give numbered instructions a
non-expert can follow, add a checklist item to `progress.md`, and follow up
next session.

Whenever a route-2 or route-3 fix covers something TopCited should offer as a
feature, add one line to `gaps.md`.

## Knowledge
- [technical-seo/crawlability-and-indexing.md](../../seo-geo/knowledge/technical-seo/crawlability-and-indexing.md)
- [technical-seo/canonicals.md](../../seo-geo/knowledge/technical-seo/canonicals.md)
- [technical-seo/sitemaps-and-indexnow.md](../../seo-geo/knowledge/technical-seo/sitemaps-and-indexnow.md)
- [technical-seo/structured-data.md](../../seo-geo/knowledge/technical-seo/structured-data.md)
- [technical-seo/llms-txt.md](../../seo-geo/knowledge/technical-seo/llms-txt.md)
- [technical-seo/core-web-vitals.md](../../seo-geo/knowledge/technical-seo/core-web-vitals.md)
- [entity-authority/brand-entity-sameas.md](../../seo-geo/knowledge/entity-authority/brand-entity-sameas.md)
- [entity-authority/social-profiles.md](../../seo-geo/knowledge/entity-authority/social-profiles.md)
- [entity-authority/directories.md](../../seo-geo/knowledge/entity-authority/directories.md)
- [entity-authority/backlinks-digital-pr.md](../../seo-geo/knowledge/entity-authority/backlinks-digital-pr.md)

## Inputs
- `sessions/<brand-slug>/improvement-plan.md`

## Outputs
- Plan rows updated to `done` / `in-progress`
- Checklist items in `progress.md` for outstanding route-3 work
- `gaps.md` entries for anything a TopCited feature should have covered

## Show
A concrete before/after for each fix (e.g. "your site now has X — here's how
to see it": re-fetch the page, or point at wherever TopCited itself now
surfaces the improvement, such as a re-run of the Stage 4 URL analysis).
