# Paper-Drive Skill Audit — March 25, 2026

Audit of all paper-drive projects in `read-rd` against the updated skill (v2, 24 anti-patterns).

## Scoring Key

| Symbol | Meaning |
|--------|---------|
| ✅ | Meets requirement |
| ❌ | Missing / violates requirement |
| ⚠️ | Partial / needs work |
| — | Not applicable |

---

## Summary Table

| Project | Papers | Slides | Source Links | Deliverable Cards | Index Style | DD Complete | Status |
|---------|--------|--------|-------------|-------------------|-------------|-------------|--------|
| **ai/genai-2026-outlook** | ✅ 3 papers | ⚠️ 1 of 3 | ❌ 3-4 each | ❌ | ⚠️ Old layout | ✅ 8/8 | Needs: links, cards, slides |
| **ai/agentic-lm-survey** | ✅ 1 paper | ✅ 1 | ❌ 3 | ❌ | ⚠️ Old layout | ⚠️ 5/? | Needs: links, cards |
| **anthro/religion-today** | ✅ 2 papers | ❌ 0 | ❌ 3 each | ✅ | ✅ | ❌ 2/6 | Needs: links, slides, S3-S6 |
| **anthro/flag-history** | ❌ | ❌ | — | ❌ | ❌ No h2s | ⚠️ 6/? | Incomplete |
| **cog-sci/attachment-theory** | ❌ | ❌ | — | ❌ | ⚠️ | ⚠️ 6/7 | Needs: papers, slides, cards |
| **cog-sci/religion-psychology** | ❌ | ❌ | — | ❌ | ⚠️ | ✅ 6/6 | Needs: papers, slides, cards |
| **cog-sci/science-of-humor** | ❌ | ❌ | — | ❌ | ⚠️ | ❌ 3/7 | Incomplete |
| **cog-sci/sleep-and-dreams** | ❌ | ❌ | — | ❌ | ⚠️ | ✅ 6/6 | Needs: papers, slides, cards |
| **cog-sci/stoicism-in-practice** | ❌ | ❌ | — | ❌ | ⚠️ | ✅ 6/6 | Needs: papers, slides, cards |
| **craft/art-of-typography** | ❌ | ❌ | — | ❌ | ⚠️ | ❌ 1/6 | Incomplete |
| **craft/constructed-languages** | ❌ | ❌ | — | ❌ | ⚠️ | ❌ 0/6 | Incomplete |
| **craft/science-of-music** | ❌ | ❌ | — | ❌ | ⚠️ | ❌ 2/7 | Incomplete |
| **neuro/brain-energy** | ❌ | ❌ | — | ❌ | ⚠️ | ✅ 6/6 | Needs: papers, slides, cards |
| **philosophy/paradoxes** | ❌ | ❌ | — | ❌ | ⚠️ | ❌ 1/7 | Incomplete |
| **philosophy/persuasion-survey** | ❌ | ❌ | — | ❌ | ❌ No h2s | ⚠️ 5/? | Incomplete |
| **philosophy/sophies-world-companion** | — | — | — | ❌ | ❌ Different format | ✅ 7/? | Not paper-drive? |
| **philosophy/sophies-world-reader** | — | — | — | ❌ | ❌ Different format | ⚠️ | Not paper-drive? |
| **philosophy/stoicism-landscape** | ❌ | ❌ | — | ❌ | ⚠️ | ❌ 1/6 | Incomplete |
| **sci-fi-te/retrocausal-emotion** | ❌ | ✅ 1 | — | ❌ | ⚠️ | ✅ 7/7 | Needs: papers, cards |
| **physics/the-cosmos** | ❌ | ❌ | — | ❌ | ⚠️ | ❌ 2/7 | Incomplete |
| **sci-fi-te/time-travel-fiction** | ❌ | ❌ | — | ❌ | ⚠️ | ✅ 6/6 | Needs: papers, slides, cards |

---

## Violations by Category

### 1. No Papers (CRITICAL — 17 of 20 projects)

Papers are the whole point of paper-drive. Only 3 projects have any:

- **ai/genai-2026-outlook** — 3 papers (survey, tensions, scenarios) ✅
- **ai/agentic-lm-survey** — 1 paper (survey) ⚠️ missing tensions paper
- **anthro/religion-today** — 2 papers (survey, tensions) ✅

The remaining 17 projects have zero papers. Projects with completed deep-dives that are ready for papers:

| Priority | Project | DDs Done | Ready for Papers? |
|----------|---------|----------|-------------------|
| 1 | cog-sci/religion-psychology | 6/6 | ✅ Yes |
| 2 | cog-sci/sleep-and-dreams | 6/6 | ✅ Yes |
| 3 | cog-sci/stoicism-in-practice | 6/6 | ✅ Yes |
| 4 | neuro/brain-energy | 6/6 | ✅ Yes |
| 5 | sci-fi-te/time-travel-fiction | 6/6 | ✅ Yes |
| 6 | sci-fi-te/retrocausal-emotion | 7/7 | ✅ Yes (has slides, no paper) |
| 7 | anthro/religion-today | 2/6 | ❌ S3-S6 DDs needed first |

### 2. No Slides (CRITICAL — 17 of 20 projects)

Each paper should have an accompanying slide deck. Only 3 projects have any slides:

- **ai/genai-2026-outlook** — 1 slide deck for 3 papers ⚠️ (should be 3)
- **ai/agentic-lm-survey** — 1 slide deck ✅
- **sci-fi-te/retrocausal-emotion** — 1 slide deck (but no paper!) ⚠️

### 3. Source Links in Papers (CRITICAL — all existing papers fail)

Every paper should have 20+ external source links. Actual counts:

| Paper | External Links | Required |
|-------|---------------|----------|
| genai-outlook/survey-paper.html | 4 | 20+ |
| genai-outlook/tensions-paper.html | 4 | 20+ |
| genai-outlook/scenarios-paper.html | 4 | 20+ |
| agentic-lm-survey/survey-paper.html | 3 | 20+ |
| religion-today/survey-paper.html | 3 | 20+ |
| religion-today/tensions-paper.html | 3 | 20+ |

**Every single existing paper fails the source link density check.** This is the failure mode the updated skill was designed to prevent.

### 4. No Deliverable Cards at Top of Index (19 of 20 projects)

Only `anthro/religion-today` has the `deliverable-grid` / `deliverable-card` layout. All other projects use the old `section-list` layout for papers (if they have papers at all) or have no papers section.

### 5. Incomplete Deep-Dives (10 projects)

Projects where the index lists more sections than have HTML deep-dives:

| Project | Built | Listed | Missing |
|---------|-------|--------|---------|
| anthro/religion-today | 2 | 6 | S3, S4, S5, S6 |
| cog-sci/science-of-humor | 3 | 7 | S4, S5, S6, S7 |
| craft/art-of-typography | 1 | 6 | S2-S6 |
| craft/constructed-languages | 0 | 6 | S1-S6 |
| craft/science-of-music | 2 | 7 | S3-S7 |
| philosophy/paradoxes | 1 | 7 | S2-S7 |
| philosophy/stoicism-landscape | 1 | 6 | S2-S6 |
| physics/the-cosmos | 2 | 7 | S3-S7 |
| cog-sci/attachment-theory | 6 | 7 | S7 |

### 6. Index Style (inconsistent across projects)

- Only religion-today has deliverable cards at top
- genai-2026-outlook uses old Papers & Presentations as section-list (should be cards)
- Many projects mark all sections as "done" even when DDs don't exist on disk (e.g., constructed-languages: 0 DDs, 7 "done")

---

## Projects That May Not Be Paper-Drive

Two projects appear to follow a different pattern:

- **philosophy/sophies-world-companion** — No literature collection, no .project/ metadata, "About This" heading. Appears to be a read-along companion, not a research survey.
- **philosophy/sophies-world-reader** — No literature collection, no .project/ metadata. Appears to be a chapter reader, not a research survey.

These might not need paper-drive treatment.

---

## Recommended Action Plan

### Phase 1: Fix Existing Papers (highest impact, lowest effort)
1. Add source hyperlinks to all 6 existing papers (genai, agentic, religion-today)
2. Add section-sources footers to each paper section
3. Run verification suite on all papers

### Phase 2: Complete Ready Projects (papers + slides for projects with all DDs done)
Priority order:
1. religion-psychology (6/6 DDs)
2. sleep-and-dreams (6/6 DDs)
3. stoicism-in-practice (6/6 DDs)
4. brain-energy (6/6 DDs)
5. time-travel-fiction (6/6 DDs)
6. retrocausal-emotion (7/7 DDs, already has slides)

### Phase 3: Update All Indexes
1. Add deliverable cards to all project indexes
2. Fix status badges to match actual state (several say "done" for unbuilt DDs)
3. Standardize ordering: Deliverables → Overview → Deep-Dives → [project-specific]

### Phase 4: Complete Incomplete Projects
Build remaining deep-dives, then papers + slides:
- religion-today (S3-S6)
- science-of-humor (S4-S7)
- art-of-typography (S2-S6)
- constructed-languages (S1-S6)
- science-of-music (S3-S7)
- paradoxes (S2-S7)
- stoicism-landscape (S2-S6)
- the-cosmos (S3-S7)

### Phase 5: Missing Slides
Add slide decks for every paper. Currently:
- genai-2026-outlook needs 2 more slides (has 1 for 3 papers)
- religion-today needs 2 slides
- All Phase 2 projects need slides alongside their papers
