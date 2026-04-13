# Agent Tracking — read-rd

> **Rule**: Every sub-agent spawned in this repo must be logged here. See `CLAUDE.md` and `.project/AGENTS.md` for full instructions.

---

# NPOV & Scholastic Rigor Review — Agent Tracking
**Started**: 2026-03-27
**Completed**: 2026-03-27
**Goal**: Remove personal POV injection, ensure logical consistency & scholastic rigor across all paper-drives and deep-dives

## Agents

| # | ID | Scope | Status | Notes File |
|---|-----|-------|--------|------------|
| 1 | cog-sci-1 | attachment-theory, brain-energy, dream-incorporation | DONE | cog-sci/{attachment-theory,brain-energy,dream-incorporation}/claude-npov-rvw.md |
| 2 | cog-sci-2 | fashionable-despair, religion-psychology, science-of-humor | DONE | cog-sci/{fashionable-despair,religion-psychology,science-of-humor}/claude-npov-rvw.md |
| 3 | cog-sci-3 | sleep-and-dreams, stoicism-in-practice | DONE | cog-sci/{sleep-and-dreams,stoicism-in-practice}/claude-npov-rvw.md |
| 4 | ai | agentic-lm-survey, genai-2026-outlook | DONE | ai/{agentic-lm-survey,genai-2026-outlook}/claude-npov-rvw.md |
| 5 | anthro | flag-history, religion-today | DONE | anthro/{flag-history,religion-today}/claude-npov-rvw.md |
| 6 | craft | art-of-typography, constructed-languages, science-of-music | DONE | craft/{art-of-typography,constructed-languages,science-of-music}/claude-npov-rvw.md |
| 7 | philosophy | paradoxes, persuasion-survey, stoicism-landscape, sophies-world-* | DONE | philosophy/{paradoxes,persuasion-survey,stoicism-landscape,sophies-world-companion,sophies-world-reader}/claude-npov-rvw.md |
| 8 | physics-scifi | the-cosmos, retrocausal-emotion, time-travel-fiction | DONE | physics/the-cosmos/claude-npov-rvw.md, sci-fi-te/{retrocausal-emotion,time-travel-fiction}/claude-npov-rvw.md |
| 9 | self | audhd, career, wellbeing, how-to-know-a-person | DONE | self/claude-npov-rvw.md |
| 10 | misc | hiking/bay-area, standalone dd.html files | DONE | hiking/bay-area/claude-npov-rvw.md |

## Final Summary
- **Total files edited**: 92
- **Total insertions/deletions**: 247 / 248 (near-perfect 1:1 replacements)
- **Review notes written**: 25 (in respective project directories as claude-npov-rvw.md)

### Issue breakdown (approximate across all agents)
- **TONE**: ~60% of fixes — editorial superlatives, enthusiast language, informal register
- **POV**: ~25% of fixes — second-person "you/your", first-person "we/our"
- **RIGOR**: ~10% of fixes — uncited statistics, unsupported claims, overstatements
- **BIAS**: ~5% of fixes — one-sided framing, geographic skew, product favoritism

### Cleanest projects (no/minimal issues)
- physics/the-cosmos (0 changes)
- philosophy/paradoxes (minimal)
- cog-sci/brain-energy (minimal)

### Most issues found
- ai/agentic-lm-survey (Anthropic product favoritism, uncited revenue figures)
- cog-sci/fashionable-despair (editorial voice throughout)
- sci-fi-te/retrocausal-emotion (second-person address in physics explanations)

### Logical consistency
No contradictions or broken arguments found in any project. Structure and methodology are sound across the board.

---

# Paper-Drive Build Agents

## Active
| # | Date | Agent ID | Task | Status | Output |
|---|------|----------|------|--------|--------|
| 11 | 2026-03-27 | waffle-evolution | Build anthro/waffle-evolution paper-drive (survey+tensions+position+7 DDs) | running | anthro/waffle-evolution/ |
| 12 | 2026-03-27 | atrophy-decisions | Build cog-sci/atrophy-decisions paper-drive (survey+tensions+position+8 DDs) | running | cog-sci/atrophy-decisions/ |

## Completed
| # | Date | Agent ID | Task | Status | Output |
|---|------|----------|------|--------|--------|
| 13 | 2026-03-27 | bananas-foster | Build anthro/bananas-foster paper-drive | done | anthro/bananas-foster/ (7 DDs + survey) |
| 14 | 2026-03-27 | ice-cream-culture | Build anthro/ice-cream-culture paper-drive | done | anthro/ice-cream-culture/ (7 DDs + survey) |
| 15 | 2026-04-01 | april-fools-cont | April fools: survey slides + position paper + index update | done | Already complete from prior session |
| 16 | 2026-04-10 | mml-c4-notes | Write study notes for MML C4 (Matrix Decompositions) | done | study/ml-math/notes/c4-matrix-decompositions.md |
| 17 | 2026-04-10 | mml-c5c7-notes | Write study notes for MML C5 + C7 | done | study/ml-math/notes/c5-vector-calculus.md, c7-continuous-optimization.md |
| 18 | 2026-04-10 | mml-c6-notes | Write study notes for MML C6 | done | study/ml-math/notes/c6-probability-distributions.md |
| 19 | 2026-04-10 | mml-c8-notes | Write study notes for MML C8 | done | study/ml-math/notes/c8-models-data.md |
| 20 | 2026-04-10 | mml-c9-notes | Write study notes for MML C9 | done | study/ml-math/notes/c9-linear-regression.md |
| 21 | 2026-04-10 | mml-c10-notes | Write study notes for MML C10 | done | study/ml-math/notes/c10-pca.md |
| 22 | 2026-04-10 | mml-c11-notes | Write study notes for MML C11 | done | study/ml-math/notes/c11-gmms.md |
| 23 | 2026-04-10 | mml-c12-notes | Write study notes for MML C12 | done | study/ml-math/notes/c12-svms.md |
| 24 | 2026-04-10 | mml-c2-dd | Build interactive page for MML C2 | done | study/ml-math/c2-linear-algebra.dd.html |
| 25 | 2026-04-10 | mml-c3-dd | Build interactive page for MML C3 | done | study/ml-math/c3-analytic-geometry.dd.html |
| 26 | 2026-04-10 | mml-c4-dd | Build interactive page for MML C4 | done | study/ml-math/c4-matrix-decompositions.dd.html |
| 27 | 2026-04-10 | mml-c5-dd | Build interactive page for MML C5 | done | study/ml-math/c5-vector-calculus.dd.html |
| 28 | 2026-04-10 | mml-c6-dd | Build interactive page for MML C6 | done | study/ml-math/c6-probability-distributions.dd.html |
| 29 | 2026-04-10 | mml-c7-dd | Build interactive page for MML C7 | done | study/ml-math/c7-continuous-optimization.dd.html |
| 30 | 2026-04-10 | mml-c8-dd | Build interactive page for MML C8 | done | study/ml-math/c8-models-data.dd.html |
| 31 | 2026-04-10 | mml-c9-dd | Build interactive page for MML C9 | done | study/ml-math/c9-linear-regression.dd.html |
| 32 | 2026-04-10 | mml-c10-dd | Build interactive page for MML C10 | done | study/ml-math/c10-pca.dd.html |
| 33 | 2026-04-10 | mml-c11-dd | Build interactive page for MML C11 | done | study/ml-math/c11-gmms.dd.html |
| 34 | 2026-04-10 | mml-c12-dd | Build interactive page for MML C12 | done | study/ml-math/c12-svms.dd.html |
