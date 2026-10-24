# AI usage detection (manipulation check)

## What this is (tell the user)
An automated trust check that scans a page right now for signs its content was
machine-generated or artificially manipulated to game AI rankings, and returns a
plain verdict: clean, suspicious, or manipulated.

## When the workflow uses it
Stage 4 (Site audit): for pages that look suspicious or heavily AI-generated,
get a concrete verdict rather than a guess. Also on request, as a standalone
check on any public URL.

## Calls
*Internal* — not in the public spec and there's no CLI verb yet; it works via
`topcited api` but may change:

```bash
topcited api -X POST /sci-defense/analyze -d '{"url": "https://acmecoffee.com/blog/best-espresso-machines"}'
```

Returns immediately (no polling) with a `verdict` of `clean`, `suspicious`, or
`manipulated`, a `combined_score`, per-detector scores, and a short
`text_preview` of what was scanned.

Two lookalikes to ignore: `POST /sci-defense/public-analyze` is the
unauthenticated, IP-rate-limited version behind the public demo page, and
`POST /audit-requests` is the "get a free audit" lead form — it only records
contact details for a human follow-up and analyzes nothing. Neither is for an
agent session.

## UI links
- `{TOPCITED_UI_URL}/optimization/sci-defense` — the signed-in manipulation check.
- `{TOPCITED_UI_URL}/try-sci-defense` — the public demo (listed only so you don't
  confuse the two).

Default locale (`en`) is unprefixed — don't add `/en/`.

## Cost & quota
**5 T-coins per check** (`sci_defense`), spent when the call starts — state that
before running it. Refunded automatically if the detection pipeline itself
fails; not refunded for a URL problem (HTTP 422).

## Failure modes
- The call is **synchronous** — the response is the final result; don't build a
  polling loop.
- Exit 4 → the `sci_defense` allowance is used up; explain, don't retry, point
  at billing.
- HTTP 422 → the URL couldn't be fetched, resolves to a private address
  (blocked), returned a non-2xx status, had no readable text, or redirected too
  many times or to a non-HTTP scheme. Ask for a different, publicly reachable
  URL rather than retrying the same one.
