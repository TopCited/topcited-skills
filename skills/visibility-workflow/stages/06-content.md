# Stage 6 — Content

## Purpose (tell the user)
"Content is how you earn visibility: one in-depth page on your core topic plus
supporting articles — the structure search engines and AI assistants treat as
real expertise."

## Primary TopCited operations
- Generate the pillar + cluster page set — [topcited-api/references/content-pillar-cluster.md](../../topcited-api/references/content-pillar-cluster.md)
- Ground topic and query choices in AI-suggested keywords, prompts, and
  quotable content sentences — [topcited-api/references/recommendations.md](../../topcited-api/references/recommendations.md)
- Rewrite or improve an existing page instead of drafting a new one, where
  that's the better fit — [topcited-api/references/seo-geo-analysis.md](../../topcited-api/references/seo-geo-analysis.md)
  (GEO optimizer, optimization submissions)

## Flow
1. Optionally run keyword and content-sentence recommendations first — they
   turn the Stage 3 competitor research and the brand brief into concrete
   candidates instead of the user inventing topics from scratch. Each run
   spends 3 T-coins; mention that before calling it, and let the user accept
   only the suggestions they want.
2. Propose a pillar topic and its clusters, drawing on the brand brief, the
   Stage 3 competitor/keyword summary, and any accepted recommendations.
   **Suggest-and-approve.**
3. Before starting the run, warn the user this is the most credit-hungry step
   in the whole workflow, and that its cost scales with the number of pages
   requested. Check their balance and compute the actual figure for the page
   count you are proposing (see the `topcited-api` skill's
   `references/content-pillar-cluster.md`) — quote that number, not a
   remembered one.
4. Start the run and poll until complete; it's a long-running job (research,
   scrape, analyze, draft, generate are separate stages), so tell the user to
   check back rather than wait live.
5. The user reviews drafts in the TopCited UI before anything is published
   anywhere.

**Routed action (agent-direct):** refine or edit drafts and adapt tone based
on the user's feedback. For a smaller fix to a page that already exists (not
a new pillar page), use a content-optimization submission instead of a fresh
pillar/cluster run.

## Knowledge
- [content-strategy/keyword-intent-research.md](../../seo-geo/knowledge/content-strategy/keyword-intent-research.md)
- [content-strategy/pillar-cluster-model.md](../../seo-geo/knowledge/content-strategy/pillar-cluster-model.md)
- [content-strategy/eeat.md](../../seo-geo/knowledge/content-strategy/eeat.md)
- [content-strategy/ai-citation-signals.md](../../seo-geo/knowledge/content-strategy/ai-citation-signals.md)

## Inputs
- `sessions/<brand-slug>/brand-brief.md`
- Competitor/keyword summary from `progress.md` (Stage 3)
- `sessions/<brand-slug>/improvement-plan.md`

## Outputs
- Run id and draft links recorded in `progress.md`

## Show
The pillar/cluster run's detail page — stage timeline, draft preview, page
list, export (UI-links pattern in the topcited-api skill, references/content-pillar-cluster.md).
