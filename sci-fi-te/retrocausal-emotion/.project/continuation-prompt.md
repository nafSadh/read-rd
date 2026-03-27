# Continuation Prompt — Retrocausality, Hope & Depression

## Repo
https://github.com/nafSadh/read-rd

## Project subfolder
`physics/retrocausal-emotion/`

## What's completed
- Literature collection: 43 sources, 7 sections, 6 tensions
- Overview deep-dive: `overview.dd.html` — all 7 sections at summary level with SVGs, citations, writer's takeaways
- All 7 markdown notes: `notes/01-block-universe.md` through `notes/07-literary.md`
- S1 HTML deep-dive: `s1-block-universe.dd.html` — FULL build (5 sub-sections, 5 SVGs, 50K+ chars)
- S2-S7 HTML scaffolds: template + section structure, but detail panels are placeholder stubs

## What's next
1. **Expand S2-S7 detail panels** — each needs 6-10K chars per panel (like S1). Use the markdown notes as source material. Each panel needs:
   - `<div class="detail-header">` with section number
   - 2-4 sub-sections with `<h3>` headers
   - At least one SVG diagram in `<div class="diagram-wrap">`
   - At least one `<div class="callout">` with writer's takeaway
   - Source links (first mention per panel)
2. **Cross-reference links** between section deep-dives (S1→S3, S2→S4, etc.)
3. **Source citation links** in all expanded detail panels
4. **Synthesis paper**: "The Geometry of Feeling" — build from completed sections
5. **Slide deck** — 20-30 slides using read-aid slide template
6. **Project index page** — landing page linking all deliverables

## Template system
CSS cached at `/home/claude/survey/template_css.txt` (26K)
JS cached at `/home/claude/survey/template_js.txt` (17K)
Extract from `/mnt/skills/user/read-aid/references/deep-dive-reference.html` if not present.
Hero markers: `← CHANGE` in JS. Body must be EMPTY (JS builds DOM).

## Design consistency
- Sidebar logo: 1-3 chars, `<em>` for accent color
- Badge format: `S{N} · RETROCAUSAL EMOTION · {N} SOURCES`
- SVG palette: indigo=#5b5bd6, teal=#0ea5e9, purple=#7c3aed, green=#14966e
- Font: IBM Plex Mono for labels, Jost for body, EB Garamond for serif accents
- Writer's Takeaway callout in every detail panel

## Related projects
- `physics/block-universe.dd.html` — existing physics foundation (don't duplicate)
- `sci-fi-te/nonlinear-time.dd.html` — existing time essay
- `self/wellbeing.dd.html` — personal context
