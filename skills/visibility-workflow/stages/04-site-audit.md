# Stage 4 — Site audit

## Purpose (tell the user)
"This is a health check of your website: what's stopping search engines and AI
assistants from finding, understanding, and trusting it. You'll get a ranked
list in plain language."

## Primary TopCited operations
- Register the site, crawl it, list issues — [topcited-api/references/seo-geo-analysis.md](../../topcited-api/references/seo-geo-analysis.md)
  (site audits)
- Quick single-page score + AI-visibility check on any page worth a closer
  look — [topcited-api/references/seo-geo-analysis.md](../../topcited-api/references/seo-geo-analysis.md)
  (URL analysis)
- Manipulation/trust check on a page that looks artificially gamed —
  [topcited-api/references/audit.md](../../topcited-api/references/audit.md) (sci-defense analyze)
- Where a finding is really a content-rewrite problem, the GEO optimizer and
  optimization submissions can illustrate the fix inline —
  [topcited-api/references/seo-geo-analysis.md](../../topcited-api/references/seo-geo-analysis.md)

## Flow
1. Register the site, trigger an audit run, and poll until it's terminal —
   this costs 9 T-coins; state that before triggering.
2. List the issues the crawl found.
3. For pages that look suspicious or heavily AI-generated, run a manipulation
   check (`sci-defense/analyze`) to get a concrete verdict rather than a
   guess — this costs 5 T-coins per check; state that before triggering.
4. End the stage by instantiating `improvement-plan.md`: turn every finding
   into a row with a plain-language "why it matters," a route
   (topcited/agent/user), and get the user's approval item by item — don't
   bulk-approve the whole list at once.

**Routed action (agent-direct):** fetch key pages yourself to verify and
illustrate findings in plain language (e.g. show the user the missing
structured data on their own product page).

## Knowledge
- [technical-seo/crawlability-and-indexing.md](../../seo-geo/knowledge/technical-seo/crawlability-and-indexing.md)
- [technical-seo/canonicals.md](../../seo-geo/knowledge/technical-seo/canonicals.md)
- [technical-seo/sitemaps-and-indexnow.md](../../seo-geo/knowledge/technical-seo/sitemaps-and-indexnow.md)
- [technical-seo/structured-data.md](../../seo-geo/knowledge/technical-seo/structured-data.md)
- [technical-seo/llms-txt.md](../../seo-geo/knowledge/technical-seo/llms-txt.md)
- [technical-seo/core-web-vitals.md](../../seo-geo/knowledge/technical-seo/core-web-vitals.md)
- [geo/citation-optimization.md](../../seo-geo/knowledge/geo/citation-optimization.md)
- [foundations/how-search-ranking-works.md](../../seo-geo/knowledge/foundations/how-search-ranking-works.md)

## Inputs
- `sessions/<brand-slug>/brand-brief.md`

## Outputs
- `sessions/<brand-slug>/improvement-plan.md` (approved, row by row)

## Show
The audit run's issue list and, for any page checked individually, its
analysis (UI-links pattern in the topcited-api skill, references/seo-geo-analysis.md); the manipulation-check
result page (UI-links pattern in the topcited-api skill, references/audit.md) for any page run through it.
