# Competitors

## What this is (tell the user)
A "competitor" here means anyone who shows up when your customers search for
what you sell — not always the company you'd point to as your rival. TopCited
tracks these so it can compare how often AI assistants and search engines
mention you versus them, and can scan each one's website to see what
keywords they're targeting.

## When the workflow uses it
Stage 3 (Competitor research): once the brand exists, get an initial
competitor list — either from the user directly or by asking TopCited to
suggest some — then save it against the brand, and scan each saved
competitor's website to extract the keywords it targets, reading the results
per competitor here. The brand-wide dashboard and overlap view (scan every
eligible competitor at once, compare keyword overlap across all of them)
live in [brands.md](brands.md) since those endpoints are brand-scoped, not
competitor-scoped. Later stages (monitoring, reporting) read the saved
competitor list to compare share-of-voice.

## Operations
| I want to… | Call | Reference |
|---|---|---|
| List a brand's competitors | `GET /api/v1/brands/{brand_id}/competitors` | [endpoints/competitors.md](endpoints/competitors.md) |
| Add one competitor | `POST /api/v1/brands/{brand_id}/competitors` | [endpoints/competitors.md](endpoints/competitors.md) |
| Add several at once | `POST /api/v1/brands/{brand_id}/competitors:bulk` | [endpoints/competitors.md](endpoints/competitors.md) |
| Discover competitors with AI | `POST /api/v1/brands/{brand_id}/competitors:suggest` | [endpoints/competitors.md](endpoints/competitors.md) |
| Get one competitor | `GET /api/v1/competitors/{competitor_id}` | [endpoints/competitors.md](endpoints/competitors.md) |
| Update a competitor | `PATCH /api/v1/competitors/{competitor_id}` | [endpoints/competitors.md](endpoints/competitors.md) |
| Remove a competitor | `DELETE /api/v1/competitors/{competitor_id}` | [endpoints/competitors.md](endpoints/competitors.md) |
| List one competitor's extracted keywords | `GET /api/v1/competitors/{competitor_id}/keywords` | [endpoints/competitors.md](endpoints/competitors.md) |
| Trigger a keyword scan for one competitor | `POST /api/v1/competitors/{competitor_id}/keyword-scans` | [endpoints/competitors.md](endpoints/competitors.md) |
| Get that competitor's latest scan status/result | `GET /api/v1/competitors/{competitor_id}/keyword-scans/latest` | [endpoints/competitors.md](endpoints/competitors.md) |

## Example
```bash
scripts/tc-api.sh POST /api/v1/brands/{brand_id}/competitors:suggest \
  -d '{"query": "best project management software"}'
```
Returns `{"competitors": [{"name": "...", "description": "..."}, ...]}` — three
suggestions, not yet saved. To keep any of them, call the bulk-create endpoint
with the ones the user picked:
```bash
scripts/tc-api.sh POST /api/v1/brands/{brand_id}/competitors:bulk \
  -d '[{"name": "Rival Co", "website": "https://rival.com"}]'
```
Bulk create is all-or-nothing: if any item collides with an existing competitor's
name/alias under that brand, the whole batch is rejected (409) and none are saved.

```bash
scripts/tc-api.sh POST /api/v1/competitors/{competitor_id}/keyword-scans
```
Returns `202` immediately with the scan record in `pending` status — this
kicks off a background job, it does not return keywords. Poll:
```bash
scripts/tc-api.sh GET /api/v1/competitors/{competitor_id}/keyword-scans/latest
```
until `status` is `completed` (or `failed`), then read the extracted keywords
with `GET /api/v1/competitors/{competitor_id}/keywords`. A competitor needs a
`website` before it can be scanned (400 otherwise), and only one scan can be
in flight per competitor at a time (409 if you trigger a second one while the
first is still `pending`/`running`).

## UI links
- `{TOPCITED_UI_URL}/competitors` — the competitors page reads the active brand from
  client-side brand context, not from the URL, so there is no `{brand_id}` segment in
  the route itself.
- `{TOPCITED_UI_URL}/competitor-keywords` — per-competitor keyword scan results and
  the trigger button live here, same brand-context pattern as `/competitors`.

Default locale (`en`) is unprefixed — don't add `/en/`.

## Cost & quota
`POST .../competitors:suggest` makes one LLM call. It **does** go through
quota: one `suggestions` unit is checked-and-spent before the LLM call, then
refunded (net zero) if the LLM returns nothing. Over-cap callers get 402
before the LLM call ever runs.
The per-plan `suggestions` allowance varies by plan — read the user's live
numbers from `GET /api/v1/users/me/usage` rather than assuming.

`POST .../keyword-scans` spends one `competitor_keyword_scans` unit at route
entry, same as `sci-defense/analyze` in [audit.md](audit.md) — **except this
one is not refunded on scan failure**. The background job fetches the
competitor's website corpus and SERP signals, then runs one LLM call to
extract keyword candidates; if any of that throws, the scan record is marked
`failed` and the spent unit stays spent.
It draws from the same `competitor_keyword_scans` allowance as
`POST /brands/{brand_id}/competitor-keywords/scan-all` in
[brands.md](brands.md); read the live numbers from
`GET /api/v1/users/me/usage`.

`GET .../keywords` and `GET .../keyword-scans/latest` are free reads.
All plain CRUD operations (list/create/bulk/get/update/delete competitor) are
free — no LLM or quota cost.

## Failure modes
- 402 from `:suggest` → plan's `suggestions` quota exhausted; tell the user,
  don't retry, point to billing.
- 402 from `POST .../keyword-scans` → plan's `competitor_keyword_scans` quota
  exhausted; tell the user, don't retry, point to billing. Unlike `:suggest`,
  a scan that fails *after* this check does not get the unit back — that's
  expected, not a bug to work around.
- 409 on create/bulk-create → name or alias collides with an existing competitor
  under the same brand; list existing competitors first and ask the user whether to
  reuse or rename.
- 404 on get/update/delete/keywords/keyword-scans → wrong `competitor_id`, or it
  belongs to a brand you don't own; re-list before retrying.
- 400 on `POST .../keyword-scans` → the competitor has no `website` set; ask the
  user for one (or `PATCH` the competitor) before retrying.
- 409 on `POST .../keyword-scans` → a scan is already `pending`/`running` for this
  competitor; poll `.../keyword-scans/latest` instead of retriggering.
- 404 on `GET .../keyword-scans/latest` → no scan has ever been triggered for this
  competitor yet; that's a normal "nothing to show" state, not an error to surface
  alarmingly.
- `:suggest` results are not persisted — always follow up with create/bulk-create
  for anything the user wants to keep.
- `POST .../keyword-scans` is **asynchronous** (202, background job) — unlike most
  of this API surface, do not expect the response body to contain results; poll
  `.../keyword-scans/latest` for `status`.
