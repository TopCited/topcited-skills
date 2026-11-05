# Rewrite patterns

**Evidence note (read before promising anything).** Controlled studies found no reliable citation
lift from JSON-LD (Ahrefs difference-in-differences, 2026-05) or llms.txt (Ahrefs and SE Ranking logs
and correlations, 2025-2026), and Google says it uses neither for its AI features. Do these for rich
results, clarity and hygiene, not as a growth lever. What the evidence supports more: pages that match
the question asked, put the answer early, show price/specs/dates, carry sourced and *verifiable*
numbers, and are mentioned by third parties. See [evidence.md](evidence.md).

Templates for step 4. Replace every `<placeholder>` with real facts from the site; if
you don't have the fact, ask or leave the field out. Never invent.

## Title and meta description

```
Before: Home
After:  <Primary topic> for <audience> | <Brand>          (≤ 60 chars)

Meta:   <What the reader gets, with one concrete detail>. <Differentiator or proof>.   (110–160 chars)
```

## Answer-first opening (GEO)

Open the page with one or two sentences that fully answer the page's main question,
then expand. AI answer engines lift self-contained passages; a buried answer is not
liftable. Pair each claim with a number, a date and a named source.

## JSON-LD — Organization + WebSite (site-wide)

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

# Search/answer crawlers — keep allowed so you can be cited:
# OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot, Perplexity-User
# Training crawlers (GPTBot, ClaudeBot, Google-Extended, CCBot) are a separate policy
# choice for the owner — ask, don't decide.

Sitemap: https://<domain>/sitemap.xml
```

## llms.txt

```
# <Brand>
> <One-sentence description of what the site is and who it is for.>

## Key pages
- [<Page title>](https://<domain>/<path>): <what it covers, one line>

## Optional
- [<Page title>](https://<domain>/<path>): <one line>
```

Details and evidence on what llms.txt does and doesn't do:
[technical-seo/llms-txt.md](../../seo-geo/knowledge/technical-seo/llms-txt.md).
