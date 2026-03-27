# Paper-Drive Project Templates

Reference templates for the standard files in a paper-drive project.

---

## literature-collection.md

```markdown
# {Project Title} — Literature Collection

> One-line description of what this collection covers.

**Compiled:** {Date}
**Scope:** {Dimensions covered}
**Method:** {How sources were found}

---

## 1. {Section Name}

### 1.1 {Sub-section (optional)}

| ID | Source | Key Data Points | Date |
|----|--------|----------------|------|
| {S}-01 | **{Source Name}** ({org/authors}) | {2-3 key findings with numbers} | {Date} |
| {S}-02 | ... | ... | ... |

## 2. {Next Section}
...

---

## Collection Statistics

| Category | Sources |
|----------|---------|
| {Section 1} | N |
| {Section 2} | N |
| **Total** | **N sources** |
```

---

## .project/todo.md

```markdown
# TODO — {Project Title}

## Deliverables Plan

### Section Deep-Dives (Markdown + HTML each)
- [ ] S1: {Name} ({brief scope})
- [ ] S2: {Name}
...

### Papers & Slides
- [ ] Survey paper: "{Title}" + slide deck
- [ ] Tensions paper: "{Title}" + slide deck

### Supporting
- [ ] Section index page
- [ ] Slide deck
- [ ] Methodology document

## Source Adequacy Assessment

| Section | Current Sources | Adequate? | Gaps |
|---------|----------------|-----------|------|
| S1 | 0 | TBD | |
| S2 | 0 | TBD | |
```

---

## .project/changelog.md

```markdown
# Changelog — {Project Title}

All changes to the project.

---

## Session: {Date}

### Phase N: {Phase Name}
- {What was done}
- {Key decisions made}
- {What changed from plan}
```

---

## .project/methodology.md (Living Document)

Created at project start. Updated every session. Final pass at project end.

```markdown
# Methodology — {Project Title}

**Started:** {Date}
**Last updated:** {Date}

---

## Research Question

{What we're investigating. Why it matters. What prompted this project.}

## Scope & Dimensions

{The N axes this survey covers.}

**Deliberately excluded:** {What we chose NOT to cover and why. This is as important as what we included.}

## Source Strategy

{How sources are found: web search, arXiv, Semantic Scholar, citation tracking, industry reports, government data.}

{Source types prioritized: academic papers, industry reports, survey data, analyst predictions, government statistics.}

{Known biases in our sources: e.g., English-language bias, arXiv preprint bias, Western survey samples.}

## Reading & Synthesis Approach

{Technical survey (reading papers deeply) vs discourse survey (what people are saying)?}

{Reading depth tiers if applicable.}

## Deliverables Plan

{What papers, deep-dives, slides we intend to produce.}

## Decisions Log

{Updated each session. Record scope changes, methodology refinements, surprises.}

### Session {Date}
- {Decision}: {Rationale}

## Limitations

{Added during final pass. What was excluded, reading depth tradeoffs, source biases, single-researcher limitations.}

## What Broke

{Added during final pass. Bugs, wrong downloads, data issues. Honesty here is itself a contribution.}
```

---

## .project/continuation-prompt.md

```markdown
# Continuation Prompt — {Project Title}

Paste this into a new thread to resume.

---

## Prompt

I'm continuing work on a research project: **{Project Title}**.

**Repo:** {URL}
**Subfolder:** `{path}/`
**Live:** {Pages URL}

### What this project is

{2-3 sentence description of the project and its goal.}

### Methodology

We follow a **paper-drive** workflow. The key discipline: before building any section deep-dive, assess whether sources are sufficient. If not, search for what's missing. Only proceed when adequate.

### Current state

**Completed:**
- {List completed deliverables with source counts}

**Next:**
- **{Next section}** — {assessment status}. {Specific instructions.}
- {Remaining sections}

**After all sections:** {What papers/slides to build.}

### Template system

{How HTML deep-dives are built. Cache locations. How to extract if missing.}

### What to do now

{Specific next action.}
```

---

## index.html (created in Step 2)

The index is the project's monitoring dashboard. Created immediately, updated every commit.

**Check sibling project indexes** in the repo before building. Match CSS variables, font stack, class names.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{Project Title}</title>
  <!-- fonts: EB Garamond, IBM Plex Mono, Jost -->
  <style>
    /* Match sibling project CSS variables and classes exactly */
    /* Required classes: .deliverable-grid, .deliverable-card,
       .section-list, .section-item, .section-num, .section-body,
       .section-title, .section-desc, .section-links,
       .status.done, .status.wip, .status.planned,
       .tension-list, .tension-item, .tension-num */
  </style>
</head>
<body>
  <div class="container">
    <!-- HERO -->
    <div class="badge"><span class="dot"></span> {CATEGORY} · {DATE}</div>
    <h1>{Title} <em>{Accent}</em></h1>
    <div class="subtitle">{Description}</div>
    <div class="rule"></div>
    <div class="meta">
      <p>{Intro paragraph}</p>
      <p style="margin-top:12px;font-size:14px;color:var(--dim)">
        <a href=".project/methodology.md">Methodology</a> ·
        <a href="literature-collection.md">Literature Collection</a> ·
        <a href=".project/changelog.md">Changelog</a> ·
        <a href=".project/todo.md">TODO</a>
      </p>
    </div>

    <!-- KEY DELIVERABLES (top cards) -->
    <h2>Key Deliverables</h2>
    <div class="deliverable-grid">
      <div class="deliverable-card">
        <div class="section-title">Survey <em>Paper</em> <span class="status planned">planned</span></div>
        <div class="section-desc">{Description}</div>
        <div class="section-links">
          <a class="wip">Paper (pending)</a>
          <a class="wip">Slides (pending)</a>
        </div>
      </div>
      <div class="deliverable-card">
        <div class="section-title">{Second Paper} <span class="status planned">planned</span></div>
        <div class="section-desc">{Description}</div>
        <div class="section-links">
          <a class="wip">Paper (pending)</a>
          <a class="wip">Slides (pending)</a>
        </div>
      </div>
    </div>

    <!-- OVERVIEW (built last, after all sections) -->
    <div class="rule"></div>
    <h2>Overview</h2>
    <ul class="section-list">
      <li class="section-item">
        <div class="section-num">&mdash;</div>
        <div class="section-body">
          <div class="section-title">{Project} <em>Overview</em> <span class="status planned">planned</span></div>
          <div class="section-desc">{N}-section overview covering all dimensions.</div>
          <div class="section-links"><a class="wip">Deep Dive (pending)</a></div>
        </div>
      </li>
    </ul>

    <!-- SECTION DEEP-DIVES -->
    <div class="rule"></div>
    <h2>Section Deep-Dives</h2>
    <ul class="section-list">
      <li class="section-item">
        <div class="section-num">S1</div>
        <div class="section-body">
          <div class="section-title">{Section 1 Title} <span class="status planned">planned</span></div>
          <div class="section-desc">{Brief description}</div>
          <div class="section-links"><a class="wip">Deep Dive (pending)</a></div>
        </div>
      </li>
      <!-- ... S2–SN ... -->
    </ul>

    <!-- PROJECT-SPECIFIC SECTIONS (e.g., tensions — add as appropriate) -->

    <div class="footer">
      Part of <a href="../../">{repo}</a> research collection
    </div>
  </div>
  <!-- Theme toggle button + script (match sibling projects) -->
</body>
</html>
```

**Update rules:**
- Flip `planned` → `wip` → `done` as work progresses
- Replace `<a class="wip">` with real `<a href="...">` when files are created
- Slides link from the SAME card as their paper
- Add project-specific sections (tensions, resources, etc.) when content warrants them

---

## notes/{NN}-{name}.md

```markdown
# S{N}: {Section Name}

> One-line summary.

**Sources:** N ({list them})
**Adequacy:** {Verdict}

---

## 1. {Sub-topic}

{Synthesis across sources. Not source-by-source.}

## 2. {Sub-topic}
...

---

## What Sources Agree On

1. **{Finding}** — {evidence}
2. ...

## Where Sources Disagree

1. **{Topic}:** {Source A} says {X} vs {Source B} says {Y}
2. ...
```

---

## HTML Deep-Dive Build Pattern (Python)

```python
# 1. Load cached template CSS and JS
with open('template_css.txt') as f: css = f.read()
with open('template_js.txt') as f: js = f.read()

# 2. Define content arrays
sections = [
  { 'num': '01', 'short': 'Label', 'title': 'Full <em>Title</em>' },
  ...
]
summaries = [ '<p>...</p>', ... ]  # Center panel content
details = [ '<h3>...</h3><p>...</p>', ... ]  # Right panel content

# 3. Build JS arrays as strings
sec_js = 'const sections = [\n'
for s in sections:
    sec_js += "  {{ num: '{}', short: '{}', title: '{}' }},\n".format(
        s['num'], s['short'], s['title'])
sec_js += '];\n'

# Same for summaries and details (as template literals)
# IMPORTANT: escape backticks and ${} inside content

# 4. Patch hero content in template JS
patched_js = js.replace(
    'CATEGORY · LABEL',  # ← CHANGE marker
    'YOUR CATEGORY · YOUR LABEL'
).replace(
    'Your Topic <em>Title</em>',  # ← CHANGE marker
    'Your <em>Title</em>'
)

# 5. Assemble HTML — BODY MUST BE EMPTY
html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital@0;1&family=IBM+Plex+Mono:wght@400;600&family=Jost:wght@400;500;600&display=swap" rel="stylesheet">
  <style>{css}</style>
</head>
<body data-theme="light">
<script>
{sec_js}
{sum_js}
{det_js}
{patched_js}
</script>
</body>
</html>'''

# 6. Validate JS before writing
import subprocess
with open('/tmp/check.js', 'w') as f: f.write(sec_js + sum_js + det_js + patched_js)
r = subprocess.run(['node', '--check', '/tmp/check.js'], capture_output=True, text=True)
assert r.returncode == 0, f"JS invalid: {r.stderr[:200]}"
```

### Common bugs and fixes:
- **Blank page:** HTML body has content AND JS builds DOM → remove body content
- **JS syntax error:** Single `/` comments instead of `//` in template → sed fix
- **Broken template literals:** Unescaped backticks or `${` in content → escape them
- **Missing array:** `const sections` not defined → check Python injection

---

## Template Cache Extraction (do once per project)

The read-aid deep-dive template is a single HTML file. Extract its CSS and JS into separate cached files for reuse across sections:

```python
import re

with open('/mnt/skills/user/read-aid/references/deep-dive-reference.html') as f:
    html = f.read()

# Extract CSS
css_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
css = css_match.group(1)

# Extract JS — the DOM-building code, NOT the example content arrays
js_match = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
full_js = js_match.group(1)

# The template JS contains example sections/summaries/details arrays
# followed by the DOM-building code. Split at the DOM builder.
# Look for the line that starts building (typically "const app = ..." or
# the first function that creates DOM elements).
# In practice: everything AFTER the details array closing `];` is template JS.

# Save
with open('/home/claude/survey/template_css.txt', 'w') as f:
    f.write(css)
with open('/home/claude/survey/template_js.txt', 'w') as f:
    f.write(full_js)  # Will patch per section
```

**Hero markers to patch** (search for `← CHANGE` in the JS):
1. Badge text: e.g. `GENAI 2026 · S1 · 8 SOURCES`
2. Title: e.g. `LLMs &amp; Foundation <em>Models</em>`
3. Subtitle: e.g. `Capability, cost, compute, and the geopolitics of open-source`
4. Sidebar logo: e.g. `<div class="sidebar-logo">L<em>M</em></div>`

---

## Practical Build Approach (simpler than the Python-dict method)

In practice, writing the content arrays directly as a JavaScript file is simpler than building them from Python dicts. This was the actual pattern used in the GenAI 2026 project:

```python
# 1. Write content as a .js file with sections/summaries/details arrays
# Use JavaScript template literals (backticks) for HTML content

# 2. Build the HTML by concatenating:
with open('/home/claude/survey/template_css.txt') as f: css = f.read()
with open('/home/claude/survey/template_js.txt') as f: template_js = f.read()
with open('s3_content.js') as f: content_js = f.read()

# 3. Patch hero markers
template_js = template_js.replace('OLD BADGE', 'GENAI 2026 · S3 · 10 SOURCES')
template_js = template_js.replace('Old <em>Title</em>', 'AI <em>Agents</em>')
# ... etc

# 4. Assemble
html = f'''<!DOCTYPE html>
<html lang="en"><head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>S3: AI Agents — GenAI 2026 Outlook</title>
  <link href="https://fonts.googleapis.com/css2?family=..." rel="stylesheet">
  <style>{css}</style>
</head>
<body>
<script>
{content_js}

{template_js}
</script>
</body>
</html>'''

with open('s3-agents.dd.html', 'w') as f:
    f.write(html)
```

The content .js file is temporary (deleted after build). The HTML is the deliverable.

---

## Detail Panel Content Examples

### Minimal (avoid this — too thin)
```javascript
`<div class="detail-header"><div class="num">03</div><h2>Where Agents <em>Work</em></h2></div>
<p>Agents succeed in narrow tasks. Customer service has 115+ companies. Voice AI is growing.</p>`
```

### Target quality (analytical mini-essay)
```javascript
`<div class="detail-header"><div class="num">03</div><h2>Where Agents <em>Work</em></h2></div>
<p>The pattern across all sources is consistent: agents deliver real value when deployed against
<strong>narrow, repetitive tasks with clear success criteria and structured inputs/outputs.</strong>
They fail when asked to handle open-ended, multi-system, judgment-intensive work.</p>
<div class="diagram-wrap"><svg viewBox="0 0 400 250" xmlns="http://www.w3.org/2000/svg">
  <!-- 20-30 SVG elements: labeled boxes, stat callouts, comparison columns -->
</svg></div>
<h3>Where the Money Is</h3>
<p>CB Insights identifies five market segments with genuine revenue traction. <strong>Multimodal
customer service</strong> is the most mature, with 115+ companies competing and six private
companies exceeding $100M in revenue. The economics are straightforward: high-volume,
highly structured, clear KPIs.</p>
<h3>The Results When It Works</h3>
<p>G2&rsquo;s data from enterprises with production agents: median 40% cost reduction, 80%
containment rate, 23% speed-to-market improvement. These are not marginal gains. The catch
is in &ldquo;mature workflows&rdquo; &mdash; the gains come after significant investment in
integration, training, and iteration.</p>
<div class="callout"><strong>Salesforce&rsquo;s prediction:</strong> &ldquo;Brand identity
will be defined by AI agent quality.&rdquo; If true, agent capability becomes a competitive
differentiator on par with product quality.</div>`
```

Note: `&rsquo;` for apostrophes, `&mdash;` for em dashes, `&ldquo;`/`&rdquo;` for quotes. HTML entities required inside JS template literals in this context.

---

## Paper HTML Template

Papers are **standalone final deliverables** — no references to deep-dives. Uses the same design system (EB Garamond, Jost, IBM Plex Mono, light/dark toggle) but with a scrollable paper layout instead of the three-panel deep-dive layout.

**Key differences from deep-dives:**
- Body has content (not empty body with JS DOM building)
- Sidebar nav links to `#section-id` anchors (scroll, not panel swap)
- All source names are hyperlinked using URLs from literature-collection.md
- Each section ends with a sources footer
- Zero `*.dd.html` references

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{Paper Title} — {Project Name}</title>
  <!-- Same font stack as deep-dives -->
  <style>
    /* Same CSS variables as deep-dives (light/dark themes) */
    /* Paper-specific layout: fixed sidebar + scrollable main */
    .sidebar { width: 200px; position: fixed; /* ... */ }
    .main { margin-left: 200px; /* ... */ }
    .paper-hero { /* hero with badge, title, subtitle, meta */ }
    .paper-body { max-width: 860px; margin: 0 auto; padding: 0 80px; }
    .paper-section { padding: 48px 0; border-bottom: 1px solid var(--border); }
    .paper-section h2 { font-family: var(--serif); font-size: 32px; }
    .paper-section h3 { font-family: var(--sans); font-size: 10px; text-transform: uppercase; }
    .paper-section p { font-family: var(--serif); font-size: 17px; line-height: 2; }
    .paper-stat-row { display: flex; border: 1px solid var(--border); }
    .paper-stat { flex: 1; text-align: center; padding: 14px; }
    .section-sources { font-family: var(--mono); font-size: 11px; color: var(--dim); margin-top: 24px; padding-top: 12px; border-top: 1px solid var(--border); }
    .section-sources a { color: var(--accent); }
  </style>
</head>
<body data-theme="light">
  <div class="sidebar">
    <div class="sidebar-head">
      <div class="sidebar-logo">{L}<em>{M}</em></div>
      <div class="sidebar-sub">{Paper Type}</div>
    </div>
    <div class="sidebar-nav">
      <a href="#abstract" class="sidebar-item" data-target="abstract">
        <span class="sidebar-num">—</span><span class="sidebar-label">Abstract</span>
      </a>
      <a href="#s1" class="sidebar-item" data-target="s1">
        <span class="sidebar-num">01</span><span class="sidebar-label">{Section}</span>
      </a>
      <!-- ... -->
    </div>
    <div class="sidebar-foot">
      <a href="index.html">← Project</a>
    </div>
  </div>
  <button class="theme-btn"></button>
  <div class="main">
    <div class="paper-hero">
      <div class="paper-badge"><span class="dot"></span>{PROJECT} · {PAPER TYPE} · {N} SOURCES</div>
      <h1 class="paper-title">{Title} <em>{Accent}</em></h1>
      <p class="paper-subtitle">{Description}</p>
      <div class="paper-meta"><span>{Date}</span><span>{N} Dimensions</span><span>{N} Sources</span></div>
    </div>
    <div class="paper-body">
      <section class="paper-section" id="abstract">
        <div class="s-num">ABSTRACT</div>
        <h2>Abstract</h2>
        <p>...</p>
      </section>

      <section class="paper-section" id="s1">
        <div class="s-num">SECTION 01</div>
        <h2>{Section Title} <em>{Accent}</em></h2>
        <p><a href="https://..." target="_blank">Source Name</a> found that ...</p>
        <!-- Source names hyperlinked on first mention per section -->
        <div class="diagram-wrap"><svg><!-- SVG diagram --></svg></div>
        <div class="paper-stat-row">
          <div class="paper-stat"><span class="val">{N}</span><span class="lbl">{Label}</span></div>
        </div>
        <div class="section-sources">
          <strong>Sources:</strong>
          <a href="..." target="_blank">G-01</a> Pew 2025 ·
          <a href="..." target="_blank">G-04</a> Gallup ·
        </div>
      </section>
      <!-- ... more sections ... -->
    </div>
  </div>
  <script>/* Theme toggle + sidebar active tracking + smooth scroll */</script>
</body>
</html>
```

**Build checklist for papers:**
- [ ] All source names hyperlinked (first mention per section)
- [ ] Each section has a sources footer with literature-collection IDs
- [ ] Zero references to `*.dd.html` files
- [ ] `grep -c '<a href' paper.html` returns 20+ for multi-section papers
- [ ] SVGs pass overflow check
- [ ] Sidebar nav anchors all resolve
- [ ] Theme toggle works
- [ ] Responsive at mobile widths
