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

## Status

Bootstrap phase. The publishing stack and implementation are intentionally not fixed by these docs yet.

The first implementation should optimize for GitHub Pages, Markdown-native authoring, mathematical notation, syntax-highlighted code, diagrams, RSS, and excellent reading performance before adding anything more elaborate.

## Design reference

The visual system is adapted from the IBM design analysis published by [getdesign.md](https://getdesign.md/ibm/design-md), itself based on publicly observable IBM / Carbon patterns.

Harmonic Labyrinths borrows the precision of that language rather than attempting to imitate IBM branding. This project is independent and is not affiliated with or endorsed by IBM.
