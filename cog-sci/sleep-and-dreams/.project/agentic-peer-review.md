# Agentic Peer Review — Sleep & Dreams

**Reviewed:** 2026-03-26 (Round 2)
**Reviewer:** Claude Opus 4.6 (automated peer review)
**Project path:** `cog-sci/sleep-and-dreams/`
**Previous review:** 2026-03-25 (Round 1, grade A-)

---

## Overall Assessment

**Grade: A**

This project has meaningfully improved since Round 1. The two most impactful changes are the addition of a dedicated tensions paper (`tensions-paper.html`) and the retrofit of Wikipedia-style inline citations across all 7 deep-dive files. Together, these address the two highest-priority Round 1 recommendations: the tensions paper elevates the project from descriptive survey to analytical contribution, and the citation retrofit brings source traceability to the deep-dives that previously lacked it. The slide count discrepancy has been corrected. Two Round 1 weaknesses persist: the acknowledged source gaps in the literature collection remain unfilled, and the methodology deliverables checklist still shows "Synthesis paper" as unchecked. These are minor relative to the overall quality. The project now delivers a complete paper-drive package: 57 sources, 7 deep-dives with inline citations, a standalone survey paper, a slide deck, a tensions paper, research notes, and clean project metadata.

---

## Completeness Scorecard

| # | Component | Status | Notes |
|---|-----------|--------|-------|
| 1 | `.project/methodology.md` | Complete | Clear research question, scope, source strategy, exclusions. Deliverables checklist has one unchecked item ("Synthesis paper") |
| 2 | `.project/changelog.md` | Complete | 3 sessions documented with decisions, deliverables, and verification steps |
| 3 | `.project/todo.md` | Complete | All items checked (including citations retrofit, tensions paper). Slide count corrected. Optional future work identified |
| 4 | `literature-collection.md` | Complete | 57 sources, 6 sections, gap analysis per section, tension table, collection statistics |
| 5 | `index.html` | Complete | Section listing, status badges, key tensions, deliverable cards (survey + tensions papers), theme toggle |
| 6 | Overview deep-dive | Complete | `overview.dd.html` with 6 sections, SVG diagrams, 6 inline citations |
| 7 | Section deep-dives (6) | Complete | S1-S6 all present, 7-8 subsections each, stat blocks, feature grids, callouts. 36 inline citations across 6 files |
| 8 | Survey paper | Complete | `survey-paper.html` -- standalone (0 dd.html refs), 96 links, 28 superscript citations, 3 SVGs, 6 tension cards, section source footers |
| 9 | Survey slides | Complete | `survey-slides.html` -- 13 slides, 10 SVGs, theme toggle. Changelog now correctly says 13 |
| 10 | Tensions paper | Complete | `tensions-paper.html` -- 6 tension blocks with vs-grids, 11 superscript citations, SVG tension map, sidebar nav, theme toggle |

---

## Content Quality

### Source Assessment

**Strengths:**
- 57 sources spanning 1977-2026, with genuinely current material (Cell 2024 glymphatic breakthrough, 2025 human demonstration, 2026 lucid dreaming meta-analysis)
- Each section's gap analysis is honest and specific (e.g., S1 acknowledges missing Siegel 2009 and Borbely primary paper)
- The tension table in the literature collection captures six genuine scientific disputes with both positions represented
- Source statistics tracked: 34 peer-reviewed, 12 science journalism, 11 reference

**Weaknesses (persisting from Round 1):**
- Acknowledged source gaps remain unfilled: Siegel (2009), Wilson & McNaughton (1994), Domhoff's neurocognitive model, Voss et al. (2009), Stickgold (2005), Morin et al. CBT-I meta-analysis, Haar Horowitz et al. dream engineering. These are foundational papers in their subfields
- No source quality stratification: Calm.com and Careica Health appear alongside Cell and Science without tier differentiation
- Walker's "Why We Sleep" continues to serve as both organizing framework and flagged-problematic source; this tension is noted but not resolved

### Synthesis Quality

**Strengths:**
- The cross-section synthesis identifies the "sleep science pipeline problem" as a meta-pattern, paralleling the attachment-theory folk distortion analysis from another project
- Orthosomnia identified as an ironic consequence of sleep science popularization -- a genuinely insightful observation
- The central unresolved question (glymphatic as unifying explanation vs. one of many) is correctly framed
- Cross-section connections mapped: S1 to S3 (evolution to dream function), S2 to S6 (brain to disorders), S4 to S3 (lucid dreaming to dream theories), S5 to S6 (modern life to disorders)

**Weaknesses:**
- Synthesis remains descriptive rather than adjudicative -- tensions are identified but the project does not attempt to weigh which positions have stronger evidentiary support
- No engagement with what kind of evidence would resolve the dream function debate (philosophy of science question)

### Survey Paper Quality

**Strengths:**
- Fully standalone: 0 references to dd.html files
- 96 hyperlinks, 28 superscript citations with hover tooltips
- 3 SVG diagrams integrated into paper body
- 6 tension cards distributed across sections
- Section source footers for traceability
- Sidebar navigation with scroll tracking
- Well-crafted CSS with light/dark theme support

**Weaknesses:**
- Some sections closely mirror deep-dive summaries rather than offering a distinct synthesis voice
- The abstract builds to the thesis (sleep is irreducibly multi-functional) rather than stating it up front

### Tensions Paper Quality (New in Round 2)

**Strengths:**
- 6 tension blocks with structured vs-grids presenting both sides
- 11 superscript citations with hover tooltips
- SVG tension map diagram
- Consistent design language with survey paper (sidebar nav, theme toggle, same CSS architecture)
- Each tension block includes evidence for both positions and identifies stakes

**Weaknesses:**
- Does not include resolution criteria for any tension (what evidence would tip the balance)
- The tensions paper is structured as exposition rather than argument -- it presents disputes but does not evaluate which side has more support

### Slide Deck Quality

**Strengths:**
- 13 slides with 10 SVG diagrams
- Proper slide-deck UX (arrow keys, click/swipe navigation, theme toggle)
- Section dividers provide clear structure

**Weaknesses:**
- Content substantially overlaps with survey paper sections rather than presenting a distinct narrative arc optimized for oral presentation

### Deep-Dive Citation Quality (New in Round 2)

**Strengths:**
- 42 inline citations across 7 dd.html files, all with hover tooltips linking to sources
- Citation CSS added to `dd-shared.css` for consistent styling
- Citations are placed at the point of claim, not just at section level

**Weaknesses:**
- Distribution is uneven: S1 has 8 citations, S4 has only 3. The lucid dreaming section cites 8 sources in the literature collection but only 3 in the deep-dive
- Overview has 6 citations across 6 sections (averaging 1 per section), which is thin for summary-level claims that aggregate multiple sources

---

## Strengths

1. **Responsive to review.** Three of six Round 1 recommendations were addressed: tensions paper written, slide count corrected, Wikipedia-style citations added across all deep-dives. This demonstrates genuine iterative improvement.

2. **Source-first discipline.** Literature collection was built before deep-dives, with source adequacy assessed per section. This core paper-drive principle is followed correctly.

3. **Honest treatment of contested science.** Walker's popularization is used but flagged (Guzey critique). The glymphatic system is presented with discovery excitement and evidentiary thinness. Dream theories are presented as genuinely unresolved. The tensions paper formalizes this intellectual honesty.

4. **Complete deliverable set.** Every component of a paper-drive project is present: literature collection, 7 deep-dives with inline citations, survey paper, slide deck, tensions paper, 7 research notes, index page, project metadata (methodology, changelog, todo).

5. **Current sources.** The project incorporates 2024-2026 research including the Cell 2024 glymphatic mechanism paper, 2025 human glymphatic demonstration, and 2026 lucid dreaming meta-analysis. This is not a project built from textbook knowledge alone.

6. **Consistent design system.** All HTML deliverables (7 deep-dives, survey paper, tensions paper, slides, index) share a coherent visual language with light/dark theme support, consistent typography (EB Garamond, Jost, IBM Plex Mono), and citation styling.

---

## Weaknesses

1. **Acknowledged source gaps still unfilled.** This was the top Round 1 recommendation and remains unaddressed. The literature collection identifies 7+ missing foundational papers (Siegel 2009, Wilson & McNaughton 1994, Voss et al. 2009, Stickgold 2005, Morin et al., Domhoff, Haar Horowitz et al.) across all six sections. For a 57-source project, adding these would strengthen the scholarly foundation without major effort.

2. **Methodology deliverables not reconciled.** The methodology checklist still shows "[ ] Synthesis paper" as unchecked. The survey paper likely fulfills this role, but the checkbox has not been updated. This creates ambiguity about whether an additional deliverable was planned.

3. **Source quality tiers absent.** The literature collection still does not distinguish between source tiers. Primary research papers (Cell, Science, PNAS) sit alongside pop-science summaries (Calm.com, Neurolaunch, Careica Health) without quality indicators. A simple tier column would strengthen credibility.

4. **Uneven citation density in deep-dives.** S4 (lucid dreaming) has only 3 inline citations despite 8 sources in the literature collection. The overview averages 1 citation per section. More consistent citation density would strengthen traceability.

5. **Tensions paper lacks resolution criteria.** The tensions paper presents 6 disputes effectively but does not specify what evidence would resolve each one. Adding a "what would settle this" section to each tension would transform it from exposition to analytical contribution.

6. **Single-day construction.** All three changelog sessions occurred on March 25, 2026. While this does not necessarily reduce quality, it means the project has not benefited from iterative refinement across separate working days.

---

## Recommendations

1. **Fill the top 3 source gaps.** Prioritize Siegel (2009) for S1 (evolutionary alternatives to Walker's framework), Wilson & McNaughton (1994) for S2 (hippocampal replay -- foundational to memory consolidation claims), and Morin et al. for S6 (CBT-I evidence base). These are the most consequential gaps for the project's credibility.

2. **Check the "Synthesis paper" box in methodology.md** or clarify the distinction. If the survey paper fulfills this role, mark it complete. If not, define what additional work is needed.

3. **Add resolution criteria to the tensions paper.** For each of the 6 tensions, add a short paragraph: "What evidence would resolve this?" This would elevate the tensions paper from descriptive to prescriptive and distinguish it from the survey paper's tension cards.

4. **Equalize citation density in deep-dives.** Bring S4 (lucid dreaming) up from 3 citations to at least 6, matching other sections. Add 1-2 more citations to the overview sections that currently have only 1 each.

5. **Add a source tier column to the literature collection.** A simple classification (Tier 1: primary research / Tier 2: review-meta-analysis / Tier 3: science journalism / Tier 4: popular-reference) would take minimal effort and meaningfully improve the collection's utility.

6. **Consider a gap-filling session on a separate day.** The project would benefit from a session focused solely on retrieving missing sources and updating the sections that cite them, ideally with some time between sessions for perspective.
