# Paper-Drive: How These Research Projects Work

> A methodology document capturing the end-to-end workflow used for the Agentic LLM Survey and GenAI 2026 Outlook projects. Written to inform a future `paper-drive` skill.

---

## What Is a Paper-Drive Project?

A paper-drive project starts with a research question and builds toward a publishable paper (or set of papers) through a disciplined sequence: literature collection → source assessment → deep reading → per-section deep-dives → synthesis → paper drafts → presentations.

The key insight: **the deep-dives are the research, not just deliverables.** Each section deep-dive forces you to confront whether your sources actually support your claims, where they contradict each other, and what's missing. The papers and slides are downstream artifacts of that confrontation.

---

## Project Structure

Every paper-drive project lives in a subfolder with this structure:

```
ai/{project-name}/
├── .project/
│   ├── changelog.md       # Session-by-session timeline
│   ├── todo.md            # Deliverables plan + source adequacy table
│   └── methodology.md     # How the research was conducted (written at end)
├── notes/
│   ├── 00-synthesis.md    # Cross-section synthesis notes
│   ├── 01-{section}.md    # Per-section markdown deep-dive
│   ├── 02-{section}.md
│   └── ...
├── literature-collection.md   # Master source list with key data points
├── {project}.slides.html      # Slide deck (reading-assist template)
├── survey-paper.html          # Rendered paper
├── survey-paper.md            # Paper draft (markdown)
├── index.html                 # Project landing page
├── s1-{name}.dd.html          # Section 1 deep-dive (reading-assist template)
├── s2-{name}.dd.html          # Section 2 deep-dive
└── ...
```

The root `index.html` links all entry points. The parent repo's root index links to the project's `index.html`.

---

## The Workflow (7 Phases)

### Phase 0: Framing

**Input:** A research question or area of interest.  
**Output:** A `literature-collection.md` skeleton with section structure.

Steps:
1. User states the research question or area
2. Identify **dimensions** — the 4-9 axes the survey will cover
3. Name the sections (these become the deep-dive units)
4. Create the project directory structure
5. Do a broad web search sweep (3-5 searches) to populate initial sources
6. Write `literature-collection.md` with sources organized by section, each entry recording: source name, key data points, date
7. Identify **tensions** — places where sources directly contradict each other. These are the most interesting findings and often become a paper of their own.
8. Commit and push. The lit collection is the first deliverable.

**Decisions at this phase:**
- How many sections? (4-9 is the sweet spot; more than 9 means you need sub-projects)
- Is this a **technical survey** (reading papers deeply) or a **discourse survey** (what people are saying)? This affects source types and reading depth.
- What papers do you expect to write? (survey paper, tensions paper, scenarios paper, etc.)

### Phase 1: Source Assessment (Per-Section, Before Building)

**Input:** The literature collection for one section.  
**Output:** A verdict: adequate or not. If not, specific gaps identified and searched.

**This is the most important discipline in the entire workflow.** Before building any section deep-dive, ask:

1. **How many sources do I have?** Minimum 5-6 for a standalone deep-dive. 3 or fewer = not enough.
2. **What do they cover well?** List the sub-topics with good coverage.
3. **What's missing?** Be specific: "I have no primary data on X" not "I need more sources."
4. **Are there canonical references I'm missing?** (Stanford AI Index for AI trends, WEF for employment, Pew/KPMG for public opinion, Epoch AI for compute)
5. **For a discourse survey:** Do I have both sides of the debate? Every tension needs sources on each side.
6. **For a technical survey:** Do I have the primary papers, not just secondary commentary?

**If inadequate:** Search for specific gaps. Add to literature collection. Re-assess. Only proceed when adequate.

**Update the TODO source adequacy table** with the verdict for each section.

### Phase 2: Reading

**Input:** Adequate sources for one section.  
**Output:** A markdown deep-dive (`notes/{NN}-{name}.md`).

For **web sources** (industry reports, blog posts, news articles):
- Fetch the full page via `web_fetch`
- Extract key claims, data points, quotes (paraphrased)
- Note the source's perspective and potential bias

For **academic papers** (arXiv, journals):
- Download PDF via `curl`
- Extract text via PyMuPDF
- Three reading tiers: full (short/high-impact), deep (40-70%, skip related work/proofs), extraction (abstract + key results only)

For **survey/report data** (Stanford AI Index, KPMG, Pew, etc.):
- Find the summary/key findings page
- Extract specific numbers with methodology notes
- Note sample size, geography, date range

**The markdown deep-dive structure:**
```markdown
# S{N}: {Section Name}

> One-line summary of what this section covers.

**Sources:** N (list them)
**Adequacy:** Verdict and any notes

---

## 1. {First sub-topic}
{Synthesis across sources, not source-by-source}

## 2. {Second sub-topic}
...

## N. What Sources Agree On
{Bulleted list}

## N+1. Where Sources Disagree
{Bulleted list with sources on each side}
```

The markdown is the **working document** — it's where the thinking happens. It should be honest about what sources say and don't say.

### Phase 3: HTML Deep-Dive Build

**Input:** Completed markdown for one section.  
**Output:** An interactive HTML deep-dive (`s{N}-{name}.dd.html`).

Uses the reading-assist skill's **deep-dive template** (three-panel: sidebar nav, summary center, detail right). Built via Python script that injects three JavaScript arrays:

```javascript
const sections = [
  { num: '01', short: 'Label', title: 'Full <em>Title</em>' },
  ...
];
const summaries = [ `<p>...</p>`, ... ];
const details = [ `<h3>...</h3><p>...</p>`, ... ];
```

**Key constraints:**
- Body must be empty — JS builds entire DOM
- Template CSS and JS copied verbatim from reading-assist reference
- Hero content (logo, badge, title, subtitle) patched into the template JS string
- 6-10 sections per deep-dive
- Each summary: 2-3 paragraphs, fits in center panel without scrolling
- Each detail: 3-5 sub-sections with headers, lists, callout boxes

**Common bugs:**
- HTML in body AND JS building DOM = double rendering (blank page)
- Single `/` instead of `//` for JS comments (template artifact)
- Unescaped backticks or `${` inside template literal strings
- `const sections[]` array missing or malformed

### Phase 4: Forward Citation Sweep (Optional, for Technical Surveys)

**Input:** Key papers from the literature collection.  
**Output:** Additional papers found via citation tracking.

Uses Semantic Scholar API:
```
GET https://api.semanticscholar.org/graph/v1/paper/ArXiv:{ID}/citations
    ?fields=title,year,publicationDate&limit=50
```

Selection criteria for new papers:
1. Direct relevance to taxonomy/framework
2. Novel findings that change or strengthen conclusions
3. Recency (published after initial reading)

Also: supplementary arXiv keyword searches for recent months.

### Phase 5: Synthesis & Paper Drafts

**Input:** All section deep-dives completed.  
**Output:** Paper draft(s) in markdown + rendered HTML.

Paper types that emerge naturally from the workflow:
- **Survey paper:** Comprehensive overview with per-section summaries, unified framework
- **Tensions paper:** Where sources contradict each other and what that means
- **Scenarios paper:** Forward-looking, comparing different predictions
- **Position paper:** Your thesis, backed by the evidence

**Paper structure** (for argument-style survey):
1. Abstract (written last, ~250 words)
2. Introduction (the thesis)
3. Method (how you conducted the survey)
4. Sections 3-N (one per taxonomy axis, leading with strongest quantitative result)
5. Synthesis (key findings, research agenda)
6. References

The paper HTML uses a separate template: sidebar nav, Crimson Pro/Source Sans 3 typography, light/dark toggle.

### Phase 6: Slides

**Input:** Completed paper draft.  
**Output:** Slide deck HTML (`{project}.slides.html`).

Uses reading-assist skill's **slide deck template** (Crimson Pro/IBM Plex Mono/Source Sans 3). Structure mirrors the paper:

- Title slide
- TOC with taxonomy diagram (SVG)
- One section divider + 1-2 content slides per section
- Synthesis / key findings
- Research agenda
- Closing slide

**Every content slide has an SVG diagram.** Citation tooltips on key claims (superscript `[N]` with hover showing full reference).

Target: 20-30 slides. One idea per slide.

### Phase 7: Index Page & Methodology

**Input:** All deliverables complete.  
**Output:** `index.html` landing page, `.project/methodology.md`.

The index page links everything: paper (HTML + markdown), slides, section deep-dives, literature collection, project management files. Uses the deep-dive template's design system.

Methodology written last — documents how the research was actually conducted, including what broke and how it was fixed, what was excluded and why, and limitations.

---

## The Source Adequacy Discipline

This is the workflow's most important innovation. The rule:

> **Never build a section deep-dive without first assessing whether your sources are sufficient. If they aren't, search for what's missing. Only proceed when adequate.**

The assessment is recorded in `.project/todo.md` in a table:

| Section | Current Sources | Adequate? | Gaps |
|---------|----------------|-----------|------|
| S1 | 8 | ✅ | Done |
| S2 | 3 | ❌ | Need: X, Y, Z |

This prevents the most common failure mode: writing confidently from insufficient evidence. It also creates a natural checkpoint where the human can redirect ("skip S2, prioritize S5") based on what's actually available.

---

## Git Discipline

Every phase transition gets a commit with a descriptive message. The commit history serves as an execution trace. Key patterns:

- Literature collection: `"GenAI 2026: initial literature collection (51 sources)"`
- Section completion: `"S1: LLMs & Foundation Models — deep-dive + markdown (8 sources)"`
- Bug fixes: `"Fix S1: add missing sections[] array (caused JS error)"`
- Checkpoints: `"Checkpoint: S1 complete, S2 assessed (insufficient)"`

Push after every commit. The repo is both the deliverable and the audit trail.

---

## What Makes This Different from Just Writing

1. **Source assessment before building** — forces honesty about evidence
2. **Tensions as first-class findings** — disagreements between sources are the most valuable output
3. **Dual-format outputs** — markdown (machine-readable, searchable) + HTML (human-readable, interactive)
4. **Incremental building** — each section is a standalone deliverable; the paper is synthesized from completed sections, not written from scratch
5. **Transparent methodology** — changelog, TODO, commit history all document the process
6. **Reading-assist templates** — consistent, professional HTML output without per-project design work

---

## Estimated Effort Per Section

| Phase | Time (with Claude) | Output |
|-------|-------------------|--------|
| Source assessment | 5-10 min | Verdict + gap searches |
| Reading (web sources) | 10-20 min | Extracted data points |
| Reading (papers, per paper) | 15-30 min | Notes per paper |
| Markdown deep-dive | 10-15 min | 2-5K words |
| HTML deep-dive build | 5-10 min | 40-60K HTML |
| **Per section total** | **30-60 min** | **Markdown + HTML** |

For a full project (8 sections + paper + slides): ~8-12 hours of active work across 2-4 sessions.

---

## Skill Trigger Phrases

A future `paper-drive` skill should trigger on:
- "survey what people are saying about X"
- "write a paper on X"
- "do a literature review of X"
- "build a research project on X"
- "what does the discourse say about X"
- "create a survey of X"
- Mention of "deep-dive" + "sections" + "paper"
- References to an existing paper-drive project ("continue the GenAI outlook")
