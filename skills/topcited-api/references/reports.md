# Reports

## What this is (tell the user)
A snapshot document that pulls together everything TopCited knows about the
brand's visibility right now — monitoring results, site health, competitor
standing — into one shareable file. Generate one when the user wants something to
save, print, or hand to a boss or client rather than reading numbers off a
dashboard.

## When the workflow uses it
Cross-cutting: reports are a deliverable, not a stage. Most useful after Stage 4
(Site audit) or Stage 8 (Review & ongoing monitoring), once there's an audit or a
monitoring history to summarize.

## Commands
| I want to… | Command |
|---|---|
| Generate and wait | `topcited report generate --wait --yes` (`-t geo_audit` default, or `-t client_report`; `-P key=value` for parameters) |
| List reports | `topcited report list` |
| Show one | `topcited report show <id>` |
| Download | `topcited report download <id> --format pdf -o report.pdf` (`--format html` also works) |

Downloads use the default dark theme; the API also accepts `?theme=light` on
`/reports/<id>/download/pdf` and `…/html` if the user wants it (fetch binary PDFs
with curl and `$(topcited auth token --show)` — `topcited api` handles text
only). The PDF is rendered server-side, so it takes a moment longer than HTML.

## UI links
- `{TOPCITED_UI_URL}/reports` — the reports page: list, "Generate report" dialog,
  and an in-page viewer. There's no per-report route — viewing and downloading
  both happen in dialogs there.

Default locale (`en`) is unprefixed — don't add `/en/`.

## Cost & quota
**10 T-coins** per generated report (`reports`), refunded if generation fails
internally. `--dry-run` can't estimate it yet (it shows the balance) — quote the
10 yourself. Listing, showing and downloading existing reports is free.

## Failure modes
- `report generate` refuses with `brand_mismatch` when the CLI's brand isn't the
  account's server-side active brand — reports always use the latter; see
  [brands.md](brands.md).
- Exit 4 → the `reports` allowance is used up; explain, don't retry, point at
  billing.
- Exit 7 → still generating; `topcited wait <job>`.
- Exit 5 on an id → wrong or someone else's report; `topcited report list`.
- A report is a point-in-time snapshot. If the user wants current numbers,
  generate a new one rather than re-downloading an old one.
