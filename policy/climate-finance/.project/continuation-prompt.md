# Continuation Prompt — Climate Finance

## Repo & Location
- **Repo:** github.com/nafSadh/read-rd
- **Project subfolder:** `policy/climate-finance/`
- **Live URL:** read.sadh.app/policy/climate-finance/
- **PAT:** (provide at runtime)

## What's Completed (3/8 sections)
- Literature collection: 72 sources, all 8 sections at adequacy
- **S1: Geopolitics** — done (7 panels, 12 sources, 6 SVGs)
- **S2: NCQG** — done (7 panels, 8 sources, 3 SVGs)
- **S3: MDB Reform** — done (7 panels, 9 sources, 2 SVGs)

## What's Next (5 remaining sections)

### Suggested order
1. **S5: Loss & Damage** (8 sources) — FRLD operationalization, BIM $250M, US withdrawal, justice framing
2. **S4: Bilateral & Dev Finance** (13 sources) — ODA collapse, debt-for-climate swaps, JETP cancellations
3. **S6: Carbon Markets & Article 6** (9 sources) — VCM crisis, CDM legacy, first credits misfiring
4. **S7: Domestic Public Spending** (7 sources) — IRA rollback litigation, EU Green Deal, China
5. **S8: Adaptation vs. Mitigation Gap** (6 sources) — UNEP AGR 2025, $26B vs $310-365B need

### After All Sections
- Overview deep-dive
- Survey paper + slides
- Tensions paper + slides

## Template System
- CSS: `/home/claude/survey/template_css.txt`
- JS DOM builder: `/home/claude/survey/template_js.txt` (extract after `// DOM BUILDER` marker)
- Python builder pattern: read CSS + JS, patch hero markers, inject content/details arrays, assemble HTML
- Validate with: `node --check` on extracted JS
- Files at project root: `s{N}-{name}.dd.html`

## Cross-References to Add
When building remaining sections, add links between completed sections:
- S1 ↔ S2: geopolitics shapes NCQG outcome
- S1 ↔ S3: US withdrawal impacts MDB reform
- S2 ↔ S3: NCQG relies on MDB scaling
- S3 → S8: MDB adaptation shortfall (already linked)

## Established Patterns
- 7 sections per deep-dive (consistent across S1-S3)
- Detail panels: 6-10K chars with h3 subs, SVG diagrams, callout boxes
- Source links: first mention per detail panel as `<a href target="_blank">`
- Index updated at each commit with status badge flip + real links
