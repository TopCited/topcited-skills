# Brands

## What this is (tell the user)
A "brand" is TopCited's home for everything about your business — your website,
what you sell, and who your rivals are. Every other feature (competitor research,
audits, content, monitoring) hangs off your brand, so we set this up first.

## When the workflow uses it
Stage 1 (Intake): create or select the brand right after getting the website URL.
Later stages read the brand from the session's brand brief and act on it as the
active brand.

## Commands
| I want to… | Command |
|---|---|
| List brands | `topcited brand list` |
| Pick the brand later commands act on | `topcited brand use <name\|id>` (or `--brand` / `TOPCITED_BRAND` per command) |
| Show the active brand (incl. its id) | `topcited brand show [brand]` |
| Create a brand | `topcited api -X POST /brands -d '{"name": "Acme Coffee", "website": "https://acmecoffee.com"}'` |
| Check brand count against the plan cap | `topcited api /brands/limits` |
| Rename / change website | `topcited api -X PATCH /brands/<id> -d '{"website": "https://…"}'` |

*Internal* (works via `topcited api`, not in the public spec, may change):
competitor-keyword views for Stage 3 — `GET /brands/<id>/competitor-keywords/dashboard`,
`GET /brands/<id>/competitor-keywords/overlap`, and
`POST /brands/<id>/competitor-keywords/scan-all` (scan every eligible competitor
at once — see [competitors.md](competitors.md) for the per-competitor half);
`DELETE /brands/<id>`.

## Choosing the active brand
A brand reference is an exact id, a 6+ character id prefix, or the name
(case-insensitive). The CLI resolves the active brand as `--brand` /
`TOPCITED_BRAND` → `topcited brand use` (stored per API host) → the account's
server-side active brand → the only brand. With several brands and none
selected, commands exit 2 — run `brand use` first.

`monitor sets create` and `report generate` always use the **server-side**
active brand, which the CLI can't change. If it differs from the brand the CLI
points at, they refuse with `brand_mismatch`; switch brands in the web app's
brand switcher, or run with the `--brand` the hint names. A newly created brand
becomes the server-side active brand only if the user had none.

## UI links
- `{TOPCITED_UI_URL}/onboarding` — brand creation for a signed-in user with no
  brand; `{TOPCITED_UI_URL}/onboarding/setup` is the wizard right after it.
- `{TOPCITED_UI_URL}/dashboard` — brand switching, renaming and deleting all
  happen from the brand switcher in the console header (on every console page),
  not a dedicated settings route.
- `{TOPCITED_UI_URL}/competitor-keywords` — the competitor-keyword dashboard and
  overlap views. It reads the active brand from the app, so there's no brand id
  in the URL.

Default locale (`en`) is unprefixed — don't add `/en/`.

## Cost & quota
Creating, updating and listing brands spends nothing, but the number of brands
is capped by plan (exit 4 when over) — check `/brands/limits` before offering to
create one. The competitor-keyword dashboard and overlap reads are free;
`scan-all` spends one `competitor_keyword_scans` unit per competitor it starts
(see [competitors.md](competitors.md)).

## Failure modes
- Exit 4 on create → the plan's brand cap is reached; explain, don't retry, point
  at billing.
- HTTP 400 on create/update → the `website` couldn't be parsed as a URL (e.g. no
  scheme); ask the user to re-enter it.
- Exit 6 on create/update → the name collides with another of the user's brands.
- Exit 5 → wrong or stale brand; `topcited brand list` to refresh.
- Deleting the user's only brand is refused (brands can't go to zero), and
  deleting the active brand silently makes the newest remaining brand active —
  re-list afterwards rather than assuming. Deleting cascades competitors and
  detaches (doesn't destroy) query sets, reports, SEO sites and content.
- `scan-all` returning `started: 0, skipped: N` isn't an error — every
  competitor was ineligible (no website / scan already running) or the quota was
  already used up; check the dashboard rather than retrying blindly.
