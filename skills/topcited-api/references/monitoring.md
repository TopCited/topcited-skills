# Monitoring

## What this is (tell the user)
We regularly ask Google and the AI assistants (ChatGPT, Gemini, and similar) the
questions your customers actually ask, and track whether your brand shows up in
the answers — and where your competitors do instead. A "query set" (shown in the
app as a "Topic") is a themed group of those questions; each question in it is a
"query." Running the set fires every query at every configured engine and records
who got mentioned, how prominently, and with what sentiment.

## When the workflow uses it
Stage 2 (Baseline monitoring): right after the brand brief exists, derive an
initial prompt set, create a query set, and trigger the first run — the "before
photo," taken early so improvement is measurable later. Stage 8 (Review & ongoing
monitoring): refine the set with everything learned since, and compare the new
numbers against the Stage 2 baseline.

## Commands
| I want to… | Command |
|---|---|
| List the active brand's sets | `topcited monitor sets list` (`--all` for every brand) |
| Create a set | `topcited monitor sets create "Payroll software" -p chatgpt -p gemini -q "best payroll software for startups"` |
| Show a set with its queries (and query ids) | `topcited monitor sets show <set>` |
| Add queries | `topcited monitor queries add <set> "best payroll app" "payroll for contractors"` (`--type`) |
| Delete queries | `topcited monitor queries rm <query-id…>` |
| Estimate a run | `topcited monitor run <set> --dry-run` |
| Run now and wait | `topcited monitor run <set> --wait --yes` |
| Visibility, gaps, share of voice | `topcited monitor results [--set <set>] [--since YYYY-MM-DD] [--until …]` |
| Pause / rename / change platforms | `topcited api -X PATCH /monitoring/query-sets/<id> -d '{"paused": true}'` |
| Raw runs for a set | `topcited api /monitoring/runs -f query_set_id=<id> --paginate` |
| Mention-rate time series, per-query table, mentions | `topcited api /monitoring/metrics/visibility` · `/monitoring/metrics/per-query` · `/monitoring/mentions` (same `query_set_id` / date filters) |
| Projected spend vs balance | `topcited api /monitoring/credit-forecast` (also in `topcited usage`) |

A set is referenced by id, a 6+ character id prefix, or name; when names tie,
the active brand's set wins.

*Internal* (works via `topcited api`, not in the public spec, may change):
`DELETE /monitoring/query-sets/<id>`, `PATCH /monitoring/queries/<qid>`,
`POST /monitoring/query-sets/<id>/suggest-queries` and `…/suggest-query-pairs`
(LLM-suggested queries), `POST …/competitors:add-all`,
`GET /monitoring/runs/<run_id>/sources`, `DELETE …/runs` (clear history).

## Things `--help` won't tell you
- **Platforms and query types.** `-p` takes `chatgpt`, `gemini`, `grok`,
  `google`, `bing`, `brave`, `deepseek`, `baidu_search`; pass at least one.
  `--type` routes each query: `llm_prompt` (AI assistants, the default),
  `search_keyword` (search engines), `universal` (both). A query only runs on
  the platforms its type routes to.
- **Scheduling.** Sets run automatically **once a day**; `--manual` creates one
  that only runs on `monitor run`. There is no other cadence — don't set
  `schedule_cron` through `topcited api` — leave the field out (the API is
  adding validation that rejects non-daily crons with a 422).
- **Runs are a batch, not one job.** `monitor run` creates one run per (query ×
  platform) and returns a `job` ref; results land as each finishes. With
  `--wait` the CLI follows the whole batch. A batch where some runs failed
  reports `partial` and exits 0; all failed exits 1. A run can also be
  `SKIPPED` if credits ran out mid-batch — some queries ran, others didn't.
- **Don't delete queries that have history.** `queries rm` on a query with past
  runs is refused (exit 6, `query_has_runs`); deactivate it instead with
  `topcited api -X PATCH /monitoring/queries/<qid> -d '{"is_active": false}'`.

## UI links
- `{TOPCITED_UI_URL}/monitoring` — the Query Tracking view: topics, queries,
  run trigger, and every metrics chart.
- `{TOPCITED_UI_URL}/monitoring?topics={query_set_id}` — one set pre-selected.
  (The old `/monitoring/[id]` route only redirects here — link to this form.)

Default locale (`en`) is unprefixed — don't add `/en/`.

## Cost & quota
- **1 T-coin per query per engine, per run** — not per set and not per click. A
  15-query set on 2 engines costs up to 30 T-coins a run, and an automatic set
  spends that every day. `monitor run --dry-run` prints the exact estimate
  (active queries × the platforms each routes to) against your balance;
  `exceeds: true` means the run may not finish before credits run out.
- `suggest-queries` / `suggest-query-pairs` spend one `suggestions` unit
  (2 T-coins) per call, refunded only if the LLM returns nothing.
- Creating and editing sets and queries, listing runs, and every metrics read
  are free.

## Failure modes
- `monitor run` exits 1 with `query_set_empty` when no query in the set is
  active and routable to its platforms — add a runnable query first.
- `monitor sets create` refuses with `brand_mismatch` when the CLI's brand isn't
  the account's server-side active brand — see [brands.md](brands.md).
- Exit 7 from `--wait` → the batch is still running; `topcited wait <job>`.
- Metrics calls without a set filter need an active brand; with none, they fail
  rather than guess a scope.
- HTTP 422 from the bucketed metrics endpoints → a malformed date window (one
  end only, start after end, span over 365 days) or `fill=true` with
  `bucket=batch`; fix the parameters rather than retrying.
