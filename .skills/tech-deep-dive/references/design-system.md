# Design System Reference

Complete CSS, HTML structure, and component library for asyng deep dive pages.

## Fonts (Google Fonts CDN)

```html
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=IBM+Plex+Mono:wght@300;400;500&family=Satoshi:wght@400;500;700;900&display=swap" rel="stylesheet">
```

- **Instrument Serif** (regular + italic): Hero headings only. Use `<em>` with accent color for the tool name.
- **Satoshi**: Body text, section headers, feature cards.
- **IBM Plex Mono**: Code, labels, badges, stats, timestamps, chips.

## CSS Variables

Set `--accent` per tool (see SKILL.md accent color table). All other variables are constant:

```css
:root {
  --bg: #08080c;        /* deepest background */
  --bg2: #0e0e14;       /* card/section background */
  --bg3: #14141e;       /* highlighted node background */
  --border: #1a1a2a;    /* default borders */
  --border-hi: #2a2a44; /* hover borders */
  --text: #b0b0c4;      /* body text */
  --dim: #5a5a72;       /* secondary text, labels */
  --bright: #eaeaf2;    /* headings, emphasized text */
  --accent: #5865F2;    /* CHANGE PER TOOL */
  --accent2: /* slightly lighter accent for code highlights */
  --accent-glow: /* accent at 12% opacity for badge backgrounds */
  --green: #3ba573;     /* pro/positive */
  --red: #d94848;       /* con/negative */
  --amber: #d4a030;     /* partial/warning */
  --serif: 'Instrument Serif', Georgia, serif;
  --sans: 'Satoshi', -apple-system, sans-serif;
  --mono: 'IBM Plex Mono', monospace;
}
```

## Film Grain Overlay

Applied via `body::after` with a fixed SVG noise pattern at very low opacity:

```css
body::after {
  content: '';
  position: fixed;
  top: 0; left: 0;
  width: 100%; height: 100%;
  pointer-events: none;
  opacity: 0.03;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  z-index: 9999;
}
```

## Page Structure

```html
<body>
<div class="wrap">             <!-- max-width: 960px, centered -->

  <div class="crumb">...</div> <!-- breadcrumb: asyng / research / landscape / {tool} -->

  <div class="hero">           <!-- hero section -->
    <div class="hero-badge">   <!-- pulsing dot + company + license badge -->
    <h1>Tool <em>Name</em></h1>
    <p class="hero-sub">       <!-- one paragraph hook -->
    <div class="hero-line">    <!-- vertical accent line on right edge -->
  </div>

  <div class="stats">          <!-- horizontal stats bar with key metrics -->
    <div class="stat">...</div>
  </div>

  <!-- Expandable sections (6-8 of these) -->
  <div class="section" id="s1">
    <div class="section-header" onclick="toggle('s1')">
      <h2><span class="num">01</span> Section Title</h2>
      <span class="arrow">→</span>
    </div>
    <div class="section-body">
      <!-- Deep content: paragraphs, feature grids, diagrams, code blocks, timelines -->
    </div>
  </div>

  <footer>...</footer>
</div>

<script>
function toggle(id) { document.getElementById(id).classList.toggle('open'); }
document.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => document.getElementById('s1').classList.add('open'), 600);
});
</script>
</body>
```

## Component Library

### Hero Badge (pulsing dot)
```html
<div class="hero-badge"><span class="dot"></span> Company · License Type</div>
```
The dot pulses via `animation: pulse 2s infinite` (opacity 1 → 0.3 → 1).

### Stats Bar
```html
<div class="stats">
  <div class="stat"><div class="stat-val">Value</div><div class="stat-lbl">Label</div></div>
  <!-- 4-6 stats, flex layout with 1px gap borders -->
</div>
```

### Expandable Section
```css
.section-body {
  max-height: 0;
  overflow: hidden;
  transition: max-height .5s cubic-bezier(.4,0,.2,1), padding .3s;
}
.section.open .section-body {
  max-height: 5000px;  /* large enough for any content */
  padding: 0 24px 28px;
}
```
Arrow rotates 90° on open with cubic-bezier transition.

### Feature Grid (2-column)
```html
<div class="feat-grid">
  <div class="feat"><h4>Feature Name</h4><p>Description with real detail.</p></div>
  <!-- repeat -->
</div>
```

### SVG Architecture Diagram
Key classes for SVG elements:
- `.node` — default box (fill: --bg2, stroke: --border)
- `.node-hi` — highlighted box (fill: --bg3, stroke: --accent)
- `.node-text` — label inside box (fill: --bright, 11px)
- `.node-sub` — sublabel (fill: --dim, 9px)
- `.edge` — connection line (stroke: --dim)
- `.edge-hi` — animated dashed line (stroke: --accent, stroke-dasharray: 6,3, animated)
- `.lbl` / `.lbl-hi` — floating labels outside boxes

Animated dashed lines:
```css
.edge-hi {
  stroke: var(--accent);
  stroke-width: 1.5;
  fill: none;
  stroke-dasharray: 6, 3;
  animation: dash 1s linear infinite;
}
@keyframes dash { to { stroke-dashoffset: -9; } }
```

Arrow marker definition (include once per SVG):
```svg
<defs>
  <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 z" fill="var(--accent)"/>
  </marker>
</defs>
```

### Timeline
```html
<div class="timeline">
  <div class="tl-item">
    <div class="tl-date">Month Year</div>
    <div class="tl-text">What happened. Be specific.</div>
  </div>
</div>
```
Left border with accent-colored dots at each item.

### Pro/Con Verdict
```html
<div class="verdict">
  <div class="v-col pro"><h4>STRENGTHS</h4><ul><li>Specific strength</li></ul></div>
  <div class="v-col con"><h4>WEAKNESSES</h4><ul><li>Specific weakness</li></ul></div>
</div>
```
Pro items get green ✓ prefix, con items get red ✗ prefix.

### asyng Relevance Box
```html
<div class="asyng-rel">
  <h4>Role: {Competitor|Component|Inspiration|Dev Tool}</h4>
  <p>Specific analysis of relationship to asyng.</p>
</div>
```
Left border in accent color, subtle background.

### Code Block
```html
<pre>actual code or config here
second line
third line</pre>
```

### Chip Row
```html
<div class="chips">
  <span class="chip">tag-name</span>
</div>
```

## Staggered Load Animations

Hero elements fade up with increasing delays:
```css
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(12px); }
  to { opacity: 1; transform: translateY(0); }
}

.crumb     { opacity: 0; animation: fadeUp .6s .1s forwards; }
.hero-badge { opacity: 0; animation: fadeUp .6s .2s forwards; }
.hero h1   { opacity: 0; animation: fadeUp .8s .3s forwards; }
.hero-sub  { opacity: 0; animation: fadeUp .6s .45s forwards; }
.stats     { opacity: 0; animation: fadeUp .6s .55s forwards; }
```

## Responsive Breakpoints

```css
@media (max-width: 700px) {
  .hero h1 { font-size: 40px; }
  .stats { flex-wrap: wrap; }
  .stat { flex: none; width: 50%; }
  .feat-grid, .verdict { grid-template-columns: 1fr; }
}
```

## Full CSS Template

Here is the complete CSS to copy into each page's `<style>` block. Only change `--accent`, `--accent2`, and `--accent-glow` per tool:

```css
:root{--bg:#08080c;--bg2:#0e0e14;--bg3:#14141e;--border:#1a1a2a;--border-hi:#2a2a44;--text:#b0b0c4;--dim:#5a5a72;--bright:#eaeaf2;--accent:#5865F2;--accent2:#7983f5;--accent-glow:#5865F220;--green:#3ba573;--red:#d94848;--amber:#d4a030;--serif:'Instrument Serif',Georgia,serif;--sans:'Satoshi',-apple-system,sans-serif;--mono:'IBM Plex Mono',monospace;}
*{margin:0;padding:0;box-sizing:border-box;}
body{background:var(--bg);color:var(--text);font-family:var(--sans);-webkit-font-smoothing:antialiased;overflow-x:hidden;}
body::after{content:'';position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;opacity:0.03;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");z-index:9999;}
.wrap{max-width:960px;margin:0 auto;padding:48px 28px 80px;}
.crumb{font-family:var(--mono);font-size:11px;color:var(--dim);margin-bottom:40px;letter-spacing:0.5px;opacity:0;animation:fadeUp .6s .1s forwards;}
.crumb a{color:var(--accent);text-decoration:none;}
.hero{margin-bottom:56px;position:relative;}
.hero-badge{display:inline-flex;align-items:center;gap:8px;font-family:var(--mono);font-size:11px;color:var(--accent);background:var(--accent-glow);border:1px solid color-mix(in srgb, var(--accent), transparent 70%);padding:4px 12px;border-radius:20px;margin-bottom:20px;opacity:0;animation:fadeUp .6s .2s forwards;}
.hero-badge .dot{width:6px;height:6px;background:var(--accent);border-radius:50%;animation:pulse 2s infinite;}
@keyframes pulse{0%,100%{opacity:1;}50%{opacity:0.3;}}
.hero h1{font-family:var(--serif);font-size:64px;font-weight:400;color:var(--bright);line-height:1.05;letter-spacing:-2px;margin-bottom:16px;opacity:0;animation:fadeUp .8s .3s forwards;}
.hero h1 em{font-style:italic;color:var(--accent);}
.hero-sub{font-size:17px;line-height:1.7;color:var(--dim);max-width:620px;opacity:0;animation:fadeUp .6s .45s forwards;}
.hero-line{position:absolute;top:0;right:-28px;width:1px;height:100%;background:linear-gradient(to bottom,transparent,var(--accent),transparent);opacity:0.15;}
.stats{display:flex;gap:1px;margin-bottom:56px;background:var(--border);border-radius:8px;overflow:hidden;opacity:0;animation:fadeUp .6s .55s forwards;}
.stat{flex:1;background:var(--bg2);padding:16px 20px;text-align:center;}
.stat-val{font-family:var(--mono);font-size:15px;color:var(--bright);font-weight:500;}
.stat-lbl{font-size:11px;color:var(--dim);margin-top:4px;}
.section{border:1px solid var(--border);border-radius:10px;margin-bottom:12px;overflow:hidden;transition:border-color .2s;}
.section:hover{border-color:var(--border-hi);}
.section.open{border-color:color-mix(in srgb, var(--accent), transparent 60%);}
.section-header{display:flex;align-items:center;justify-content:space-between;padding:20px 24px;cursor:pointer;user-select:none;transition:background .15s;}
.section-header:hover{background:var(--bg2);}
.section-header h2{font-family:var(--sans);font-size:16px;font-weight:700;color:var(--bright);display:flex;align-items:center;gap:10px;}
.section-header h2 .num{font-family:var(--mono);font-size:11px;color:var(--dim);font-weight:400;width:20px;}
.section-header .arrow{font-family:var(--mono);font-size:14px;color:var(--dim);transition:transform .3s cubic-bezier(.4,0,.2,1);}
.section.open .arrow{transform:rotate(90deg);color:var(--accent);}
.section-body{max-height:0;overflow:hidden;transition:max-height .5s cubic-bezier(.4,0,.2,1),padding .3s;}
.section.open .section-body{max-height:5000px;padding:0 24px 28px;}
.section-body p{font-size:14px;line-height:1.75;margin-bottom:14px;}
.section-body h3{font-size:14px;font-weight:700;color:var(--bright);margin:20px 0 8px;}
.section-body code{font-family:var(--mono);font-size:12px;background:#ffffff08;padding:2px 7px;border-radius:3px;color:var(--accent2);}
.section-body pre{background:var(--bg);border:1px solid var(--border);border-radius:6px;padding:16px;font-family:var(--mono);font-size:12px;line-height:1.7;overflow-x:auto;margin:14px 0;}
.feat-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:16px 0;}
.feat{background:var(--bg2);border:1px solid var(--border);border-radius:6px;padding:16px;transition:border-color .15s;}
.feat:hover{border-color:var(--border-hi);}
.feat h4{font-size:13px;font-weight:700;color:var(--bright);margin-bottom:6px;}
.feat p{font-size:12px;color:var(--dim);margin:0;line-height:1.6;}
.verdict{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:16px 0;}
.v-col h4{font-size:12px;font-family:var(--mono);letter-spacing:1px;margin-bottom:10px;}
.v-col.pro h4{color:var(--green);}.v-col.con h4{color:var(--red);}
.v-col ul{list-style:none;padding:0;}
.v-col li{font-size:13px;padding:5px 0 5px 16px;position:relative;line-height:1.5;}
.v-col.pro li::before{content:'✓';position:absolute;left:0;color:var(--green);font-size:11px;}
.v-col.con li::before{content:'✗';position:absolute;left:0;color:var(--red);font-size:11px;}
.diagram-wrap{margin:20px 0;padding:20px;background:var(--bg);border:1px solid var(--border);border-radius:8px;overflow-x:auto;}
.diagram-wrap svg{width:100%;height:auto;}
.diagram-wrap svg text{font-family:'IBM Plex Mono',monospace;}
.diagram-wrap svg .node{fill:var(--bg2);stroke:var(--border);stroke-width:1;}
.diagram-wrap svg .node-hi{fill:var(--bg3);stroke:var(--accent);stroke-width:1.5;}
.diagram-wrap svg .edge{stroke:var(--dim);stroke-width:1;fill:none;}
.diagram-wrap svg .edge-hi{stroke:var(--accent);stroke-width:1.5;fill:none;stroke-dasharray:6,3;animation:dash 1s linear infinite;}
@keyframes dash{to{stroke-dashoffset:-9;}}
.diagram-wrap svg .lbl{fill:var(--dim);font-size:10px;}
.diagram-wrap svg .lbl-hi{fill:var(--accent);font-size:10px;}
.diagram-wrap svg .node-text{fill:var(--bright);font-size:11px;font-weight:500;}
.diagram-wrap svg .node-sub{fill:var(--dim);font-size:9px;}
.asyng-rel{background:var(--bg2);border:1px solid var(--border);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;padding:24px;margin:20px 0;}
.asyng-rel h4{color:var(--accent);font-size:14px;margin-bottom:8px;}
.asyng-rel p{font-size:13px;margin:0;line-height:1.7;}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:12px 0;}
.chip{font-family:var(--mono);font-size:10px;color:var(--dim);background:#ffffff05;border:1px solid var(--border);padding:3px 9px;border-radius:3px;}
.timeline{margin:16px 0;padding-left:20px;border-left:2px solid var(--border);}
.tl-item{padding:8px 0 8px 16px;position:relative;}
.tl-item::before{content:'';position:absolute;left:-25px;top:14px;width:8px;height:8px;background:var(--accent);border-radius:50%;border:2px solid var(--bg);}
.tl-date{font-family:var(--mono);font-size:11px;color:var(--accent);margin-bottom:2px;}
.tl-text{font-size:13px;line-height:1.5;}
footer{padding-top:32px;border-top:1px solid var(--border);display:flex;justify-content:space-between;font-family:var(--mono);font-size:10px;color:#1e1e2e;margin-top:48px;}
footer a{color:var(--accent);text-decoration:none;}
@keyframes fadeUp{from{opacity:0;transform:translateY(12px);}to{opacity:1;transform:translateY(0);}}
@media(max-width:700px){.hero h1{font-size:40px;}.stats{flex-wrap:wrap;}.stat{flex:none;width:50%;}.feat-grid,.verdict{grid-template-columns:1fr;}}
```
