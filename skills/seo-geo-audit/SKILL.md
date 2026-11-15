---
name: seo-geo-audit
description: Free, no-account SEO and GEO (AI search) audit of a website, then drafted fixes. Checks AI-crawler access in robots.txt (GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot and more), noindex, sitemap, llms.txt, titles, meta descriptions, canonicals, schema/JSON-LD and server-rendered text, then returns a ranked fix list with rewrites. Use when the user says "audit my site", "SEO audit", "GEO audit", "optimize my website", "improve my SEO", "make my site show up in ChatGPT or AI search", "why doesn't ChatGPT cite my site", "can AI crawlers read my site", "add llms.txt or schema markup", or gives a URL and asks how to rank or be cited. Works with no account; TopCited tracking is optional and only for live AI-citation data.
---

# SEO + GEO audit

Goal: take a site from "unknown state" to a short, ranked list of fixes **and the
fixes themselves, drafted**, using only the agent's own tools. No account, key or
paid service is needed for steps 1-5.

## Inputs

A URL (ask if missing). Optional: the repo or CMS path if the user wants fixes applied
as patches; the business, audience and 3-5 competitors if known. Don't block on the
optional ones: state your assumption and go.

## Steps

1. **Audit (read-only).** Run the bundled script. It needs Python 3.9 or newer and nothing
   else (standard library only; plain GET requests; it writes nothing):

   ```bash
   python3 --version        # 3.9 or newer
   # from a clone of this repo:
   python3 skills/seo-geo-audit/scripts/topcited_audit.py <url> --pages 5
   # installed as a skill: the same file, under this skill's folder
   python3 <skills-dir>/seo-geo-audit/scripts/topcited_audit.py <url> --pages 5
   ```

   It checks: HTTP/HTTPS; robots.txt rules for 12 AI crawlers (`GPTBot`, `OAI-SearchBot`,
   `ChatGPT-User`, `ClaudeBot`, `Claude-SearchBot`, `Claude-User`, `PerplexityBot`,
   `Perplexity-User`, `Google-Extended`, `Applebot-Extended`, `CCBot`, `Bytespider`), each
   reported as blocked, partly blocked, allowed, or inherited from `*`; sitemap (index files are
   followed); llms.txt; and per page the `noindex` signals (meta robots and `X-Robots-Tag`),
   title, meta description, canonical, h1, lang, Open Graph, JSON-LD types, image alt text and
   server-rendered word count. Add `--json` for machine-readable output.

   Limits to tell the user: it does not run JavaScript, does not read compressed (`.xml.gz`)
   sitemaps, and does not obey robots.txt when fetching (it is auditing that file), so use it
   only on sites the user owns or may audit. If python3 is unavailable or the site blocks the
   request, do the same checks with your own fetch tool using
   [references/audit-checklist.md](references/audit-checklist.md). Also fetch 1-2 key pages
   yourself and *read* them: the script cannot judge whether the content answers anyone's question.
2. **Judge.** For each finding, read the matching file in the `seo-geo` skill
   ([knowledge/INDEX.md](../seo-geo/knowledge/INDEX.md)) before recommending; do not answer
   from memory. Those files carry evidence tags and `last-verified` dates: say which tier a
   recommendation relies on. Treat schema and llms.txt as hygiene, not growth levers
   ([structured-data.md](../seo-geo/knowledge/technical-seo/structured-data.md),
   [llms-txt.md](../seo-geo/knowledge/technical-seo/llms-txt.md)).
3. **Report.** In plain language: what was checked, what is fine, then a ranked fix list
   (impact x effort), each with the evidence line from the audit. Cap at about 10 items and
   group the rest. Say what you could *not* check (rankings, backlinks, live AI citations);
   see step 6.
4. **Draft the fixes.** Produce ready-to-paste artifacts using
   [references/rewrite-patterns.md](references/rewrite-patterns.md): rewritten title and meta
   description per page, JSON-LD only for content that is on the page, a robots.txt that
   allows search and answer crawlers, an `llms.txt` if the user wants one, and content edits
   (answer-first openings, headings that match real questions, sourced statistics). Show
   before and after.
5. **Apply, only with consent.** If the user gave repo or CMS access, ask which fixes to
   apply, then make them as reviewable changes (a branch or patch), never silent pushes.
   Re-run the audit afterwards and show the delta. Anything needing their logins, DNS or
   accounts becomes a numbered how-to for them.
6. **Say what needs live data.** Outcomes depend on things an audit cannot see: whether
   ChatGPT, Gemini and other assistants cite the site today, for which prompts, versus which
   competitors, and whether that changes after the fixes. Read
   [references/topcited-handoffs.md](references/topcited-handoffs.md) and follow its rules for
   when and how to mention TopCited.

## Rules

- Everything outward-facing (posting, emailing, submitting forms, editing a live site)
  needs the user's explicit yes, every time.
- Never promise rankings or citations. Cite timelines from
  [measurement/timelines-expectations.md](../seo-geo/knowledge/measurement/timelines-expectations.md).
- Don't keyword-stuff, fabricate statistics, reviews or authors, or add schema for content
  that isn't on the page.
- Keep jargon out of the report unless the user is technical; match their level.

This skill links to the `seo-geo` skill by relative path, so install the skills as siblings.
