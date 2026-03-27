# Agentic Peer Review — Constructed Languages Survey

**Reviewed:** 2026-03-26 (Round 2)
**Reviewer:** Claude Opus 4.6 (automated peer review)
**Project path:** `craft/constructed-languages/`
**Prior review:** 2026-03-25 (Round 1) -- archived as `agentic-peer-review.2026-03-26-pre.md`

---

## Overall Assessment

**Stage:** Complete -- all core deliverables are built and functional.

| Criterion | Grade | Notes |
|-----------|-------|-------|
| Literature Collection | **A** | 55 sources across 6 sections, well-organized with adequacy self-assessment. Unchanged since R1 |
| Source Diversity | **A-** | Academic, encyclopedic, primary, interview, and popular sources. Wikipedia reliance acknowledged in methodology |
| Research Notes | **A** | 7 notes files with consistent structure, "agree/disagree" sections, and genuine critical engagement |
| Deep-Dive HTMLs | **A-** | All 7 deep-dives now exist (overview + s1-s6). Three-panel layout with inline citations, stat boxes, timelines, SVGs. Section deep-dives are slightly smaller than overview (~29-36 KB vs ~82 KB) but functional and content-complete |
| Synthesis & Cross-Cutting Analysis | **A** | "Six Tensions" framework and "Five Cross-Cutting Findings" remain the intellectual backbone. Well-integrated across all deliverables |
| Papers | **A-** | Survey paper (survey-paper.html, ~35 KB) built around Six Tensions framework with 29 inline citations and full reference list. Sidebar navigation, scroll spy, theme toggle |
| Slide Decks | **N/A** | Not started. Noted in todo.md as unbuilt |
| Project Metadata | **A-** | Methodology, changelog, and todo are present, accurate, and internally consistent. Todo correctly reflects current state |
| Index Page | **A** | Clean design, all links functional, status badges accurate. Theme toggle, tensions summary |
| Overall | **A-** | A complete, well-executed survey project. All core deliverables built. Strong research, strong synthesis, strong presentation |

---

## Completeness Scorecard

| Deliverable | Expected | Actual | Status |
|-------------|----------|--------|--------|
| `literature-collection.md` | 1 | 1 | Complete |
| Research notes (markdown) | 7 | 7 | Complete |
| `index.html` | 1 | 1 | Complete |
| `overview.dd.html` | 1 | 1 | Complete (82 KB, 710 lines) |
| Section deep-dives (`s1-s6.dd.html`) | 6 | 6 | Complete (29-36 KB each, 156-194 lines) |
| `survey-paper.html` | 1 | 1 | Complete (35 KB, 185 lines, 29 citations) |
| `.project/methodology.md` | 1 | 1 | Complete |
| `.project/changelog.md` | 1 | 1 | Complete and accurate |
| `.project/todo.md` | 1 | 1 | Complete, reflects current status |
| SVG diagrams / images | Several | 14+ | SVGs embedded in HTML across all 7 deep-dives. 2 raster images (hero.png, s01-scripts.png) |
| Audio overview | 0-1 | 1 | `overview.mp3` present |
| Generation script | 0-1 | 1 | `_generate_sections.py` present, used to build s1-s6 from overview template |
| Slide deck | 0-1 | 0 | Not started |

---

## Content Quality

### Literature Collection
Unchanged from R1. The 55 sources remain well-chosen and span from Hildegard von Bingen (1150s) through Dijkstra's EWD 667 (1978) to Marc Brooker's 2025 LLM response. The tabular format with ID codes is consistent and the self-assessment of adequacy per section is good practice. Each section has 8-11 sources, adequate for survey-level coverage.

### Research Notes
The strongest textual asset. Each note follows a consistent structure: epigraph, source count, 7-9 substantive subsections, "What Sources Agree On," and "Where Sources Disagree." The last two sections demonstrate genuine critical engagement. The synthesis note identifies non-obvious cross-cutting themes (the Control Paradox, Programming Languages as the Most Successful Conlangs).

### Section Deep-Dives (NEW since R1)
All six section deep-dives now exist on disk and are functional. Each uses the three-panel reading-assist layout (sidebar, summary center, detail right) generated from a shared template via `_generate_sections.py`. Features include:
- Wikipedia-style inline citations with hover tooltips (7-10 per deep-dive)
- Stat boxes with key figures
- Timelines (s1-history, s3-media, s4-relativity, s5-sign, s6-programming)
- Feature grids (s3: Na'vi features, s6: Dijkstra vs Brooker)
- Verdict panels with pro/con layout
- SVG content (s2-tolkien has 2 SVGs including language family tree)
- Theme toggle and responsive design
- Sidebar navigation with scroll-spy

The section deep-dives are smaller than the overview (~29-36 KB vs ~82 KB) because they are generated with inline JavaScript content rather than hand-built HTML. This is a reasonable trade-off for consistency.

### Survey Paper (NEW since R1)
The synthesis paper is well-structured around the Six Tensions framework. It includes 7 content sections (Abstract, Control Paradox, Communities, Sapir-Whorf, Natural vs. Designed, Programming, Six Tensions) plus a Methods/Limitations section and a 29-item reference list. Each section includes tension cards that connect to the broader framework. The paper draws from all six dimensions of the survey and integrates citations from across the full literature collection.

### Writing Quality
Prose remains clear, engaging, and well-paced across all deliverables. The project successfully avoids both dry encyclopedic tone and excessive informality. The "Six Tensions" framing gives the survey a thesis beyond mere catalog.

### Visual Design
All HTML deliverables share a cohesive visual language: consistent typography (EB Garamond, Jost, IBM Plex Mono), light/dark theme support, gradient overlays, and grain texture. The section deep-dives use CSS custom properties extensively, enabling consistent theming. The self-contained inline CSS/JS pattern (no external dd-shared.css/js) is a deliberate architectural choice that trades some duplication for zero-dependency deployability.

---

## Strengths

1. **Dramatic progress since R1.** The project went from "excellent foundation, critical gaps" to "complete project" in one session. All six section deep-dives and the survey paper were built, closing the major weaknesses identified in R1.

2. **Exceptional research design.** The six-dimension scope remains creative and well-justified. The programming-languages-as-conlangs angle is original and genuinely adds value to the survey.

3. **Strong synthesis paper.** The survey-paper.html organizes 55 sources into a coherent argument via the Six Tensions framework. The inline citations (29) with hover tooltips are well-implemented. The paper reads as a genuine synthesis, not a rehash of the notes.

4. **Consistent template architecture.** The `_generate_sections.py` script enabled consistent generation of all six section deep-dives from the overview template. This ensures visual and structural consistency while reducing manual effort.

5. **Internal consistency restored.** The R1 review flagged metadata contradictions between changelog, todo.md, and index.html. These are now resolved. The todo.md accurately reflects the current state, the changelog documents all phases, and all index.html status badges correctly read "done."

6. **Citation infrastructure.** Every deep-dive and the survey paper include Wikipedia-style inline citations with hover tooltips linking to sources from the literature collection. This is a significant quality marker that connects the HTML deliverables back to the source material.

7. **Good source diversity.** Each section draws on multiple source types: encyclopedic, academic, popular, and primary. No section relies on a single source type alone.

---

## Weaknesses

1. **No slide deck.** The todo.md acknowledges this gap. For a paper-drive project, a presentation artifact would round out the deliverables. This is a minor gap given the strength of the other deliverables.

2. **Section deep-dives lack section-specific images.** Only `hero.png` and `s01-scripts.png` exist as raster images. The image-banana-claude.md notes a prompt mismatch between v1 and v2 styles. The deep-dives rely on SVGs and CSS for visual interest rather than custom illustrations per section.

3. **CSS/JS duplication across deep-dives.** Each deep-dive is self-contained (~10-12 KB of inline CSS). While this is a deliberate architectural decision for zero-dependency deployability, it means any design change must be propagated to 7+ files. The `_generate_sections.py` script mitigates this for the section deep-dives but not for the overview or survey paper.

4. **Toki Pona, Ithkuil, and Lojban sourcing gap persists.** R1 flagged that the S4 notes discuss Toki Pona, Ithkuil, and Lojban as thought-experiment conlangs, but none appear in the literature collection. This remains unfixed. If they are discussed in the notes, they should be sourced.

5. **Survey paper omits some tensions in body text.** The paper devotes full sections to T2 (Creator vs. Community), T3 (Strong vs. Weak Whorf), T4 (Natural vs. Designed), and T5 (Formal vs. Natural Notation), and mentions T1 (Art vs. Utility) and T6 (Minimalism vs. Richness) in the final tensions section. But T1 and T6 lack the same depth of treatment as the other four tensions.

6. **Overview deep-dive uses different CSS formatting from section deep-dives.** The overview has hand-formatted CSS (indented, readable) while the section deep-dives use minified CSS. This is a cosmetic difference only, but it means the overview template is harder to compare directly with its generated children.

---

## Recommendations

1. **Add Toki Pona and Ithkuil to the literature collection.** These are discussed substantively in the S4 notes (Section 5: "The Conlang as Thought Experiment") but have no corresponding entries in `literature-collection.md`. Adding 2-3 sources would close this gap.

2. **Consider a slide deck.** The Six Tensions framework is well-suited to a presentation format. Each tension could be one slide with concrete examples from the survey. This would be the highest-impact remaining deliverable.

3. **Expand T1 and T6 treatment in the survey paper.** Currently these two tensions get only brief mention in Section 06. Even one paragraph each with citations would bring them to parity with the other four tensions.

4. **Add section-specific hero images.** The image-banana-claude.md file documents planned images but only two exist. Even one sketch-style image per section deep-dive would improve visual engagement.

5. **Consider adding Guy Steele's "Growing a Language" (1998).** This was flagged in R1 and remains relevant. Steele's OOPSLA talk is a natural primary source for S6 that directly addresses how programming languages grow through community adoption -- connecting to the Control Paradox theme.

6. **Document the generation script.** The `_generate_sections.py` script is a key architectural component but has minimal documentation. A brief comment block explaining how to regenerate section deep-dives (and when to do so) would help future maintainability.
