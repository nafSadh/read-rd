# Methodology — The Architecture of Influence

**Document version:** March 24, 2026
**Scope:** Complete methodology for the persuasion survey, adapted from the methodology of the "Agentic LLMs in the Wild" survey in `ai/agentic-lm-survey/.project/methodology.md`.

---

## 1. Research Question

**Starting point:** The researcher had already produced a deep-dive on Dark Psychology & Manipulation (`philosophy/dark-psychology.dd.html`) covering the Dark Triad, manipulation tactics, Cialdini's principles, coercive control, and social engineering. Separately, the agentic LLM survey documented MCP security vulnerabilities (23–41% attack amplification) and prompt injection bypass rates (78%+). The question: can we trace a single thread from Aristotle's *Rhetoric* through dark psychology to LLM-powered persuasion, showing that the underlying grammar of influence has been invariant for 2,350 years while the speed and scale of deployment has undergone a discontinuity?

**Framing decision:** Unlike a narrow NLP survey (Durmus et al. 2024, which covers only LLM persuasion) or a psychology textbook (Cialdini, which covers only human influence), we chose a *full-spectrum argument paper* that bridges philosophy, psychology, computer science, and law. The thesis: every act of persuasion — ancient or AI-generated — operates through the same channels Aristotle identified, but LLMs represent the first time persuasion can be automated, personalized, interactive, and deployed at scale simultaneously.

---

## 2. Taxonomy Design

### 2.1 The Five Axes

The taxonomy was designed to tell a story: understand the grammar (RHETORIC), see how it's weaponized (EXPLOIT), learn the defenses (DEFEND), confront the AI discontinuity (AUTOMATE), assess governance responses (GOVERN).

| Axis | Scope | Key Differentiator |
|------|-------|-------------------|
| **RHETORIC** | Classical foundations: Aristotle → Cialdini → Kahneman | The invariant grammar underlying all persuasion |
| **EXPLOIT** | Dark psychology, cognitive biases, manipulation | How the grammar gets weaponized |
| **DEFEND** | Stoicism → CBT → inoculation → prebunking | 2,300 years of counter-technology |
| **AUTOMATE** | LLM persuasion, deepfakes, synthetic media | The machine persuader — the discontinuity |
| **GOVERN** | EU AI Act, TAKE IT DOWN Act, technical defenses | Legal and normative responses |

### 2.2 Relationship to Existing Work

- **Extends** the existing dark-psychology.dd.html deep-dive (which covers EXPLOIT partially)
- **Parallels** the agentic LLM survey's structure (5 sections, deep-dive HTMLs + paper draft)
- **Bridges** the agentic survey's OPERATE section (security) with the psychology of manipulation
- **Novel contribution:** No existing survey connects ancient rhetoric → modern psychology → AI persuasion → governance in a single arc

### 2.3 Validation

The taxonomy was validated by checking whether each source maps cleanly to one axis:
- Aristotle's *Rhetoric* → RHETORIC (not EXPLOIT, because Aristotle treated rhetoric as morally neutral)
- Cialdini's *Influence* → RHETORIC (principles) + EXPLOIT (weaponized use) — span indicates a real boundary
- Stoic texts → DEFEND (unambiguous)
- LLM persuasion papers → AUTOMATE (unambiguous)
- EU AI Act → GOVERN (unambiguous)

---

## 3. Literature Collection

### 3.1 Source Types

Unlike the agentic LLM survey (which drew primarily from arXiv papers), this survey draws from five source types:

| Source Type | Examples | Coverage |
|-------------|----------|----------|
| Ancient texts | Aristotle *Rhetoric*, Plato *Gorgias*, Epictetus *Discourses* | RHETORIC, DEFEND |
| Psychology books | Cialdini *Influence*, Kahneman *Thinking Fast and Slow*, Robertson *Philosophy of CBT* | RHETORIC, EXPLOIT, DEFEND |
| Academic papers | Salvi et al. 2024, Bai et al. 2025, Hackenburg et al. 2025, Roozenbeek et al. 2022 | AUTOMATE, DEFEND |
| Legislation | EU AI Act, TAKE IT DOWN Act, DEFIANCE Act, Colorado AI Act | GOVERN |
| Industry/news | Arup deepfake fraud, Cambridge Analytica, Google/Jigsaw prebunking campaigns | AUTOMATE, EXPLOIT, DEFEND |

### 3.2 Search Strategy

Web searches used domain-specific queries:
- "LLM persuasion capabilities research 2025 2026 survey" (not "AI influence")
- "Aristotle rhetoric persuasion Cialdini influence ethics history"
- "stoicism resilience cognitive behavioral therapy inoculation misinformation prebunking"
- "AI deepfake synthetic media persuasion regulation governance 2025 2026"
- "cognitive biases manipulation dark psychology systematic review"
- "persuasion with large language models survey Salvi taxonomy"

### 3.3 Selection Criteria

Sources were prioritized if they:
1. Are foundational to the field (Aristotle, Cialdini, Kahneman, McGuire)
2. Provide quantitative results from controlled experiments (Salvi et al., Bai et al., Hackenburg et al.)
3. Document real-world incidents (Arup deepfake, Cambridge Analytica)
4. Represent current legislation or governance frameworks (EU AI Act, TAKE IT DOWN Act)
5. Bridge multiple axes of the taxonomy (Robertson bridging DEFEND and RHETORIC)

Sources were deprioritized if they:
- Were narrow application studies without generalizable findings
- Covered domains already well-surveyed without structural change
- Were opinion pieces without empirical evidence

---

## 4. Reading Process

### 4.1 Reading Strategy (Three Tiers)

Adapted from the agentic LLM survey methodology:

**Primary sources (ancient texts, foundational books):** Not read cover-to-cover in this session. Key passages, arguments, and frameworks extracted from Stanford Encyclopedia of Philosophy, secondary analyses, and direct quotes from known passages. Honest accounting: we're working from well-established scholarly consensus about these texts, not fresh close reads.

**Modern academic papers:** Read via web search results, abstracts, and key findings. Papers from Nature Communications, Science, PNAS, and Scientific Reports were assessed through their published findings. No PDFs were downloaded and text-extracted in this session (unlike the agentic LLM survey).

**Legislation and governance documents:** Assessed via legal analysis blogs, official government summaries, and news coverage. Primary legislative text was not read line-by-line.

### 4.2 What Was Extracted Per Source

For each source:
- **Key claims with specific numbers** (e.g., "51% persuasiveness boost," "77,000 participants," "46 states enacted legislation")
- **Frameworks or taxonomies** (e.g., Aristotle's three appeals, Cialdini's seven principles, ELM central/peripheral routes)
- **Connections to other sources in the collection**
- **Claims that support or challenge our thesis**

### 4.3 Honest Accounting

This survey's reading depth is shallower per-source than the agentic LLM survey, but broader in scope:
- **No PDFs downloaded or text-extracted** — all sources assessed via web research
- **Ancient texts assessed via secondary scholarship** — we rely on well-established interpretations
- **Quantitative claims cross-checked across multiple search results** — e.g., the "77,000 participants" figure appears consistently across Science, Oxford University press release, and arXiv versions
- **Legislation assessed via legal analysis, not primary text**

---

## 5. Writing Process

### 5.1 Deep-Dives (Interactive HTML)

Each of the five taxonomy sections is written as an interactive HTML deep-dive using the reading-assist skill's deep-dive template:
- Three-panel layout (sidebar nav, summary center, expandable detail right)
- 8 subsections per deep-dive with summary + detail views
- Components: stat bars, chip tags, feature grids, callout boxes, verdict panels, security warnings
- CSS and JS copied verbatim from the template; only content arrays differ

### 5.2 Survey Paper Draft

Written as a single markdown file, structured as an argument paper:
- Thesis-driven (not a catalog)
- Each section leads with its strongest quantitative result or historical claim
- Synthesis section ties all five axes together

### 5.3 Supporting Artifacts

- `README.md` — project overview
- `persuasion-survey-proposal.md` — full proposal with taxonomy, section breakdown, differentiation
- `literature-collection.md` — bibliography organized by taxonomy section
- `.project/methodology.md` — this document
- `index.html` — landing page

---

## 6. Tooling

### 6.1 Infrastructure

- **Repository:** github.com/nafSadh/read-rd, subfolder `philosophy/persuasion-survey/`
- **Deployment:** GitHub Pages at nafsadh.github.io/read-rd/philosophy/persuasion-survey/
- **Build system:** Deep-dive HTMLs built by injecting content arrays into template CSS/JS
- **No PDF extraction:** Unlike the agentic LLM survey, this project did not download/extract PDFs

### 6.2 Claude's Role

Same model as the agentic LLM survey — Claude handles web research, content writing, HTML building, and project management. Human provides research question, strategic direction, scope decisions, and quality feedback.

---

## 7. Limitations

1. **No primary source reading:** Ancient texts and modern papers were assessed via secondary sources, web search results, and published abstracts/findings. No PDFs were text-extracted.

2. **Cross-disciplinary breadth vs. depth tradeoff:** Covering 2,350 years across philosophy, psychology, CS, and law means no single domain is covered at the depth a specialist would expect.

3. **Recency of AI persuasion research:** The LLM persuasion field is moving fast. Papers from January–March 2026 may not yet be indexed by Semantic Scholar.

4. **Legislation snapshot:** Governance section reflects the legislative landscape as of March 2026. Bills in progress (DEFIANCE Act) may have changed status.

5. **Single-session execution:** Like the agentic LLM survey, this entire project was executed in a single extended conversation.

---

## 8. Reproducibility

The project is version-controlled at github.com/nafSadh/read-rd with all artifacts in `philosophy/persuasion-survey/`. Any future researcher can:

1. Start from `literature-collection.md` as a reading list
2. Download the cited papers from their published venues
3. Verify quantitative claims against original sources
4. Extend coverage by reading sources we assessed only via secondary analysis
5. Update the governance section as legislation evolves
