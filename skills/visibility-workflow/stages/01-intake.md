# Stage 1 — Intake

## Purpose (tell the user)
"Before I can help people find you, I need to understand your business the way a
customer would. I'll ask a few questions — there are no wrong answers, and if
you're not sure, I'll suggest options and you pick."

## Primary TopCited operations
- Create/select brand — [topcited-api/references/brands.md](../../topcited-api/references/brands.md)

## Flow
1. Ask for the website URL. Fetch the homepage yourself and skim it — your
   suggestions below come from this.
2. Confirm, then create the brand (or reuse an existing one — list first).
3. Guided interview, one question at a time:
   - What do you sell or offer?
   - Who buys it? (audience)
   - Why do customers pick you over alternatives? (differentiator)
   - Which companies do you consider rivals?
   - Any geographies or languages that matter?
   **Suggest-and-approve:** whenever the user is unsure, propose 2–3 candidates
   derived from their website and let them pick or correct.
4. Ask whether they can share materials (slides, one-pagers, docs) — TopCited has
   no upload feature today, so save anything they share into
   `sessions/<brand-slug>/materials/` and reference the paths in the brand brief.
   Record one line in `gaps.md`: a files-upload API would be needed for a product
   version of this step. Ask whether they can grant access to their website's code
   or CMS, explaining plainly: "if you can, I'll be able to fix technical things for
   you directly instead of sending you instructions."

## Knowledge
- [foundations/seo-geo-aeo-differences.md](../../seo-geo/knowledge/foundations/seo-geo-aeo-differences.md)
  (for explaining what we're about to do overall)

## Inputs
None (first stage).

## Outputs
- `sessions/<brand-slug>/brand-brief.md` (from template, fully filled)
- `sessions/<brand-slug>/materials/` populated with anything the user shared
- `progress.md` stage row → done, log entry
- `gaps.md` entry for the missing files-upload API (see Flow step 4)

## Show
The brand page in the TopCited UI (UI-links pattern in the topcited-api skill, references/brands.md), so the user
sees their brand exists on the platform.
