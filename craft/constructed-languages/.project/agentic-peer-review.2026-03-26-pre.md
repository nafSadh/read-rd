# Agentic Peer Review — Constructed Languages Survey

**Reviewed:** 2026-03-25
**Reviewer:** Claude Opus 4.6 (automated peer review)
**Project path:** `craft/constructed-languages/`

---

## Overall Assessment

**Stage:** Early-to-mid -- literature collection and notes are complete; HTML deliverables are largely unbuilt.

| Criterion | Grade | Notes |
|-----------|-------|-------|
| Literature Collection | **A** | 55 sources across 6 sections, well-organized, adequacy assessed per section |
| Source Diversity | **A-** | Mix of academic papers, encyclopedic references, primary documents, interviews, and popular sources. Slight over-reliance on Wikipedia for factual grounding, acknowledged in methodology |
| Research Notes | **A** | All 7 notes files (synthesis + 6 sections) are substantive, well-structured, and consistently formatted with "sources agree/disagree" sections |
| Deep-Dive HTMLs | **D** | Only 1 of 7 deep-dives exists on disk (overview.dd.html). The 6 section deep-dives (s1 through s6) are referenced in index.html but do not exist as files |
| Synthesis & Cross-Cutting Analysis | **A** | The "Six Tensions" framework and "Five Cross-Cutting Findings" are genuinely insightful. The synthesis notes demonstrate real analytical work |
| Papers | **N/A** | No synthesis papers exist |
| Slide Decks | **N/A** | No slide decks exist |
| Project Metadata | **B+** | Methodology, changelog, and todo files are present and thoughtful. The todo.md is stale and inaccurate (see Weaknesses) |
| Index Page | **A-** | Clean design with theme toggle, well-organized section listing, tension summary. Links to non-existent deep-dives are broken |
| Overall | **B-** | Excellent research foundation with a critical gap: 6 of 7 planned deep-dives are unbuilt |

---

## Completeness Scorecard

| Deliverable | Expected | Actual | Status |
|-------------|----------|--------|--------|
| `literature-collection.md` | 1 | 1 | Complete |
| Research notes (markdown) | 7 | 7 | Complete |
| `index.html` | 1 | 1 | Complete |
| `overview.dd.html` | 1 | 1 | Complete |
| Section deep-dives (`s1-s6.dd.html`) | 6 | 0 | **Missing** |
| `.project/methodology.md` | 1 | 1 | Complete |
| `.project/changelog.md` | 1 | 1 | Complete |
| `.project/todo.md` | 1 | 1 | Present but stale |
| Synthesis paper | 1 | 0 | Not started |
| Slide deck | 1 | 0 | Not started |
| SVG diagrams / images | Several | 2 | `hero.png`, `s01-scripts.png` present |
| Audio overview | 0-1 | 1 | `overview.mp3` present (bonus) |
| Generation script | 0-1 | 1 | `_generate_sections.py` present |

---

## Content Quality

### Literature Collection
The 55 sources are well-chosen and span a genuine range: from Hildegard von Bingen through Dijkstra's EWD 667 to Marc Brooker's 2025 LLM response. The tabular format with ID codes, source names, key data points, and dates is consistent and useful. The source adequacy self-assessment at the bottom is a good practice. Source count per section (8-11) is adequate for survey-level coverage.

### Research Notes
The notes are the strongest asset of this project. Each section note follows a consistent structure: introductory quote, source count and adequacy assessment, 7-9 substantive subsections, "What Sources Agree On" section, and "Where Sources Disagree" section. The last two sections are particularly valuable -- they demonstrate critical engagement rather than mere summarization.

The synthesis note (`00-synthesis.md`) identifies genuinely interesting cross-cutting themes. The "Control Paradox" (finding #1) and "Programming Languages Are the Most Successful Conlangs" (finding #5) are non-obvious claims that emerge from comparative analysis rather than being present in any single source.

### Overview Deep-Dive
The overview deep-dive is a complete, well-built interactive HTML document (~71 KB) with 8 sections, proper theming, and the three-panel reading-assist layout. It demonstrates the target quality for the missing section deep-dives.

### Writing Quality
Prose across all notes is clear, engaging, and well-paced. The project avoids both dry encyclopedic tone and excessive informality. Specific factual claims are well-grounded (dates, source counts, speaker estimates). The "Six Tensions" framing is an effective rhetorical device that gives the survey a thesis beyond mere catalog.

---

## Strengths

1. **Exceptional research design.** The six-dimension scope (history, Tolkien, media, relativity, sign languages, programming) is creative and well-justified. The programming-languages-as-conlangs angle is original and adds genuine value.

2. **Strong synthesis.** The project does not merely collect and summarize. The tensions framework, cross-cutting findings, and "agree/disagree" sections show real analytical thinking. The connection between Schleyer's control of Volapuk and programming-language governance failures is the kind of insight that justifies a comparative approach.

3. **Consistent methodology.** Every section follows the same structure. Source adequacy is assessed before building. The methodology file honestly acknowledges limitations (English-language bias, Wikipedia reliance, recency bias, novelty of the programming parallel).

4. **Clean index page design.** The `index.html` is well-designed with theme toggle support, clear hierarchy, and the tensions summary section provides a strong reason to read further.

5. **Good source diversity within each section.** Each section draws on multiple source types: encyclopedic, academic, popular, primary. No section relies on a single source type alone.

6. **Audio asset.** The `overview.mp3` file is a useful addition that most paper-drive projects lack.

---

## Weaknesses

1. **Critical deliverable gap: 6 of 7 deep-dives are missing.** The `index.html` links to `s1-history.dd.html` through `s6-programming.dd.html`, but none of these files exist on disk. This is the project's most significant problem. The changelog claims these were built ("Phase 3: Section Deep-Dives (S1-S6)"), but the files are not present. This is either a data-loss issue or the changelog was written prospectively rather than retrospectively.

2. **Stale and inaccurate project metadata.** The `todo.md` describes the status as "Early -- research done, 0 of 6 section deep-dives built" and lists all deep-dives as not built, which contradicts the changelog's claim that they were completed. Meanwhile, the `index.html` marks all sections as "done" with green status badges. The project metadata is internally inconsistent. The todo.md title says "Hand-off" suggesting it was written for session handoff, but its contents do not match the changelog.

3. **No synthesis paper or slide deck.** The paper-drive workflow builds toward publishable papers and presentations. This project has not reached that stage. Given the quality of the notes, a synthesis paper would be straightforward to produce.

4. **Broken links in index.html.** All six section deep-dive links (`s1-history.dd.html` through `s6-programming.dd.html`) are broken because the target files do not exist.

5. **Limited visual assets.** Only `hero.png` and `s01-scripts.png` are present. The changelog references SVG diagrams (timelines, family trees, tension matrices) that presumably exist only within `overview.dd.html`. The section deep-dives, which would contain section-specific SVGs, are missing.

6. **No `dd-shared.css` or `dd-shared.js`.** The todo.md notes these are missing infrastructure. The overview deep-dive appears to be self-contained (inline styles and script), which means each section deep-dive would need to duplicate the full CSS/JS or these shared files need to be created first.

---

## Recommendations

1. **Prioritize building the 6 section deep-dives.** The notes are complete and high-quality. The overview deep-dive provides a working template. The `_generate_sections.py` script may automate much of this. This is the single highest-impact action for the project.

2. **Fix the metadata inconsistency.** Reconcile the changelog, todo.md, and index.html status badges. If deep-dives were lost, note that in the changelog. If they were never built, update the changelog to remove the false Phase 3 claims and change index.html status badges from "done" to "pending" or remove them.

3. **Extract shared CSS/JS.** Before building 6 more deep-dives, extract the common styles and scripts from `overview.dd.html` into `dd-shared.css` and `dd-shared.js`. This will reduce maintenance burden and ensure visual consistency.

4. **Add a synthesis paper.** The synthesis notes are strong enough to support a paper-format HTML. The "Six Tensions" framework would work well as the paper's organizing structure.

5. **Consider adding more primary sources for S6 (Programming).** The methodology acknowledges that the programming-language parallel is novel and that "few sources directly compare conlangs and programming languages." Iverson's Turing Award lecture "Notation as a Tool of Thought" (1979) is referenced indirectly but could be cited as a primary source. Guy Steele's "Growing a Language" (1998 OOPSLA talk) is a natural fit that is currently absent.

6. **Add at minimum a note about Toki Pona.** The S4 notes mention Toki Pona, Ithkuil, and Lojban as thought-experiment conlangs, but none appear in the literature collection. If they are discussed in the notes, they should be sourced.
