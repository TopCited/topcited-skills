# Stage 3 — Competitor research

## Purpose (tell the user)
"Now let's look at who's currently winning your customers' attention — not
always who you think of as rivals, but whoever shows up when your customers
search."

## Primary TopCited operations
- Seed rivals, discover more, save the competitor set — [topcited-api/references/competitors.md](../../topcited-api/references/competitors.md)
- Scan each competitor's keywords, and read the brand-wide keyword dashboard
  and overlap view — [topcited-api/references/competitors.md](../../topcited-api/references/competitors.md)
  (per-competitor scan/list) and [topcited-api/references/brands.md](../../topcited-api/references/brands.md)
  (brand-scoped dashboard/overlap, since those endpoints hang off the brand)

## Flow
1. Seed the competitor list from rivals the user named in the brand brief.
2. Ask TopCited to discover more (`:suggest`) — this is an LLM call and spends
   a `suggestions` credit; mention that before calling it.
3. **Suggest-and-approve:** show the discovered candidates alongside the
   user-named ones, let the user pick, then bulk-create the approved set.
4. For each saved competitor with a website, trigger a keyword scan (or scan
   every eligible competitor at once from the brand dashboard) to see what
   keywords they target. Scans run in the background — poll rather than wait.
   Each competitor scanned costs 5 T-coins — state that before triggering,
   and if scanning every eligible competitor at once, state the total
   (N competitors × 5 T-coins).
5. Read the dashboard and overlap views to see where the brand's keyword
   footprint is thin against competitors — this feeds Stage 4 and Stage 6.

**Routed action (agent-direct):** fetch competitors' public pages yourself to
characterize positioning and messaging beyond what the keyword scan returns —
ordinary page fetches only, never scraping beyond that.

## Knowledge
- [content-strategy/keyword-intent-research.md](../../seo-geo/knowledge/content-strategy/keyword-intent-research.md)

## Inputs
- `sessions/<brand-slug>/brand-brief.md`

## Outputs
- Competitor set + keyword scans saved in TopCited (source of truth)
- A written keyword/positioning summary (from the scans plus your own page
  fetches) recorded in `progress.md`'s log entry for this stage — Stage 4
  reads it from there when building `improvement-plan.md`

## Show
The competitors page and the competitor-keywords dashboard (pattern from
the topcited-api skill: references/competitors.md and references/brands.md).
