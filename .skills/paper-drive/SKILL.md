---
name: paper-drive
description: >
  Multi-session research project skill for building literature surveys, research papers, and deep-dive collections. Use this skill whenever the user wants to survey a topic across multiple dimensions, build toward a paper or set of papers, do a literature review, or create a structured research project with section-by-section deep-dives. Triggers for: "survey what people are saying about X", "write a paper on X", "do a literature review of X", "build a research project on X", "create a survey of X", any mention of "literature collection" + "deep-dives" + "paper", references to continuing an existing paper-drive project ("continue the GenAI outlook", "pick up where we left off on the survey"). Also triggers when a user uploads or references multiple papers/sources and wants them synthesized into a structured output. This skill orchestrates long-running multi-session research — it is NOT for single-source reading (use read-aid for that).
---

# Paper-Drive

A long-running research project skill that builds from literature collection through section deep-dives to papers and presentations. Designed for multi-session work where each session advances the project incrementally.

## Core Principle

**The source adequacy discipline:** Never build a section deep-dive without first assessing whether sources are sufficient. If they aren't, search for what's missing. Only proceed when adequate. This single rule prevents the most common failure mode — writing confidently from insufficient evidence.

## Relationship to Other Skills

- **read-aid:** Paper-drive uses read-aid templates for HTML output (deep-dive three-panel layout, slide decks). Read-aid handles single-source pedagogy; paper-drive handles multi-source synthesis across sessions.
- **pdf / pdf-reading:** Used within paper-drive for reading uploaded papers.
- **docx / xlsx:** May be used if user wants paper output in Word format or data in spreadsheet.

## When Starting a New Project

### Step 1: Understand Scope

Before doing anything, clarify with the user:

1. **Research question or area.** What are we surveying?
2. **Dimensions.** What are the 4-9 axes to cover? (More than 9 = split into sub-projects)
3. **Type.** Technical survey (reading papers deeply) or discourse survey (what people are saying)?
4. **End goal.** Which papers? Survey paper (always), plus: tensions paper, position paper, scenarios paper?
5. **Repository.** Where does this live? (existing repo or new?)

### Step 2: Create Project Structure

Every paper-drive project gets this directory structure. **Create it immediately** — don't wait until later:

```
{project-name}/
├── .project/
│   ├── changelog.md          # Session-by-session timeline
│   ├── todo.md               # Deliverables plan + source adequacy table
│   └── methodology.md        # Living document — started at project creation, evolved every session
├── notes/
│   └── 00-synthesis.md       # Cross-section synthesis (built incrementally)
├── index.html                # Project landing page — created NOW, updated every commit
├── literature-collection.md  # Master source list
```

**methodology.md starts on day one.** Don't wait until the end. Write it as a living document that captures decisions as they're made:

```markdown
# Methodology — {Project Title}

## Research Question
{What we're investigating and why}

## Scope & Dimensions
{The N axes this survey covers, and what's deliberately excluded}

## Source Strategy
{How sources are found — web search, arXiv, citation tracking, etc.}
{What types of sources are prioritized and why}

## Reading & Synthesis Approach
{Technical survey vs discourse survey}
{Reading depth tiers if applicable}

## Deliverables Plan
{What papers, deep-dives, slides we intend to produce}

---
*This document evolves as the project progresses. Each session updates
it with decisions made, scope changes, and methodological refinements.*
```

Update methodology.md and todo.md every session with: scope changes, new decisions about source strategy, sections that required gap-filling and what was found, anything that changed from the original plan, and current completion status.

**The TODO must include a source adequacy table from day one:**

```markdown
| Section | Current Sources | Adequate? | Gaps |
|---------|----------------|-----------|------|
| S1: ... | 0 | TBD | |
| S2: ... | 0 | TBD | |
```

**index.html is created NOW** — as soon as you know the project dimensions and deliverables. See "Index Page Structure" below for layout. All sections start as `<span class="status planned">planned</span>`. The index is your single monitoring dashboard for the entire project; it gets updated at every commit as items move from planned → wip → done.

#### Index Page Structure

The index page ordering depends on the project. The standard sections are:

1. **Hero** — Badge, title, subtitle, metadata links (methodology, lit collection, changelog, todo)
2. **Key Deliverables (top cards)** — 2–3 vertical cards for the paper outputs (survey paper, tensions paper, etc.). These go at the TOP, before overview and deep-dives. Each card shows: title, short description, status badge, and links. Slides link from the same card as their associated paper — don't give slides a separate card. Start as `planned`, flip to `done` when built.
3. **Overview** — Single section-item linking to the overview deep-dive
4. **Section Deep-Dives** — S1–SN as section-list items
5. **Project-specific sections** — Depends on the content:
   - **Tensions** — where sources disagree. Standard for research/survey projects. Heading should reflect the content: "Key Tensions," "Six Tensions," "Cross-Cutting Tensions," etc.
   - **Resources** — links to literature collection, external tools. Optional.
   - Other sections as appropriate for the domain.
6. **Footer** — repo link, related projects, attribution

**Key deliverable cards (when applicable) use a horizontal grid layout:**

```html
<h2>Key Deliverables</h2>
<div class="deliverable-grid">
  <div class="deliverable-card">
    <div class="section-title">Survey <em>Paper</em> <span class="status planned">planned</span></div>
    <div class="section-desc">Comprehensive survey synthesizing all N dimensions.</div>
    <div class="section-links">
      <a class="wip">Paper (pending)</a>
      <a class="wip">Slides (pending)</a>
    </div>
  </div>
</div>
```

CSS for the grid (add to the index stylesheet):

```css
.deliverable-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 12px;
  margin-bottom: 12px;
}
.deliverable-card {
  border: 1px solid var(--border);
  padding: 20px 24px;
  transition: all 0.2s;
}
.deliverable-card:hover {
  border-color: var(--accent);
  background: var(--accent-soft);
}
```

As papers are completed, update the status badge and swap `<a class="wip">` placeholders for real links. Slides link from the same card as their paper:

```html
<div class="section-links">
  <a href="survey-paper.html">Paper →</a>
  <a href="survey-slides.html">Slides →</a>
</div>
```

**Check sibling project indexes** in the repo for style conformity before building. Match the same CSS variables, font stack, and class naming conventions.

### Step 3: Literature Collection (First Deliverable)

Do a broad web search sweep (5-10 searches across all dimensions). Build `literature-collection.md`:

- Organize by section
- Each entry: ID, source name, key data points, date
- End with **Collection Statistics** table (count per section, total)

**Commit and push immediately.** The lit collection is the first deliverable — don't bundle it with other work.

### Step 4: Begin the Section Build Loop

After the literature collection is committed, go straight into section deep-dives (see below). **Do NOT build the overview first.** The overview is a synthesis — it requires the depth of understanding that only comes from building each section's deep-dive.

### Step 5: Review & Assess Completeness

After all planned section deep-dives are built, step back and review:

1. **Are additional sections needed?** The deep-dive process often reveals dimensions that weren't in the original plan. A section on religion & science might reveal enough material on AI-and-faith to warrant its own section. Add sections if the evidence demands it.
2. **What patterns emerged?** Where do sources disagree? What surprised you? What connects across sections in unexpected ways? These observations feed the overview and papers.
3. **Update the index** — flip all completed sections to `done`, add any new sections as `wip`.

Only after this review, proceed to the overview and papers (see "After All Sections").

---

## The Section Build Loop

For each section (S1, S2, ..., SN), follow this sequence **without exception**:

### A. Source Assessment (MANDATORY)

Before writing a single line of content, assess:

1. **Count:** How many sources do I have for this section? Minimum 5-6 for a standalone deep-dive.
2. **Coverage:** What sub-topics are well covered? List them.
3. **Gaps:** What's specifically missing? Be concrete: "no primary data on X" not "need more."
4. **Canonical references:** Am I missing standard references for this domain?
   - AI performance → Stanford AI Index
   - Compute/scaling → Epoch AI
   - Employment → BLS, WEF, Brookings
   - Public opinion → Pew, KPMG/Melbourne, Ipsos
   - Industry predictions → Gartner, IDC, Forrester
5. **Balance:** For discourse surveys, do I have both sides of every tension/debate?

**Present the assessment to the user.** State the verdict clearly: "6 sources, adequate" or "3 sources, NOT enough — missing X, Y, Z."

**If inadequate:** Search for specific gaps. Add to literature collection. Re-assess. **Do not proceed until adequate.**

**Update the TODO source adequacy table** with the verdict.

### B. Reading & Markdown Deep-Dive

For web sources: fetch via `web_fetch`, extract key claims and data points.
For papers: download PDF, extract via PyMuPDF, read at appropriate depth.

Write `notes/{NN}-{name}.md`:

```markdown
# S{N}: {Section Name}

> One-line summary.

**Sources:** N (list)
**Adequacy:** Verdict

---

## 1. {Sub-topic synthesized across sources}
{NOT source-by-source. Synthesize.}

## 2. {Next sub-topic}
...

## N. What Sources Agree On
- ...

## N+1. Where Sources Disagree
- {Claim}: {Source A says X} vs {Source B says Y}
```

### C. HTML Deep-Dive

Build using read-aid's deep-dive template. Read the template reference (`/mnt/skills/user/read-aid/references/deep-dive-reference.html`) if CSS/JS not cached.

**Critical rules:**
- Body must be **empty** — JS builds the entire DOM
- Python script injects `sections[]`, `summaries[]`, `details[]` arrays
- Patch hero content by replacing `← CHANGE` markers in the template JS
- 6-10 sections per deep-dive
- Verify JS validity with `node --check` before committing

#### Template Cache Setup (do once per project)

1. Read `/mnt/skills/user/read-aid/references/deep-dive-reference.html`
2. Extract CSS (everything between `<style>` and `</style>`)
3. Extract template JS (everything between `<script>` and `</script>`, EXCLUDING the content arrays — just the DOM-building code)
4. Save to working directory:
   - `/home/claude/survey/template_css.txt`
   - `/home/claude/survey/template_js.txt`

The template JS contains hero markers with `← CHANGE` comments:
- Badge: `GENAI 2026 · S1 · 8 SOURCES` (or similar)
- Title: `Your Topic <em>Title</em>`
- Subtitle: description text
- Sidebar logo: `<div class="sidebar-logo">L<em>M</em></div>`

Each section build patches these 4 markers with section-specific values.

#### Detail Panel Depth Standards

**This is where quality is won or lost.** Detail panels must be analytical mini-essays, not bullet-point summaries of the markdown notes.

| Quality | Chars | Paragraphs | Description |
|---------|-------|------------|-------------|
| ❌ Thin  | <2K   | 2-3        | Data dump, bullet lists |
| ⚠️ OK    | 3-5K  | 4-6        | Narrative but shallow |
| ✅ Deep   | 6-10K | 6-9        | Analytical arguments with evidence |

Target: **6-10K characters per detail panel.** Each should contain:
- `<div class="detail-header">` with section number and em-wrapped title
- 2-4 sub-sections with `<h3>` headers
- At least one SVG diagram (wrapped in `<div class="diagram-wrap">`)
- At least one `<div class="callout">` box with a key insight
- Cross-references to related sections (linked, not bare)
- Source names linked to their reports (first mention per panel)

### D. Verification

Run the SVG overflow check and link integrity check after building each section. See `references/verification.md` for the scripts.

### E. Linking Pass

After building sections (can be done per-section or in a batch after multiple sections), do a systematic pass:

#### Cross-References

Every bare S1–S8 mention in content links to the corresponding deep-dive:

```html
<a href="s3-agents.dd.html" title="AI Agents">S3</a>
```

- Include `title` attribute with section name (shows on hover)
- Skip self-references (S4 in s4-workplace.dd.html stays unlinked)
- Skip badge/nav/SVG occurrences

#### Source Citations

Link first mention of each source **per detail panel** (not just per file). Readers enter at any panel and should see linked references.

```html
<a href="https://mckinsey.com/..." target="_blank">McKinsey</a>
```

**Key patterns:**
- Possessive forms need separate matches: both `McKinsey` and `McKinsey&rsquo;s`
- **Never match bare `IBM`** — it appears in `IBM Plex Mono` font declarations hundreds of times. Only match specific forms: `IBM&rsquo;s framework`, `IBM&rsquo;s position`, etc.
- Skip matches inside `<svg>`, `<a>`, `font-family`, and HTML tag attributes
- After linking, verify: balanced `<a>`/`</a>` tags, zero links inside SVG, zero nested `<a>` tags

### F. Commit & Push

Commit with descriptive message. Push immediately. Provide the live URL to the user.

**Commit message pattern:**
```
S{N}: {Name} — deep-dive + markdown ({N} sources, {N} SVGs)

{Brief description of key findings}
```

---

## Writing Style

The deep-dives and papers are for readers who are smart and curious but may not live in your domain. They shouldn't need a PhD to follow, but they also shouldn't feel talked down to. The goal is the style of a great longform magazine piece — thorough, engaging, confident.

**Do:**
- Lead with the most interesting finding, not the background. The reader can get context as they go.
- Use specific numbers. "Costs dropped 280× in 18 months" is better than "costs dropped dramatically."
- Name the sources naturally. "Goldman finds that young tech workers are already affected" reads better than "According to Goldman Sachs Research (Briggs & Dong, 2025)."
- Write in active voice. "Stanford's Landay predicts..." not "It is predicted by Stanford's Landay that..."
- Let tensions carry the narrative. Disagreement is more interesting than consensus.
- End sections with what we don't know — the honest edges are where readers learn the most.

**Don't:**
- Don't over-explain obvious things. If you're writing about LLMs for someone reading a GenAI survey, you don't need to define "large language model."
- Don't hedge everything. If 5 sources agree, say so plainly. Reserve hedging for genuine uncertainty.
- Don't write source-by-source. Synthesize by sub-topic. The reader wants to understand the landscape, not read a bibliography.
- Don't use "it is important to note that" or "it should be noted." Just say the thing.
- Don't pad. If a section is naturally short because the data is thin, let it be short. Padding undermines trust.

**Tone calibration:** Imagine explaining this to a curious, well-read person — a scholar in an adjacent field, a software engineer who reads widely, an educated generalist. They want the substance, they can handle complexity, but they won't tolerate jargon without payoff or throat-clearing before the point.

---

## SVG Diagram Standards

SVG diagrams appear inline in detail panels. They must follow strict rules to avoid overflow, rendering issues, and visual inconsistency.

### Layout Rules
- viewBox: **400px wide** (height varies, typically 180-280px)
- First element: background rect matching viewBox **exactly** (`x="0" y="0" width="400" height="{vb_height}"`)
- **When you change viewBox height, ALWAYS update the background rect to match.** A mismatch leaves visible gaps.
- Wrap every SVG in `<div class="diagram-wrap">`

### Text Overflow Prevention (CRITICAL)

All text must have **>5px margins** from viewBox edges AND from containing rect edges.

**Character width formulas:**
- IBM Plex Mono (monospace): `width ≈ font-size × 0.62 × char_count`
- Jost (sans-serif): `width ≈ font-size × 0.52 × char_count`

**For `text-anchor="middle"`**, check BOTH edges:
- left edge = `x - (text_width / 2)`
- right edge = `x + (text_width / 2)`

**Practical limits:**
- Max ~50 characters at font-size 8 monospace in a 400px viewBox (centered)
- Max ~18 characters at font-size 7 monospace inside a 130px-wide box (centered)
- If text doesn't fit: reduce font-size, shorten text, OR break into two `<text>` lines

**After building any section with SVGs, run the verification script** in `references/verification.md`.

### Text Styling
- Use CSS classes, not hardcoded colors: `class="lbl"` (muted), `class="lbl-hi"` (accent)
- Font: `font-family="'IBM Plex Mono',monospace"` for data/labels
- Font: `font-family="'Jost',sans-serif"` for headings inside SVG
- Minimum font-size: 7px for annotations, 8px for labels, 9-10px for primary content

### Color Palette

Use these consistently across all sections. Map to concepts (e.g., purple for primary category, green for results, violet for contrasts).

**Rect fills (transparent overlays):**
- Purple: `fill="rgba(91,91,214,0.06)"` / `stroke="#5b5bd6"`
- Violet: `fill="rgba(124,58,237,0.08)"` / `stroke="#7c3aed"`
- Blue: `fill="rgba(14,143,208,0.06)"` / `stroke="#0e8fd0"`
- Green: `fill="rgba(20,150,110,0.04)"` / `stroke="#14966e"`
- Muted: `fill="rgba(0,0,0,0.03)"` (callout/annotation boxes)

**Text CSS classes (inside SVG):**
- `class="lbl"` — muted label text (theme-mapped)
- `class="lbl-hi"` — accent/highlight text
- `class="border"` — muted borders/lines

### Standard SVG Structure

```xml
<div class="diagram-wrap"><svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="400" height="240" fill="rgba(0,0,0,0.025)" rx="6"/>
  <text x="200" y="20" text-anchor="middle" font-family="'IBM Plex Mono',monospace"
        font-size="10" class="lbl" letter-spacing="1.5">CHART TITLE</text>
  <line x1="30" y1="32" x2="370" y2="32" stroke="currentColor" class="border" stroke-width="0.5"/>
  <!-- Content zone: y=44 to y=220 -->
  <!-- Bottom callout -->
  <rect x="50" y="220" width="300" height="16" fill="rgba(0,0,0,0.03)" rx="3"/>
  <text x="200" y="230" text-anchor="middle" font-family="'IBM Plex Mono',monospace"
        font-size="7" class="lbl">Bottom annotation — max ~45 chars</text>
</svg></div>
```

### Information Density
A good SVG has 15-30+ elements. If fewer than 10, it's too sparse — pack more information in. Use labeled boxes, stat callouts, timelines, comparison columns, or flow diagrams.

---

## After All Sections

### Overview Deep-Dive

Build the overview **only after all section deep-dives are complete.** By this point you have deep, source-grounded understanding of every dimension — the overview benefits from that depth rather than being a shallow pre-read.

Use read-aid's deep-dive template. One section per dimension. Summary level — but informed by the full analysis in each section. The overview should capture what you now know that you didn't know at the literature-collection stage: which tensions are sharpest, which findings surprised you, which dimensions connect in unexpected ways.

Source assessment for the overview is unnecessary — you've already assessed every section.

### Papers

Synthesize from completed section deep-dives. Every paper-drive project produces at minimum a survey paper. **Projects in the repo that have deep-dives but no papers are incomplete** — they should be updated when resumed. Paper types:

- **Survey paper:** Per-section summaries with unified framework. Structure: Abstract → Intro (thesis) → Method → Sections → Synthesis → References.
- **Tensions paper:** Where sources contradict and what it means. Focus on the tension table from the literature collection.
- **Scenarios paper:** Comparing different forward predictions.

Build as markdown first, then render as HTML (sidebar nav, academic typography, light/dark toggle).

**Paper files live at project root** (e.g., `survey-paper.html`, `tensions-paper.html`) — NOT in a `papers/` subdirectory. Same level as deep-dives.

#### Paper-Specific Rules

Papers are **standalone final deliverables**. A reader should be able to read a paper without ever seeing the deep-dives. Deep-dives are internal/intermediate work products — papers must not reference or link to them. All evidence in a paper comes from the original sources via the literature collection.

1. **Every source name must be a hyperlink on first mention per section.** The literature collection has the URLs:
   ```html
   <a href="https://pewresearch.org/..." target="_blank">Pew Research</a> found that...
   ```
   After first mention in a section, the bare name is fine. Additionally, add a superscript citation for key claims (see Citation & Linking Discipline below).

2. **Stat claims need source attribution.** Not just "347 million Muslims" but "Pew's 2025 study found 347 million Muslims." The source name should be linked, and the claim should carry a superscript citation.

3. **Single consolidated References section at the bottom of the paper.** No per-section source footers. Use Wikipedia-style `<sup class="fn"><a href="#ref-N">[N]</a><span class="tip"><a href="URL" target="_blank">Title →</a></span></sup>` inline, with a numbered `<ol class="ref-list-num">` at the bottom. See Citation & Linking Discipline for the full HTML/CSS pattern.

4. **No references to deep-dives.** Papers don't say "See S1 deep-dive for details." The paper IS the details. Deep-dives are working documents that fed the synthesis; they're not part of the reader's journey.

5. **Build links and citations inline as you compose.** Don't plan to "add links later" — it never happens. Number sources in order of first appearance.

**Verification after building any paper:**
- grep for source names mentioned without `<a href` — every source from the literature collection that appears should be linked
- grep for any `dd.html` references — these should not exist in papers
- `grep -c 'class="fn"' paper.html` — if under 10 for a multi-section paper, citations are sparse
- `grep -c '<li id="ref-' paper.html` — should match total unique sources cited

### Slides

**Each paper should have an accompanying slide deck.** Slides are linked from the same deliverable card on the index, not listed separately.

Use read-aid's slide-deck template. 20-30 slides. One idea per slide. SVG diagrams (see SVG Diagram Standards above). Hover citations on key claims. Same citation discipline as papers — source names linked, stats attributed.

Slide decks are also standalone — they don't reference deep-dives.

### Methodology (Final Pass)

methodology.md has been evolving since project creation. Do a final pass: add a Limitations section (what was excluded and why, reading depth tradeoffs, source biases), a Reproducibility section (how someone could replicate or extend the work), and a "What Broke" section (bugs, wrong downloads, data issues encountered and how they were resolved). The honesty of this document is itself a contribution.

---

## Proactive Behaviors

These are things the skill should do **without being asked** — they represent decisions the user previously had to make manually:

### Structural Consistency
- **index.html is created in Step 2** — before the literature collection, before any deep-dives. It's the first HTML file in the project.
- Every HTML page gets a dark/light theme toggle. No exceptions.
- Every new HTML gets added to the project index AND the parent repo's root index.
- All deliverables (deep-dives, papers, slides) live at project root — NOT in subdirectories like `papers/` or `slides/`. Flat structure.
- For subfolders with multiple files, the root index links only to the cover page (index.html), not individual deep-dives.
- **Index page style must match sibling projects in the same repo.** Before building or modifying an index, check 1-2 other project index pages (e.g., genai-2026-outlook) for the CSS classes, section structure, and ordering convention. Don't invent new card layouts.

### Heading Accent Word (`<em>`)
The `<em>` word in headings is the **differentiator** — the word that distinguishes THIS section from all other sections in the same document. It answers "what is unique about THIS section?" not "what is this document about?"

**The rule:** Accent the word that, if removed, would make the heading indistinguishable from other headings.

**Heuristics:**
1. **The document's subject word is NEVER the differentiator.** In a humor paper, "Humor" and "Laughter" appear in most headings — they carry zero distinguishing information. In a religion paper, "Religion" is never the accent. Accent the lens: *Cognitive* Science of Religion, *Neuroscience* of Laughter, *Developmental* Psychology of Religion.
2. **The word that makes the heading unique IS the differentiator.** *Block* Universe (not Block *Universe*), *Retrocausality* & Bidirectional Causation, *Developmental* Psychology.
3. **Lens/approach beats subject.** *Moral* Psychology > Moral *Psychology*. *Cultural* Comedy > Cultural *Comedy*.
4. **Surprising or novel concepts beat generic containers.** *Intelligence*, Aggression & Dark Humor (the surprising finding) > Intelligence, Aggression & Dark *Humor* (generic subject).
5. **Last-word accent is fine when the last word IS the differentiator.** Comedy Structure & *Craft* (craft is specific), Dark Humor & *Taboo* (taboo is the distinctive angle), The *Neuroscience* of Laughter (neuroscience is the approach; laughter is the subject of every section).
6. **Never auto-accent the last word programmatically.** No `.map((w, j) => j === last ? '<em>' : w)` patterns. Every accent word is a deliberate editorial choice.

**Examples — GOOD vs BAD:**
```
✓ The *Cognitive* Science of Religion     — cognitive distinguishes from anthropological/sociological
✗ The Cognitive Science of *Religion*     — religion is every section's subject

✓ AI & *Computational* Humor             — computational is the domain
✗ AI & Computational *Humor*             — humor is every section's subject

✓ *Literary* Applications                — literary is the specific type of application
✗ Literary *Applications*                — applications is generic filler

✓ The *Neuroscience* of Laughter          — neuroscience is the approach/lens
✗ The Neuroscience of *Laughter*          — laughter is the paper's subject, not a differentiator

✓ Depression as *Bidirectional* Loop      — bidirectional is the reframe
✗ Depression as Bidirectional *Loop*      — loop is structural, not distinctive
```

### Completeness Checking
After building any deliverable, verify:
- [ ] File renders (JS validates, no double-rendering)
- [ ] SVGs pass overflow check (run verification script)
- [ ] Links pass integrity check (balanced tags, no SVG links)
- [ ] **Source names are hyperlinked** (grep for unlinked source names from literature collection)
- [ ] **For deep-dives:** cross-references (S1–SN) are hyperlinked to corresponding deep-dives
- [ ] **For papers/slides:** zero references to deep-dive files (papers are standalone)
- [ ] **Heading accent words:** `<em>` falls on the differentiator, not a repeated subject word or generic last word
- [ ] **index.html updated** — status badge flipped, real links added
- [ ] Linked from project index (if exists)
- [ ] Linked from root index
- [ ] Committed and pushed
- [ ] Live URL provided to user

### Citation & Linking Discipline

**Every reader-facing deliverable — deep-dives, papers, slides — must have proper source linking and citations.** The literature collection is the URL database. No deliverable should mention a source by name without linking it.

**Universal rules (all deliverables):**
- The literature collection has every source name and URL. When a source appears in any deliverable, its first mention per section/panel/slide MUST be an `<a href>` link.
- Write links inline as you compose. Don't plan to "add links later" — it never happens.
- After building any HTML deliverable, run: `grep -c '<a href' file.html` — if the count is low relative to the number of sources mentioned, something is wrong.
- A deliverable that mentions "Pew Research" or "Goldman Sachs" or "PRRI" repeatedly with zero hyperlinks is a failure, not a draft.

**In deep-dives:** Link source names to their reports (first mention per detail panel).

**In papers — Wikipedia-style superscript citations:**

Papers use a consolidated citation system modeled on Wikipedia. **No per-section source footers.** Instead:

1. **Inline superscripts** — Use `<sup class="fn"><a href="#ref-N">[N]</a><span class="tip"><a href="URL" target="_blank">Title →</a></span></sup>` where N is the source number. The `[N]` click scrolls to the bottom reference list. The tooltip hover shows the source title as a clickable link to the actual source.

2. **Single consolidated References section** at the bottom of the paper, after Methods/Limitations:
   ```html
   <section class="paper-section" id="references">
     <div class="s-num">REFERENCES</div>
     <h2>References</h2>
     <ol class="ref-list-num">
       <li id="ref-1" value="1"><a href="URL">Source Title (Year)</a></li>
       ...
     </ol>
   </section>
   ```

3. **Required CSS** for the citation system:
   ```css
   sup{font-size:11px;line-height:0;vertical-align:super}
   sup.fn{position:relative;cursor:pointer;font-family:var(--sans)}
   sup.fn>a{color:var(--accent);font-weight:600;text-decoration:none;border-bottom:none}
   sup.fn:hover>a{color:var(--bright)}
   sup.fn .tip{display:none;position:absolute;bottom:calc(100% + 4px);left:50%;transform:translateX(-50%);background:var(--bg2);border:1px solid var(--border);padding:8px 14px;font-family:var(--sans);font-size:13px;font-weight:400;color:var(--text);white-space:normal;max-width:480px;min-width:200px;z-index:50;pointer-events:auto;line-height:1.5;box-shadow:0 4px 16px rgba(0,0,0,0.15)}
   sup.fn .tip a{color:var(--accent);text-decoration:none;border-bottom:1px dotted var(--accent)}
   sup.fn .tip a:hover{color:var(--bright);border-bottom-style:solid}
   sup.fn:hover .tip,sup.fn .tip:hover{display:block}
   .ref-list-num{padding-left:2.5em;margin:0}
   .ref-list-num li{font-family:var(--mono);font-size:12px;color:var(--dim);padding:5px 0;border-bottom:1px solid color-mix(in srgb,var(--border),transparent 50%);line-height:1.6}
   .ref-list-num li::marker{color:var(--accent);font-weight:600}
   .ref-list-num li a{color:var(--text);text-decoration:none;border-bottom:1px dotted var(--border)}
   ```

4. **Key behaviors:** Hover on `[N]` shows tooltip with source title as clickable link (opens in new tab). Tooltip stays open when pointer moves to it (`pointer-events:auto`). Click `[N]` scrolls to the numbered reference at bottom. Font is sans-serif (not monospace) for readability.

5. **Numbering:** Sources are numbered in order of first appearance in the paper, starting at 1. Add a "References" link to the sidebar nav.

6. **No nested `<a>` tags.** The `[N]` link and the tooltip link must be siblings inside `<sup>`, not nested. Structure: `<sup class="fn"><a href="#ref-N">[N]</a><span class="tip"><a href="URL" target="_blank">Title →</a></span></sup>`

**In slides:** Add `<span class="cite">[ID]</span>` for key claims, styled with `font-family:var(--mono);font-size:11px;color:var(--dim)`. Source links in a references/colophon slide.

### Git Discipline
- Commit after every logical unit of work (not batched)
- Push after every commit (don't wait)
- **Update index.html at every commit** — flip status badges (planned → wip → done), add real links as files are created, update descriptions. The index is the monitoring dashboard; it must always reflect current state.
- Descriptive commit messages with what changed and why
- After push, provide the live URL

### Session Handoff
When the user signals end of session (or context is getting long):
1. Commit a checkpoint with current state
2. Update `.project/changelog.md` with what was done
3. Update `.project/todo.md` with current status (check off completed items, update source adequacy table, note what's next)
4. Update `.project/methodology.md` with any decisions made this session
5. Generate a continuation prompt (saved to `.project/continuation-prompt.md` AND displayed to user)

The continuation prompt must include: repo URL, project subfolder, what's completed, what's next (with specific instructions like "assess S2 sources first"), template system notes, and related projects for reference. **Never include API keys, PATs, or other secrets in the continuation prompt file** — GitHub push protection will block the push. Use placeholders like `(provide at runtime)`.

---

## Source Adequacy Minimums by Domain

| Domain | Minimum Sources | Must-Have References |
|--------|----------------|---------------------|
| AI/ML technology | 6-8 | Stanford AI Index, Epoch AI |
| Employment/labor | 6-8 | BLS, WEF, Brookings, one Fed bank |
| Public opinion | 5-6 | Pew, KPMG/Melbourne or Ipsos |
| Industry predictions | 5-7 | Gartner, IDC or Forrester, one consulting firm |
| Regulation/policy | 4-6 | Government sources, one legal scholar |
| Economics/infrastructure | 5-6 | Goldman Sachs or similar, Epoch AI |
| Scientific domain | 6-8 | 3+ primary papers, 1+ survey |
| Multimodal/creative AI | 5-7 | Model benchmarks, safety/deepfake data |

---

## Anti-Patterns to Avoid

1. **Building before assessing.** The #1 failure mode. Always assess sources first.
2. **Source-by-source writing.** Deep-dives synthesize across sources by sub-topic, not paper-by-paper.
3. **Forgetting to push.** Commit AND push after every deliverable. Provide URL.
4. **Inconsistent structure.** Every project gets the same directory layout and file naming.
5. **Missing links.** Every new file must be linked from index pages.
6. **HTML body content + JS DOM building.** The read-aid deep-dive template requires an empty body. Content in body AND JS building DOM = blank page.
7. **Overclaiming.** If a source says X, write "Source says X" not "X is true." Source adequacy doesn't mean the sources are right.
8. **Bundling too much in one commit.** Commit each logical unit separately for clean history.
9. **Skipping the tensions.** Disagreements between sources are the most valuable findings. Always surface them.
10. **No continuation prompt.** Long-running projects span sessions. Always generate handoff material.
11. **ViewBox/background-rect mismatch.** When expanding viewBox height, ALWAYS update the background rect to match. `viewBox="0 0 400 200"` needs `<rect ... width="400" height="200"/>`.
12. **IBM Plex Mono false positives.** Never regex-match bare "IBM" as a source name in linking passes. The font declaration appears 200+ times. Only match specific forms like `IBM&rsquo;s framework`.
13. **Thin detail panels.** If panels are <3K chars, they're data dumps not analysis. Target 6-10K per panel. Check character count after building.
14. **First-mention-only linking.** Linking each source once per *file* is too sparse — readers enter at any panel. Link first mention per *detail panel* instead.
15. **SVG text overflow.** Never trust visual estimates. Calculate: `char_count × font-size × 0.62` for monospace. Run the verification script before committing.
16. **Papers without source links.** The #1 paper failure mode. A paper that mentions sources by name without hyperlinking them is not a paper — it's a draft. The literature collection has every URL. Use them inline as you write, not in a deferred linking pass. Papers must use Wikipedia-style `<sup class="fn">[N]</sup>` citations with hover tooltips and a single consolidated References section at the bottom. If `grep -c 'class="fn"' paper.html` returns fewer than 10 citations for a multi-section paper, something is wrong.
17. **Papers in subdirectories.** Papers, slides, and deep-dives all live at project root (e.g., `survey-paper.html` next to `s1-topic.dd.html`). Never create `papers/` or `slides/` subdirectories.
18. **Index style drift.** Before modifying or creating an index page, check 1-2 sibling project indexes in the same repo. Use the same CSS classes and section structure. Don't invent new card layouts or grid systems.
19. **Secrets in committed files.** Never put API keys, PATs, or other secrets in files that will be committed (including `continuation-prompt.md`). GitHub push protection will block the push. Use `(provide at runtime)` as a placeholder.
20. **Compose-then-link workflow.** Writing any deliverable and planning to "add links later" guarantees the links never get added. Build `<a href>` tags inline as you compose. The literature collection is your URL lookup table. This applies to deep-dives, papers, AND slides.
21. **Overview before sections.** The overview is a synthesis. Building it before the section deep-dives means writing from shallow understanding. Build all sections first, then write the overview with the depth you've earned.
22. **Deferred index creation.** The index is created in Step 2 — the moment you know the project dimensions. It starts with all items as `planned` and gets updated at every commit. Don't wait until "everything is done" to build the index; by then you've lost the monitoring benefit.
23. **Papers referencing deep-dives.** Papers are standalone final deliverables. They must not link to or mention deep-dive files (`*.dd.html`). Deep-dives are internal working documents that fed the synthesis. If a reader needs to "see the deep-dive for details," the paper hasn't done its job.
24. **Papers without slides.** Each paper should have an accompanying slide deck. A paper without slides is incomplete.
25. **Per-section source footers in papers.** Papers use a single consolidated References section at the bottom, not per-section `<div class="section-sources">` blocks. Per-section footers are for deep-dives only. Papers use Wikipedia-style `<sup>[N]</sup>` inline citations pointing to the bottom reference list.
26. **Nested `<a>` tags in citations.** The citation `[N]` link and the tooltip source link must be siblings inside `<sup>`, never nested. Invalid: `<sup><a class="fn">[N]<span><a>...</a></span></a></sup>`. Valid: `<sup class="fn"><a>[N]</a><span class="tip"><a>...</a></span></sup>`.
27. **Monospace citations.** Citation superscripts and tooltip text use `var(--sans)`, not `var(--mono)`. Monospace is for the reference list items only.
28. **Last-word accent in headings.** The `<em>` word in headings must be the differentiator — the word that makes THIS heading unique among siblings. Accenting the last word by default (or programmatically) produces generic, decorative styling instead of meaningful emphasis. If the accented word appears in multiple headings in the same document (e.g., "Religion" in a religion project), it's wrong — accent the lens word instead.
