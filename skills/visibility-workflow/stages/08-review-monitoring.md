# Stage 8 — Review & ongoing monitoring

## Purpose (tell the user)
"Let's compare where you are now against the day we started, tune what we
track going forward, and set a routine so this keeps improving."

## Primary TopCited operations
- Refine query sets, add queries learned across Stages 3–7, read results
  against the Stage 2 baseline — [topcited-api/references/monitoring.md](../../topcited-api/references/monitoring.md)
- Generate a shareable snapshot of everything TopCited knows about the
  brand's visibility now — [topcited-api/references/reports.md](../../topcited-api/references/reports.md)

## Flow
1. Compare current monitoring numbers against the Stage 2 baseline in plain
   language — what improved, what didn't move yet. Be honest about
   timelines: indexing and AI-citation changes take weeks, not days.
2. Add any queries learned since the baseline (competitor gaps from Stage 3,
   new topics from Stage 6, channels from Stage 7) to the query set.
3. Offer to generate a report — a shareable snapshot the user can save or
   hand to someone else — 10 T-coins; mention that before generating.
4. Close out remaining `progress.md` checklist items, or carry open ones over
   with a clear next step.
5. Agree a check-in cadence (e.g. monthly) for future sessions.

## Knowledge
- [measurement/baselines-and-kpis.md](../../seo-geo/knowledge/measurement/baselines-and-kpis.md)
- [measurement/llm-share-of-voice.md](../../seo-geo/knowledge/measurement/llm-share-of-voice.md)
- [measurement/timelines-expectations.md](../../seo-geo/knowledge/measurement/timelines-expectations.md)
- [geo/industry-norms.md](../../seo-geo/knowledge/geo/industry-norms.md)

## Inputs
- Baseline reference from `progress.md` (Stage 2)
- `sessions/<brand-slug>/progress.md`

## Outputs
- Updated query set in TopCited
- Final session summary appended to `progress.md`

## Show
The monitoring dashboard, now vs. baseline —
`{TOPCITED_UI_URL}/monitoring?topics={query_set_id}` (UI-links pattern in the
topcited-api skill, references/monitoring.md), and the generated report if the user wanted one
(UI-links pattern in the topcited-api skill, references/reports.md).
