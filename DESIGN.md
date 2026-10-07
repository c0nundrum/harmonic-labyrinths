---
version: 0.1
name: harmonic-labyrinths-design
description: "A reading-first personal technical blog with Carbon-inspired precision: IBM Plex typography, a restrained blue accent, square geometry, hairlines instead of shadows, and a 4px spatial rhythm."
reference: "https://getdesign.md/ibm/design-md"
---

# Harmonic Labyrinths Design Rules

This document is the source of truth for visual decisions in Harmonic Labyrinths.

The system begins with the IBM design analysis published by getdesign.md and the visual language of Carbon, but adapts those ideas to a personal editorial site. The goal is **not** to reproduce ibm.com. The goal is to borrow its precision, restraint, typography, and geometry while optimizing for long technical reading.

Harmonic Labyrinths is independent and is not affiliated with or endorsed by IBM.

Every value in this document is translated into CSS exactly once, as custom properties in `assets/css/tokens.css`. Stylesheets use tokens, not raw values; change a value here first, then in the tokens file.

## 1. Design character

The site should feel:

- precise, technical, and calm;
- editorial before promotional;
- dense enough to reward exploration, but never crowded;
- intentionally flat rather than decorative;
- recognizably personal without becoming visually noisy.

The writing is the dominant object on the page. Navigation and chrome should recede.

### Core rule

> Prefer structure over decoration.

Hierarchy should come from typography, spacing, alignment, surface changes, and hairlines before color, shadow, animation, or ornament.

## 2. Color

The palette is intentionally narrow.

| Role | Value | Use |
| --- | --- | --- |
| Primary | `#0f62fe` | Links, focus, primary actions, rare emphasis |
| Primary hover | `#0050e6` | Hovered primary actions |
| Primary pressed | `#002d9c` | Pressed state |
| Ink | `#161616` | Primary text |
| Ink muted | `#525252` | Metadata, secondary text |
| Ink subtle | `#8d8d8d` | Tertiary text only |
| Canvas | `#ffffff` | Main background |
| Surface 1 | `#f4f4f4` | Alternate sections, code-adjacent surfaces |
| Surface 2 | `#e0e0e0` | Stronger separators / disabled surfaces |
| Inverse | `#161616` | Code blocks and rare inverse regions |
| Inverse ink | `#f4f4f4` | Text on inverse surfaces |
| Success | `#24a148` | Semantic success only |
| Warning | `#f1c21b` | Semantic warning only |
| Error | `#da1e28` | Semantic error only |

### Color rules

- Blue is scarce. It means interaction, focus, or deliberate emphasis.
- Do not introduce a second decorative accent color.
- Do not use gradients as general decoration.
- Do not communicate state by color alone.
- Long-form article backgrounds remain neutral.

## 3. Typography

### Families

Use **IBM Plex Sans** for interface and prose.

Use **IBM Plex Mono** for:

- code;
- terminal output;
- inline technical identifiers when monospace adds meaning;
- compact technical labels when appropriate.

Do not use monospace simply to make something feel "technical."

Fallbacks:

```css
font-family: "IBM Plex Sans", "Helvetica Neue", Arial, sans-serif;
font-family: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
```

### Hierarchy

| Role | Size | Weight | Line height | Notes |
| --- | ---: | ---: | ---: | --- |
| Display | clamp(2.75rem, 7vw, 4.75rem) | 300 | 1.12 | Home / major section title |
| Article title | clamp(2.25rem, 5vw, 3.75rem) | 300 | 1.15 | Long-form title |
| H1 | 2.625rem | 300 | 1.20 | Page-level heading |
| H2 | 2rem | 400 | 1.25 | Major article section |
| H3 | 1.5rem | 400 | 1.33 | Subsection |
| Lead | 1.25rem | 400 | 1.50 | Dek / introductory paragraph |
| Prose | 1.125rem | 400 | 1.60 | Main article body |
| UI body | 1rem | 400 | 1.50 | Navigation and general UI |
| Small | 0.875rem | 400 | 1.40 | Metadata |
| Caption | 0.75rem | 400 | 1.40 | Captions / tertiary information |

### Typography rules

- Display text at 42px and above should normally use weight 300.
- Body text uses weight 400. Reserve 600 for emphasis; avoid 700 unless content semantics demand it.
- Body/UI text may use the Carbon-like `0.16px` positive tracking.
- Use sentence case. Avoid all-caps tracked "enterprise" eyebrows.
- Keep line length comfortable: **60–78 characters** for article prose.
- Headings may extend wider than prose, but must remain visually tied to the article column.
- Do not justify body text.

## 4. Spatial system

Use a **4px base grid**.

Preferred spacing tokens:

| Token | Value |
| --- | ---: |
| 1 | 4px |
| 2 | 8px |
| 3 | 12px |
| 4 | 16px |
| 6 | 24px |
| 8 | 32px |
| 12 | 48px |
| 16 | 64px |
| 24 | 96px |

Avoid arbitrary one-off spacing values when a token is close enough.

### Page geometry

- Overall layouts may follow Carbon's 16 / 8 / 4 column idea.
- Article prose width is set by characters per line (60–78), not pixels. IBM Plex Sans is narrow: at prose size a 720px column measured 80–92 characters per line, so the prose column is **600px (37.5rem)**, which measures roughly 60–76.
- Supporting figures, equations, diagrams, code, and tables may break out into a wider column of **832px (52rem)**.
- On large screens, whitespace should come from grid alignment rather than giant empty hero sections.
- Separate sections using rhythm, subtle surface changes, or 1px hairlines.

## 5. Shape and depth

Default border radius: **0px**.

Small exceptions may use 2–4px only where the shape communicates a distinct control state or third-party content.

### Rules

- Buttons: square.
- Cards: square.
- Inputs: square.
- Images: square unless the source itself has meaningful shape.
- No pill buttons.
- No floating glass panels.
- No generic drop shadows.

Depth hierarchy:

1. whitespace;
2. 1px border / hairline;
3. background surface change;
4. inverse surface when strongly justified.

Shadow is a last resort, not a default.

## 6. Navigation

Navigation should be small and predictable.

The primary navigation should expose only durable destinations, for example:

- Writing
- Notes
- About

Do not add navigation items merely because content can be categorized.

### Header

- 48–56px high on desktop.
- Site name or compact mark at the left.
- Minimal links aligned to the grid.
- 1px bottom divider is preferred to shadow.
- Sticky navigation is optional; if used, it must not consume excessive vertical space.

### Footer

The footer may use the inverse `#161616` surface.

Keep it useful rather than large: identity, source repository, RSS, and a small number of durable links are enough.

## 7. Article pages

Article pages are the most important template.

Preferred order:

1. optional series / section context;
2. title;
3. description / dek;
4. date, updated date, reading metadata if genuinely useful;
5. article body;
6. references / further reading when relevant;
7. previous / next entry for a real series.

### Reading rules

- Keep core prose in the narrow reading column.
- Use generous space before H2 sections.
- Footnotes must be easy to move between in both directions.
- Heading anchors should be linkable without permanently noisy hash icons.
- Long articles may have a table of contents, but it should not compete with reading.
- Never place unrelated calls to action inside the prose.

## 8. Technical content

Technical content is first-class, not an embedded afterthought.

### Code

- Use IBM Plex Mono.
- Preserve horizontal scrolling rather than wrapping code destructively.
- Always provide adequate contrast.
- Show language labels only when useful.
- Copy buttons are optional and should remain quiet.
- Code blocks may use the inverse surface.

### Mathematics

- Inline mathematics must align comfortably with prose.
- Display equations may use the wider article region.
- Equation numbering should only be added when the text refers to equations by number.

### Diagrams

- Prefer SVG where practical.
- Diagrams should inherit the neutral + blue palette unless the data requires additional semantic colors.
- Every meaningful diagram needs alt text or an adjacent textual explanation.
- Avoid decorative diagrams that do not clarify the argument.

### Tables

- Use hairlines, not boxed cards around every cell.
- Left-align text by default.
- Align numbers by meaning.
- Allow horizontal scrolling on narrow viewports.

## 9. Cards and indexes

Article cards are primarily an information hierarchy, not a visual component showcase.

A card may contain:

- title;
- short description;
- date;
- tags or series context when useful.

Rules:

- No shadow.
- 1px hairline or surface change for separation.
- Whole-card click targets are acceptable when semantics remain correct.
- Do not make every article look like a product tile.
- Prefer lists over cards when a list communicates chronology or density better.

## 10. Interaction

Interaction should feel immediate and unsurprising.

- Minimum touch target: **48px** where practical.
- Keyboard focus must always be visible.
- Primary focus color is `#0f62fe`.
- Hover must never be the only way to discover essential information.
- Avoid animations that delay navigation or reading.
- Respect `prefers-reduced-motion`.

Motion, when used, should explain state change rather than decorate the page.

## 11. Responsive behavior

Use content-driven breakpoints. Carbon's approximate thresholds are a useful starting point:

- mobile: 320px+
- tablet: 672px+
- desktop: 1056px+
- large desktop: 1312px+
- max grid: 1584px

Rules:

- Do not simply shrink desktop composition.
- Article prose remains readable before sidebars are preserved.
- Sidebars / TOCs may collapse inline or behind a disclosure.
- Multi-column indexes collapse toward one column.
- Technical figures may scroll horizontally when reduction would destroy legibility.
- Display type scales with `clamp()`; do not hard-code 76px headings on phones.

## 12. Accessibility

Target WCAG 2.2 AA.

Every implementation must preserve:

- semantic heading order;
- keyboard access;
- visible focus;
- sufficient color contrast;
- labels for controls;
- alt text for meaningful images;
- reduced-motion preferences;
- reasonable zoom and text reflow;
- no interaction that requires a pointing device.

Accessibility is part of the design system, not a later audit.

## 13. Do / don't

### Do

- use IBM Plex as the visual anchor;
- use light-weight large headings;
- use a 4px spatial rhythm;
- keep corners square;
- use blue with restraint;
- use hairlines and surface changes instead of shadows;
- make prose width a deliberate design constraint;
- let figures and code expand when they need room;
- keep navigation quieter than the writing.

### Don't

- turn the site into an IBM clone;
- use IBM logos or imply IBM affiliation;
- add rounded SaaS cards;
- use pill-shaped CTAs;
- add glassmorphism, decorative blur, or ambient glow;
- use multiple decorative accent colors;
- bold every heading;
- add animation for atmosphere;
- add JavaScript where HTML and CSS solve the problem;
- sacrifice reading quality to preserve a grid.

## 14. Decision order

When design rules conflict, decide in this order:

1. accessibility;
2. reading comprehension;
3. semantic structure;
4. consistency with this document;
5. visual resemblance to the reference system.

The site exists to carry ideas. The design exists to make those ideas easier to encounter.
