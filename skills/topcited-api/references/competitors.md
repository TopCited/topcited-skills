# Competitors

## What this is (tell the user)
A "competitor" here means anyone who shows up when your customers search for
what you sell — not always the company you'd point to as your rival. TopCited
tracks these so it can compare how often AI assistants and search engines
mention you versus them, and can scan each one's website to see what keywords
they're targeting.

## When the workflow uses it
Stage 3 (Competitor research): seed the list from rivals the user named, ask
TopCited to suggest more, save the approved set, then scan each saved
competitor's website for the keywords it targets. The brand-wide keyword
dashboard and overlap view live in [brands.md](brands.md). Later stages
(monitoring, reporting) compare share of voice against this list.

## Commands
| I want to… | Command |
|---|---|
| List the active brand's competitors | `topcited competitors list` |
| Add one | `topcited competitors add Gusto -w gusto.com -a "Gusto Payroll"` (`-a` repeatable: other names AI answers use) |
| Get one | `topcited api /competitors/<id>` |

*Internal* (works via `topcited api`, not in the public spec, may change). Get
the brand id from `topcited brand show --json`:

| I want to… | Call |
|---|---|
| Discover competitors with AI | `topcited api -X POST /brands/<id>/competitors:suggest -d '{"query": "best payroll software"}'` |
| Add several at once (all-or-nothing) | `topcited api -X POST /brands/<id>/competitors:bulk -d '[{"name": "Rival Co", "website": "https://rival.com"}]'` |
| Update / remove | `topcited api -X PATCH /competitors/<cid> -d '{…}'` · `topcited api -X DELETE /competitors/<cid>` |
| Start a keyword scan | `topcited api -X POST /competitors/<cid>/keyword-scans` |
| Poll the latest scan | `topcited api /competitors/<cid>/keyword-scans/latest` |
| Read extracted keywords | `topcited api /competitors/<cid>/keywords` |

`:suggest` returns three suggestions that are **not saved** — add the ones the
user picks with `competitors add` or `:bulk`. A keyword scan returns `202` with
the scan `pending`; poll `.../keyword-scans/latest` until `status` is
`completed` or `failed`, then read `.../keywords`.

## UI links
- `{TOPCITED_UI_URL}/competitors` — reads the active brand from the app, so
  there's no brand id in the URL.
- `{TOPCITED_UI_URL}/competitor-keywords` — per-competitor scan results and the
  trigger button, same active-brand pattern.

Default locale (`en`) is unprefixed — don't add `/en/`.

## Cost & quota
- Listing, adding, updating and removing competitors is free.
- `:suggest` spends one `suggestions` unit (2 T-coins) before its LLM call,
  refunded if the LLM returns nothing.
- Each keyword scan spends one `competitor_keyword_scans` unit (5 T-coins) when
  it starts — **not refunded** if the scan later fails. The same allowance backs
  the brand-wide `scan-all`. Read live numbers from `topcited usage`; per-plan
  allowances vary.

## Failure modes
- Exit 4 from `:suggest` or a scan → that allowance is used up; explain, don't
  retry, point at billing.
- Exit 6 on add/bulk → the name or an alias collides with an existing competitor
  of the same brand; `:bulk` then saves none of the batch. List first and ask
  whether to reuse or rename.
- HTTP 400 on a scan → the competitor has no `website`; get one (or `PATCH` it)
  first.
- Exit 6 on a scan → one is already `pending`/`running`; poll instead of
  re-triggering.
- HTTP 404 on `.../keyword-scans/latest` → no scan has ever run for that
  competitor — a normal "nothing yet" state, not an error.
