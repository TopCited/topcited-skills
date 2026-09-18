# Reports

## What this is (tell the user)
A snapshot document that pulls together everything TopCited knows about the
brand's visibility right now — monitoring results, site health, competitor
standing — into one shareable file. Generate one when the user wants
something to save, print, or hand to a boss/client rather than reading
numbers off a dashboard.

## When the workflow uses it
Cross-cutting: reports are a deliverable, not a stage. They're most useful
after Stage 4 (Site audit) or Stage 8 (Review & ongoing monitoring) — once
there's a meaningful audit or monitoring history to summarize — but can be
generated any time the user wants a snapshot.

## Operations
| I want to… | Call | Reference |
|---|---|---|
| Generate a new report | `POST /api/v1/reports/generate` | [endpoints/reports.md](endpoints/reports.md) |
| List reports | `GET /api/v1/reports/` | [endpoints/reports.md](endpoints/reports.md) |
| Get one report's data | `GET /api/v1/reports/{report_id}` | [endpoints/reports.md](endpoints/reports.md) |
| View a report as HTML | `GET /api/v1/reports/{report_id}/view` | [endpoints/reports.md](endpoints/reports.md) |
| Download a report as an HTML file | `GET /api/v1/reports/{report_id}/download/html` | [endpoints/reports.md](endpoints/reports.md) |
| Download a report as a PDF | `GET /api/v1/reports/{report_id}/download/pdf` | [endpoints/reports.md](endpoints/reports.md) |

## Example
```bash
scripts/tc-api.sh POST /api/v1/reports/generate -d '{"report_type": "geo_audit"}'
```
`report_type` is optional — `geo_audit` is currently the only supported
value and is also the default, so an empty body (`-d '{}'`) works the same
way. Returns the full report object including `data_snapshot`, generated
synchronously (no polling needed).

```bash
scripts/tc-api.sh GET /api/v1/reports/$REPORT_ID/download/pdf > report.pdf
```
Both `download/html` and `download/pdf` accept `?theme=dark` (default) or
`?theme=light`; the PDF is rendered server-side via Playwright, so expect it
to take a moment longer than the HTML download.

## UI links
- `{TOPCITED_UI_URL}/reports` — the single reports page: list, "Generate
  report" dialog, and an in-page HTML viewer dialog. There is no
  separate per-report route — viewing and downloading both happen from
  dialogs on this page.

Default locale (`en`) is unprefixed — don't add `/en/`.

## Cost & quota
`POST /reports/generate` spends 10 T-coins (`reports`) at route entry,
refunded automatically if generation fails internally (`InternalError` —
`ReportService.generate()` re-wraps every non-user failure as
`InternalError`, so that's the only failure branch that reaches the refund).
Listing, getting, viewing, and downloading an already-generated report are
all free — the charge is only for producing a new snapshot.

## Failure modes
- `POST /reports/generate` is **synchronous** — the response is the finished
  report, not a run to poll. If it's slow, that's normal (it aggregates
  monitoring + audit + competitor data server-side); don't build a polling
  loop around it.
- 402 from `generate` → the `reports` credit balance is exhausted; explain
  in plain language, don't retry, point to billing.
- `report_type` other than `geo_audit` → 422; there is currently only one
  supported type despite the schema being named generically — don't offer
  the user a choice that doesn't exist yet.
- 404 on any `{report_id}` call → wrong or cross-tenant id; re-list reports
  to refresh before retrying.
- A report is a point-in-time snapshot, not a live view — if the user
  generated one a while ago and wants current numbers, generate a new one
  rather than re-fetching the old `report_id`.
