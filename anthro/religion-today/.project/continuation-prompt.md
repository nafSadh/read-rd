# Continuation Prompt — Religion Today

## Repo
- URL: https://github.com/nafSadh/read-rd
- PAT: (provide at runtime)
- Live: https://nafsadh.github.io/read-rd/anthro/religion-today/

## What's Done
- Literature collection (52 sources)
- Overview deep-dive + S1 + S2 HTML deep-dives
- All 6 section markdown notes (complete, adequate sources)
- **Survey paper** (`survey-paper.html`) — 42KB, 8 sections
- **Tensions paper** (`tensions-paper.html`) — 33KB, 6 tensions + meta
- Index page updated with Papers section

## What's Next
1. **Build S3 HTML deep-dive** (`s3-fundamentalism.dd.html`) from `notes/03-fundamentalism.md` — 9 sources. Use the same template as `s1-global-landscape.dd.html` (extract CSS/JS, build sections/summaries/details arrays). Target 6-10K chars per detail panel.
2. **Build S4** (`s4-religion-science.dd.html`) from `notes/04-religion-science.md` — 8 sources
3. **Build S5** (`s5-new-movements.dd.html`) from `notes/05-new-movements.md` — 8 sources
4. **Build S6** (`s6-interfaith.dd.html`) from `notes/06-interfaith.md` — 8 sources
5. **Cover image** — Gemini API key returned 403 for Imagen. May need permissions update or different model.
6. Optional: slide deck, final methodology pass

## Template System
- Deep-dives use read-aid template: empty body, JS builds DOM
- CSS and JS are inline in each HTML file (see s1/s2 for reference)
- `sections[]`, `summaries[]`, `details[]` arrays define content
- Hero markers with `← CHANGE` comments for badge, title, subtitle, sidebar logo
- SVG diagrams: 400px wide viewBox, IBM Plex Mono font, themed color palette

## Use paper-drive skill
