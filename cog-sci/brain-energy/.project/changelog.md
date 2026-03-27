# Changelog — Brain Energy & Metabolic Psychiatry Project

## Session 1 — 2026-03-25

**What happened:**
- Restructured from single deep-dive (`neuro/brain-energy.dd.html`) to full paper-drive project (`neuro/brain-energy/`)
- Moved existing overview deep-dive to `overview.dd.html` within project directory
- Created literature collection (50 sources across 6 sections) via web search
- Sources span: Palmer's foundational work, mitochondrial meta-analyses, JAMA Psychiatry RCT (2025), Stanford pilot trial, NLRP3/neuroinflammation reviews, gut-brain axis research, BHB epigenetic mechanisms, critical perspectives
- Created project metadata: methodology, todo, changelog
- Defined 6 section deep-dives: Metabolic Theory, Mitochondrial Dysfunction, Psychiatric Applications, Neuroinflammation & Gut-Brain, Interventions, Clinical Evidence & Future Directions
- Built all 6 section deep-dives with full interactive HTML (sidebar nav, detail panels, SVG diagrams, theme toggle)
- Created per-section markdown notes (notes/01-06)
- Created synthesis notes (notes/00-synthesis.md)
- Built project index page following genai-2026-outlook template

**Decisions made:**
- Consolidated from 8 overview sections to 6 thematic deep-dives (merged sources into S6, split inflammation into its own section)
- Critical perspective is a first-class element in S6, not an afterthought
- Gut-brain axis grouped with neuroinflammation (S4) rather than interventions
- BHB epigenetic signaling placed in interventions (S5) as mechanistic support for ketogenic approach
- Existing overview preserved as-is -- serves as project overview

**Project files created:**
- `overview.dd.html` -- moved from `neuro/brain-energy.dd.html`
- `literature-collection.md` -- 50 sources
- `.project/methodology.md` -- research question, scope, source strategy
- `.project/todo.md` -- deliverables plan with source adequacy table
- `.project/changelog.md` -- this file
- `notes/00-synthesis.md` -- cross-section synthesis
- `notes/01-metabolic-theory.md` through `notes/06-clinical-evidence.md`
- `s1-metabolic-theory.dd.html` through `s6-clinical-evidence.dd.html`
- `index.html` -- project index page
