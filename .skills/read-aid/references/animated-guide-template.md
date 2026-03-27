# Animated Scrolling Guide HTML Template Reference

A comprehensive design system and HTML structure for long-form scrolling explainer pages featuring animated SVG diagrams, scroll-triggered fade-ins, step navigation, and reading lists. Built for dark-only themes with accent-driven visual hierarchy.

## Fonts

Import three typeface families from Google Fonts:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital@0;1&family=JetBrains+Mono:wght@400;600&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
```

**Font Selection:**
- **Playfair Display** — Hero headings, italic emphasis, citation footer. Elegant serif with high contrast.
- **JetBrains Mono** — Labels, code snippets, badge text, tier headers. Technical monospace for structured information.
- **DM Sans** — Body text, descriptions, card content. Friendly sans-serif for readability.

## CSS Variables (Dark Theme)

Define a comprehensive color and spacing system in the root `:root` selector:

```css
:root {
  /* Backgrounds - Grayscale Depth */
  --bg-deepest: #0a0a0f;
  --bg-dark: #10101a;
  --bg-card: rgba(255, 255, 255, 0.03);

  /* Text - Hierarchical */
  --text-primary: #e8e6e1;
  --text-dim: #6b6a7a;

  /* Accents - Vibrant & Paired */
  --accent-coral: #ff6b3d;
  --accent-teal: #4ecdc4;
  --accent-gold: #ffe66d;
  --accent-purple: #a78bfa;
  --accent-pink: #f472b6;

  /* Accent 2 (secondary emphasis for hero & titles) */
  --accent-2: var(--accent-teal);

  /* Glow Effects */
  --glow-coral: rgba(255, 107, 61, 0.3);
  --glow-teal: rgba(78, 205, 196, 0.3);

  /* Borders & Dividers */
  --border-card: 1px solid rgba(255, 255, 255, 0.06);

  /* Spacing (base 16px) */
  --spacing-xs: 0.5rem;
  --spacing-sm: 1rem;
  --spacing-md: 2rem;
  --spacing-lg: 3rem;
  --spacing-xl: 6rem;
}

body {
  background: var(--bg-deepest);
  color: var(--text-primary);
  font-family: 'DM Sans', sans-serif;
  line-height: 1.6;
}
```

## Page Structure

The template uses a **single-column scrolling layout** with no sidebar or floating panels:

```
Hero Section (Full Viewport)
  ↓
Section 01 (Numbered, Scroll-Triggered)
  ├─ SVG Stage (Diagram Container)
  └─ Step Navigation (Optional)
  ↓
Section 02
  ├─ Architecture Cards Grid
  └─ Copy
  ↓
Section 03
  └─ More Content
  ↓
Reading List / Resources (Tiered Grid)
  ↓
Footer (Citation)
```

## Hero Section

The hero section spans the full viewport and centers content with a radial gradient overlay.

### HTML Structure

```html
<section class="hero">
  <div class="hero-content">
    <span class="hero-kicker">Animated Guide</span>
    <h1>Your Explainer Title Here</h1>
    <p class="hero-sub">A compelling subheading that frames the journey. Use <em>emphasis</em> for key concepts.</p>
  </div>
  <div class="scroll-cue">
    <span>Scroll to explore</span>
    <svg class="arrow" width="16" height="16" viewBox="0 0 16 16" fill="none">
      <path d="M8 2v10M3 8l5 5 5-5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </div>
</section>
```

### CSS

```css
.hero {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(
    circle at 30% 20%,
    rgba(78, 205, 196, 0.08) 0%,
    rgba(255, 107, 61, 0.04) 40%,
    transparent 100%
  );
  pointer-events: none;
  z-index: 1;
}

.hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
  max-width: 800px;
  padding: 2rem;
}

.hero-kicker {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: var(--accent-coral);
  display: block;
  margin-bottom: 1.5rem;
  animation: fadeUp 0.8s ease-out;
}

.hero h1 {
  font-family: 'Playfair Display', serif;
  font-size: clamp(3rem, 8vw, 7rem);
  font-weight: 700;
  line-height: 1.1;
  margin-bottom: 1.5rem;
  background: linear-gradient(
    135deg,
    var(--text-primary) 0%,
    var(--accent-2) 50%,
    var(--accent-2) 100%
  );
  background-size: 200% 200%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: fadeUp 0.8s ease-out 0.1s both, shimmer 3s ease-in-out 1s infinite;
}

.hero-sub {
  font-size: 1.1rem;
  max-width: 520px;
  margin: 0 auto;
  color: var(--text-dim);
  animation: fadeUp 0.8s ease-out 0.2s both;
}

.hero-sub em {
  color: var(--accent-2);
  font-style: italic;
  font-weight: 500;
}

.scroll-cue {
  position: absolute;
  bottom: 3rem;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.85rem;
  color: var(--text-dim);
  z-index: 2;
  animation: fadeUp 0.8s ease-out 0.4s both;
}

.scroll-cue .arrow {
  color: var(--accent-coral);
  animation: bounce 2s ease-in-out infinite;
}

@media (max-width: 600px) {
  .hero {
    padding: 2rem;
  }

  .hero h1 {
    font-size: clamp(2rem, 6vw, 3.5rem);
  }

  .hero-sub {
    font-size: 1rem;
  }
}
```

## Sections

Content sections are numbered, scroll-triggered, and fade in as the user scrolls.

### HTML Structure

```html
<section class="section" id="section-01">
  <div class="section-header">
    <span class="section-number">01 — Foundation</span>
    <h2>The Opening Concept</h2>
  </div>
  <p>Your explanatory paragraph with context-setting information.</p>
  <!-- SVG Stage, Cards, or Step Navigation go here -->
</section>
```

### CSS

```css
.section {
  max-width: 1100px;
  margin: 0 auto;
  padding: var(--spacing-xl) var(--spacing-md);
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.8s ease-out, transform 0.8s ease-out;
}

.section.visible {
  opacity: 1;
  transform: translateY(0);
}

.section-number {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--accent-coral);
  display: block;
  margin-bottom: 1rem;
}

.section h2 {
  font-family: 'Playfair Display', serif;
  font-size: clamp(1.8rem, 4vw, 2.8rem);
  margin-bottom: 2rem;
  color: var(--text-primary);
}

.section p {
  font-size: 1.05rem;
  max-width: 600px;
  color: var(--text-dim);
  margin-bottom: 2rem;
  line-height: 1.8;
}

.section p strong {
  color: var(--text-primary);
  font-weight: 600;
}

@media (max-width: 600px) {
  .section {
    padding: var(--spacing-lg) var(--spacing-sm);
  }
}
```

## SVG Stage

Large diagram containers for architecture visualizations and animated content.

### HTML Structure

```html
<div class="svg-stage">
  <svg viewBox="0 0 900 400" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="gradient-coral" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:var(--accent-coral);stop-opacity:1" />
        <stop offset="100%" style="stop-color:var(--accent-teal);stop-opacity:0.5" />
      </linearGradient>
      <filter id="glow-coral">
        <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
        <feMerge>
          <feMergeNode in="coloredBlur"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
      <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
        <polygon points="0 0, 10 3, 0 6" fill="var(--accent-teal)"/>
      </marker>
    </defs>

    <!-- Example: Flow line with animation -->
    <line x1="100" y1="200" x2="800" y2="200" stroke="var(--accent-teal)"
          stroke-width="2" marker-end="url(#arrowhead)" class="flow-line"/>

    <!-- Example: Animated node -->
    <circle cx="450" cy="200" r="20" fill="var(--accent-coral)" class="pulse-node"/>
  </svg>
</div>
```

### CSS

```css
.svg-stage {
  width: 100%;
  border-radius: 16px;
  background: var(--bg-card);
  border: var(--border-card);
  padding: 2rem;
  margin: 2rem 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.svg-stage svg {
  width: 100%;
  height: auto;
  display: block;
  max-width: 100%;
}

/* Flow line animation */
.flow-line {
  stroke-dasharray: 800;
  stroke-dashoffset: 800;
  animation: flowRight 3s ease-in-out infinite;
}

.flow-line-down {
  stroke-dasharray: 400;
  stroke-dashoffset: 400;
  animation: flowDown 3s ease-in-out infinite;
}

/* Node animations */
.pulse-node {
  animation: nodeAppear 0.6s ease-out, pulse 2s ease-in-out 0.6s infinite;
}

.attention-dot {
  animation: attentionPulse 1.5s ease-in-out infinite;
}

.data-particle {
  animation: dataFlow 4s linear infinite;
}

/* Matrix/grid cell fade */
.matrix-cell {
  animation: matrixFade 2s ease-in-out infinite;
  opacity: 0.3;
}

@media (max-width: 700px) {
  .svg-stage {
    padding: 1rem;
  }
}
```

## Step Navigation

Interactive pill buttons for exploring diagram sections within a single page section.

### HTML Structure

```html
<div class="step-nav">
  <button class="step-btn active" data-step="1">Layer 1</button>
  <button class="step-btn" data-step="2">Layer 2</button>
  <button class="step-btn" data-step="3">Layer 3</button>
  <button class="step-btn" data-step="4">Integration</button>
</div>
```

### CSS

```css
.step-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin: 2rem 0;
}

.step-btn {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 0.6rem 1.2rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 100px;
  background: transparent;
  color: var(--text-dim);
  cursor: pointer;
  transition: all 0.3s ease;
}

.step-btn:hover {
  border-color: var(--accent-coral);
  color: var(--accent-coral);
}

.step-btn.active {
  background: var(--accent-coral);
  color: var(--bg-deepest);
  border-color: var(--accent-coral);
}

@media (max-width: 600px) {
  .step-nav {
    gap: 0.5rem;
  }

  .step-btn {
    padding: 0.5rem 0.9rem;
    font-size: 0.65rem;
  }
}
```

## Architecture Cards Grid

2-column grid for showcasing components, layers, or architectural elements.

### HTML Structure

```html
<div class="arch-grid">
  <div class="arch-card">
    <h3>Component Name</h3>
    <p>Description of this architectural element or component. Explain its role in the system.</p>
  </div>
  <div class="arch-card">
    <h3>Another Component</h3>
    <p>Further elaboration on capabilities and interactions.</p>
  </div>
  <!-- More cards as needed -->
</div>
```

### CSS

```css
.arch-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 1.5rem;
  margin: 3rem 0;
}

@media (max-width: 700px) {
  .arch-grid {
    grid-template-columns: 1fr;
  }
}

.arch-card {
  background: var(--bg-card);
  border: var(--border-card);
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.4s ease;
}

.arch-card:hover {
  border-color: var(--accent-teal);
  transform: translateY(-4px);
  box-shadow: 0 0 30px var(--glow-teal);
}

.arch-card h3 {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--accent-2);
  margin-bottom: 0.75rem;
}

.arch-card p {
  font-size: 0.95rem;
  color: var(--text-dim);
  line-height: 1.7;
}
```

## Reading List / Resources

A tiered, filterable resource section with visual badges and hover effects.

### HTML Structure

```html
<section class="reading-list">
  <div class="section-header">
    <span class="section-number">Resources</span>
    <h2>Further Reading</h2>
  </div>

  <div class="tier tier-1">
    <div class="tier-header">
      <span class="tier-badge tier-1-badge">Essential</span>
    </div>
    <div class="resource-grid">
      <div class="resource-card">
        <div class="resource-icon">📖</div>
        <div class="resource-body">
          <h4>Resource Title</h4>
          <p class="author">Author Name</p>
          <p>Brief description of the resource and why it's important for understanding the topic.</p>
        </div>
        <div class="resource-tag">article</div>
      </div>
      <!-- More resource cards -->
    </div>
  </div>

  <div class="tier tier-2">
    <div class="tier-header">
      <span class="tier-badge tier-2-badge">Foundational</span>
    </div>
    <div class="resource-grid">
      <!-- Resource cards -->
    </div>
  </div>

  <!-- Additional tiers: tier-3, tier-4, tier-5 -->

  <div class="suggested-path">
    <h3>Suggested Learning Path</h3>
    <div class="path-steps">
      <div class="path-step">Start Here</div>
      <svg width="20" height="4" viewBox="0 0 20 4">
        <line x1="0" y1="2" x2="16" y2="2" stroke="var(--accent-coral)" stroke-width="1.5"/>
        <polygon points="16,2 20,0 20,4" fill="var(--accent-coral)"/>
      </svg>
      <div class="path-step">Deepen</div>
      <svg width="20" height="4" viewBox="0 0 20 4">
        <line x1="0" y1="2" x2="16" y2="2" stroke="var(--accent-coral)" stroke-width="1.5"/>
        <polygon points="16,2 20,0 20,4" fill="var(--accent-coral)"/>
      </svg>
      <div class="path-step">Master</div>
    </div>
  </div>
</section>
```

### CSS

```css
.reading-list {
  max-width: 1100px;
  margin: 0 auto;
  padding: var(--spacing-xl) var(--spacing-md);
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.8s ease-out, transform 0.8s ease-out;
}

.reading-list.visible {
  opacity: 1;
  transform: translateY(0);
}

.tier {
  margin-bottom: 3rem;
}

.tier-header {
  margin-bottom: 1.5rem;
}

.tier-badge {
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.65rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  padding: 0.4rem 0.8rem;
  border-radius: 4px;
  font-weight: 600;
}

.tier-1-badge {
  background: var(--accent-coral);
  color: var(--bg-deepest);
}

.tier-2-badge {
  background: var(--accent-teal);
  color: var(--bg-deepest);
}

.tier-3-badge {
  background: var(--accent-purple);
  color: var(--bg-deepest);
}

.tier-4-badge {
  background: var(--accent-gold);
  color: var(--bg-deepest);
}

.tier-5-badge {
  background: var(--accent-pink);
  color: var(--bg-deepest);
}

.resource-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 1.5rem;
}

@media (max-width: 700px) {
  .resource-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 500px) {
  .resource-grid {
    grid-template-columns: 1fr;
  }
}

.resource-card {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: 1rem;
  background: var(--bg-card);
  border: var(--border-card);
  border-left: 3px solid var(--accent-coral);
  border-radius: 8px;
  padding: 1.25rem;
  align-items: start;
  transition: all 0.3s ease;
}

.resource-card:hover {
  transform: translateX(4px);
  border-left-color: var(--accent-teal);
  box-shadow: -6px 0 20px var(--glow-teal);
}

.resource-icon {
  font-size: 1.5rem;
  text-align: center;
  flex-shrink: 0;
}

.resource-body h4 {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-primary);
  margin-bottom: 0.4rem;
}

.resource-body .author {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  color: var(--text-dim);
  margin-bottom: 0.6rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.resource-body p {
  font-size: 0.9rem;
  color: var(--text-dim);
  line-height: 1.6;
}

.resource-tag {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.65rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-dim);
  padding: 0.4rem 0.6rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 4px;
  white-space: nowrap;
  flex-shrink: 0;
}

.suggested-path {
  margin-top: 2rem;
  padding: 2rem;
  background: var(--bg-card);
  border-top: 2px solid;
  border-image: linear-gradient(90deg, var(--accent-coral), var(--accent-teal)) 1;
  border-radius: 8px;
}

.suggested-path h3 {
  font-family: 'Playfair Display', serif;
  font-size: 1.2rem;
  margin-bottom: 1.5rem;
}

.path-steps {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.path-step {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 0.6rem 1.2rem;
  background: rgba(78, 205, 196, 0.1);
  border: 1px solid rgba(78, 205, 196, 0.3);
  border-radius: 6px;
  color: var(--accent-teal);
}

@media (max-width: 500px) {
  .path-steps {
    flex-direction: column;
    gap: 0.5rem;
  }

  .path-steps svg {
    display: none;
  }
}
```

## Animations & Keyframes

Comprehensive animation set for fades, slides, glows, and data visualizations.

```css
/* Entrance animations */
@keyframes fadeUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes shimmer {
  0%, 100% {
    background-position: 0% center;
  }
  50% {
    background-position: 100% center;
  }
}

@keyframes bounce {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(6px);
  }
}

/* Flow & diagram animations */
@keyframes flowRight {
  from {
    stroke-dashoffset: 800;
  }
  to {
    stroke-dashoffset: 0;
  }
}

@keyframes flowDown {
  from {
    stroke-dashoffset: 400;
  }
  to {
    stroke-dashoffset: 0;
  }
}

@keyframes nodeAppear {
  from {
    r: 0;
    opacity: 0;
  }
  to {
    r: 20;
    opacity: 1;
  }
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.6;
  }
}

@keyframes attentionPulse {
  0%, 100% {
    r: 5;
    opacity: 1;
  }
  50% {
    r: 8;
    opacity: 0.4;
  }
}

@keyframes dataFlow {
  0% {
    offset-distance: 0%;
    opacity: 0;
  }
  10% {
    opacity: 1;
  }
  90% {
    opacity: 1;
  }
  100% {
    offset-distance: 100%;
    opacity: 0;
  }
}

@keyframes matrixFade {
  0%, 100% {
    opacity: 0.3;
  }
  50% {
    opacity: 0.8;
  }
}
```

## Scroll Observer JavaScript

Implements IntersectionObserver to trigger visibility animations on sections and reading list.

```javascript
// Initialize scroll-triggered animations
const observerOptions = {
  threshold: 0.15,
  rootMargin: '0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      // Optionally stop observing after visibility is triggered
      // observer.unobserve(entry.target);
    }
  });
}, observerOptions);

// Observe all sections and reading list
document.querySelectorAll('.section, .reading-list').forEach(el => {
  observer.observe(el);
});

// Optional: Step button interaction handler
document.querySelectorAll('.step-btn').forEach(btn => {
  btn.addEventListener('click', (e) => {
    const step = e.target.dataset.step;

    // Remove active class from all buttons
    document.querySelectorAll('.step-btn').forEach(b => {
      b.classList.remove('active');
    });

    // Add active class to clicked button
    e.target.classList.add('active');

    // Trigger diagram update or animation based on step
    // Example: triggerDiagramStep(step);
  });
});
```

## Responsive Design

The template adapts gracefully across breakpoints:

```css
/* Standard: Desktop/Tablet (1100px+) */
/* All grids display at full width with optimal spacing */

/* Tablet (700px) */
@media (max-width: 700px) {
  .arch-grid {
    grid-template-columns: 1fr;
  }

  .resource-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .svg-stage {
    padding: 1rem;
  }
}

/* Mobile (600px) */
@media (max-width: 600px) {
  .section {
    padding: var(--spacing-lg) var(--spacing-sm);
  }

  .hero {
    padding: 2rem;
  }

  .hero h1 {
    font-size: clamp(2rem, 6vw, 3.5rem);
  }

  .resource-grid {
    grid-template-columns: 1fr;
  }

  .path-steps {
    flex-direction: column;
    gap: 0.5rem;
  }

  .path-steps svg {
    display: none;
  }
}

/* Phone (500px) */
@media (max-width: 500px) {
  .hero-kicker {
    font-size: 0.65rem;
  }

  .section-number {
    font-size: 0.65rem;
  }

  .step-nav {
    gap: 0.5rem;
  }

  .step-btn {
    padding: 0.5rem 0.9rem;
    font-size: 0.65rem;
  }
}
```

## Footer

Simple footer with centered citation and border divider.

### HTML Structure

```html
<footer class="page-footer">
  <p><em>"The best interface is no interface."</em> — Your citation here, <strong>Source Name</strong></p>
</footer>
```

### CSS

```css
.page-footer {
  max-width: 1100px;
  margin: 0 auto;
  padding: var(--spacing-xl) var(--spacing-md);
  border-top: 1px solid rgba(255, 255, 255, 0.06);
  text-align: center;
}

.page-footer p {
  font-family: 'Playfair Display', serif;
  font-style: italic;
  color: var(--text-dim);
  max-width: 600px;
  margin: 0 auto;
}

.page-footer em {
  color: var(--accent-coral);
}

.page-footer strong {
  color: var(--text-primary);
  font-weight: 600;
  font-style: normal;
}

@media (max-width: 600px) {
  .page-footer {
    padding: var(--spacing-lg) var(--spacing-sm);
  }

  .page-footer p {
    font-size: 0.95rem;
  }
}
```

## Complete Example HTML Skeleton

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Animated Scrolling Guide</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital@0;1&family=JetBrains+Mono:wght@400;600&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <section class="hero">
    <div class="hero-content">
      <span class="hero-kicker">Animated Guide</span>
      <h1>Your Explainer Title</h1>
      <p class="hero-sub">Engage your audience with <em>animated visuals</em> and scroll-triggered reveals.</p>
    </div>
    <div class="scroll-cue">
      <span>Scroll to explore</span>
      <svg class="arrow" width="16" height="16" viewBox="0 0 16 16" fill="none">
        <path d="M8 2v10M3 8l5 5 5-5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>
  </section>

  <section class="section" id="section-01">
    <div class="section-header">
      <span class="section-number">01 — Foundation</span>
      <h2>The Opening Concept</h2>
    </div>
    <p>Content and explanation.</p>
    <div class="svg-stage">
      <!-- SVG Diagram -->
    </div>
  </section>

  <section class="section" id="section-02">
    <div class="section-header">
      <span class="section-number">02 — Architecture</span>
      <h2>System Components</h2>
    </div>
    <div class="arch-grid">
      <div class="arch-card">
        <h3>Component A</h3>
        <p>Description</p>
      </div>
      <div class="arch-card">
        <h3>Component B</h3>
        <p>Description</p>
      </div>
    </div>
  </section>

  <section class="reading-list">
    <div class="section-header">
      <span class="section-number">Resources</span>
      <h2>Further Reading</h2>
    </div>
    <div class="tier tier-1">
      <div class="tier-header">
        <span class="tier-badge tier-1-badge">Essential</span>
      </div>
      <div class="resource-grid">
        <div class="resource-card">
          <div class="resource-icon">📖</div>
          <div class="resource-body">
            <h4>Resource Title</h4>
            <p class="author">Author Name</p>
            <p>Description</p>
          </div>
          <div class="resource-tag">article</div>
        </div>
      </div>
    </div>
  </section>

  <footer class="page-footer">
    <p><em>"Attribution quote."</em> — Source</p>
  </footer>

  <script src="script.js"></script>
</body>
</html>
```

## Key Design Principles

1. **Single Column Flow** — All content stacks vertically; no sidebars or interruptions
2. **Scroll-Triggered Reveals** — Sections fade in as they enter viewport (15% threshold)
3. **Accent-Driven Hierarchy** — Coral, teal, purple, gold, and pink guide visual attention
4. **Typography as Navigation** — Three font families create clear information hierarchy
5. **SVG-First Diagrams** — Large viewBox canvases allow responsive, sharp graphics
6. **Dark-Only Theme** — No light mode toggle; consistent deep background (#0a0a0f)
7. **Glow Effects** — Subtle box-shadows and radial gradients add depth
8. **Micro-interactions** — Hover states, button animations, and flow lines engage users

## Implementation Notes

- Use `max-width: 1100px` centering for all content sections
- SVG viewBox should scale responsively without media queries
- Keep font sizes in `clamp()` for fluid scaling between mobile and desktop
- All animations use CSS, no external animation libraries required
- IntersectionObserver threshold of 0.15 ensures sections trigger early in viewport
- Avoid fixed positioning; use relative/absolute within sections only
- Test animations at 60fps on mobile devices

## Gold-Standard Section Examples

### Example 1: Two-Column Content with SVG Diagram

This example demonstrates a typical section with text content on the left and a complex SVG diagram on the right. Notice the title structure, key idea box highlighting, and SVG container:

```html
<section class="section" id="section-01">
  <div class="section-header">
    <span class="section-number">01 — Foundation</span>
    <h2>Words Don't Know Their Own Context</h2>
  </div>
  <div class="slide-body col-2">
    <div class="text-col">
      <p class="point">When a sentence enters a model, each word starts as an <strong>isolated vector</strong> — a list of numbers that encodes what the word <em>is</em>, but not what it <em>means here</em>.</p>
      <p class="point">The word <strong>"bank"</strong> has one embedding. It doesn't know if it's:</p>
      <p class="point">— <em>"I sat by the river <strong>bank</strong>"</em><br>
      — <em>"I went to the <strong>bank</strong> to deposit money"</em></p>
      <p class="point">Same word. Same vector. Completely different meanings.</p>
      <div class="key-idea">
        <div class="kicker">The question</div>
        <p>How does a token figure out what it means <em>in this particular sentence</em>?</p>
      </div>
      <p class="point">Answer: it looks at the other tokens around it and absorbs their information. That process is <strong>attention</strong>.</p>
    </div>
    <div class="svg-col">
      <svg viewBox="0 0 300 300" class="fig" xmlns="http://www.w3.org/2000/svg">
        <!-- Diagram content here -->
        <g transform="translate(15, 20)">
          <text x="135" y="0" text-anchor="middle" font-size="8" fill="var(--accent-coral)">SAME WORD, DIFFERENT MEANING</text>
        </g>
      </svg>
    </div>
  </div>
</section>
```

### Example 2: Full-Width Key Idea Box

This pattern works well for core concepts and memorable statements. It uses centered layout with larger typography:

```html
<section class="section" id="section-02">
  <div class="section-header">
    <span class="section-number">02 — Core Mechanism</span>
    <h2>Attention in One Sentence</h2>
  </div>
  <div class="slide-body col-1" style="justify-content: center; align-items: center; text-align: center;">
    <div class="key-idea" style="max-width: 700px; padding: 2rem 3rem;">
      <p style="font-size: clamp(1.1rem, 2vw, 1.6rem); line-height: 1.6;">
        Every token <strong>looks at every other token</strong>,<br>
        decides what's <strong>relevant</strong>,<br>
        and absorbs a <strong>weighted mix</strong> of their information.
      </p>
    </div>
    <p class="point" style="max-width: 550px; text-align: center; margin-top: 1.5rem;">
      That's the whole thing. Everything else is the machinery that makes this one idea work with numbers.
    </p>
  </div>
</section>
```

## Comparison with Slide Deck Format

The related file `what-is-attention.html` is a gold-standard slide deck presentation using a different paradigm: absolute-positioned slides with keyboard/click navigation instead of scrolling. While both use similar design principles (dark theme, CSS variables, accent colors, SVG diagrams), they have different architectures:

- **Scrolling Guide** (this template): Infinite scroll, IntersectionObserver-triggered reveals, responsive flexbox layout
- **Slide Deck**: Full-viewport slides, absolute positioning, discrete navigation states, navigation bar overlay

Choose the appropriate template based on your use case: scrolling for long-form explainers, slides for presentations.
