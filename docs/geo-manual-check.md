# Manual check: do AI assistants mention TopCited?

Free, about 45 minutes for the core set. Use this for the engines the automated baseline could not
reach (ChatGPT app, Perplexity, Gemini, Copilot, Google AI Overviews, Claude.ai) and to repeat the
check monthly. Why it is designed this way: answers vary a lot between runs, brand lists rarely repeat
([SparkToro study via SEJ](https://www.searchenginejournal.com/ai-recommendations-change-with-nearly-every-query-sparktoro/566242)),
so measure how often a name appears across repeated runs, not rank in one answer.

## Set-up (once)
1. Use the queries in [geo-queries.csv](geo-queries.csv). Core set: the 40 non-definition queries in
   groups G1, G2, G3, G4, G11, plus G9, G10, G12, G14. Start with ten if short on time: Q01, Q02, Q06,
   Q09, Q14, Q19, Q57, Q61, Q69, Q76.
2. Make a sheet with columns: `date, engine, mode, logged_in, location, query_id, run#,
   TopCited_mentioned (Y/N), topcited-skills_mentioned (Y/N), TopCited_URL_cited (Y/N),
   competitors_named, sources_cited (domains), notes`.
3. Use a fresh/private session per run and turn off memory/personalization where the product allows
   (ChatGPT: temporary chat; Claude: new chat without projects; Gemini: signed out or activity off;
   Perplexity: signed out). Note the mode (search on/off, model, Deep Research off).

## Per engine
1. **ChatGPT (chatgpt.com):** New temporary chat, enable Search, paste the query verbatim, no extra
   instruction. Record whether TopCited appears in the text, and open the Sources list to log domains.
2. **Perplexity (perplexity.ai):** New thread, default "Search" mode, paste the query. The Sources panel
   shows cited domains; log them.
3. **Gemini (gemini.google.com):** New chat; log named tools and any source chips.
4. **Google AI Overviews:** Search the query on google.com in a private window. Not every query shows an
   AI Overview; record "no overview" when absent. Expand "Show all" to see links.
5. **Copilot (copilot.microsoft.com):** New conversation; log named tools and citations.
6. **Claude (claude.ai):** New chat, web search on; log named tools and sources.

## Runs
Run each query **3 times per engine**, a few hours or days apart if possible. Record a mention only if
the name appears in the answer text or in the cited sources list; "TopCited" as a different product
(Scopus / INSPIRE bibliometrics) does not count.

## Read-out
Mention rate = runs with a mention / total runs, per engine and per query group. Save the sheet
with the date. Repeat monthly and after each batch of site changes. Judge trends over at least
three monthly checks; one run proves nothing.

## What to do with it
- Mentioned nowhere: expected today, see [geo-plan.md](geo-plan.md).
- Mentioned but with wrong facts (old pricing, "peer-reviewed", wrong features): file it as a
  page-accuracy fix on topcited.ai.
- A competitor appears on a source we could earn a place on: add it to the outreach list in the plan.
