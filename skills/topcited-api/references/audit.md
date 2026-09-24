# Audit

## What this is (tell the user)
A "website audit" is a health check of your website: what's stopping search
engines and AI assistants from finding and trusting it. This guide covers two
different pieces of that: (1) requesting an audit — a lead form that gets a
human at TopCited to review your site and follow up, and (2) an automated
trust check that scans a page right now for signs its content has been
artificially manipulated to game AI rankings.

## When the workflow uses it
Stage 1 (Intake) / top-of-funnel: `audit-requests` is how an unauthenticated
visitor asks for a free audit — it just captures their contact details, it
does not itself analyze anything. Later stages (or a standalone trust check
the user asks for) call `sci-defense/analyze` on a specific URL to get an
immediate manipulation verdict for a signed-in session.

## Operations
| I want to… | Call | Reference |
|---|---|---|
| Submit a request for a free audit (lead capture) | `POST /api/v1/audit-requests` | [endpoints/audit-requests.md](endpoints/audit-requests.md) |
| Run a manipulation/trust check on a URL | `POST /api/v1/sci-defense/analyze` | [endpoints/sci-defense.md](endpoints/sci-defense.md) |

`POST /api/v1/sci-defense/public-analyze` also exists (unauthenticated,
per-IP daily rate limit) but is out of scope for an authenticated agent
session — use `/sci-defense/analyze` instead.

## Example
```bash
scripts/tc-api.sh POST /api/v1/audit-requests \
  -d '{"email": "owner@acmecoffee.com", "name": "Jamie Rivera", "industry": "Coffee & beverage", "needs": "Not showing up in ChatGPT answers"}'
```
Returns `{"id", "email", "name", "created_at"}` — that's it. This is a lead
record, not a report; nothing is computed or returned about the site itself.

```bash
scripts/tc-api.sh POST /api/v1/sci-defense/analyze -d '{"url": "https://acmecoffee.com/blog/best-espresso-machines"}'
```
Returns immediately (no polling) with a `verdict` of `clean`, `suspicious`, or
`manipulated`, a `combined_score`, and per-dimension scores from the PPL, SIS,
and ICD detectors, plus a 200-character `text_preview` of what was scanned.

## UI links
- `{TOPCITED_UI_URL}/` — the "get a free audit" form is a dialog, not a
  dedicated page. It's embedded on the homepage hero/CTA, `/features`, blog
  posts, and the login/invite screens — there is no single canonical route,
  `{TOPCITED_UI_URL}/` is the primary one.
- `{TOPCITED_UI_URL}/optimization/sci-defense` — the authenticated manipulation
  check (calls `/sci-defense/analyze`).
- `{TOPCITED_UI_URL}/try-sci-defense` — the public/unauthenticated version
  (calls `/sci-defense/public-analyze`, out of scope here — listed only so you
  don't confuse the two pages).

## Cost & quota
`POST /api/v1/audit-requests` is unauthenticated and free — it only writes a
row, and it is rate-limited per IP (not against plan quota).
`POST /api/v1/sci-defense/analyze` spends **5 T-coins** (`sci_defense`) at
route entry, refunded automatically if the detection pipeline itself throws
(not refunded for 422 user errors like an unreachable or private URL).

## Failure modes
- Both `/audit-requests` and `/sci-defense/analyze` are **synchronous** — the
  response you get back is the final result. There is no run/task id to poll
  and no "processing" status; do not build a polling loop for either.
- 402 from `/sci-defense/analyze` → plan's `sci_defense` quota exhausted;
  explain in plain language, don't retry, point to billing.
- 422 from `/sci-defense/analyze` → the URL couldn't be fetched, resolves to a
  private/internal address (blocked for security), returned a non-2xx status,
  had no readable text, or redirected too many times / to a non-HTTP scheme.
  Ask the user for a different, publicly reachable URL rather than retrying
  the same one.
- A successful `POST /audit-requests` does not mean an audit happened — it
  only means the lead was captured. Set the user's expectation accordingly
  (a human will follow up), and offer the `sci-defense/analyze` check if they
  want an immediate automated result instead.
