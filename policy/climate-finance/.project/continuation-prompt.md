# Continuation Prompt — Climate Finance

## Repo & Location
- **Repo:** github.com/nafSadh/read-rd
- **Project subfolder:** `policy/climate-finance/`
- **Live URL:** read.sadh.app/policy/climate-finance/
- **PAT:** (provide at runtime)

## What's Completed
- Project structure: index.html, .project/ files, literature-collection.md, notes/00-synthesis.md
- Literature collection: 63 sources across 8 sections
- Source adequacy assessed: 7/8 sections adequate, S4 (Bilateral) thin

## What's Next

### Immediate: Gap-fill S4 (Bilateral & Development Finance)
S4 has only 4 sources. Before building any deep-dive, search for:
- OECD DAC climate finance data (official tracking reports)
- Debt-for-climate swap analysis (Barbados, Ecuador, Belize examples)
- Bilateral conditionality research (ODI, Brookings)
- China/India bilateral climate aid patterns
- JETP partnership deep analysis (South Africa, Indonesia, Vietnam)
Target: at least 6 sources for S4.

### Then: Begin Section Build Loop
Pick a section to start with — S1 (Geopolitics) or S2 (NCQG) are natural openers since they set the geopolitical frame. For each section:
1. Assess sources (already done for most)
2. Fetch key sources via web_fetch for deeper reading
3. Write markdown deep-dive in `notes/`
4. Build HTML deep-dive using read-aid template
5. Commit, push, update index

### Template Setup
- Read `/mnt/skills/user/read-aid/references/deep-dive-reference.html` to cache CSS/JS
- Cache to `/home/claude/survey/template_css.txt` and `template_js.txt`

### Style Conformity
- Check sibling project indexes (e.g., `physics/the-cosmos/index.html`, `cog-sci/fashionable-despair/index.html`) for CSS/section patterns
- Deep-dives use `.dd.html` extension at project root
- Papers use `survey-paper.html` at project root

## Key Tensions Already Visible
1. **Equity vs. efficiency:** $300B "insultingly low" (Global South) vs. "tripling" (developed world framing)
2. **Grants vs. loans:** 58% of adaptation finance is debt; NCQG doesn't distinguish
3. **Greenwashing:** World Bank 45% climate target but hundreds of tenuous projects (CGDev finding)
4. **US absence:** Withdrawal creates $4B+ hole; other donors cutting too, not filling gap
5. **Carbon market integrity:** First Article 6.4 credits already 26x overestimated; CDM legacy flooding new system
6. **Adaptation deficit:** $26B/yr vs $310-365B/yr needed; mitigation wins every budget war
7. **China's ambiguous role:** Largest emitter but also largest clean energy deployer; refuses "donor" classification but provides $3.1B/yr South-South

## Related Projects for Reference
- `ai/genai-2026-outlook/` — recent paper-drive with full section build loop
- `cog-sci/fashionable-despair/` — 7-section deep-dive + survey paper + slides
- `physics/the-cosmos/` — 7-section deep-dive with overview
