# The Cosmos — Continuation Prompt

## Repository
- **Repo:** https://github.com/nafSadh/read-rd
- **Live:** https://read.sadh.app/physics/the-cosmos/
- **Project dir:** `physics/the-cosmos/`

## What's Completed
- **Literature collection:** 55 sources across 7 sections (all adequate)
- **Overview deep-dive:** `overview.dd.html` — all 7 dimensions at summary level, with inline citations
- **S1: Scales of the Universe:** `s1-scales.dd.html` + hero image, with inline citations
- **S2: The Big Bang & CMB:** `s2-bigbang.dd.html` (8 sections, ~90KB, 9 SVGs), with inline citations
- **S3: Dark Matter:** `s3-darkmatter.dd.html` (8 sections, ~82KB, 7 SVGs), with inline citations
- **S4: Dark Energy & Fate:** `s4-darkenergy.dd.html` (8 sections, 7 SVGs, inline citations)
- **S5: The Fermi Paradox:** `s5-fermi.dd.html` (8 sections, 7 SVGs, inline citations)
- **S6: Multiverse & Anthropic:** `s6-multiverse.dd.html` (8 sections, 7 SVGs, inline citations)
- **Markdown notes for all 7 sections:** in `notes/01-scales.md` through `notes/07-frontiers.md`
- **Synthesis notes:** `notes/00-synthesis.md`
- **.project/ management files:** changelog, todo, methodology, continuation prompt, peer review
- **Wikipedia-style inline citations:** All deep-dives have `<sup class="fn">` citations with tooltip previews
- **Index page:** Updated with correct status badges, 6 of 7 sections done, deep-dive links

## What's Next

### Immediate: Build S7 Frontiers
1. **Read notes:** `notes/07-frontiers.md` — fully synthesized content ready for deep-dive.
2. **Build HTML:** Use S4/S5/S6 as scaffold (same CSS, same JS template). Patch hero markers.
3. **8 sections:** JWST, Gravitational Waves, Neutrino Astronomy, Hubble Tension, Vera Rubin, DESI, What We Know by 2050, Consensus.
4. **Target:** 7-9 SVGs, inline citations from FR-01 through FR-10.
5. **Update index:** Mark S7 done, update counter to 7 of 7.

### After S7: Synthesis Paper
- Use `notes/00-synthesis.md` and the six cross-cutting tensions framework
- HTML paper format (see `ai/genai-2026-outlook/tensions-paper.html` for template)
- Include 20+ source links, Wikipedia-style citations
- The "meta-tension" insight (best theories are simultaneously triumphant and incomplete) is the thesis

### After Synthesis Paper
- Generate hero images for S2-S7 (see image generation instructions)
- Slide deck (20-30 slides)
- Cross-reference linking pass (inter-section links in all detail panels)
- Backfill S1 to match S2/S3 depth

## Template System Notes
- CSS is identical across all section deep-dives (~26K chars inline)
- JS DOM-building template is identical (~7K chars)
- Each section patches 4 hero markers: badge text, title, subtitle, sidebar logo
- `.fn` CSS for Wikipedia-style citations is included in all files
- `NB_IMAGES` config + `nano-banana.js` reference at end of body
- Body must be empty — JS builds entire DOM

## Key Files
- `.project/changelog.md` — session history
- `.project/todo.md` — deliverables + source adequacy table
- `.project/methodology.md` — paper-drive approach documentation
- `physics/the-cosmos/literature-collection.md` — master source list (55 sources)
- `physics/the-cosmos/notes/00-synthesis.md` — cross-section synthesis
