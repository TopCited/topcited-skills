# Recommendations (keywords, prompts, content sentences)

## What this is (tell the user)
Three related tools that each ask an AI to suggest something the brand should be
tracking or saying, based on what we already know about the brand and its
competitors: **keyword recommendations** (search terms worth targeting),
**prompt recommendations** (questions people ask AI assistants, worth adding to
monitoring), and **content sentences** (specific factual statements about the
brand worth working into content so AI assistants can quote them back
accurately). Nothing is added to the brand's real lists until you accept it.

## When the workflow uses it
Stages 2/3/8: keyword and prompt recommendations turn brand and competitor
research into a starting query set instead of the user inventing questions.
Stage 6: content sentences give pillar/cluster drafts something quotable and
accurate.

## Commands
| I want to… | Command |
|---|---|
| Generate prompts worth tracking | `topcited recommend prompts --wait --yes` |
| …focused on a topic | `topcited recommend prompts --topic "payroll compliance" --wait --yes` |
| Generate keywords | `topcited recommend keywords --wait --yes` |
| Generate content sentences | `topcited recommend content --topic "payroll compliance" --wait --yes` |
| Show the latest results without spending | `topcited recommend <kind> --list` |
| The brand's full lists (saved + staged) | `topcited api /brands/<id>/keywords` · `/brands/<id>/prompts` · `/brands/<id>/content-sentences` |

Without `--topic`, prompt and content runs are competitor-driven.

*Internal* (works via `topcited api`, not in the public spec, may change). Get the
brand id from `topcited brand show --json`:
- Accept a staged suggestion: `POST /brands/<id>/keywords/<kid>:accept`,
  `…/prompts/<pid>:accept`, `…/content-sentences/<sid>:accept`.
- Add or delete manually: `POST /brands/<id>/keywords` / `…/prompts`;
  `DELETE …/<item_id>`.
- Push a library prompt into monitoring Topics: `POST /brands/<id>/prompts/<pid>:add-to-topics`.
- Import prompts already used in Topics: `GET /brands/<id>/prompts/importable`,
  then `POST /brands/<id>/prompts:import`.
- Refresh keyword difficulty/volume/CPC: `POST /brands/<id>/keywords:difficulty`.

## Things `--help` won't tell you
- There is only ever **"the latest run"** per kind per brand — no run ids.
  Starting a second run before the first finishes replaces what `--wait` and
  `--list` see; the CLI reports a run replaced under it as `superseded`.
- Results arrive **staged**. Show them to the user and accept only the ones they
  want; accepting the same item twice, or a stale id, returns 404 — re-list to
  get current ids.
- `prompts:importable` is empty until the brand has monitoring history — that's
  expected.

## UI links
- `{TOPCITED_UI_URL}/keywords` — keyword library and recommendations.
- `{TOPCITED_UI_URL}/prompts` — prompt library and recommendations *and* the
  content-sentences panel (no separate content-sentences page).
- `{TOPCITED_UI_URL}/competitor-keywords` — the competitor-keyword views keyword
  recommendations are grounded in.

Default locale (`en`) is unprefixed — don't add `/en/`.

## Cost & quota
- Each run — keywords, prompts, or content sentences — spends **3 T-coins** at
  start, refunded only if the run fails to dispatch or fails internally; not
  refunded because the suggestions disappoint. `--dry-run` can't estimate these
  yet (it shows the balance), so quote the 3 T-coins yourself.
- `keywords:difficulty` spends 3 T-coins only if some keyword is stale against
  a 45-day cache; otherwise it returns `up_to_date` for free.
- `--list`, accepting, adding manually, importing and deleting are free.

## Failure modes
- Exit 4 → that feature's allowance is used up; explain, don't retry, point at
  billing.
- A run that completes with zero usable suggestions still cost its 3 T-coins —
  a normal outcome, not a bug.
- Exit 7 → still running; `topcited wait <job>`.
