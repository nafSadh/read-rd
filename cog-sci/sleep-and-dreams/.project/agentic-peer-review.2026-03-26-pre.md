# Agentic Peer Review — Sleep & Dreams

**Reviewed:** 2026-03-25
**Reviewer:** Claude Opus 4.6 (automated peer review)
**Project path:** `cog-sci/sleep-and-dreams/`

---

## Overall Assessment

**Grade: A-**

This is a well-executed paper-drive project covering sleep science and dream research across six coherent dimensions. The literature collection is substantial (57 sources), the deep-dives are consistently structured, the survey paper is standalone with proper inline citations, and the slide deck is a genuine complement rather than a rehash. The project demonstrates strong source-first discipline (literature collection built before deep-dives), honest treatment of contested claims (Walker's popularization, glymphatic controversy, dream theory pluralism), and a clear editorial voice. The primary weaknesses are a reliance on secondary/popular sources where primary literature exists, some acknowledged gaps in the literature collection that were never filled, and the absence of a dedicated tensions paper despite the project's strong tension-identification instincts.

---

## Completeness Scorecard

| Component | Status | Notes |
|-----------|--------|-------|
| `.project/methodology.md` | Complete | Clear research question, scope boundaries, source strategy, exclusion list |
| `.project/changelog.md` | Complete | Two sessions documented with decisions and verification steps |
| `.project/todo.md` | Complete | All items checked, optional future work identified |
| `literature-collection.md` | Complete | 57 sources, 6 sections, gap analysis per section, tension table, statistics |
| `index.html` | Complete | Section listing, status badges, key tensions, deliverable cards, theme toggle |
| Overview deep-dive | Complete | `overview.dd.html` with 6 sections, SVG diagrams |
| Section deep-dives (6) | Complete | S1-S6 all present, 7-8 subsections each, stat blocks, feature grids, callouts |
| `dd-shared.css` + `dd-shared.js` | Complete | Shared scaffold for all section deep-dives |
| Research notes (7) | Complete | `00-synthesis.md` through `06-disorders.md` |
| Survey paper | Complete | `survey-paper.html` — standalone, 96 links, 3 SVGs, 28 superscript citations, 6 tension cards, section source footers |
| Survey slides | Complete | `survey-slides.html` — 13 slides (changelog says 21), 10 SVGs, theme toggle |
| Audio overview | Present | `overview.mp3` exists |
| Tensions paper | Not started | Listed as optional future work |

---

## Content Quality

### Source Assessment

**Strengths:**
- Source date range spans 1977-2026, including genuinely current material (Cell 2024, multiple 2025 papers, one 2026 review)
- Each section identifies its own gaps honestly (e.g., "Gaps: Borbely primary 1982 paper directly, Siegel 2009 alternative evolutionary theory")
- The tension table in the literature collection is a standout feature, capturing six genuine scientific disputes with both sides represented
- Source statistics are tracked (34 peer-reviewed, 12 journalism, 11 reference)

**Weaknesses:**
- Several acknowledged gaps were never addressed across sessions: Siegel (2009), Wilson & McNaughton (1994 -- primary), Domhoff's neurocognitive model, Voss et al. (2009), Stickgold (2005), Morin et al. CBT-I meta-analysis, Haar Horowitz et al. dream engineering primary papers
- Some sources are lower-tier: Calm.com, Neurolaunch, BPS Medical, Careica Health. These are used for accessible summaries but cited alongside PMC and Cell papers without source-quality differentiation
- Walker's "Why We Sleep" is treated simultaneously as an organizing framework and a source with known factual problems -- the project notes this tension well but still leans on Walker's framework throughout S1

### Synthesis Quality

**Strengths:**
- The cross-section synthesis (`00-synthesis.md`) identifies a genuinely insightful meta-pattern: the "sleep science pipeline problem" paralleling the attachment-theory folk distortion pattern
- The identification of orthosomnia (obsessive sleep optimization) as an ironic consequence of sleep science popularization shows sophisticated thinking
- The central unresolved question -- whether the glymphatic system is THE unifying explanation or one of several -- is correctly identified as the field's biggest open question
- Cross-section connections are mapped (S1->S3, S2->S6, S4->S3, S5->S6)

**Weaknesses:**
- The synthesis stays at the level of identifying tensions rather than attempting to adjudicate them. This is appropriate for a survey but means the project has more descriptive than analytical depth
- No engagement with the philosophy of science question: what *would* a resolution of the dream function debate look like? What kind of evidence would be decisive?

### Survey Paper Quality

**Strengths:**
- Fully standalone (0 references to dd.html files)
- 96 hyperlinks, 28 superscript citations with hover tooltips
- 3 SVG diagrams (Two-Process Model, Dream Theories Timeline, and at least one more)
- 6 tension cards distributed across sections
- Section source footers for traceability
- Wikipedia-style citation system with numbered references
- Sidebar navigation with scroll tracking

**Weaknesses:**
- The abstract, while well-written, could more clearly state the paper's thesis (that sleep is irreducibly multi-functional) up front rather than building to it
- Some sections of the paper closely mirror the deep-dive summaries rather than offering a distinct synthesis voice

### Slide Deck Quality

**Strengths:**
- 10 SVG diagrams (more than the paper)
- Proper slide-deck UX (arrow keys, click/swipe, theme toggle)
- Section dividers provide structure

**Weaknesses:**
- Changelog claims 21 slides but grep finds 13 `class="slide"` elements -- possible discrepancy worth verifying
- Slides may duplicate paper content rather than presenting a distinct narrative arc optimized for presentation

---

## Strengths

1. **Source-first discipline.** Literature collection was built before deep-dives, with source adequacy assessed per section. This is the paper-drive methodology executed correctly.

2. **Honest treatment of contested claims.** Walker's popularization is used but flagged (Guzey critique noted). The glymphatic system is presented with both the excitement of discovery and the thinness of human evidence. Dream theories are presented as genuinely unresolved rather than favoring one.

3. **Strong tension identification.** Six tensions are tracked across the project (function of sleep, why we dream, sleep need, lucid dreaming status, insomnia treatment, blue light as villain). The literature collection tension table is especially good.

4. **Complete deliverable set.** Every planned deliverable is present: literature collection, 7 deep-dives (overview + 6 sections), notes, survey paper, slides, index page. The project metadata is clean.

5. **Current sources.** Multiple 2024-2026 papers are cited, including the Cell 2024 glymphatic breakthrough, 2025 human demonstration, and 2026 lucid dreaming meta-analysis.

6. **Cross-project awareness.** The synthesis notes reference the attachment-theory project's "folk distortion" pattern, showing awareness of recurring patterns across the cog-sci domain.

---

## Weaknesses

1. **Acknowledged source gaps left unfilled.** Each section identifies missing foundational papers (Siegel 2009, Wilson & McNaughton 1994, Voss et al. 2009, Morin et al. CBT-I meta-analysis, etc.) but these were never retrieved. For a 57-source project, filling 6-8 more gaps would have strengthened the foundation materially.

2. **Mixed source quality without stratification.** Calm.com, Neurolaunch, and Careica Health appear alongside Cell and Science papers. While each serves a purpose (accessibility), the literature collection does not distinguish source tiers. A quality column (e.g., Tier 1: primary research, Tier 2: review/meta-analysis, Tier 3: science journalism, Tier 4: popular/reference) would strengthen credibility.

3. **Single-session construction.** The entire project was built in one session (March 25, 2026), then the survey paper and slides added in a second session the same day. This limits the iterative refinement that multi-session projects benefit from -- no "sleep on it" period for a project literally about sleep.

4. **Slide count discrepancy.** The changelog claims 21 slides, but the HTML contains 13 slide elements. This should be verified and the changelog corrected if needed.

5. **No tensions paper.** The project's strongest analytical contribution is its tension identification, but this remains distributed across the survey paper and literature collection. A dedicated tensions paper would elevate the project from survey to analysis.

6. **Methodology notes synthesis paper as incomplete.** The methodology deliverables checklist shows "[ ] Synthesis paper" -- which may or may not be the same as the survey paper. If different, this is an undelivered component.

---

## Recommendations

1. **Fill the acknowledged source gaps.** Prioritize Siegel (2009) for evolutionary alternatives, Wilson & McNaughton (1994) for hippocampal replay primacy, and Morin et al. for CBT-I evidence base. These are the most-cited papers in their respective subfields.

2. **Add source quality tiers to the literature collection.** A simple Tier 1/2/3 column would help readers (and future sessions) assess how well-grounded each claim is.

3. **Verify and correct the slide count.** Either the changelog or the HTML needs updating to resolve the 21-vs-13 discrepancy.

4. **Write the tensions paper.** The project has already done the hard work of identifying six genuine scientific disputes. A dedicated paper that structures each tension with evidence, stakes, and possible resolution criteria would be the highest-value next deliverable.

5. **Reconcile methodology deliverables.** The unchecked "Synthesis paper" in methodology.md should be either checked (if the survey paper fulfills it) or clearly distinguished from the survey paper.

6. **Consider a second-pass session.** Re-reading the deep-dives and survey paper after a gap would likely surface opportunities for tighter prose, stronger transitions, and deeper analytical claims -- especially in the synthesis/conclusion sections.
