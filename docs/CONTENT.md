# Content Model

Harmonic Labyrinths is broad by design. The site should support deep technical work without forcing every piece into a single subject taxonomy.

## Content types

Start with three conceptual types.

### Essays

Substantial, self-contained pieces with a clear argument, investigation, or technical walkthrough.

Examples:

- deep technical dives;
- mathematical explanations;
- architecture analysis;
- philosophical or interdisciplinary essays.

### Notes

Shorter pieces that are useful without pretending to be finished essays.

Examples:

- experiments;
- reading notes;
- implementation observations;
- small technical discoveries;
- working ideas worth preserving.

### Series

A sequence of essays or notes with an intentional reading order.

A series is metadata connecting normal pieces. It should not require a separate publishing format unless the implementation benefits from one.

## Minimal metadata

The exact syntax depends on the eventual static-site implementation, but the content model should be able to express:

```yaml
title: "..."
description: "..."
date: 2026-10-07
updated: 2026-10-07
draft: false
tags:
  - ai
series:
  name: "..."
  order: 1
```

Only `title`, `date`, and publication state should be considered fundamental.

Do not require authors to fill metadata fields solely because a generator supports them.

## Slugs and URLs

Prefer short, human-readable slugs.

Good:

```text
/context-is-not-memory/
/j-space-and-representation/
```

Avoid embedding implementation details or arbitrary category trees:

```text
/posts/2026/10/07/category/ai/article-001/
```

Dates belong in metadata unless there is a deliberate editorial reason to expose them in the URL.

Once published, URLs should remain stable.

## Article structure

A long-form article will usually contain:

1. title;
2. short description or dek;
3. publication metadata;
4. opening that states the problem or curiosity;
5. the actual argument / investigation;
6. references or further reading where useful.

This is a convention, not a template that every piece must mechanically follow.

## Voice

The writing should be personal but rigorous.

Prefer:

- clear claims;
- concrete examples;
- technical specificity;
- first-person voice when it is genuinely useful;
- explicit uncertainty;
- strong opinions when they are argued for.

Avoid:

- corporate marketing language;
- inflated claims;
- fake neutrality;
- unnecessary jargon;
- generic AI-generated transitions;
- conclusions that merely repeat the introduction.

The site should sound like a person thinking carefully in public.

## Technical rigor

### Sources

Prefer primary sources when available:

- papers;
- specifications;
- original documentation;
- source code;
- experiment data;
- direct statements from authors or maintainers.

Place citations close to the claims they support.

Distinguish clearly between:

- established fact;
- interpretation;
- experimental observation;
- speculation;
- personal opinion.

For fast-moving AI topics, include model / system versions and dates when they materially affect the claim.

### Mathematics

When using mathematics:

- define notation before relying on it;
- state assumptions;
- show enough intermediate reasoning that the result can be followed;
- prefer a smaller number of meaningful equations over ornamental formalism.

Math should clarify the argument, not certify it as serious.

### Code

Code examples should be:

- minimal enough to understand;
- complete enough to be meaningful;
- labeled with language when useful;
- tested when the article claims they work.

If code is intentionally pseudocode, say so.

### Experiments

For empirical work, record enough information to reproduce or interpret the result:

- setup;
- inputs / dataset;
- model and version;
- relevant parameters;
- number of runs;
- evaluation method;
- known limitations.

Do not turn a small experiment into a universal claim.

## Figures and diagrams

Figures should do explanatory work.

Each meaningful figure needs:

- a caption or nearby explanation;
- alt text when it conveys information;
- a source / attribution when it is not original.

Prefer diagrams that remain understandable in the site's restrained neutral + blue visual system.

## Tags and categories

Keep taxonomy shallow.

Tags are for discovery, not ontology.

Do not create a tag for every noun in an article. Add one when several pieces are likely to benefit from being browsed together.

Broad topics such as `ai`, `software`, `mathematics`, `philosophy`, or `games` are acceptable, but the site should not require every piece to fit neatly inside one of them.

## Drafts

Draft content must not appear in production feeds, indexes, sitemaps, or search.

A draft may be incomplete, ugly, contradictory, or speculative. Publishing is the boundary at which the public-facing quality bar applies.

## Editing principle

Preserve the author's argument and voice before polishing the prose.

Clarity is more important than smoothness, and specificity is more valuable than generic elegance.
