# Changelog — GenAI 2026 Outlook

All changes to the GenAI 2026 survey project.

---

## Session: March 24, 2026

### Phase 0: Inception & Literature Collection
- User requested: survey what people are saying/predicting about GenAI across LLMs, multimodal, diffusion, agents, workplace adoption, employment, public perception
- Web research across academic sources, industry reports, analyst predictions, government data, surveys
- Built `literature-collection.md` with **51 sources** across 8 sections + tensions synthesis
- Identified 6 key tensions where sources directly contradict each other

### Phase 1: Overview Deep-Dive
- Built initial overview deep-dive (`genai-2026-overview.dd.html`) covering all 9 dimensions
- Created synthesis notes (`notes/00-synthesis.md`)
- Fixed HTML rendering (body structure conflicted with template JS)

### Phase 2: Project Structure
- Created `.project/` directory (changelog, todo, paper-drive-methodology)
- Planned 8 section deep-dives + papers
- Assessing source adequacy per section before building

### Phase 3: S1 — LLMs & Foundation Models (DONE)
- 8 sources, assessed adequate
- Built `notes/01-llms.md` and `s1-llms.dd.html`

### Phase 4: S2 — Multimodal & Diffusion Models (DONE)
- Assessed: only 3 sources, NOT ENOUGH
- Searched for gaps: video gen landscape, image gen, audio/music gen, world models, deepfakes
- Found 7 additional sources → 10 total
- Breaking news: OpenAI shut down Sora entirely (March 24, 2026)
- Built `notes/02-multimodal.md` (9 sections, 10 sources)
- Built `s2-multimodal.dd.html` (10-section deep-dive)
- Updated `literature-collection.md` with M-04 through M-10

### Phase 5: S3 — AI Agents (DONE)
- Assessed: 7 sources + searched gaps → 10 total
- New sources: production reality (AzureTechInsider), adoption data (Deloitte/G2), MCP ecosystem
- Built `notes/03-agents.md` (9 sections, 10 sources)
- Built `s3-agents.dd.html` (9-section deep-dive, 6 SVG diagrams)
- Key finding: integration, not model quality, is the bottleneck

### Phase 6: S4 — Workplace Adoption & Productivity (DONE)
- Assessed: 7 sources + 3 new (McKinsey, Deloitte 2026, PwC CEO Survey)
- Built `notes/04-workplace.md` and `s4-workplace.dd.html`
- Key finding: 78-88% deploy AI, only 10-39% get enterprise value
- 4 SVG diagrams: adoption-value gap bars, three-survey comparison, value domains, barriers

### Phase 7: S6-S8 (DONE)
- S6: Public Perception & Trust — 5 sources, 6 sections, 1 SVG
  - KPMG 48K study anchor: 66% use, 46% trust, 56% mistakes
- S7: Regulation & Governance — 6 sources (+2 regulation analysis), 7 sections
  - EU AI Act Aug 2026 enforcement, US 45+ state patchwork, sovereignty
- S8: Economics & Infrastructure — 5 sources, 7 sections
  - $500B capex, 9× revenue growth, bubble question

### ALL 8 SECTIONS COMPLETE

### Phase 8: Papers, Slides, Polish (current session)
- SVG font-size CSS override fix: 322 text elements across 6 files
  Root cause: .lbl{font-size:11px} overriding SVG font-size="7" attributes
- S2 detail panels deepened: 10 panels from ❌ 1.6K avg to ⚠️ 3K avg, +3 SVGs
- Cross-reference + source citation links: 145 links across all 8 deep-dives
- Index page rewritten with prose intro and updated tensions
- Survey paper (survey-paper.md): ~4K words, 12 sections
- Tensions paper (tensions-paper.md): ~3.5K words, 6 contradictions
- Scenarios paper (scenarios-paper.md): ~3.5K words, 3 scenarios + signal dashboard
- Slide deck (survey-slides.html): 17 slides, 5 SVG diagrams, arrow-key nav
- paper-drive + read-aid skills updated with session learnings
