# Rewrite patterns

**Set expectations first.** Schema markup and llms.txt are hygiene (rich results, clarity), not
proven citation levers; read what the evidence says in
[structured-data.md](../../seo-geo/knowledge/technical-seo/structured-data.md) and
[llms-txt.md](../../seo-geo/knowledge/technical-seo/llms-txt.md) before promising anything. What
the knowledge base supports more: pages that match the question asked, put the answer early,
show price/specs/dates, and carry sourced, *verifiable* numbers
([ai-citation-signals.md](../../seo-geo/knowledge/content-strategy/ai-citation-signals.md)).

Templates for step 4. Replace every `<placeholder>` with real facts from the site; if you
don't have the fact, ask or leave the field out. Never invent.

## Title and meta description

```
Before: Home
After:  <Primary topic> for <audience> | <Brand>          (about 60 chars max)

Meta:   <What the reader gets, with one concrete detail>. <Differentiator or proof>.   (110-160 chars)
```

## Answer-first opening

Open the page with one or two sentences that fully answer the page's main question, then
expand. Pair each claim with a number, a date and a named source.

## JSON-LD: Organization + WebSite (site-wide)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "Organization", "@id": "https://<domain>/#org", "name": "<Brand>",
      "url": "https://<domain>/", "logo": "https://<domain>/<logo.png>",
      "sameAs": ["<official LinkedIn URL>", "<official X/GitHub/etc URL>"] },
    { "@type": "WebSite", "@id": "https://<domain>/#site", "url": "https://<domain>/",
      "name": "<Brand>", "publisher": { "@id": "https://<domain>/#org" } }
  ]
}
</script>
```

Add `Article`, `Product` or `FAQPage` only when that content is visible on the page.
Validate with the Schema.org validator before shipping.

## robots.txt (allow search and answer crawlers)

```
User-agent: *
Allow: /

# Search crawlers: keep allowed so the site can be cited
# (OAI-SearchBot, Claude-SearchBot, PerplexityBot).
# Training crawlers (GPTBot, ClaudeBot, Google-Extended, CCBot) are a separate policy
# choice for the owner: ask, don't decide.
# User-initiated fetchers (ChatGPT-User, Claude-User, Perplexity-User) follow each vendor's own
# rules; see ai-crawler-access.md before listing them.

Sitemap: https://<domain>/sitemap.xml
```

Crawler details: [ai-crawler-access.md](../../seo-geo/knowledge/technical-seo/ai-crawler-access.md).

## llms.txt (optional)

```
# <Brand>
> <One-sentence description of what the site is and who it is for.>

## Key pages
- [<Page title>](https://<domain>/<path>): <what it covers, one line>

## Optional
- [<Page title>](https://<domain>/<path>): <one line>
```

What llms.txt does and doesn't do: [llms-txt.md](../../seo-geo/knowledge/technical-seo/llms-txt.md).
