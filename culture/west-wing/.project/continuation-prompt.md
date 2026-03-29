# Continuation Prompt — West Wing & Democratic Backsliding

## Repo
`github.com/nafSadh/read-rd` — subfolder `culture/west-wing/`
PAT: (provide at runtime)

## What exists

### Completed deliverables
- **Deep dive:** `west-wing-politics.dd.html` — unified 8-section interactive page on The West Wing vs contemporary politics (idealism/realism, executive power, bipartisanship, media/press). 34 sources, 2 SVG diagrams.
- **Survey paper:** `survey-paper.html` — standalone paper with Wikipedia-style `[N]` hover citations, 18 inline citations, 20 references. Sidebar nav, theme toggle.
- **Slide deck:** `backsliding-slides.html` — 17 slides on democratic backsliding globally. V-Dem 2026, Carnegie, IDEA, RSF data. 8 SVGs. Arrow-key navigable.
- **Fiction draft:** `lgrotg.md` — short story where a typo ("lgrotg" = "let's get rid of the governments") sparks a global movement toward direct democracy. Currently a fable — power concedes too easily, no friction, doesn't earn its ending.
- **Literature collection:** `literature-collection.md` — 34 sources across 4 dimensions + cross-cutting.
- **Project files:** `.project/changelog.md`, `.project/todo.md`, `.project/methodology.md`

### On the root index
All deliverables are listed under `culture/` → `Culture & Politics` on `read.sadh.app`.

## What's next — two possible forks

### Fork A: Revise the fiction
Rewrite `lgrotg.md` with real friction. The current draft is a fable where power concedes without resistance. The revision should:
- Add a section where the Buen Retiro movement faces actual opposition (the mayor's brother-in-law has contracts, the police are called, someone gets arrested)
- Show a *cabildo* failing — a land dispute that the open council can't resolve, factions forming, the system nearly breaking
- Make Jón's platform in Reykjavík get co-opted or attacked (a fishing conglomerate gaming the endorsement threshold, a disinformation campaign)
- Give Doña Carmen a real antagonist, not just an absent mayor
- The ending should still land on hope — but hope that's been tested, not assumed
- Keep the tone: warm, wry, specific. Not cynical. The story believes in what it's depicting, it just doesn't let its characters have it for free.
- Keep Section V removed (the "thesis statement" section from the earlier essay `slow-enough-to-miss.md` had the same problem — show, don't explain)

### Fork B: Democratic backsliding as its own paper-drive project
Spin the backsliding slides into a full research project with its own deep-dives:
- S1: What Is Democratic Backsliding (Bermeo, Levitsky & Ziblatt, V-Dem framework)
- S2: The Global Picture (V-Dem 2026 data, IDEA 2025, Freedom House)
- S3: The Playbook (executive aggrandizement patterns across cases)
- S4: Case Studies (Hungary, Turkey, India, U.S. — comparative)
- S5: Press Freedom as Canary (RSF, CJR, Knight Institute)
- S6: Resistance & Recovery (Poland, Brazil, Botswana, what works)
- Survey paper + slides as final deliverables
- This would be a standalone project at `culture/democratic-backsliding/` or `politics/backsliding/`

### Fork C: Both
Revise the fiction AND build the research project. The fiction becomes a creative companion piece to the academic survey — the Calvino to the V-Dem.

## Template notes
- Deep dives use `read-aid` deep-dive template (empty body, JS builds DOM, `sections[]`/`summaries[]`/`details[]` arrays)
- Papers use the sidebar-nav paper template (see `anthro/religion-today/survey-paper.html` for the exact CSS)
- Slides use the `read-aid` slide-deck template (arrow-key nav, auto-hiding nav bar, three-state theme toggle)
- **Critical:** When using `create_file` tool, template literals with backticks get escaped. Use Python scripts to generate HTML files to avoid `\`` corruption. Validate with `node --check` after extracting JS.

## Related projects in the repo
- `anthro/religion-today/` — religion survey with same paper template (good reference for citation style)
- `ai/genai-2026-outlook/` — largest paper-drive project in the repo (good reference for index page structure)
- `cog-sci/fashionable-despair/` — most recent completed project
