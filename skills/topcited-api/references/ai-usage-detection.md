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
topcited api -X POST sci-defense/analyze -d '{"url": "https://acmecoffee.com/blog/best-espresso-machines"}'
```

Returns immediately (no polling) with a `verdict` of `clean`, `suspicious`, or
`manipulated`, a `combined_score`, per-detector scores, and a short
`text_preview` of what was scanned.

Two lookalikes to ignore: `POST /sci-defense/public-analyze` is the
unauthenticated, IP-rate-limited version behind the public demo page, and
`POST /audit-requests` is the "get a free audit" lead form — it only records
contact details for a human follow-up and analyzes nothing. Neither is for an
agent session.

## What it looks at, and what it doesn't
Tell the user this before they rely on a verdict.

- It fetches the URL from TopCited's servers, extracts the page's **text from the HTML**
  (it drops `script`, `style`, `head`, `noscript`, `nav`, `header` and `footer` elements
  and keeps roughly the first 8,000 characters), and scores that text.
- The scores come from three text-level detectors: a perplexity-based check for
  injected strings (`ppl_score`, `ppl_label`), a four-dimension reasoning/review
  manipulation score (`sis_score`, with `attribute_alignment`, `narrative_purposiveness`,
  `comparative_aggressiveness`, `temporal_coherence`), and a comparative-density check
  (`icd_score`). They are combined into `combined_score` and the `verdict`.
- **It does not interpret CSS or JavaScript.** It is not a hidden-text, cloaking or
  keyword-stuffing detector: text hidden by styling (which is still in the HTML, so it is
  scored like any other text), white-on-white text and off-screen elements are not
  recognised as hidden, and content served only to crawlers is not seen. If the question
  is "is there hidden text on this page?", read the page source or the rendered DOM
  yourself and say that the verdict does not cover it.
- The public demo behind `/try-sci-defense` runs a reduced analysis (without the
  language-model stage), so its scores are not comparable with this call.

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
