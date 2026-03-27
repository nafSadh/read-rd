# Deep-Dive Template — Architecture Notes

> The canonical reference is **`deep-dive-reference.html`** — a working HTML file you can open in a browser. It contains the full CSS, JS, and 3 example sections demonstrating every component. **Copy the CSS and JS verbatim from that file.** This document explains the *why* behind the design decisions.

## Data-Driven Architecture

The template uses a JavaScript-driven approach — no hand-written DOM. You define three parallel arrays:

```js
const sections  = ["Section Title", ...];   // sidebar nav + section headings
const summaries = [`<html for main scroll>`, ...];  // center panel content
const details   = [`<html for detail panel>`, ...];  // right panel (opened by "read deep dive" links)
```

The JS builder constructs the entire shell (sidebar, main scroll, right panel, topbar, theme toggle) from these arrays. This means you only write content — never layout markup.

## Three-Panel Layout

- **Sidebar** (180px, collapses to 52px on mobile): Logo + nav links. Auto-highlights on scroll via `IntersectionObserver`.
- **Main scroll** (center): Section blocks with summary content. Each section is a `.section-block` with a subtle alternating background pattern on odd items.
- **Right detail panel** (50% width, slides in from right): Opened by clicking "read deep dive →" links. Has its own scroll context and close button.

## Theme System

Two themes toggled via `data-theme` on `<html>`:

- **Light ("Academic")**: Warm paper background (`#faf8f3`), cool slate-blue text (`#363b48`), blue accent (`#2e6ab4`). Book-like feel.
- **Dark ("Luxury Violet/Cyan")**: Deep navy background (`#0b0e18`), muted gray text (`#8490aa`), violet accent (`#9b7aed`), cyan secondary (`#4ee8d0`).

**Critical rule**: Themes differ ONLY in color variables. Typography, spacing, and layout are identical. This prevents reflow on toggle.

## Typography Stack

| Font | Role |
|------|------|
| **Jost** (sans) | Body text, headings, UI, nav — the primary typeface |
| **EB Garamond** (serif) | Italic accent text, select stylistic elements |
| **IBM Plex Mono** (mono) | Code, stats, labels, tags, timestamps |

## Available Components

All components are demonstrated in the reference HTML. Here's a quick index:

| Component | Class/Element | Use for |
|-----------|--------------|---------|
| Stat bar | `.s-stat` | Key metrics with labels |
| Feature grid | `.feat-grid` | 2-3 column feature cards |
| Verdict | `.verdict` | Pro/con comparison |
| Timeline | `.timeline` | Chronological events |
| Callout | `.callout` | Highlighted quotes or key points |
| Security box | `.security-box` | Warning/important info blocks |
| Diagram wrap | `.diagram-wrap` | SVG container with caption |
| Price grid | `.price-grid` | Comparison cards (not just pricing) |
| Chips | `.chips` | Tag-like labels |
| Styled list | `.s-list` | Pro/con or feature lists |
| Code block | `<pre>` | Code with monospace styling |
| Links | `a` | Theme-aware styled links (dotted underline, accent hover) |

## Link Styling

Links use theme-aware colors instead of browser defaults. Base links use `var(--dim)` with a dotted underline (50% transparent), transitioning to `var(--accent)` with a solid underline on hover. Inside `.section-block` and `.detail` panels, links use `var(--text)` as the base color with a subtle accent-tinted underline, ensuring they're readable in both themes without clashing with the palette. Uses `border-bottom` instead of `text-decoration` for finer visual control.

## SVG Dark Mode System

SVGs use **hardcoded hex fills** (not CSS variables). The dark theme remaps them via CSS attribute selectors:

```css
[data-theme="dark"] .fig rect[fill="#f0f0f0"] { fill: #1a1f2d; }
[data-theme="dark"] .fig text[fill="#1a1a1a"] { fill: #c8cdd8; }
```

This means: always use `class="fig"` on SVGs, and always hardcode fills. The CSS handles the rest.

## Mobile Behavior

- Sidebar collapses to icon-only (52px)
- Right detail panel becomes full-width overlay
- Section padding reduces from `40px 8px` to `28px 8px`
- Font sizes scale down slightly

## Checklist Before Delivery

- [ ] CSS and JS copied verbatim from reference HTML
- [ ] `← CHANGE` markers updated (hero badge, title, subtitle, sidebar logo)
- [ ] All SVGs use `class="fig"` and hardcoded hex fills
- [ ] Both themes look correct
- [ ] Mobile layout works
- [ ] Each section has both a summary and detail entry
