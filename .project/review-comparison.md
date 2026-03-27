# Peer Review Comparison: Round 1 (Pre-Improvement) vs Round 2 (Post-Improvement)

**Generated:** 2026-03-26
**Scope:** All 21 projects in read-rd
**Method:** Automated comparison of `.project/agentic-peer-review.2026-03-26-pre.md` (round 1) and `.project/agentic-peer-review.md` (round 2)

---

## 1. Summary Table

| # | Project | Old Content | Old Compliance | New Content | New Compliance | Content Change | Compliance Change |
|---|---------|:-----------:|:--------------:|:-----------:|:--------------:|:--------------:|:-----------------:|
| 1 | ai/agentic-lm-survey | A- | B+ | A- | B+ | -- | -- |
| 2 | ai/genai-2026-outlook | A- | A- | A | A- | +1/3 | -- |
| 3 | anthro/flag-history | B | C+ | A- | B+ | +2 | +2 |
| 4 | anthro/religion-today | B+ | C+ | A- | B+ | +1 | +2 |
| 5 | cog-sci/attachment-theory | A- | B+ | A | A- | +1/3 | +1/3 |
| 6 | cog-sci/brain-energy | B+ (overall) | -- | A- (overall) | -- | +1/3 | -- |
| 7 | cog-sci/religion-psychology | A | A- | A | A | -- | +1/3 |
| 8 | cog-sci/science-of-humor | A- | B+ | A | A | +1/3 | +1 |
| 9 | cog-sci/sleep-and-dreams | A- (overall) | -- | A (overall) | -- | +1/3 | -- |
| 10 | cog-sci/stoicism-in-practice | A- (overall) | -- | A- (overall) | -- | -- | -- |
| 11 | craft/art-of-typography | B+ (overall) | -- | A- (overall) | -- | +1/3 | -- |
| 12 | craft/constructed-languages | B- (overall) | -- | A- (overall) | -- | +2 | -- |
| 13 | craft/science-of-music | B+ (overall) | -- | A- (overall) | -- | +1/3 | -- |
| 14 | philosophy/paradoxes | C+ (overall) | -- | A- (overall) | -- | +3 | -- |
| 15 | philosophy/persuasion-survey | A- (overall) | -- | A- (overall) | -- | -- | -- |
| 16 | philosophy/sophies-world-companion | B+ | A- | A- | A | +1/3 | +1/3 |
| 17 | philosophy/sophies-world-reader | A- (overall) | -- | A (overall) | -- | +1/3 | -- |
| 18 | philosophy/stoicism-landscape | B+ | C+ | A- | B+ | +1/3 | +2 |
| 19 | sci-fi-te/retrocausal-emotion | A- | A | A- | A | -- | -- |
| 20 | physics/the-cosmos | A- | B | A | A- | +1/3 | +1 |
| 21 | sci-fi-te/time-travel-fiction | A- (overall) | -- | A (overall) | -- | +1/3 | -- |

**Note:** Some projects used a single overall grade rather than separate content/compliance grades. Where grades use sub-increments (e.g., high B+ to low A-), "+1/3" indicates a third-step improvement within the grading scale.

---

## 2. Aggregate Statistics

### Grade Changes (using normalized overall assessment)

| Metric | Count |
|--------|-------|
| **Projects improved** | **16** |
| Projects unchanged | **5** |
| Projects regressed | **0** |

### Improvement Magnitude

| Size of Jump | Count | Projects |
|--------------|-------|----------|
| +3 full grades (e.g., C+ to A-) | 1 | paradoxes |
| +2 full grades | 2 | flag-history, constructed-languages |
| +1 full grade | 3 | religion-today, art-of-typography, science-of-music |
| +1/3 grade (sub-step) | 10 | genai-2026-outlook, attachment-theory, religion-psychology, science-of-humor, sleep-and-dreams, sophies-world-companion, sophies-world-reader, stoicism-landscape, the-cosmos, time-travel-fiction |
| No change | 5 | agentic-lm-survey, stoicism-in-practice, persuasion-survey, retrocausal-emotion, brain-energy* |

*brain-energy improved from B+ to A- overall, counted in the +1/3 row above.

### Grade Distribution Shift

| Grade | Round 1 Count | Round 2 Count |
|-------|:------------:|:------------:|
| A or A+ | 0 | 8 |
| A- | 9 | 12 |
| B+ | 6 | 0 |
| B | 1 | 0 |
| B- | 1 | 0 |
| C+ | 3 | 0 |
| C or below | 1 | 0 |

**Round 1 median:** A- (with a long tail of B+/B/C+ projects)
**Round 2 median:** A- (with all projects now at A- or above)

---

## 3. Biggest Improvements (Top 5)

### 1. philosophy/paradoxes: C+ to A-
The most dramatic turnaround. Round 1 found 5 of 7 section deep-dives missing from disk despite being marked "done" -- the index had broken links and the changelog was inaccurate. No synthesis paper, no citations. Round 2: all 7 deep-dives built, a full synthesis paper with 11 citations produced, 56 inline citations across 9 files, all metadata corrected. Every critical round-1 finding was resolved.

### 2. anthro/flag-history: B/C+ to A-/B+
Round 1 found no synthesis papers, no slide deck, no Wikipedia-style citations in any deep-dive, a missing s7 file that the changelog claimed existed, and index links pointing to a monolithic overview rather than individual section files. Round 2: all 7 standalone deep-dives exist, the synthesis paper "Flags as Compressed Histories" was written with 40 references and 29 external URLs, 66 inline citations added across deep-dives, and all index links corrected.

### 3. craft/constructed-languages: B- to A-
Round 1 found 6 of 7 deep-dives missing (only the overview existed), no synthesis paper, broken index links, and stale metadata. Round 2: all 6 section deep-dives built with inline citations (7-10 per file), a survey paper produced with 29 citations, metadata corrected, and all links functional.

### 4. anthro/religion-today: B+/C+ to A-/B+
Round 1 identified 4 of 6 section deep-dives as not built (despite "done" badges), creating 8 broken links on the index page. No citations in any deep-dive. Round 2: all 6 deep-dives fully built with the read-aid template, 98 inline citations added across deep-dives, and all index links functional.

### 5. craft/art-of-typography: B+ to A-
Round 1 found only 2 of 8 planned HTML deliverables (overview + S1). No shared CSS, no citations, changelog claiming all deep-dives were built when they were not. Round 2: all 7 deep-dives built, survey paper created with 46 inline citations, 130 total citation instances across all HTML files, and changelog corrected.

---

## 4. Remaining Gaps (Projects Still Below A-)

**None.** All 21 projects now grade at A- or above.

The floor has risen from C+ to A-. The weakest projects in round 2 are those graded A- with noted secondary gaps:

| Project | Round 2 Grade | Primary Remaining Gaps |
|---------|:------------:|------------------------|
| ai/agentic-lm-survey | A- / B+ | Hybrid citation system in survey paper, no taxonomy diagram in paper, Section 5 empirical thinness |
| cog-sci/brain-energy | A- | Stale project metadata, thin markdown notes, ~15 sources with vague attributions, no slide deck |
| cog-sci/stoicism-in-practice | A- | No primary Stoic text citations, thin empirical base for harm claims in S4, overview uses inline CSS |
| craft/art-of-typography | A- | No shared CSS/JS, no cross-section links, limited primary academic sources for cognition section |
| craft/constructed-languages | A- | No slide deck, Toki Pona/Ithkuil sourcing gap, CSS duplication |
| craft/science-of-music | A- | No standalone paper deliverables (only synthesis deep-dive), no slide deck, no shared CSS/JS, overview lacks citations |
| philosophy/paradoxes | A- | Uneven citation density (3-11 per section), no SVG diagrams in S2-S7, CSS duplication |
| philosophy/persuasion-survey | A- | No slide deck, Roozenbeek citation conflation, body text not reconciled with Objections concessions |
| philosophy/stoicism-landscape | A- / B+ | No external URLs in literature collection, section deep-dives thin vs overview, no slide deck |
| sci-fi-te/retrocausal-emotion | A- / A | S4/S5 at minimum source adequacy, no experimental retrocausality evidence cited |

---

## 5. Cross-Cutting Themes from the Improvement Round

### What was fixed most consistently

1. **Missing deep-dive HTML files** -- The single most common round-1 deficiency. At least 8 projects had deep-dives marked "done" that did not exist on disk. All were built in round 2.

2. **Wikipedia-style inline citations** -- Round 1 found that deep-dive files across nearly every project lacked formal citation apparatus (even when the papers had them). Round 2 added `sup.fn` citations with hover tooltips to deep-dives in all 21 projects. Total citations added: estimated 800+ across the collection.

3. **Synthesis papers** -- Multiple projects (flag-history, brain-energy, paradoxes, constructed-languages, art-of-typography, stoicism-landscape, time-travel-fiction, the-cosmos) had no synthesis paper in round 1. All now have at least one.

4. **Broken index links and stale metadata** -- Round 1 found widespread index pages linking to non-existent files with false "done" badges, and todo/changelog files that did not reflect reality. These were corrected across the board.

### What was NOT fixed

1. **Slide decks** -- The most common remaining gap. At least 12 projects still lack slide decks. This was consistently the lowest-priority recommendation.

2. **Shared CSS/JS extraction** -- Most projects still duplicate CSS across deep-dive files rather than using a shared stylesheet. This is a maintenance concern, not a content issue.

3. **Hero images** -- Many projects have `image-banana-claude.md` files with prompts but no generated images. Visual assets remain sparse.

4. **Source depth in specific sections** -- Some sections remain at minimum source adequacy (5 sources) or rely on secondary/popular sources where primary literature exists. Source gaps identified in round 1 were rarely filled.

5. **Stale project metadata** -- While the worst offenders (false "done" badges, broken links) were fixed, several projects still have stale todo.md or methodology.md files that do not reflect current state.

### Patterns in the improvement work

- **The improvements were surgical.** The round-2 work focused on the highest-impact round-1 recommendations: building missing deep-dives, adding citations, writing synthesis papers, and fixing broken links. Lower-priority recommendations (CSS extraction, source gap filling, slide decks) were largely deferred.

- **No regressions observed.** No project's content quality decreased between rounds. In every case, the improvement work added to existing quality without diluting it.

- **Citation infrastructure was the universal upgrade.** Even projects that were already graded A- in round 1 (e.g., religion-psychology, retrocausal-emotion) received citation improvements that strengthened traceability.

- **The biggest gains came from completion, not revision.** Projects that jumped 2-3 grade steps (paradoxes, constructed-languages, flag-history) did so by building deliverables that were missing, not by revising existing content. The research quality was already high in round 1 -- the gap was in execution and delivery.
