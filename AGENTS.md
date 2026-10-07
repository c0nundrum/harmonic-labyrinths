# AGENTS.md

Instructions for coding agents and contributors working in this repository.

## Before changing anything

Read:

1. [README.md](./README.md)
2. [DESIGN.md](./DESIGN.md)
3. [docs/CONTENT.md](./docs/CONTENT.md)

These files define the product intent, visual constraints, and editorial model.

## Project posture

Harmonic Labyrinths is a personal static site, not a SaaS application.

Optimize for:

- GitHub Pages compatibility;
- Markdown-native authoring;
- long-form technical reading;
- fast static delivery;
- low maintenance;
- durable URLs;
- accessibility;
- few dependencies.

Do not introduce a framework, CMS, database, server runtime, analytics platform, or client-side state library unless the task actually requires it.

## Implementation rules

### Keep the stack small

Prefer, in order:

1. semantic HTML;
2. CSS;
3. build-time generation;
4. small progressive-enhancement JavaScript;
5. heavier client-side machinery only when clearly justified.

Every new dependency should solve a concrete problem that is difficult to solve cleanly with the existing stack.

### Treat content as source

Published writing should remain understandable and editable in plain text files.

Do not bury article content inside UI component source code.

If the implementation adds front matter, shortcodes, MDX, or similar syntax, keep the authoring model simple and document the convention in `docs/CONTENT.md`.

### Follow the design system

For UI work, [DESIGN.md](./DESIGN.md) is authoritative.

In particular:

- IBM Plex Sans is the primary text face;
- IBM Plex Mono is reserved for technical monospace content;
- use the documented neutral palette and restrained blue accent;
- default border radius is 0;
- use hairlines and surface changes instead of drop shadows;
- use the 4px spacing rhythm;
- optimize article prose for reading width;
- preserve visible keyboard focus and accessible contrast.

Do not improvise a second visual system for individual pages.

### Accessibility

New UI must be keyboard usable and semantically structured.

Before considering UI complete, check:

- headings are ordered logically;
- controls have accessible names;
- focus is visible;
- meaningful images have alt text;
- color is not the only state signal;
- reduced motion is respected;
- narrow-screen and zoomed layouts remain usable.

### Performance

Do not add large client bundles for static content.

Prefer:

- locally optimized assets;
- responsive images;
- SVG for diagrams when practical;
- deferred or absent JavaScript;
- build-time syntax highlighting where feasible.

Avoid autoplaying media, blocking third-party scripts, and oversized web fonts.

### URLs and published content

Treat published URLs as durable API surface.

Do not rename or move published articles without providing an explicit redirect strategy.

Do not silently rewrite article prose while performing unrelated implementation work.

## Documentation rules

Update documentation when a change alters a durable project rule.

Do not document transient implementation details that are obvious from the code.

Useful documentation explains:

- why a decision exists;
- what constraint it creates;
- what future work must preserve.

## Validation

Once a site implementation exists, every meaningful change should run the repository's documented build and checks.

Where supported, validate:

- static build;
- broken internal links;
- formatting / linting;
- accessibility smoke checks;
- responsive behavior;
- generated RSS / sitemap integrity.

Do not claim checks passed unless they were actually run.

## Change philosophy

Prefer the smallest coherent change.

A good contribution should leave the repository easier to understand than it found it.
