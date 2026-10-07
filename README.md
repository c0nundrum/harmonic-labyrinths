# Harmonic Labyrinths

A personal site for deep technical and intellectual writing.

**Harmonic Labyrinths** is named after the *Little Harmonic Labyrinth* dialogue in Douglas Hofstadter's *Gödel, Escher, Bach*. The reference is an influence, not a boundary: the site can wander through AI, software, mathematics, philosophy, games, systems, and whatever else becomes interesting enough to follow.

The site is intended to be published with GitHub Pages.

## Intent

Harmonic Labyrinths should feel like a long-lived personal notebook rather than a product landing page.

The goals are simple:

- publish substantial technical dives without forcing them into a narrow theme;
- make difficult material pleasant to read;
- prefer diagrams, mathematics, code, evidence, and primary sources over hand-waving;
- keep the site itself small, fast, and easy to maintain;
- allow short notes and experiments to coexist with long essays and multi-part series.

## Repository principles

1. **Content first.** Site machinery should stay subordinate to the writing.
2. **Static by default.** Prefer build-time work and plain files over runtime services.
3. **Few dependencies.** Every dependency should earn its place.
4. **Accessible by construction.** Semantic HTML, keyboard navigation, visible focus, readable contrast.
5. **URLs are durable.** Published article URLs should not casually change.
6. **Design is a system.** UI work follows [DESIGN.md](./DESIGN.md), not ad-hoc styling.
7. **Documentation stays close to decisions.** Capture rules and rationale, not implementation trivia.

## Documentation

- [DESIGN.md](./DESIGN.md) — visual language and UI rules.
- [AGENTS.md](./AGENTS.md) — constraints for coding agents and contributors.
- [docs/CONTENT.md](./docs/CONTENT.md) — editorial structure and article conventions.
- [docs/ROADMAP.md](./docs/ROADMAP.md) — implementation phases toward launch.

## Working locally

The site is built with [Hugo](https://gohugo.io/) (standard edition, v0.167.0 or newer). It is a single binary; there is no Node or Ruby toolchain.

```sh
brew install hugo          # or see gohugo.io/installation
hugo server --buildDrafts  # preview at http://localhost:1313/harmonic-labyrinths/
hugo --gc --minify         # production build into public/
```

Before pushing, run the same checks CI runs:

```sh
brew install htmltest      # link checker; Node (npx) is also needed
tools/check.sh             # build, XML, internal links, accessibility
tools/check.sh --no-a11y   # skip the headless-browser accessibility pass
```

## Deployment

Every push to `main` runs [`.github/workflows/pages.yml`](./.github/workflows/pages.yml): it builds the site, runs `tools/check.sh`, and deploys to GitHub Pages only if every check passes. Pull requests run the checks without deploying.

The repository's Pages source must be set to **GitHub Actions** (Settings → Pages). The published URL comes from `baseURL` in `hugo.toml`.

When upgrading Hugo, check the KaTeX version it embeds: `assets/css/vendor/katex.css` and `static/fonts/katex/` must match it, or math renders with misaligned glyphs.

## Status

Bootstrap phase: design, templates, technical content, and deployment are in place; launch content is next. See [docs/ROADMAP.md](./docs/ROADMAP.md).

Hugo was chosen because it covers Markdown, build-time syntax highlighting, build-time math, footnotes, RSS, sitemaps, and draft exclusion without adding package dependencies.

## Design reference

The visual system is adapted from the IBM design analysis published by [getdesign.md](https://getdesign.md/ibm/design-md), itself based on publicly observable IBM / Carbon patterns.

Harmonic Labyrinths borrows the precision of that language rather than attempting to imitate IBM branding. This project is independent and is not affiliated with or endorsed by IBM.
