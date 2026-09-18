---
topic: Community channels (Reddit, Hacker News, Discord/Slack, forums) — value-first participation without getting flagged as spam
stage-relevance: [7]
last-verified: 2026-08-20
sources:
  - internal TopCited content-distribution playbook (2026-06-14, generalized)
  - internal TopCited generated Reddit/Hacker News drafts (2026-06-14, generalized as pattern examples)
  - [primary] Hacker News guidelines (news.ycombinator.com/newsguidelines.html, accessed 2026-08-20)
  - [industry/heuristic] Reddit self-promotion norms — Reddit's own spam-policy page blocked automated fetch (HTTP 403), so these are secondary-sourced, not primary (redship.io, soar.sh, gofindevo.com, oneup.today, accessed 2026-08-20)
  - [heuristic] Discord/Slack community norms (soar.sh, letstalkshop.com, accessed 2026-08-20)
  - heuristic
---

# Community channels playbook (Reddit, Hacker News, Discord/Slack, forums)

## In plain words
Communities like Reddit and Hacker News are read closely by both people
comparing options and by the crawlers/retrieval systems behind AI answers —
which makes a genuine, well-received post there worth far more than most
other channels. But these communities actively punish anything that reads as
an ad, often with account bans, not just a downvote. The rule that makes this
channel work is simple to state and hard to actually follow: lead with real
value, and mention the product only where it's genuinely relevant — never as
the point of the post.

## What practitioners need to know

### The value-first rule, concretely
- **Post insight, not an announcement.** A post built around a genuine
  finding, dataset, comparison, or lesson-learned reads as a contribution.
  A post built around "we launched X" reads as an ad, even in venues that
  nominally allow self-promotion.
- **Mention the product once, near the end, and only if relevant.** The
  strongest pattern observed: the finding/story stands on its own without
  the product mention; the product is disclosed briefly (ideally with an
  explicit "disclosure: I build in this space" where the venue's norms call
  for it) rather than woven through the post.
- **Answer questions from your own comment history, not a fresh
  drive-by account.** Communities and their moderators are sensitive to
  accounts that only ever post about one product — that pattern alone gets
  flagged regardless of the individual post's content *(heuristic — an
  account-reputation signal, not a per-post one)*.
- **Read the specific subreddit's/forum's self-promotion rules before
  posting.** Rules vary a lot by community — some forums require a
  disclosure flair, some cap self-promo to a fixed ratio of total posts, some
  ban it outright. Checking first avoids a post being removed on a
  technicality that had nothing to do with its quality. Reddit's informal
  sitewide norm (not literal policy text — a community-converged number) is
  the **90/10 rule**: roughly 90% non-promotional participation to at most
  10% self-promotion *(heuristic, widely repeated across practitioner
  sources)*. A concrete, checkable example of a per-community rule:
  **r/indiehackers** permits exactly **one self-promotion post per product**,
  tagged "SHOW IH" and framed for feedback rather than advertisement;
  repeat promo posts get removed *(heuristic/community-reported)*.

### What gets flagged as spam
- **Posting the same content across many subreddits/forums in a short
  window.** Cross-posting identical text reads as a blast, not a
  contribution, even if the underlying content is genuinely good. On Reddit
  specifically, this is a harder consequence than social judgment: posting
  the same link to 5+ subreddits in one day with no prior comment history in
  any of them can trigger a **sitewide, largely unappealable shadowban**
  from Reddit's automated spam filter — independent of whatever any single
  subreddit's moderators think of the post *(heuristic — practitioner
  -reported outcomes, no Reddit engineering documentation found describing
  the filter itself)*.
- **A title or first line that's an ad headline** (feature list, pricing,
  "check out my new tool") rather than a claim, finding, or question a
  reader would care about independent of the product.
- **Zero engagement in the thread after posting.** Communities expect the
  poster to show up and answer questions/pushback in-thread; ghosting a
  thread you started reads as low-effort self-promotion, and un-answered
  skeptical top comments actively hurt the post's credibility to later
  readers (including anything that later gets crawled).
- **An account with no history except product mentions.** Even a
  well-written individual post gets discounted (or removed pre-emptively by
  automod) if the posting account's history is otherwise empty or
  exclusively promotional.
- **Ignoring a venue's explicit format norms.** Hacker News specifically
  punishes marketing language in "Show HN" titles — a plain, literal
  description of what the thing does outperforms anything that reads like a
  tagline *(heuristic, but a well-documented community norm)*. Being ready
  to answer pointed technical questions in the resulting thread — including
  honest limitations — is itself part of the norm, not optional politeness.
  HN's own guidelines state this directly [primary]: **"Please don't use HN
  primarily for promotion. It's ok to post your own stuff part of the time,
  but the primary use of the site should be for curiosity,"** and
  **"Don't solicit upvotes, comments, or submissions"** — booster comments
  from friends/colleagues in a thread are treated by the community as a form
  of spamming. **Show HN specifically requires something people can try**
  (use, read, watch) — a "coming soon" landing page is explicitly
  disqualified as a Show HN post [primary].

### Discord and Slack communities
Common B2B/SaaS distribution channels, and the same value-first logic
applies, with a few community-specific wrinkles *(heuristic, converged
across several 2026 practitioner sources — no platform-level primary
documentation exists since these are per-community, not sitewide, rules)*:
- **Be useful first, promote second.** Establish presence answering
  questions before ever posting a link — the same rule as Reddit/HN, just
  enforced by community culture rather than automod.
- **Most active communities restrict promotion to a dedicated channel or a
  scheduled "self-promo" window.** Posting in general channels without an
  explicit rule permitting it reads as spam by default.
- **Profile hygiene matters before any posting behavior.** A real name/photo
  and a bio describing the person (not the company) reads as legitimate; a
  company-branded join reads as suspicious immediately.
- No measured spam-flag rate or engagement-lift data was found for this
  channel — treat it at the same heuristic confidence tier as the
  Reddit/HN guidance above, not as a proven-higher- or lower-value channel.

### Pacing
Space posts out — roughly one per week per community is a reasonable
default — and rotate which community gets the post rather than repeating the
same one. A single well-received post per venue does more for both trust and
downstream citation potential than several mediocre ones.

## How this shows up in the workflow
Stage 7 (distribution) uses this file to decide what NOT to post as much as
what to post: before drafting community content, check that the piece leads
with a real finding/story that would stand on its own, and that the posting
cadence isn't bunching multiple communities' posts into the same short
window.
