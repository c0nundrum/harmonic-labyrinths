# Roadmap

The path from bootstrap to a published site. Each phase is roughly one pull request.

Mark phases as they ship; delete the file once the site is live.

## Open decision: production domain

Published URLs are durable (see [CONTENT.md](./CONTENT.md)). Moving from `c0nundrum.github.io/harmonic-labyrinths/` to a custom domain later would change every URL.

Decide before Phase 5. If a custom domain is likely, use it from the first publication.

## Phase 0 — Scaffolding ✓

Hugo configuration, permalinks, taxonomies, archetypes, section stubs, provisional skeleton layouts.

## Phase 1 — Design foundation ✓

- `assets/css/tokens.css`: every DESIGN.md value (color, spacing, type scale, breakpoints) as a custom property. Raw values appear nowhere else.
- `base.css` (reset, typography, focus, reduced motion), `prose.css` (reading column, wide breakout column), `code.css` (inverse surface).
- Self-hosted IBM Plex (OFL), latin-subset woff2: Sans 300 / 400 / 400 italic / 600, Mono 400. `font-display: swap`; preload Sans 400 only.
- A specimen page exercising every element (headings, prose, footnotes, code, math, tables, figures, cards, focus states). Excluded from indexes, feeds, and sitemap; used for design review and accessibility checks.

## Phase 2 — Templates ✓

- Base layout: skip link, 48–56px header (Writing / Notes / About), inverse footer (source, RSS).
- Article template in DESIGN.md §7 order, including series context and previous / next.
- Home, Writing and Notes indexes as chronological lists; series, tag, and 404 pages.
- Render hooks: quiet heading anchors, bidirectional footnotes, figures with captions, horizontally scrollable tables.
- Link render hook so root-relative Markdown links (`/about/`) resolve under the site's base path; today they escape a project-site subpath.
- Zero client JavaScript.

## Phase 3 — Technical content ✓

- Build-time syntax highlighting with contrast-checked colors on the inverse surface.
- Build-time math via `transform.ToMath`; display equations in the wide column.
- RSS (site and per section) and sitemap; verify drafts never appear.

## Phase 3½ — Identity ✓

IBM Plex Serif for titles and dialogue speech; the H/L trip-let mark and home figure; dialogue form; figure-ground footer. Rules in DESIGN.md §15.

## Phase 4 — Delivery

- `.github/workflows/pages.yml`: pinned Hugo, build, deploy with the official Pages actions.
- Pull request checks: build with `--panicOnWarning`, internal links (`htmltest`), accessibility smoke test (`pa11y-ci`), RSS / sitemap validity.
- Repository setting: Pages → Source → GitHub Actions. Custom domain DNS if chosen.

## Phase 5 — Launch

- About page and a first real essay replace placeholders.
- Manual pass through the AGENTS.md accessibility checklist at 320 / 672 / 1056px and 200% zoom, keyboard only.
- Publish. URLs are durable from here.

## Deliberately deferred

Dark mode (needs a DESIGN.md decision first), search, comments, analytics, client-rendered diagrams.
