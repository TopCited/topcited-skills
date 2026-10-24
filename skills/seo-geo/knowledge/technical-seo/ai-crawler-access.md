---
topic: AI crawler user agents, what robots.txt can and can't control, and the training-vs-search trade-off
stage-relevance: [4, 5]
last-verified: 2026-10-24
sources:
  - https://developers.openai.com/api/docs/bots (OpenAI crawlers; platform.openai.com/docs/bots redirects here)
  - https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler (Anthropic, 2026-04-07)
  - https://docs.perplexity.ai/guides/bots (Perplexity crawlers)
  - https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers (Google, updated 2026-10-15)
  - https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers (Google, 2026-08-19)
  - https://developers.google.com/search/docs/appearance/ai-features (Google AI features controls)
  - https://support.google.com/webmasters/answer/16908024 (Search Console "Search generative AI" control)
  - https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt (Google robots.txt spec, updated 2026-10-23)
  - https://www.rfc-editor.org/rfc/rfc9309.html (Robots Exclusion Protocol)
  - https://support.apple.com/en-us/119829 (Applebot / Applebot-Extended)
  - https://developer.amazon.com/amazonbot (Amazonbot, Amzn-SearchBot, Amzn-User)
  - https://developers.facebook.com/docs/sharing/webmasters/web-crawlers/ (Meta crawlers)
  - https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot
  - https://docs.mistral.ai/robots
  - https://commoncrawl.org/ccbot
  - https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat
  - https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/ (2025-08-04)
  - https://blog.cloudflare.com/content-signals-policy/ (2025-09-24)
  - https://blog.cloudflare.com/content-independence-day-ai-options/ (2026-07-01)
  - https://blog.cloudflare.com/radar-2025-year-in-review/
  - https://datatracker.ietf.org/wg/aipref/documents/ (IETF AI Preferences WG)
  - https://rslstandard.org/rsl (RSL 1.0)
  - heuristic
---

# AI crawler access control

## In plain words
Each AI company sends several different bots to websites: one to collect
training data, one to build the index its assistant searches, and one that
fetches a page live when a user asks about it. `robots.txt` lets a site say
yes or no to each bot separately — so a site can refuse to be used for
training and still be found and cited in AI answers. The most common
mistake is a blanket "block all AI bots" rule that quietly removes the site
from ChatGPT, Claude, or Perplexity answers too. And robots.txt is a
request, not a lock: bots that fetch on a user's behalf often ignore it.

## What practitioners need to know

### The three bot jobs — block them separately
Vendors now split crawlers by purpose. *(P — each vendor's own docs, 2026-10)*

| Vendor | Training | Search / answer index | User-initiated fetch |
|---|---|---|---|
| OpenAI | `GPTBot` | `OAI-SearchBot` | `ChatGPT-User` — "robots.txt rules may not apply" |
| Anthropic | `ClaudeBot` | `Claude-SearchBot` | `Claude-User` — honors robots.txt |
| Perplexity | — (says it doesn't crawl for model training) | `PerplexityBot` | `Perplexity-User` — "generally ignores robots.txt rules" |
| Google | `Google-Extended` (control token, not a separate crawler) | `Googlebot` (Search, incl. AI Overviews / AI Mode) | user-triggered fetchers (e.g. `Google-Agent`) — "generally ignore robots.txt rules" |
| Apple | `Applebot-Extended` (control token) | `Applebot` | — |
| Amazon | `Amazonbot` (may train Amazon models) | `Amzn-SearchBot` | `Amzn-User` — "may not follow all robots.txt directives" |
| Meta | `meta-externalagent` | `meta-webindexer` | `meta-externalfetcher` — "may bypass robots.txt" |
| Mistral | `MistralAI-Training` | `MistralAI-Index` | `MistralAI-User` |
| DuckDuckGo | — (not used for training) | `DuckAssistBot` | — |
| Common Crawl | `CCBot` (open dataset widely used for LLM training) | — | — |

Notes that change decisions:
- **OpenAI**: "Sites that are opted out of OAI-SearchBot will not be shown
  in ChatGPT search answers" (they can still appear as navigational links);
  if both `GPTBot` and `OAI-SearchBot` are allowed, OpenAI may use one crawl
  for both purposes. `OAI-AdsBot` only visits landing pages of submitted
  ChatGPT ads. OpenAI publishes IP lists per bot (`openai.com/gptbot.json`,
  `searchbot.json`, `chatgpt-user.json`). *(P)*
- **Anthropic**: "Anthropic's Bots respect 'do not crawl' signals by
  honoring industry standard directives in robots.txt," including
  `Crawl-delay`; blocking `Claude-SearchBot` or `Claude-User` "may reduce
  visibility" in Claude's search results. The old `anthropic-ai` and
  `Claude-Web` tokens are no longer on Anthropic's page. *(P; heuristic for
  the legacy tokens)*
- **Google**: `Google-Extended` covers Gemini model training and grounding
  in Gemini Apps / Vertex AI, and "does not impact a site's inclusion in
  Google Search nor is it used as a ranking signal." It does **not** keep a
  site out of AI Overviews or AI Mode. *(P)*
- **Apple**: if robots.txt names Googlebot but not Applebot, Applebot
  follows the Googlebot rules. *(P)*
- **Bytespider** (ByteDance) has no primary documentation, and press reports
  say it ignores robots.txt — block it at the server/CDN if it matters.
  (heuristic)
- **Cohere** says it does not currently crawl the web to train foundation
  models. *(P)*

### Controlling Google's AI features is different
robots.txt can't remove a site from AI Overviews / AI Mode without also
removing it from Search (blocking `Googlebot`). The real options *(P)*:
- **Snippet controls** — `nosnippet`, `data-nosnippet`, `max-snippet`, or
  `noindex` limit what Google shows, in AI features and classic snippets
  alike (`nosnippet` is all-or-nothing).
- **Search Console → Settings → "Search generative AI" control** (worldwide
  since 2026-08-31): excluding a property removes it from AI Overviews, AI
  Mode, and Discover's generative features within about 1–2 days. Google
  says it "isn't used as a ranking or inclusion signal" for the rest of
  Search, and "doesn't affect AI training" (that's still `Google-Extended`).
  Sites that opt out get no traffic from those features.

### Bing / Copilot uses meta tags, not a separate bot
`bingbot` serves both Bing Search and Copilot grounding. Bing's controls
*(P, Bing 2023; reaffirmed in Bing's 2026 guideline update per SEJ)*:
- `<meta name="robots" content="nocache">` — Copilot may cite the page but
  show only URL, title, and snippet.
- `noarchive` — the page isn't included in or linked from Copilot answers,
  and isn't used for training.
- Both keep the page in normal Bing results.

### robots.txt mechanics that trip people up
- **Groups don't inherit from `*`**: a crawler obeys only the most specific
  group that names it. A `User-agent: GPTBot` group with one `Disallow`
  does **not** also pick up the rules under `User-agent: *`. *(P — Google's
  implementation and RFC 9309)*
- Tokens match case-insensitively; within a group, the longest matching
  path wins, and allow wins a tie. *(P)*
- Google reads the first **500 KiB** and caches robots.txt up to 24h; a 5xx
  on robots.txt stops crawling, a 4xx (other than 429) means "no
  restrictions." *(P)* Other vendors document roughly 24h (OpenAI,
  Perplexity, Meta) to 72h (DuckDuckGo) before changes take effect; Amazon
  may cache up to 30 days. *(P)*
- **robots.txt is not access control** (RFC 9309 says so). To enforce a
  block, or to stop user-initiated fetchers that ignore robots.txt, act at
  the server/WAF/CDN — and verify bots by published IP ranges or reverse
  DNS, not by user-agent string, which anyone can fake. *(P)*

### Robots.txt isn't always honored
- Cloudflare reported on 2025-08-04 that Perplexity used undeclared crawlers
  (a generic Chrome-on-macOS user agent, rotating IPs outside its published
  ranges) to fetch sites that had blocked its declared bots; Cloudflare
  delisted Perplexity as a verified bot. Perplexity disputed the
  characterization. In the same test, `ChatGPT-User` honored robots.txt.
  *(I)*

### Emerging signals beyond allow/disallow
None of these is a ratified standard yet — treat them as optional extras.
- **IETF AI Preferences (aipref)**: working-group drafts define a
  `Content-Usage:` robots.txt rule and HTTP header (e.g.
  `Content-Usage: train-ai=n`). Still Internet-Drafts as of 2026-10, with
  the vocabulary draft marked as not reflecting consensus. *(P)*
- **Cloudflare Content Signals** (2025-09): `Content-Signal: search=yes,
  ai-train=no` in robots.txt, with an `ai-input` signal for grounding/RAG;
  deployed via Cloudflare's managed robots.txt on millions of domains. *(P)*
  Note the vocabulary differs from the IETF draft (`ai-train` vs
  `train-ai`).
- **RSL (Really Simple Licensing) 1.0** (2025-12): a `License:` line in
  robots.txt pointing to machine-readable licensing terms. No measured
  crawler compliance data found. *(P for the spec; heuristic for adoption)*
- **CDN defaults can block AI bots without the site owner choosing to.**
  Cloudflare has blocked AI crawlers by default on new domains since
  2025-07, and from 2026-09-15 splits AI bots into Search / Agent /
  Training categories, blocking Training and Agent by default on new
  domains' ad-carrying pages. *(P)* Cloudflare's own posts conflict on
  whether blocking "Training" also blocks multi-purpose crawlers like
  Googlebot — check the zone's actual settings, not the default you assume.

### How common blocking is
AI crawlers were the most frequently *fully* disallowed user agents in
robots.txt files in 2025, with GPTBot, ClaudeBot, and CCBot named
(Cloudflare Radar 2025). *(I)* In Cloudflare's 2026-09 figures, 17% of
sites restrict AI training and under 1% block search crawlers. *(I)* An
HTTP Archive analysis of July 2025 data found about 21% of the top 1,000
sites have GPTBot rules. *(I)* Several 2025–26 audits report many sites that
block `GPTBot` also block `OAI-SearchBot`, often by accident — and lose
ChatGPT search visibility as a result. (heuristic)

### The default recommendation
For a brand that wants AI visibility (heuristic, follows from the vendor
docs above):
1. **Allow every search/answer bot** — `Googlebot`, `bingbot`,
   `OAI-SearchBot`, `Claude-SearchBot`, `PerplexityBot`, `Applebot`,
   `DuckAssistBot`, `Amzn-SearchBot`, `meta-webindexer` — and don't block
   user-initiated fetchers you want answering questions about you.
2. **Decide training separately**: blocking `GPTBot`, `ClaudeBot`,
   `Google-Extended`, `Applebot-Extended`, `CCBot` and similar doesn't
   remove the site from those vendors' answer surfaces. Allowing training
   may help a brand show up in answers given without a live search, but no
   vendor quantifies that. (heuristic)
3. **Check the CDN/WAF layer**, not just robots.txt — a bot-management
   default can block what robots.txt allows.

```
# Example: opt out of model training, stay visible in AI answers
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: Applebot-Extended
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: *
Allow: /

Sitemap: https://example.com/sitemap.xml
```

## How this shows up in the workflow
Stage 4 (site audit) fetches `/robots.txt` and checks each AI search/answer
bot against the table above — a disallowed `OAI-SearchBot`,
`Claude-SearchBot`, or `PerplexityBot` is a direct cause of AI invisibility
and should rank near the top of the findings, alongside any CDN-level bot
blocking. Stage 5 (technical/entity fixes) applies the training-vs-search
split the brand owner chooses — explained in plain words, since it's a
business decision about training data, not an SEO best practice — and
verifies the change with a re-fetch after the vendor's documented cache
window.
