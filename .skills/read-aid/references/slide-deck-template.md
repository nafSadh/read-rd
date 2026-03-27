# Slide-Deck HTML Template — Literal Reference

This is the **exact** HTML/CSS/JS template to use when producing slide-deck format output.
Do NOT rename CSS variables, restructure the nav bar, or reinterpret any part of this template.
Copy these code blocks verbatim into your output, then fill in your own slide content.

---

## Complete HTML skeleton

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>YOUR TITLE HERE</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=IBM+Plex+Mono:wght@300;400;500;600&family=Source+Sans+3:wght@300;400;600;700&display=swap');

/* ---- THEME: LIGHT (default) ---- */
:root, [data-theme="light"] {
  --bg: #faf8f5;
  --bg-shell: #eae7e0;
  --fg: #1a1a1a;
  --dim: #6e6b64;
  --mute: #b0ada5;
  --accent: #5b5bd6;
  --accent2: #0ea5e9;
  --accent3: #7c3aed;
  --accent4: #a78bfa;
  --yellow: #0d9488;
  --card: rgba(0,0,0,0.025);
  --border: rgba(0,0,0,0.08);
  --code-bg: rgba(0,0,0,0.04);
  --eq-bg: rgba(0,0,0,0.025);
  --key-bg: linear-gradient(135deg, rgba(91,91,214,0.06), rgba(124,58,237,0.04));
  --key-border: rgba(91,91,214,0.12);
  --nav-hover-bg: rgba(91,91,214,0.04);
  --title-bg: linear-gradient(165deg, #faf8f5 0%, #f0ece4 100%);
  --shadow: 0 2px 24px rgba(0,0,0,0.08), 0 0 0 1px var(--border);
  /* SVG fills — light */
  --svg-accent-fill: rgba(91,91,214,0.08);
  --svg-accent2-fill: rgba(14,165,233,0.08);
  --svg-accent3-fill: rgba(124,58,237,0.08);
  --svg-accent4-fill: rgba(167,139,250,0.08);
  --svg-yellow-fill: rgba(13,148,136,0.08);
  --svg-subtle: rgba(0,0,0,0.04);
  --svg-info-bg: rgba(0,0,0,0.02);
  --svg-info-border: rgba(0,0,0,0.06);
}

/* ---- THEME: DARK ---- */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #17171c;
    --bg-shell: #0e0e12;
    --fg: #e4e2dc;
    --dim: #9b978e;
    --mute: #5e5b54;
    --accent: #818cf8;
    --accent2: #38bdf8;
    --accent3: #a78bfa;
    --accent4: #c4b5fd;
    --yellow: #34d399;
    --card: rgba(255,255,255,0.03);
    --border: rgba(255,255,255,0.08);
    --code-bg: rgba(255,255,255,0.06);
    --eq-bg: rgba(255,255,255,0.04);
    --key-bg: linear-gradient(135deg, rgba(129,140,248,0.08), rgba(91,155,213,0.06));
    --key-border: rgba(129,140,248,0.18);
    --nav-hover-bg: rgba(129,140,248,0.08);
    --title-bg: linear-gradient(165deg, #17171c 0%, #1c1c24 100%);
    --shadow: 0 2px 24px rgba(0,0,0,0.3), 0 0 0 1px var(--border);
    --svg-accent-fill: rgba(129,140,248,0.12);
    --svg-accent2-fill: rgba(78,205,196,0.12);
    --svg-accent3-fill: rgba(91,155,213,0.12);
    --svg-accent4-fill: rgba(176,124,232,0.12);
    --svg-yellow-fill: rgba(232,192,68,0.1);
    --svg-subtle: rgba(255,255,255,0.05);
    --svg-info-bg: rgba(255,255,255,0.03);
    --svg-info-border: rgba(255,255,255,0.06);
  }
}

[data-theme="dark"] {
  --bg: #17171c;
  --bg-shell: #0e0e12;
  --fg: #e4e2dc;
  --dim: #9b978e;
  --mute: #5e5b54;
  --accent: #818cf8;
  --accent2: #38bdf8;
  --accent3: #a78bfa;
  --accent4: #c4b5fd;
  --yellow: #34d399;
  --card: rgba(255,255,255,0.03);
  --border: rgba(255,255,255,0.08);
  --code-bg: rgba(255,255,255,0.06);
  --eq-bg: rgba(255,255,255,0.04);
  --key-bg: linear-gradient(135deg, rgba(129,140,248,0.08), rgba(91,155,213,0.06));
  --key-border: rgba(129,140,248,0.18);
  --nav-hover-bg: rgba(129,140,248,0.08);
  --title-bg: linear-gradient(165deg, #17171c 0%, #1c1c24 100%);
  --shadow: 0 2px 24px rgba(0,0,0,0.3), 0 0 0 1px var(--border);
  --svg-accent-fill: rgba(129,140,248,0.12);
  --svg-accent2-fill: rgba(78,205,196,0.12);
  --svg-accent3-fill: rgba(91,155,213,0.12);
  --svg-accent4-fill: rgba(176,124,232,0.12);
  --svg-yellow-fill: rgba(232,192,68,0.1);
  --svg-subtle: rgba(255,255,255,0.05);
  --svg-info-bg: rgba(255,255,255,0.03);
  --svg-info-border: rgba(255,255,255,0.06);
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  background: var(--bg);
  font-family: 'Source Sans 3', sans-serif;
  color: var(--fg);
  width: 100vw;
  height: 100dvh;
  overflow: hidden;
  transition: background 0.3s ease, color 0.3s ease;
}

/* Only prevent selection on nav controls, not slide content */
.nav-bar { user-select: none; }
.slide-header { user-select: none; }

/* ---- SLIDE CONTAINER ---- */
.deck {
  position: absolute;
  inset: 0;
}

.slide {
  position: absolute;
  inset: 0;
  background: var(--bg);
  border-radius: 0;
  box-shadow: none;
  padding: clamp(1.5rem, 4vh, 3.5rem) clamp(1.5rem, 5vw, 6rem);
  padding-bottom: clamp(2.5rem, 5vh, 4rem);
  display: none;
  flex-direction: column;
  overflow: hidden auto;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: thin;
  scrollbar-color: rgba(91,99,245,0.15) transparent;
  transition: background 0.3s ease;
}

.slide.active {
  display: flex;
  animation: slideIn 0.35s ease;
}

@keyframes slideIn {
  from { opacity: 0; transform: translateX(20px); }
  to { opacity: 1; transform: translateX(0); }
}

/* ---- SLIDE LAYOUT ---- */
.slide-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: clamp(0.3rem, 0.8vh, 0.6rem);
  flex-shrink: 0;
}

.slide-chapter {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.68rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
}

.slide-num {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.68rem;
  color: var(--mute);
}

.slide h1 {
  font-family: 'Crimson Pro', serif;
  font-size: clamp(1.5rem, 3.2vw, 2.5rem);
  font-weight: 700;
  line-height: 1.15;
  color: var(--fg);
  margin-bottom: clamp(0.15rem, 0.5vh, 0.3rem);
  flex-shrink: 0;
}

.slide h1 em {
  font-weight: 400;
  color: var(--accent);
}

.slide h2 {
  font-family: 'Crimson Pro', serif;
  font-size: clamp(1.15rem, 2.6vw, 1.85rem);
  font-weight: 600;
  color: var(--fg);
  margin-bottom: clamp(0.1rem, 0.4vh, 0.2rem);
  flex-shrink: 0;
}

.slide .subtitle {
  font-family: 'Crimson Pro', serif;
  font-size: clamp(0.92rem, 1.3vw, 1.15rem);
  font-style: italic;
  color: var(--dim);
  margin-bottom: clamp(0.6rem, 1.5vh, 1.2rem);
  flex-shrink: 0;
}

.slide-body {
  flex: 1;
  display: flex;
  gap: clamp(1.5rem, 3vw, 3.5rem);
  min-height: 0;
}

.slide-body.col-1 {
  flex-direction: column;
  justify-content: center;
}

.slide-body.col-2 {
  flex-direction: row;
  align-items: stretch;
}

.text-col {
  flex: 1.15;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(0.5rem, 1.2vh, 0.9rem);
  min-width: 0;
  padding-right: clamp(0rem, 1vw, 1rem);
}

/* Subtle divider between text and SVG columns */
.slide-body.col-2 .text-col {
  border-right: 1px solid var(--border);
  margin-right: 0;
}

.svg-col {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 0;
  padding: clamp(0rem, 0.5vw, 0.5rem);
}

.svg-col svg {
  width: 100%;
  height: auto;
  max-height: 100%;
}

.slide-body.col-1 .svg-col {
  flex: 1;
}

/* ---- TEXT ELEMENTS ---- */
.point {
  font-size: clamp(0.88rem, 1.3vw, 1.15rem);
  line-height: 1.6;
  color: var(--dim);
}

.point strong {
  color: var(--fg);
  font-weight: 600;
}

.point code {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.88em;
  background: var(--code-bg);
  padding: 0.12em 0.4em;
  border-radius: 3px;
  color: var(--accent2);
}

.eq-box {
  background: var(--eq-bg);
  border-left: 3px solid var(--accent);
  padding: clamp(0.6rem, 1vh, 0.85rem) clamp(0.8rem, 1.2vw, 1.2rem);
  border-radius: 0 6px 6px 0;
  font-family: 'IBM Plex Mono', monospace;
  font-size: clamp(0.82rem, 1.15vw, 1.05rem);
  color: var(--fg);
  line-height: 1.7;
  margin: clamp(0.1rem, 0.3vh, 0.2rem) 0;
}

.eq-box .label {
  font-family: 'Source Sans 3', sans-serif;
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--accent);
  display: block;
  margin-bottom: 0.2rem;
}

.note {
  font-family: 'Crimson Pro', serif;
  font-size: clamp(0.82rem, 1.1vw, 1.02rem);
  font-style: italic;
  color: var(--mute);
  border-top: 1px solid var(--border);
  padding-top: clamp(0.4rem, 0.8vh, 0.7rem);
  margin-top: auto;
}

.key-idea {
  background: var(--key-bg);
  border: 1px solid var(--key-border);
  border-radius: 8px;
  padding: clamp(0.6rem, 1.2vh, 1rem) clamp(0.8rem, 1.2vw, 1.2rem);
  margin: clamp(0.1rem, 0.4vh, 0.25rem) 0;
}

.key-idea .kicker {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.65rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 0.25rem;
}

.key-idea p {
  font-family: 'Crimson Pro', serif;
  font-size: clamp(0.9rem, 1.2vw, 1.15rem);
  color: var(--fg);
  line-height: 1.55;
}

/* Constrain content width on ultrawide screens — skip title & divider slides */
.slide:not(.title-slide):not(.section-divider) > .slide-header,
.slide:not(.title-slide):not(.section-divider) > h1,
.slide:not(.title-slide):not(.section-divider) > h2,
.slide:not(.title-slide):not(.section-divider) > .subtitle,
.slide:not(.title-slide):not(.section-divider) > .slide-body {
  max-width: 1400px;
  width: 100%;
  margin-left: auto;
  margin-right: auto;
}

/* ---- TITLE SLIDE ---- */
.title-slide {
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: clamp(2rem, 6vh, 5rem) clamp(2rem, 6vw, 8rem);
  background: var(--title-bg);
}

.title-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0;
  max-width: 800px;
}

.title-slide h1 {
  font-size: clamp(2rem, 5vw, 3.5rem);
  margin-bottom: 0.6rem;
}

.title-slide .meta {
  font-family: 'IBM Plex Mono', monospace;
  font-size: clamp(0.65rem, 0.9vw, 0.82rem);
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--dim);
  margin-top: clamp(1rem, 2.5vh, 2rem);
}

.title-slide .ref {
  font-family: 'Crimson Pro', serif;
  font-size: clamp(0.9rem, 1.3vw, 1.15rem);
  font-style: italic;
  color: var(--mute);
  margin-top: 0.4rem;
}

/* ---- TOC ---- */
.toc-list {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: clamp(0.25rem, 0.6vh, 0.5rem) clamp(1.5rem, 3vw, 3rem);
  list-style: none;
}

.toc-list li {
  font-size: clamp(0.82rem, 1.1vw, 1.02rem);
  color: var(--dim);
  padding: clamp(0.25rem, 0.5vh, 0.45rem) 0;
  border-bottom: 1px solid var(--border);
  display: flex;
  gap: 0.6rem;
  align-items: baseline;
}

.toc-list .toc-num {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.82rem;
  color: var(--accent);
  min-width: 2rem;
  flex-shrink: 0;
}

/* ---- SECTION DIVIDER ---- */
/* Light mode: warm accent background */
.section-divider {
  justify-content: center;
  align-items: flex-start;
  padding: clamp(2.5rem, 6vh, 5rem) clamp(2rem, 6vw, 8rem);
  background: linear-gradient(165deg, #f7f0ea 0%, #f0e8df 100%);
}

.section-divider .slide-chapter { color: var(--accent); opacity: 0.9; }
.section-divider .slide-num { color: var(--mute); }

.section-divider h1 {
  color: var(--fg);
  font-size: clamp(1.6rem, 4vw, 3rem);
  margin-top: clamp(1.5rem, 5vh, 4rem);
  margin-bottom: clamp(0.5rem, 1.5vh, 1rem);
}

.section-divider .subtitle {
  color: var(--dim);
  font-size: clamp(0.9rem, 1.3vw, 1.2rem);
}

.section-divider .section-num-big {
  font-family: 'Crimson Pro', serif;
  font-size: clamp(3rem, 10vw, 8rem);
  font-weight: 300;
  color: rgba(91,91,214,0.06);
  position: absolute;
  right: clamp(1rem, 3vw, 3rem);
  bottom: clamp(0.5rem, 2vw, 2rem);
  line-height: 1;
}

/* Dark mode: deeper accent-tinted background */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) .section-divider {
    background: linear-gradient(165deg, #2a1518 0%, #1e1215 60%, #241820 100%);
  }
  :root:not([data-theme="light"]) .section-divider h1 { color: #f5f0ec; }
  :root:not([data-theme="light"]) .section-divider .subtitle { color: rgba(245,240,236,0.45); }
  :root:not([data-theme="light"]) .section-divider .slide-num { color: rgba(255,255,255,0.3); }
  :root:not([data-theme="light"]) .section-divider .section-num-big { color: rgba(129,140,248,0.1); }
}
[data-theme="dark"] .section-divider {
  background: linear-gradient(165deg, #2a1518 0%, #1e1215 60%, #241820 100%);
}
[data-theme="dark"] .section-divider h1 { color: #f5f0ec; }
[data-theme="dark"] .section-divider .subtitle { color: rgba(245,240,236,0.45); }
[data-theme="dark"] .section-divider .slide-num { color: rgba(255,255,255,0.3); }
[data-theme="dark"] .section-divider .section-num-big { color: rgba(129,140,248,0.1); }

/* ---- NAVIGATION (overlay at viewport bottom) ---- */
.nav-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.6rem clamp(1rem, 3vw, 3rem) 0.4rem;
  height: auto;
  z-index: 10;
  opacity: 0;
  transition: opacity 0.3s ease;
  pointer-events: none;
  background: linear-gradient(to bottom, transparent 0%, var(--bg) 60%);
}

.nav-bar:hover, .nav-bar:focus-within, .nav-bar.visible {
  opacity: 1;
}

.nav-bar > * { pointer-events: auto; }

.nav-btn {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  border: 1px solid var(--border);
  background: var(--bg);
  color: var(--dim);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.65rem;
  transition: all 0.2s;
  flex-shrink: 0;
  padding: 0;
  line-height: 1;
}

.nav-btn:hover {
  border-color: var(--accent);
  color: var(--accent);
  background: var(--nav-hover-bg);
}

.progress-track {
  flex: 1;
  height: 2px;
  background: var(--border);
  border-radius: 1px;
  position: relative;
  overflow: hidden;
  min-width: 20px;
}

.progress-fill {
  position: absolute;
  left: 0;
  top: 0;
  height: 100%;
  background: var(--accent);
  border-radius: 1px;
  transition: width 0.35s ease;
}

.slide-counter {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.55rem;
  color: var(--mute);
  white-space: nowrap;
  min-width: 0;
}

/* Theme toggle */
.theme-btn {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  border: 1px solid var(--border);
  background: var(--bg);
  color: var(--dim);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.7rem;
  transition: all 0.2s;
  flex-shrink: 0;
  padding: 0;
  line-height: 1;
}
.theme-btn:hover {
  border-color: var(--yellow);
  color: var(--yellow);
}

/* SVG Styling */
.fig { overflow: visible; } /* prevent viewBox clipping on edges */
.fig text { font-family: 'IBM Plex Mono', monospace; }
.fig .label-text { font-family: 'Source Sans 3', sans-serif; }
/* Center text vertically in boxes when text-anchor is middle */
.fig .box-label { dominant-baseline: central; }

/* Dark mode SVG overrides — remap hardcoded fills/strokes */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) .fig text[fill="#1a1a1a"] { fill: #e4e2dc; }
  :root:not([data-theme="light"]) .fig text[fill="#6e6b64"],
  :root:not([data-theme="light"]) .fig text[fill="#b0ada5"] { fill: #9b978e; }
  :root:not([data-theme="light"]) .fig line[stroke="#6e6b64"],
  :root:not([data-theme="light"]) .fig path[stroke="#6e6b64"] { stroke: #6e6b64; }
  :root:not([data-theme="light"]) .fig rect[stroke="#6e6b64"] { stroke: #5e5b54; }
  :root:not([data-theme="light"]) .fig rect[stroke="#b0ada5"] { stroke: #5e5b54; }
  :root:not([data-theme="light"]) .fig rect[fill="rgba(0,0,0,0.04)"],
  :root:not([data-theme="light"]) .fig rect[fill="rgba(0,0,0,0.03)"] { fill: rgba(255,255,255,0.06); }
  :root:not([data-theme="light"]) .fig rect[fill="rgba(0,0,0,0.02)"] { fill: rgba(255,255,255,0.04); }
  :root:not([data-theme="light"]) .fig rect[fill="rgba(0,0,0,0.025)"] { fill: rgba(255,255,255,0.04); }
  :root:not([data-theme="light"]) .fig rect[fill="rgba(0,0,0,0.015)"] { fill: rgba(255,255,255,0.03); }
  :root:not([data-theme="light"]) .fig rect[fill="#f0ece4"] { fill: rgba(255,255,255,0.06); }
  /* accent colors shift slightly brighter in dark */
  :root:not([data-theme="light"]) .fig text[fill="#5b5bd6"] { fill: #818cf8; }
  :root:not([data-theme="light"]) .fig text[fill="#0ea5e9"] { fill: #38bdf8; }
  :root:not([data-theme="light"]) .fig text[fill="#7c3aed"] { fill: #a78bfa; }
  :root:not([data-theme="light"]) .fig text[fill="#a78bfa"] { fill: #c4b5fd; }
  :root:not([data-theme="light"]) .fig text[fill="#0d9488"] { fill: #34d399; }
  :root:not([data-theme="light"]) .fig rect[stroke="#5b5bd6"] { stroke: #818cf8; }
  :root:not([data-theme="light"]) .fig rect[stroke="#0ea5e9"] { stroke: #38bdf8; }
  :root:not([data-theme="light"]) .fig rect[stroke="#7c3aed"] { stroke: #a78bfa; }
  :root:not([data-theme="light"]) .fig rect[stroke="#a78bfa"] { stroke: #c4b5fd; }
  :root:not([data-theme="light"]) .fig rect[stroke="#0d9488"] { stroke: #34d399; }
  :root:not([data-theme="light"]) .fig line[stroke="#5b5bd6"] { stroke: #818cf8; }
  :root:not([data-theme="light"]) .fig path[stroke="#5b5bd6"] { stroke: #818cf8; }
  :root:not([data-theme="light"]) .fig path[stroke="#0d9488"] { stroke: #34d399; }
  :root:not([data-theme="light"]) .fig circle[fill="#5b5bd6"] { fill: #818cf8; }
  :root:not([data-theme="light"]) .fig circle[fill="#0ea5e9"] { fill: #38bdf8; }
  :root:not([data-theme="light"]) .fig circle[fill="#7c3aed"] { fill: #a78bfa; }
}
[data-theme="dark"] .fig text[fill="#1a1a1a"] { fill: #e4e2dc; }
[data-theme="dark"] .fig text[fill="#6e6b64"],
[data-theme="dark"] .fig text[fill="#b0ada5"] { fill: #9b978e; }
[data-theme="dark"] .fig line[stroke="#6e6b64"],
[data-theme="dark"] .fig path[stroke="#6e6b64"] { stroke: #6e6b64; }
[data-theme="dark"] .fig rect[stroke="#6e6b64"] { stroke: #5e5b54; }
[data-theme="dark"] .fig rect[stroke="#b0ada5"] { stroke: #5e5b54; }
[data-theme="dark"] .fig rect[fill="rgba(0,0,0,0.04)"],
[data-theme="dark"] .fig rect[fill="rgba(0,0,0,0.03)"] { fill: rgba(255,255,255,0.06); }
[data-theme="dark"] .fig rect[fill="rgba(0,0,0,0.02)"] { fill: rgba(255,255,255,0.04); }
[data-theme="dark"] .fig rect[fill="rgba(0,0,0,0.025)"] { fill: rgba(255,255,255,0.04); }
[data-theme="dark"] .fig rect[fill="rgba(0,0,0,0.015)"] { fill: rgba(255,255,255,0.03); }
[data-theme="dark"] .fig rect[fill="#f0ece4"] { fill: rgba(255,255,255,0.06); }
[data-theme="dark"] .fig text[fill="#5b5bd6"] { fill: #818cf8; }
[data-theme="dark"] .fig text[fill="#0ea5e9"] { fill: #38bdf8; }
[data-theme="dark"] .fig text[fill="#7c3aed"] { fill: #a78bfa; }
[data-theme="dark"] .fig text[fill="#a78bfa"] { fill: #c4b5fd; }
[data-theme="dark"] .fig text[fill="#0d9488"] { fill: #34d399; }
[data-theme="dark"] .fig rect[stroke="#5b5bd6"] { stroke: #818cf8; }
[data-theme="dark"] .fig rect[stroke="#0ea5e9"] { stroke: #38bdf8; }
[data-theme="dark"] .fig rect[stroke="#7c3aed"] { stroke: #a78bfa; }
[data-theme="dark"] .fig rect[stroke="#a78bfa"] { stroke: #c4b5fd; }
[data-theme="dark"] .fig rect[stroke="#0d9488"] { stroke: #34d399; }
[data-theme="dark"] .fig line[stroke="#5b5bd6"] { stroke: #818cf8; }
[data-theme="dark"] .fig path[stroke="#5b5bd6"] { stroke: #818cf8; }
[data-theme="dark"] .fig path[stroke="#0d9488"] { stroke: #34d399; }
[data-theme="dark"] .fig circle[fill="#5b5bd6"] { fill: #818cf8; }
[data-theme="dark"] .fig circle[fill="#0ea5e9"] { fill: #38bdf8; }
[data-theme="dark"] .fig circle[fill="#7c3aed"] { fill: #a78bfa; }

/* ---- RESPONSIVE ---- */

/* Tablet */
@media (max-width: 900px) {
  .slide-body.col-2 .text-col { border-right: none; padding-right: 0; }
  .toc-list { gap: 0.2rem 1.2rem; }
}

/* Phone */
@media (max-width: 600px) {
  .slide {
    padding: 1rem 1.2rem;
    padding-bottom: 2.2rem;
  }

  .slide .subtitle { margin-bottom: 0.5rem; }

  .slide-body.col-2 {
    flex-direction: column;
    gap: 0.8rem;
  }

  .slide-body.col-2 .text-col {
    border-right: none;
    padding-right: 0;
    border-bottom: 1px solid var(--border);
    padding-bottom: 0.6rem;
  }

  .text-col { gap: 0.4rem; }
  .svg-col { max-height: 38vh; }

  .toc-list { grid-template-columns: 1fr; }

  .nav-bar { padding: 0.3rem 0.8rem; }
  .nav-btn, .theme-btn { width: 20px; height: 20px; font-size: 0.6rem; }
  .slide-counter { font-size: 0.5rem; }
}

/* Landscape phones */
@media (max-height: 500px) {
  .slide { padding: 0.6rem 1.5rem 1.8rem; }
  .text-col { gap: 0.3rem; }
  .nav-bar { padding: 0.15rem 0.5rem; }
  .nav-btn, .theme-btn { width: 18px; height: 18px; font-size: 0.55rem; }
}

/* Animations for SVG */
@keyframes dashFlow {
  to { stroke-dashoffset: -16; }
}
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}
@keyframes pulse2 {
  0%, 100% { opacity: 0.4; }
  50% { opacity: 1; }
}
@keyframes attGlow {
  0%, 100% { r: 3; opacity: 0.3; }
  50% { r: 5; opacity: 0.9; }
}

.dash-flow {
  stroke-dasharray: 6 4;
  animation: dashFlow 0.8s linear infinite;
}

.pulse-anim {
  animation: pulse2 2s ease-in-out infinite;
}
</style>
</head>
<body>

<div class="deck" id="deck">

<!-- ===================== SLIDE 0: TITLE ===================== -->
<div class="slide title-slide active" data-n="0">
  <svg width="120" height="6" viewBox="0 0 120 6" style="margin-bottom:1.5rem;flex-shrink:0;">
    <rect width="50" height="6" rx="3" fill="#5b63f5"/>
    <rect x="54" width="30" height="6" rx="3" fill="#0e8fd0"/>
    <rect x="88" width="32" height="6" rx="3" fill="#14966e"/>
  </svg>
  <h1>YOUR TITLE with <em>emphasis</em></h1>
  <div class="ref">Subtitle line 1</div>
  <div class="ref">Subtitle line 2</div>
  <div class="meta">Arrow keys / click / swipe · ◐ for dark mode</div>
</div>

<!-- ===================== SLIDE N: SECTION DIVIDER ===================== -->
<div class="slide section-divider" data-n="N">
  <div class="slide-header">
    <span class="slide-chapter">CHAPTER NAME</span>
    <span class="slide-num">N</span>
  </div>
  <h1>Section Title</h1>
  <div class="subtitle">Brief description of what this section covers</div>
  <div class="section-num-big">01</div>
</div>

<!-- ===================== SLIDE N: CONTENT (TWO-COLUMN) ===================== -->
<div class="slide" data-n="N">
  <div class="slide-header">
    <span class="slide-chapter">CHAPTER NAME</span>
    <span class="slide-num">N</span>
  </div>
  <h2>Slide Title</h2>
  <div class="subtitle">Optional subtitle</div>
  <div class="slide-body col-2">
    <div class="text-col">
      <p class="point">Text content with <strong>bold</strong> and <code>code</code>.</p>
      <div class="eq-box">
        <span class="label">Equation Name</span>
        equation content here
      </div>
      <div class="key-idea">
        <div class="kicker">Key Idea</div>
        <p>Important takeaway in Crimson Pro serif.</p>
      </div>
      <p class="note">Footnote or aside in italic.</p>
    </div>
    <div class="svg-col">
      <svg viewBox="0 0 300 300" class="fig" xmlns="http://www.w3.org/2000/svg">
        <!-- YOUR SVG DIAGRAM HERE -->
      </svg>
    </div>
  </div>
</div>

<!-- ===================== SLIDE N: CONTENT (SINGLE-COLUMN) ===================== -->
<div class="slide" data-n="N">
  <div class="slide-header">
    <span class="slide-chapter">CHAPTER NAME</span>
    <span class="slide-num">N</span>
  </div>
  <h2>Slide Title</h2>
  <div class="slide-body col-1">
    <div class="text-col">
      <p class="point">Content here.</p>
    </div>
    <div class="svg-col">
      <svg viewBox="0 0 600 300" class="fig" xmlns="http://www.w3.org/2000/svg">
        <!-- FULL-WIDTH SVG DIAGRAM -->
      </svg>
    </div>
  </div>
</div>

</div><!-- /deck -->

<!-- NAVIGATION (fixed overlay, auto-hiding) -->
<div class="nav-bar" id="navBar">
  <button class="nav-btn" id="prevBtn" aria-label="Previous slide">←</button>
  <div class="progress-track">
    <div class="progress-fill" id="progressFill"></div>
  </div>
  <span class="slide-counter" id="slideCounter">1 / N</span>
  <button class="nav-btn" id="nextBtn" aria-label="Next slide">→</button>
  <button class="theme-btn" id="themeBtn" aria-label="Toggle theme" title="Toggle dark/light">◐</button>
</div>

<script>
const slides = document.querySelectorAll('.slide');
const total = slides.length;
const navBar = document.getElementById('navBar');
let current = 0;
let navTimeout;

function flashNav() {
  navBar.classList.add('visible');
  clearTimeout(navTimeout);
  navTimeout = setTimeout(() => navBar.classList.remove('visible'), 2000);
}

function goTo(n) {
  if (n < 0 || n >= total) return;
  slides[current].classList.remove('active');
  current = n;
  slides[current].classList.add('active');
  document.getElementById('progressFill').style.width = ((current / (total - 1)) * 100) + '%';
  document.getElementById('slideCounter').textContent = (current + 1) + ' / ' + total;
  flashNav();
}

// Show nav when mouse near bottom
document.addEventListener('mousemove', e => {
  if (e.clientY > window.innerHeight - 60) {
    navBar.classList.add('visible');
    clearTimeout(navTimeout);
    navTimeout = setTimeout(() => navBar.classList.remove('visible'), 2500);
  }
});

document.getElementById('prevBtn').addEventListener('click', () => goTo(current - 1));
document.getElementById('nextBtn').addEventListener('click', () => goTo(current + 1));

document.addEventListener('keydown', e => {
  if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); goTo(current + 1); }
  if (e.key === 'ArrowLeft') { e.preventDefault(); goTo(current - 1); }
  if (e.key === 'Home') goTo(0);
  if (e.key === 'End') goTo(total - 1);
});

// Click left/right halves of deck to navigate
document.getElementById('deck').addEventListener('click', e => {
  if (e.target.closest('.nav-bar, button, a')) return;
  const rect = e.currentTarget.getBoundingClientRect();
  const x = e.clientX - rect.left;
  if (x < rect.width * 0.35) goTo(current - 1);
  else if (x > rect.width * 0.65) goTo(current + 1);
});

// Touch swipe support
let touchStartX = 0;
document.addEventListener('touchstart', e => { touchStartX = e.touches[0].clientX; }, {passive: true});
document.addEventListener('touchend', e => {
  const dx = e.changedTouches[0].clientX - touchStartX;
  if (dx < -40) goTo(current + 1);
  if (dx > 40) goTo(current - 1);
});

// Theme toggle
const themeBtn = document.getElementById('themeBtn');
const root = document.documentElement;

function getSystemTheme() {
  return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
}

function applyTheme(theme) {
  if (theme === 'system') {
    root.removeAttribute('data-theme');
    themeBtn.textContent = '◐';
    themeBtn.title = 'Using system theme — click to toggle';
  } else {
    root.setAttribute('data-theme', theme);
    themeBtn.textContent = theme === 'dark' ? '☀' : '☽';
    themeBtn.title = theme === 'dark' ? 'Switch to light' : 'Switch to dark';
  }
}

let themeState = 'system';
themeBtn.addEventListener('click', () => {
  const sys = getSystemTheme();
  if (themeState === 'system') {
    themeState = sys === 'dark' ? 'light' : 'dark';
  } else if (themeState === 'dark') {
    themeState = 'light';
  } else {
    themeState = 'system';
  }
  applyTheme(themeState);
});

applyTheme('system');
goTo(0);
</script>

</body>
</html>
```

---

## Critical rules for using this template

1. **Copy the CSS verbatim.** Do not rename variables (use `--bg`, `--fg`, `--dim`, `--accent` etc., NOT `--bg-primary` or `--text-primary`).
2. **Copy the nav bar HTML verbatim.** The nav bar is auto-hiding (starts at `opacity: 0`), uses 22px circular buttons, has a 2px progress track, and a gradient background.
3. **Copy the JavaScript verbatim.** The `goTo()`, `flashNav()`, click-halves navigation, touch swipe, and three-state theme toggle must work exactly as shown.
4. **SVG dark mode**: Use per-element attribute selectors (e.g., `.fig text[fill="#1a1a1a"]`) to remap hardcoded colors in dark mode. Do NOT use blanket `fill: var(--svg-fill)` on all elements.
5. **Hardcode SVG colors**: Inside `<svg class="fig">`, use hardcoded hex values for fills and strokes (e.g., `fill="#5b5bd6"`). The CSS dark-mode overrides will remap them.
6. **Title slide**: Always include the decorative color bar SVG (`<svg width="120" height="6">` with three colored rects) and the `.meta` line with navigation instructions.
7. **Section dividers**: Use the warm gradient background (`linear-gradient(165deg, #f7f0ea 0%, #f0e8df 100%)`), the `.section-num-big` watermark number, and `h1` (not `h2`).
8. **Slide numbering**: Use `data-n="0"` on title, sequential integers on all other slides. Only slide 0 gets `class="slide title-slide active"`.
9. **Content slides**: Use `.slide-body.col-2` for text+SVG layouts, `.col-1` for stacked layouts. Text goes in `.text-col`, diagrams in `.svg-col`.
10. **Font roles**: Crimson Pro for headings and key-idea text, IBM Plex Mono for code/labels/equations/SVG text, Source Sans 3 for body text and UI.

## Slide type summary

| Type | Class | Key features |
|------|-------|--------------|
| Title | `.slide.title-slide` | Centered, color bar SVG, `h1`, `.ref` lines, `.meta` |
| Section divider | `.slide.section-divider` | Warm gradient bg, `h1`, `.subtitle`, `.section-num-big` watermark |
| Content (2-col) | `.slide` with `.slide-body.col-2` | `.text-col` + `.svg-col` side by side |
| Content (1-col) | `.slide` with `.slide-body.col-1` | Stacked text then SVG |

## Text element summary

| Element | Class | Usage |
|---------|-------|-------|
| Paragraph | `.point` | Main body text, uses `<strong>` and `<code>` |
| Equation box | `.eq-box` | Math/formulas, with `.label` span |
| Key idea | `.key-idea` | Highlighted callout with `.kicker` label |
| Note | `.note` | Italic footnote, pushed to bottom via `margin-top: auto` |
| Subtitle | `.subtitle` | Italic line under slide title |


---

## Gold-Standard Slide Examples

These are real slides from a polished output. Use these as a quality bar for your own content. Notice the SVG detail, the use of concrete values, the semantic color-coding, and how each slide teaches exactly one idea.

### Example: Title Slide

```html
<!-- ===================== SLIDE 0: TITLE ===================== -->
<div class="slide title-slide active" data-n="0">
  <svg width="120" height="6" viewBox="0 0 120 6" style="margin-bottom:1.5rem;flex-shrink:0;">
    <rect width="40" height="6" rx="3" fill="#5b63f5"/>
    <rect x="44" width="40" height="6" rx="3" fill="#0e8fd0"/>
    <rect x="88" width="32" height="6" rx="3" fill="#14966e"/>
  </svg>
  <h1><em>Attention</em> Is All You Need</h1>
  <div class="ref">Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin</div>
  <div class="ref">NeurIPS 2017 · The paper that started the Transformer era</div>
  <div class="meta">A ground-up refresher with worked examples · Arrow keys / click / swipe</div>
</div>
```

### Example: Section Divider

```html
<!-- ===================== SLIDE 6: SECTION DIVIDER ===================== -->
<div class="slide section-divider" data-n="6">
  <div class="slide-header">
    <span class="slide-chapter">§3.2</span>
    <span class="slide-num">6</span>
  </div>
  <h1>The Core Idea:<br>Attention</h1>
  <div class="subtitle">"An attention function maps a query and a set of key-value pairs to an output"</div>
  <div class="section-num-big">II</div>
</div>
```

### Example: Content Slide (col-2 with SVG)

```html
<!-- ===================== SLIDE 7: ATTENTION INTUITION ===================== -->
<div class="slide" data-n="7">
  <div class="slide-header">
    <span class="slide-chapter">§3.2 · Intuition</span>
    <span class="slide-num">7</span>
  </div>
  <h2>Attention = Soft Dictionary Lookup</h2>
  <div class="slide-body col-2">
    <div class="text-col">
      <p class="point">Imagine you're reading the word <strong>"it"</strong> in: <em>"The <strong>cat</strong> sat on the mat because <strong>it</strong> was tired."</em></p>
      <p class="point">To understand "it", you need to figure out what it refers to. You instinctively look back at earlier words and decide "cat" is the most relevant.</p>
      <p class="point">Attention does exactly this, mechanically:</p>
      <p class="point"><strong>Query (Q):</strong> "it" asks — "what am I looking for?"</p>
      <p class="point"><strong>Key (K):</strong> each earlier word advertises — "here's what I am"</p>
      <p class="point"><strong>Value (V):</strong> each earlier word offers — "here's my info if you pick me"</p>
      <p class="point">The dot product <code>Q·K</code> measures how well the query matches each key. High match → high attention weight → that word's value contributes more to the output.</p>
      <div class="key-idea">
        <div class="kicker">In plain terms</div>
        <p>Every token asks a question (Q). Every token posts an ad (K). If the question matches the ad, the information (V) flows.</p>
      </div>
    </div>
    <div class="svg-col">
      <svg viewBox="0 0 300 340" class="fig" xmlns="http://www.w3.org/2000/svg">
        <text x="150" y="15" text-anchor="middle" font-size="8" fill="#5b63f5" letter-spacing="0.08em">ATTENTION FROM "it"</text>
        <!-- Words -->
        <g transform="translate(20, 30)" font-size="11" class="label-text">
          <text x="0" y="0" fill="#9e9bac">The</text>
          <text x="0" y="28" fill="#5b63f5" font-weight="600">cat</text>
          <text x="0" y="56" fill="#9e9bac">sat</text>
          <text x="0" y="84" fill="#9e9bac">on</text>
          <text x="0" y="112" fill="#9e9bac">the</text>
          <text x="0" y="140" fill="#9e9bac">mat</text>
          <text x="0" y="168" fill="#9e9bac">because</text>
          <text x="0" y="196" fill="#0e8fd0" font-weight="600">it</text>
          <text x="0" y="224" fill="#9e9bac">was</text>
          <text x="0" y="252" fill="#9e9bac">tired</text>
        </g>
        <!-- Attention weights as bars -->
        <g transform="translate(80, 22)">
          <text x="100" y="-4" text-anchor="middle" font-size="7" fill="#5c5a6b" letter-spacing="0.05em">ATTENTION WEIGHT</text>
          <rect x="0" y="0" width="12" height="10" rx="1" fill="rgba(91,99,245,0.08)"/>
          <text x="20" y="9" font-size="7" fill="#9e9bac">0.03</text>
          <rect x="0" y="28" width="120" height="10" rx="1" fill="rgba(91,99,245,0.6)"/>
          <text x="128" y="37" font-size="8" fill="#5b63f5" font-weight="500">0.42</text>
          <rect x="0" y="56" width="30" height="10" rx="1" fill="rgba(91,99,245,0.12)"/>
          <text x="38" y="65" font-size="7" fill="#9e9bac">0.08</text>
          <rect x="0" y="84" width="8" height="10" rx="1" fill="rgba(91,99,245,0.06)"/>
          <text x="16" y="93" font-size="7" fill="#9e9bac">0.02</text>
          <rect x="0" y="112" width="10" height="10" rx="1" fill="rgba(91,99,245,0.08)"/>
          <text x="18" y="121" font-size="7" fill="#9e9bac">0.03</text>
          <rect x="0" y="140" width="45" height="10" rx="1" fill="rgba(91,99,245,0.15)"/>
          <text x="53" y="149" font-size="7" fill="#9e9bac">0.12</text>
          <rect x="0" y="168" width="20" height="10" rx="1" fill="rgba(91,99,245,0.1)"/>
          <text x="28" y="177" font-size="7" fill="#9e9bac">0.05</text>
          <rect x="0" y="196" width="80" height="10" rx="1" fill="rgba(14,143,208,0.4)"/>
          <text x="88" y="205" font-size="8" fill="#0e8fd0" font-weight="500">0.25</text>
        </g>
        <!-- Sum note -->
        <g transform="translate(20, 280)">
          <rect width="260" height="40" rx="6" fill="rgba(20,150,110,0.04)" stroke="rgba(20,150,110,0.1)" stroke-width="0.5"/>
          <text x="130" y="16" text-anchor="middle" font-size="8" fill="#14966e">Output for "it" = 0.42 × V("cat") + 0.25 × V("it")</text>
          <text x="130" y="30" text-anchor="middle" font-size="8" fill="#14966e">+ 0.12 × V("mat") + 0.08 × V("sat") + …</text>
        </g>
      </svg>
    </div>
  </div>
</div>
```
