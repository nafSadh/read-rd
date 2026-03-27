---
name: read-aid
description: >
  Create interactive HTML learning materials from source material (papers, articles, codebases, transcripts, web research). Three formats: slide decks (arrow-key presentations with SVG diagrams), deep dives (sidebar + expandable panels), and animated scrolling guides (scroll-triggered SVG animations). Use whenever the user wants to learn a topic visually, turn a paper into slides, create an explainer or study guide, make a visual walkthrough, build lecture slides, or produce any educational HTML. Triggers for: "make slides about X", "explain this paper visually", "create a study guide", "turn this into a presentation", "help me understand X with diagrams", "break this down slide by slide", "teach me X", "make an interactive explainer". Focuses on pedagogy — deeply understanding material and restructuring it for learning.
---

# Reading Assist

Create interactive HTML learning materials that help people genuinely understand complex topics.

## Philosophy

The goal is never "summarize this into HTML." The goal is to become a thoughtful teacher: read the source material deeply, identify what's genuinely hard to understand and why, then restructure the ideas into a format that builds understanding progressively. Good pedagogical content has a few hallmarks:

- It starts where the learner is, not where the author is
- It builds concepts one at a time, each depending on what came before
- It uses concrete examples before abstractions
- It makes the invisible visible — diagrams, worked examples, analogies
- It's honest about what's hard and why

## Source Material

This skill works with anything readable: research papers, blog posts, textbook chapters, documentation, transcripts, codebases, data files, or topics that need web research across multiple sources. The source material determines the approach:

- **Single paper/article**: Close read, then restructure for learning. Preserve the intellectual substance but reorder for pedagogy.
- **Textbook chapter**: Companion material — assume the reader has the textbook. Focus on the parts that are hardest to grok from text alone (diagrams, worked examples, building intuition).
- **Multiple sources / web research**: Synthesize into a coherent narrative. The learning material should feel like one unified explanation, not a collage.
- **Code/technical docs**: Focus on the "why" and mental model, not just the "what." Show how pieces connect.

## Output Formats

There are three formats, each suited to different learning goals. Read the corresponding reference file before producing output.

### 1. Slide Deck (`references/slide-deck-template.md`)

**Best for**: Step-by-step concept building, paper walkthroughs, lecture companions, "explain X from zero"

An arrow-key navigable presentation where each slide presents one idea. Two-column layout: text on the left, SVG diagram on the right. Section divider slides break the deck into chapters. Includes a table of contents slide, a nav bar with progress indicator, and light/dark theme toggle.

Design: Crimson Pro (serif headings), IBM Plex Mono (code/labels), Source Sans 3 (body). Clean academic feel in light mode; deep indigo in dark mode.

**When to choose this format**: The material has a natural sequential structure. You're explaining how something works step by step. The reader benefits from seeing one idea at a time with accompanying visuals. Good for: paper walkthroughs, algorithm explanations, concept introductions, tutorials.

### 2. Deep Dive (`references/deep-dive-reference.html`)

**Best for**: Comprehensive reference pages, product/technology analysis, multi-faceted topic exploration

A three-panel layout: sidebar navigation on the left, summary sections in the center, and an expandable detail panel on the right. Each section has a summary view and a "read deep dive" link that opens the full analysis in the right panel. Supports feature grids, pro/con verdicts, timelines, pricing cards, stat bars, callout boxes, and SVG architecture diagrams.

Design: Jost (body/UI), EB Garamond (serif accents), IBM Plex Mono (code/labels). Unified purple/cyan accent palette across both themes. Cool slate-blue text in light mode; luxury violet/cyan in dark mode. Themes differ only in colors, never in typography or layout, ensuring flicker-free toggle.

**The reference file is a working HTML file** — open it in a browser to see the exact design. It contains 3 example sections demonstrating all available components. HTML comments at the top document every component. Look for `← CHANGE` markers for hero badge, title, subtitle, and sidebar logo.

Also see `references/deep-dive-template.md` for a prose description of the template architecture if you need to understand the design system conceptually.

**When to choose this format**: The material is multi-faceted and the reader might want to explore non-linearly. There are distinct sections that can stand alone. Good for: technology evaluations, comprehensive topic overviews, reference documents, comparison analyses.

**⚠️ CRITICAL: The `<body>` must be EMPTY.** The deep-dive template JS builds the entire DOM dynamically. If you put HTML elements in the body AND the JS also builds layout, you get a blank page (double-rendering). The body tag should contain nothing but the `<script>` block. This is the #1 build bug — it has happened on every project.

**Hero content — four `← CHANGE` markers to patch:**
1. `sidebar-logo`: 1-3 character logo, `<em>` for accent color (e.g., `D<em>D</em>`)
2. `hero-badge`: category label (e.g., `DEEP DIVE · 8 SOURCES`)
3. `hero-title`: main title with `<em>` for accent (e.g., `LLMs &amp; Foundation <em>Models</em>`)
4. `masthead-sub`: subtitle line

**Available components in summary/detail HTML:**
- `<div class="s-stat">` — stat bar with `<div class="st"><div class="sv">280×</div><div class="sl">label</div></div>` cells
- `<div class="callout"><h4>Title</h4><p>...</p></div>` — accent-bordered callout box
- `<div class="security-box"><h4>Title</h4><p>...</p></div>` — warning/critical callout
- `<div class="s-chip">label</div>` — small tag/chip
- `<div class="feat"><h4>Title</h4><p>description</p></div>` — feature card (use in grids)
- `<ul><li>...</li></ul>` — standard lists
- `<code>inline code</code>` — inline code
- `<pre>code block</pre>` — code block
- Standard HTML: `<h3>`, `<h4>`, `<p>`, `<strong>`, `<em>`, `<a href>`

**SVG CSS classes in deep-dive template** (used on `<text>` elements inside SVGs):
- `class="lbl"` — muted label text (theme-mapped gray)
- `class="lbl-hi"` — accent/highlight text (theme-mapped purple)
- `class="border"` — muted stroke for lines and dividers

These are different from slide-deck classes (`fig`, `label-text`). Deep-dive SVGs should use `lbl`/`lbl-hi` exclusively. Do NOT use `var(--accent)` — hardcode hex fills and let the CSS attribute selectors handle dark mode.

**Detail panel depth** (when used in paper-drive or multi-section projects):
Detail panels should be analytical mini-essays, not summaries. Target 6-10K characters with 2-4 sub-sections (`<h3>`), at least one SVG diagram (in `<div class="diagram-wrap">`), and at least one `<div class="callout">` box. Panels under 2K characters are too thin.

### 3. Animated Scrolling Guide (`references/animated-guide-template.md`)

**Best for**: Visual storytelling, architecture walkthroughs, "how X works" explainers

A long-form scrolling page with a hero section, numbered sections that fade in on scroll, large SVG canvases with animated data flow, interactive step-navigation buttons, architecture card grids, and a reading list / resource section at the end.

Design: Playfair Display (hero headings), JetBrains Mono (labels/code), DM Sans (body). Dark-only with warm accent colors (coral, teal, gold, purple). Cinematic feel with radial gradient backgrounds, glow effects, and animated flow lines.

**When to choose this format**: The material benefits from large, animated diagrams. You're telling a story about how a system works. The visual flow matters more than dense text. Good for: architecture explanations, system design walkthroughs, "how does X work under the hood" pieces.

## Process

### Step 1: Understand the Source Material

Read everything the user provides. If the source is a URL or topic requiring research, use web search to gather material from multiple angles — official docs, tutorials, blog posts explaining it, academic papers, community discussions. Take notes on:

- What are the core concepts? What order should they be introduced?
- What's hard to understand from text alone? (These need diagrams.)
- What analogies or concrete examples would help?
- What do people commonly misunderstand about this topic?
- What's the right level of depth for this audience?

### Step 2: Choose the Format

If the user didn't specify, choose based on the material:

- Sequential explanation of concepts → **Slide deck**
- Multi-faceted reference / analysis → **Deep dive**
- Architecture or system walkthrough → **Animated guide**

If a single topic is large enough, consider producing multiple complementary artifacts (e.g., an introductory slide deck AND a detailed reference deep dive).

### Step 3: Read the Template Reference

Read the reference file for the chosen format(s) from `references/`. These contain the complete CSS, HTML structure, component library, and design tokens. Follow the template closely for structure and styling — the templates have been carefully tuned for readability and visual quality.

### Step 4: Plan the Content Architecture

Before writing any HTML, outline:

- The sections/slides and what each one teaches
- Where diagrams are needed and what they should show
- The conceptual dependencies (what must come before what)
- Key equations, code examples, or worked examples to include

For slide decks: aim for 20-50 slides. Each slide should present exactly one idea.
For deep dives: aim for 6-10 sections with both summary and detail views.
For animated guides: aim for 5-8 sections with 1-2 large SVG diagrams each.

#### Slide Deck Content Standards

**Chapter labels (`.slide-chapter`)**: When explaining a paper, use section references from the paper itself: `§3.2 · Attention`, `§3.5 · Position`, `§5.4 · Results`. This grounds the learning material in the source and helps readers cross-reference. For non-paper topics, use concise descriptive labels.

**Title slide**: Include the full author list and venue/date when covering a paper. The `.ref` lines should give context: "NeurIPS 2017 · The paper that started the Transformer era". The `.meta` line should describe what kind of content it is: "A ground-up refresher with worked examples · Arrow keys / click / swipe".

**Content depth**: Every slide should feel like it was written by someone who deeply understands the material, not someone summarizing it. Include:
- Specific numbers from the source (embedding dimensions, BLEU scores, training details, dataset sizes)
- Paper-specific insights and design decisions ("Why sinusoidal? Because PE(pos+k) is a linear function of PE(pos)")
- Practical context and modern relevance ("Modern models like GPT-2+ use learned positional embeddings instead. LLaMA uses RoPE.")
- Honest notes about limitations or what came next

**Every content slide should have an SVG diagram.** If a slide is text-only with `col-1` and no SVG, that's a red flag — find a way to visualize what's being explained. Even abstract concepts can be shown as flow diagrams, comparison charts, or annotated examples.

### Step 5: Build the HTML

- Single standalone .html file (no external dependencies except Google Fonts CDN)
- All CSS in a `<style>` block, copied VERBATIM from the template reference
- All JS in a `<script>` block, copied VERBATIM from the template reference
- SVG diagrams inline (not image tags) — these are a core part of the pedagogy
- **Every HTML output MUST have a light/dark theme toggle.** No exceptions. The slide deck and deep dive templates include one; animated guide is dark-only.
- Responsive layout that works on mobile
- **CRITICAL**: Copy the template's CSS, nav bar HTML, and JavaScript exactly. Do not rename variables, restructure components, or reinterpret styling. The templates have been tuned precisely — your job is to fill in the content, not redesign the shell.

#### Multi-File Projects: CSS/JS Caching

When building multiple deep-dives or slides in one project (e.g., 5 section deep-dives + 1 slide deck), extract the CSS and JS from the reference HTML once and reuse:

```python
# Extract from reference (do once per project)
import re
with open('deep-dive-reference.html') as f:
    html = f.read()
css = re.search(r'<style>(.*?)</style>', html, re.DOTALL).group(1)
js_blocks = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
js = js_blocks[-1]  # Last script block is the app JS

# Cache to files
with open('template_css.txt', 'w') as f: f.write(css)
with open('template_js.txt', 'w') as f: f.write(js)
```

Then for each deep-dive, use the Python build pattern:

```python
# 1. Define content as Python data
sections = [
  { 'num': '01', 'short': 'Label', 'title': 'Full <em>Title</em>' },
]
summaries = ['<p>Summary HTML...</p>']
details = ['<h3>Detail heading</h3><p>Detail HTML...</p>']

# 2. Convert to JS arrays (template literals)
sec_js = 'const sections = [\n'
for s in sections:
    sec_js += "  {{ num: '{}', short: '{}', title: '{}' }},\n".format(
        s['num'], s['short'], s['title'])
sec_js += '];\n'

# For summaries and details, use backtick template literals.
# IMPORTANT: escape backticks and ${} in content!
sum_js = 'const summaries = [\n'
for s in summaries:
    escaped = s.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
    sum_js += '  `{}`'.format(escaped) + ',\n'
sum_js += '];\n'
# Same for details

# 3. Patch hero content by replacing ← CHANGE markers in template JS
patched_js = js.replace('CATEGORY · LABEL', 'YOUR LABEL')
# ... patch all four markers

# 4. Assemble — BODY MUST BE EMPTY (deep-dive) or contain only slides (slide deck)
html = f'<body data-theme="light">\n<script>\n{sec_js}\n{sum_js}\n{det_js}\n{patched_js}\n</script>\n</body>'

# 5. Validate JS before writing
import subprocess
with open('/tmp/check.js', 'w') as f:
    f.write(sec_js + sum_js + det_js + patched_js)
r = subprocess.run(['node', '--check', '/tmp/check.js'],
                   capture_output=True, text=True)
assert r.returncode == 0, f"JS invalid: {r.stderr[:200]}"
```

#### Template Literal Escaping

When injecting HTML content into JavaScript template literal strings (backtick-delimited), these characters must be escaped in the content:
- Backticks: `` ` `` → `` \` ``
- Dollar-brace interpolation: `${` → `\${`
- Backslashes: `\` → `\\`

Failure to escape causes silent JS syntax errors that result in a blank page with no visible error.

### Step 6: Quality Check

Before delivering:

- Does each section/slide teach exactly one concept?
- Are diagrams genuinely illuminating, not decorative?
- Does the progression build understanding or just list facts?
- Would someone actually learn from this, or is it just a pretty summary?
- Are equations/code accurate?
- Does the theme toggle work? Does it look good on mobile?
- Are all SVG elements properly themed for both light and dark modes?

#### SVG Pre-Commit Verification

Before committing any HTML with SVG diagrams, verify:

1. **Bounds:** Every `<text>` x < viewBox width − 15px. Every `<rect>`: x + width ≤ viewBox width, y + height ≤ viewBox height.
2. **Text in boxes:** If a box is at y=50 height=60, all text inside must have y between 50 and 110.
3. **Font size:** Minimum 7px for annotations, 8px for labels, 9-10px for primary content.
4. **Element count:** A good SVG has 15-30+ elements. Fewer than 10 = too sparse.
5. **Color consistency:** Same concept = same color across all diagrams in the project.
6. **Dark mode:** All fills are hardcoded hex (not CSS variables). The CSS attribute selectors handle remapping.

Ideally, open the HTML in a browser to visually verify. If you can't, at minimum validate the SVG XML is well-formed and viewBox dimensions make sense.

#### JS Validation

Always run `node --check` on the script content before committing. A syntax error in injected JS produces a blank page with no visible error message.

## SVG Diagram Guidelines — The Most Important Part

Diagrams are the heart of this skill. They are what separate a great learning resource from a mediocre wall of text with clip art. Every SVG must be **hand-crafted to teach**, not generated as a generic schematic.

### Craft Standards

Each SVG should feel like a **figure from an excellent textbook** — detailed, precise, with real data:

- **Use concrete examples, not abstractions.** Don't draw a box labeled "Input Sequence X". Instead, show actual tokens: "The", "cat", "sat", "on" — each in its own rect with a specific color. If showing embeddings, use plausible numbers: `[0.12, −0.87, 0.44, …]` with a note like "512 dims".
- **Pack information density.** A good SVG has 15-30+ elements (rects, texts, paths, lines). If your SVG has fewer than 10 elements, it's probably too sparse. Show the actual mechanism, not a cartoon of it.
- **Animate where it clarifies.** Use `<animate>` for sine waves, `stroke-dasharray` with `dashFlow` animation for data flow arrows, `pulse2` for attention highlights. Animations should show *process* — data moving, values changing, attention shifting.
- **Use the full color palette with semantic purpose.** Don't just use `--accent` for everything. Map colors to concepts consistently: e.g., `#5b63f5` (indigo) for queries, `#0e8fd0` (teal) for keys, `#14966e` (green) for outputs, `#4338ca` (deep purple) for values, `#9e9bac` (grey) for annotations. This palette carries meaning across slides.
- **Add bottom callout boxes.** Many diagrams benefit from a summary callout at the bottom — a rect with very low-opacity fill, thin border, and a one-line takeaway: "Attention = look at other words to understand yourself".
- **Show comparisons.** The best diagrams are often split: "BEFORE" vs "AFTER", "RNN: Sequential" vs "Transformer: Parallel", with a subtle dividing line and contrasting color coding.

### Technical SVG Requirements

- Use semantic grouping (`<g>` with transforms) for logical units
- Hardcode hex fills in SVG elements (e.g., `fill="#5b5bd6"`). The CSS dark-mode overrides will remap them automatically via attribute selectors.
- Do NOT use `var(--accent)` inside SVGs — hardcoded fills are required for the dark mode remapping system to work.
- Use `class="fig"` on all SVGs so the dark mode overrides apply
- Use `class="label-text"` on annotation text that should be in Source Sans 3, not monospace
- Use `font-family` attribute directly on `<text>` elements when needed (SVGs don't inherit CSS font stacks reliably)
- For worked examples: show actual numbers, walk through the computation visually step by step
- **NEVER use `<sup>`, `<sub>`, `<code>`, or any HTML tags inside SVG `<text>` elements** — they don't render in SVG and produce garbled text. Instead, write superscripts/subscripts as plain text (e.g., `WQ` not `W<sup>Q</sup>`, `dk` not `d<sub>k</sub>`, `KT` not `K<sup>T</sup>`). Use Unicode subscripts (₁₂₃ₖ) when available.

### ViewBox Sizing — Critical for Fit

Getting viewBox dimensions right prevents diagrams from overflowing their containers. The slide CSS uses `width: 100%` and `height: auto` on SVGs, so the viewBox aspect ratio determines how tall the SVG renders. A wide viewBox in a narrow container results in a very tall render that overflows the slide.

**col-2 layout** (text left, SVG right): The SVG column gets roughly half the slide width. Use viewBox widths of **340–400px**. Heights of 320–400px work well.

**col-1 layout** (text above, SVG below): The SVG gets the full slide width but vertical space is limited. Use viewBox widths of **380–500px** maximum. Wider viewBoxes (600+) will either overflow horizontally or render too tall. If your diagram needs to show two things side by side (e.g., Encoder and Decoder), stack them closer together within ~480px rather than spreading to 700px.

**Bounds checking — the #1 source of visual bugs**: Simple x-coordinate checks are insufficient. You must calculate the *rendered text width* based on character count and font size:

- **Monospace (IBM Plex Mono):** `text_width ≈ font_size × 0.62 × char_count`
- **Sans-serif (Jost, Source Sans 3):** `text_width ≈ font_size × 0.52 × char_count`

For `text-anchor="middle"`, check BOTH edges: `x ± (text_width / 2)`. All text must have **>5px margins** from viewBox edges AND from containing rect edges.

**Practical limits:**
- Max ~50 characters at font-size 8 monospace in a 400px viewBox (centered)
- Max ~18 characters at font-size 7 monospace inside a 130px-wide box (centered)
- If text doesn't fit: reduce font-size, shorten text, or break into two `<text>` lines

**Background rect rule:** The first `<rect>` in a deep-dive SVG should match the viewBox exactly (`x="0" y="0" width="{vw}" height="{vh}"`). **When you change viewBox height (e.g., to give bottom text more room), ALWAYS update the background rect to match.** A mismatch leaves visible gaps or clipping.

**Data inside boxes**: When showing values inside labeled boxes (e.g., embedding vectors in token cards), the text must fit within the box's y-bounds. If a box is at `y=50` with `height=60`, all text inside it must have y-coordinates between 50 and 110. Don't let values spill below the box bottom — make the box taller or use a more compact text layout like `[0.2, 0.1, 0.4, 0.3]` on one or two lines instead of one value per line.

### Color Palette for SVGs (hardcoded hex values)

| Color | Hex | Light fill | Role |
|-------|-----|-----------|------|
| Indigo | `#5b5bd6` / `#5b63f5` | `rgba(91,91,214,0.08)` | Primary concept, queries |
| Teal | `#0ea5e9` / `#0e8fd0` | `rgba(14,143,208,0.08)` | Secondary concept, keys |
| Purple | `#7c3aed` / `#4338ca` | `rgba(124,58,237,0.08)` | Tertiary concept, values |
| Green | `#0d9488` / `#14966e` | `rgba(20,150,110,0.04)` | Results, outputs, success |
| Dark text | `#1a1a1a` | — | Headings in SVG |
| Dim text | `#6e6b64` / `#5c5a6b` | — | Labels, connectors |
| Muted text | `#b0ada5` / `#9e9bac` | — | Annotations, dim notes |
| Subtle bg | `rgba(0,0,0,0.025)` | — | Neutral boxes, containers |

## File Naming

- Slide decks: `{topic}-slides.html`
- Deep dives: `{topic}-deep-dive.html`
- Animated guides: `{topic}-guide.html`

Multiple related files can be bundled (e.g., a curriculum on transformers might produce several slide decks covering different aspects plus a reference deep dive).

## Multi-File Projects

When this skill is used within a larger project (e.g., via the `paper-drive` skill), several deep-dives and slide decks share the same template CSS/JS. Key patterns:

1. **Cache CSS/JS once.** Extract from the reference HTML at project start. Reuse the cached files for every deep-dive and slide deck in the project (see Step 5 above).

2. **Consistent hero styling.** All deep-dives in a project should use the same sidebar-logo style, badge format, and design language. Only the title and subtitle change per section.

3. **Consistent color semantics.** If indigo means "primary concept" in S1, it means "primary concept" in S5. Map colors to meaning at the project level, not per-file.

4. **File naming convention.** For projects with section numbers: `s1-{name}.dd.html`, `s2-{name}.dd.html`, etc. For slides: `{project}.slides.html`. For overview: `{project}-overview.dd.html`.

5. **Every file needs a theme toggle.** Deep-dive and slide templates include one. Verify it's present in every output — especially if you're building a custom index page, which doesn't use a template.

6. **Cross-references between sections.** When one deep-dive mentions another section (e.g., "S3" in S1's text), link it:
   ```html
   <a href="s3-agents.dd.html" title="AI Agents">S3</a>
   ```
   Include `title` for hover tooltips. Skip self-references.

7. **Source citation links.** When source names appear in detail panels, link first mention per panel to the source report/study:
   ```html
   <a href="https://mckinsey.com/..." target="_blank">McKinsey</a>
   ```
   Match possessive forms separately (`McKinsey&rsquo;s`). Never match bare `IBM` — it collides with `IBM Plex Mono` font declarations.

8. **SVG verification.** After building any HTML with SVGs, verify text doesn't overflow. Calculate rendered width: `char_count × font_size × 0.62` (mono) or `× 0.52` (sans). Check that all text has >5px margins from viewBox edges and containing rects. Check that background rects match viewBox dimensions.

## Common Build Bugs

A quick reference for issues that recur across projects:

| Symptom | Cause | Fix |
|---------|-------|-----|
| Blank page (deep-dive) | HTML in `<body>` AND JS building DOM | Remove all body HTML; only `<script>` goes in body |
| Blank page (no error) | Unescaped backtick or `${` in template literal | Escape: `` \` `` and `\${` |
| JS syntax error | Single `/` comment instead of `//` | Check extracted JS; fix with sed or manually |
| SVG overflows slide | viewBox too wide for column | col-2: max 400px wide; col-1: max 500px |
| SVG invisible in dark mode | Used CSS variables instead of hardcoded hex | Use hex fills; CSS attribute selectors handle dark mode |
| Theme toggle missing | Custom page built outside template | Add toggle button + JS manually |
| Section not rendering | `const sections` array missing or malformed | Check Python injection; validate with `node --check` |
| SVG text clipped | Rendered text wider than viewBox or containing rect | Calculate width: `chars × font_size × 0.62`; break text or reduce font |
| Visible gap below SVG | viewBox expanded but background rect not updated | Always update bg rect dimensions to match viewBox |
| Source links match font names | Regex matches `IBM` in `IBM Plex Mono` declarations | Never match bare `IBM`; only match `IBM&rsquo;s framework` etc. |
| Links inside SVG break rendering | `<a href>` placed inside `<text>` in SVG | Remove; SVG text elements cannot contain `<a>` tags |
