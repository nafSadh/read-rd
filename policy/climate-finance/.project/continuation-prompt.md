# Continuation Prompt — Climate Finance

## Repo & Location
- **Repo:** github.com/nafSadh/read-rd
- **Project subfolder:** `policy/climate-finance/`
- **Live URL:** read.sadh.app/policy/climate-finance/
- **PAT:** (provide at runtime)

## What's Completed
- Project infrastructure: index.html, .project/ files, literature-collection.md
- Literature collection: 72 sources across 8 sections (all at adequacy)
- **S1: Geopolitics** — deep-dive complete (7 sections, 12 sources, 6 SVGs)
- **S2: NCQG** — deep-dive complete (7 sections, 8 sources, 3 SVGs)

## What's Next

### Remaining Deep-Dives (in suggested order)
1. **S3: Multilateral Funds & MDB Reform** (9 sources) — WB 45% target, GCF, greenwashing debate, Evolution Roadmap
2. **S5: Loss & Damage** (8 sources) — FRLD operationalization, $250M BIM, US withdrawal, justice framing
3. **S4: Bilateral & Development Finance** (13 sources) — ODA collapse, debt-for-climate swaps, JETP cancellations
4. **S6: Carbon Markets & Article 6** (9 sources) — VCM crisis, CDM legacy, first Article 6 credits misfiring
5. **S7: Domestic Public Spending** (7 sources) — IRA rollback, EU Green Deal, China state investment
6. **S8: Adaptation vs. Mitigation Gap** (6 sources) — UNEP AGR 2025 ($310-365B need vs $26B flows)

### After All Sections
- Overview deep-dive (synthesis across all 8 dimensions)
- Survey paper + slides
- Tensions paper + slides (if warranted)

## Template System
- CSS cached at `/home/claude/survey/template_css.txt`
- JS DOM builder cached at `/home/claude/survey/template_js.txt`
- Hero markers: badge, title, subtitle, sidebar logo (all use `← CHANGE` comments)
- Content: `sections[]`, `summaries[]`, `details[]` arrays
- Python builder script pattern established in S1/S2 builds

## Key Patterns Established
- 7 sections per deep-dive
- Detail panels target 6-10K chars with h3 sub-sections, SVG diagrams, callout boxes, source links
- SVGs: 400px wide, background rect matching viewBox, IBM Plex Mono for labels
- Cross-references between sections using `<a href="sN-name.dd.html" title="Section Name">SN</a>`
- Source links: first mention per detail panel
- Commit after each section deep-dive; push immediately; update index status badges

## Key Tensions Surfaced So Far
1. $300B "tripling" vs "insultingly low" — same number, opposite framing
2. Grants vs loans — 58% of adaptation finance is debt; NCQG doesn't distinguish
3. Greenwashing — WB 45% climate target but hundreds of tenuous projects
4. US absence creating austerity cover rather than compensatory increases
5. China's voluntary counting — strategic ambiguity as leverage
6. No adaptation subgoal — mitigation wins every budget war
7. Inflation erosion — $300B in 2035 worth far less than today

## Related Projects
- `physics/the-cosmos/` — 7-section deep-dive with overview
- `cog-sci/fashionable-despair/` — full paper-drive with survey paper + slides
- `ai/genai-2026-outlook/` — full paper-drive with section loop
