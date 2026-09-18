# Stage 2 — Baseline monitoring

## Purpose (tell the user)
"Before we change anything, let's measure how visible you are today — which of
your customers' questions you show up for in Google and in AI assistants like
ChatGPT. In a few weeks you'll see exactly how much this improved."

## Primary TopCited operations
- Create query set, add queries, trigger the first run — [topcited-api/references/monitoring.md](../../topcited-api/references/monitoring.md)

## Flow
1. Derive 10–20 candidate queries from the brand brief: a mix of what-they-sell
   searches ("espresso machines for home baristas"), comparison searches
   ("X vs Y"), and "best X for Y" searches. Mark each as a search query or an
   AI-assistant prompt.
2. **Suggest-and-approve:** show the user the list, plain language, let them
   add, edit, or drop entries before anything is created.
3. Create the query set (Topic) and add the approved queries.
4. Before triggering the first run, warn about cost: every run charges 1 T-coin
   per query per engine, so a 15-query set on 2 engines can cost up to 30
   T-coins. Check the user's remaining balance first and state a concrete
   number, not just "it costs credits."
5. Trigger the run. Runs are asynchronous — tell the user results trickle in
   over the next few minutes, not instantly.

Routed actions: none — this stage is entirely a TopCited-route stage.

## Knowledge
- [measurement/baselines-and-kpis.md](../../seo-geo/knowledge/measurement/baselines-and-kpis.md)
- [geo/prompt-visibility.md](../../seo-geo/knowledge/geo/prompt-visibility.md)
- [geo/assistant-sourcing-behavior.md](../../seo-geo/knowledge/geo/assistant-sourcing-behavior.md)
- [geo/industry-norms.md](../../seo-geo/knowledge/geo/industry-norms.md)
- [foundations/how-llms-source-answers.md](../../seo-geo/knowledge/foundations/how-llms-source-answers.md)

## Inputs
- `sessions/<brand-slug>/brand-brief.md`

## Outputs
- Query-set id and the baseline run/batch reference recorded in `progress.md`

## Show
The monitoring UI for the query set — `{TOPCITED_UI_URL}/monitoring?topics={query_set_id}`
(UI-links pattern in the topcited-api skill, references/monitoring.md), so the user can watch results arrive.
