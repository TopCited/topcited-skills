# Brands

## What this is (tell the user)
A "brand" is TopCited's home for everything about your business — your website,
what you sell, and who your rivals are. Every other feature (competitor research,
audits, content, monitoring) hangs off your brand, so we set this up first.

## When the workflow uses it
Stage 1 (Intake): create or select the brand right after getting the website URL.
Later stages read the brand id from the session's brand brief.

## Operations
| I want to… | Call | Reference |
|---|---|---|
| Create the brand | `POST /api/v1/brands` | [endpoints/brands.md](endpoints/brands.md) |
| List existing brands | `GET /api/v1/brands` | [endpoints/brands.md](endpoints/brands.md) |
| Check brand count against the plan cap | `GET /api/v1/brands/limits` | [endpoints/brands.md](endpoints/brands.md) |
| Update brand name/website | `PATCH /api/v1/brands/{brand_id}` | [endpoints/brands.md](endpoints/brands.md) |
| Delete a brand | `DELETE /api/v1/brands/{brand_id}` | [endpoints/brands.md](endpoints/brands.md) |
| Get the brand's competitor-keyword dashboard (Stage 3) | `GET /api/v1/brands/{brand_id}/competitor-keywords/dashboard` | [endpoints/brands.md](endpoints/brands.md) |
| Get keyword overlap across the brand's competitors (Stage 3) | `GET /api/v1/brands/{brand_id}/competitor-keywords/overlap` | [endpoints/brands.md](endpoints/brands.md) |
| Scan keywords for every eligible competitor at once (Stage 3) | `POST /api/v1/brands/{brand_id}/competitor-keywords/scan-all` | [endpoints/brands.md](endpoints/brands.md) |

The last three are the brand-scoped half of the "analyze competitor keywords"
feature — see [competitors.md](competitors.md) for the per-competitor half
(list one competitor's keywords, trigger/read a single scan).

## Example
```bash
scripts/tc-api.sh POST /api/v1/brands -d '{"name": "Acme Coffee", "website": "https://acmecoffee.com"}'
```
Returns the brand object with its `id` — record it in the brand brief; every later
stage needs it. If the user has no active brand yet, this new brand becomes active
automatically.

## UI links
- `{TOPCITED_UI_URL}/onboarding` — where a signed-in user with no brand starts brand
  creation (matches `POST /api/v1/brands`).
- `{TOPCITED_UI_URL}/onboarding/setup` — the setup wizard that runs right after brand
  creation.
- `{TOPCITED_UI_URL}/dashboard` — brand switching, renaming, and deleting all happen
  from the brand switcher's dropdown in the console header, present on every
  console page, not a dedicated brand-settings route. `GET /brands/limits` backs
  the client-side gate on the switcher's "Add brand" action.
- `{TOPCITED_UI_URL}/competitor-keywords` — the competitor-keywords dashboard/overlap
  page. It reads the active brand from client-side brand context like `/competitors`
  below, so there is no `{brand_id}` segment in the route.

Default locale (`en`) is unprefixed, so these bare paths resolve directly — don't
add `/en/`. Other locales (e.g. `pl`) would use `/pl/onboarding`.

## Cost & quota
Creating a brand does **not** spend a credit, but the number of brands you
may hold is capped by plan, checked before insert (a 402 when you are over).
`GET /brands/limits` is a free read of that same cap — call it before
offering to create a brand.
Updating a brand's name/website does not meter anything — it only fails on an
unparseable URL (400), a duplicate name (409), or a brand you don't own (404).
Deleting a brand does not meter anything either. It cascades competitors
(DB-level `ON DELETE CASCADE`) and detaches (sets `brand_id = NULL` on) query
sets, reports, SEO sites/analyses, content submissions, and pipeline tasks —
none of that data is destroyed.
`GET .../competitor-keywords/dashboard` and `.../overlap` are free reads — the
dashboard attaches cached keyword-difficulty data only (no DataForSEO fetch,
no LLM call) from a single batched cache lookup.
`POST .../competitor-keywords/scan-all` is a **partial-fulfillment** operation,
not all-or-nothing: it walks the brand's competitors, silently skips ones with
no website or an already-in-progress scan, then spends one
`competitor_keyword_scans` quota unit per remaining competitor via
the plan's `competitor_keyword_scans` allowance until it is exhausted — the
competitors it already started are still dispatched as background scans, the
rest count toward `skipped` in the response. It never 402s; check
`started`/`skipped` in the response body instead.
The per-plan `competitor_keyword_scans` allowance varies by plan; read the
user's live numbers from `GET /api/v1/users/me/usage` rather than assuming.

## Failure modes
- 402 on create → plan's brand-count cap reached; explain in plain language, do not
  retry, and point the user at the billing/upgrade page.
- 400 on create/update → the `website` value couldn't be parsed as a URL; ask the
  user to re-enter it (e.g. missing scheme).
- 409 on create/update → the name collides with another of the user's brands.
- 404 on update/delete → wrong or stale `brand_id`; call `GET /api/v1/brands` again
  to refresh the id before retrying.
- 400 on delete → the brand is the user's only remaining brand; brands can't go to
  zero. Tell the user to create a replacement brand first if they really want to
  retire this one.
- Deleting the active brand silently reassigns `active_brand_id` to the newest
  remaining brand — re-fetch `GET /api/v1/brands` (or the user object) after a
  delete rather than assuming the old active brand id is still valid.
- `scan-all` returning `started: 0, skipped: N` is not an error — it means every
  competitor was ineligible (no website / scan already running) or the quota was
  already exhausted before this call; don't retry blindly, inspect why via
  `GET .../competitor-keywords/dashboard`.
