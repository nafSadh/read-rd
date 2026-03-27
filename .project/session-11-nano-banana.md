# Session 11 — Nano Banana Image Integration

**Date:** 2026-03-25
**Worktree:** jovial-hoover

## What Was Done

### Nano Banana AI Image System
- Created `nano-banana.css` + `nano-banana.js` — shared scaffold for image placeholders
- Integrated into 22 deep-dive pages across 6 topics
- Generated 37 images via Gemini API (`gemini-3.1-flash-image-preview`)
- Two style rounds:
  - **v1 (photorealistic)** — kept for Flag History (8 images) originally, also for Hail Mary
  - **v2 (sketch)** — minimal ink line drawing on cream paper, violet accent, for all other topics
- Hail Mary regenerated to sketch in v3 (model ignored sketch suffix for sci-fi prompts — came out as colorful concept art, which was accepted)
- Style guide saved to `.project/image-style-ref.md`

### Index Pages
- `pages-with-images.html` — card grid with thumbnails for all 22 image pages
- `narrated-pages.html` — list of all 19 audio narrations with inline playback
- Both linked from home `index.html`

### Page Rebuilds
4 broken deep-dive pages rebuilt from scratch using poetry-syllabus scaffold:
- `ai/ml-blog.dd.html` — was minified with nested backtick bug
- `craft/poetry-collection.dd.html` — was minified, wouldn't render
- `cog-sci/religion-psychology/overview.dd.html` — hybrid HTML/JS pattern
- `philosophy/sophies-world-reader/01-awakening.dd.html` — missing shell wrapper
- `craft/poetry-syllabus.dd.html` — fixed missing `shell.className = 'shell'`

## Key Learnings

### Nano Banana / Gemini Image API
- Model: `gemini-3.1-flash-image-preview` (Nano Banana 2 / Flash)
- Config must include `responseModalities: ['IMAGE', 'TEXT']`
- Returns base64 PNG in `response.candidates[0].content.parts[].inlineData`
- 503 errors are frequent under load — exponential backoff essential (3s → 6s → 12s → 24s)
- Some responses return empty (no `inlineData`) — need null check
- Style suffix adherence varies by subject: sketch style works great for objects/landscapes/diagrams, but sci-fi/space prompts tend to override toward concept art regardless

### Sketch Style That Works
```
, minimal ink line drawing on warm cream paper, single violet accent color,
clean sparse lines, editorial sketch style, playful and elegant, no photorealism
```
- Matches the read-rd design system (Jost + EB Garamond + grain texture + violet accent)
- Best for: labeled diagrams, workspace scenes, landscapes, conceptual illustrations
- Weak for: sci-fi scenes, anything requiring color differentiation

### Deep-Dive Page Architecture
- The standard scaffold requires `shell.className = 'shell'` — forgetting this causes layout to break silently (content renders but no flex layout)
- Template literals (backticks) for content arrays CANNOT contain backtick characters for inline code — must use `<code>` tags instead
- Minified files are nearly impossible to debug — always rebuild from scratch using the scaffold pattern
- The `poetry-syllabus.dd.html` is the canonical working template for rebuilds
- Audio embed scripts (the IIFE at the end) must be preserved when rebuilding — they look for `.masthead-sub`, `.masthead-rule`, and `#ctrl-group`

### nano-banana.js Injection Timing
- The JS runs after page scripts via `setTimeout(inject, 200)` — works for JS-built DOMs
- Hero images must go in `.main-scroll-inner` (scrollable), NOT `.main-head` (has `overflow:hidden`)
- `detail-hero` hook that monkey-patches `window.openDetail` is fragile — CSS selector targets (`'.section-block:nth-child(N)'`) with `position: 'prepend'` is more reliable for section images

### Git Workflow in Worktrees
- Can't `git checkout main` from a worktree — must merge from the main repo directory
- `git stash pop` after merge can silently overwrite merged changes if stashed files overlap — always verify with `grep` after merge
- Agents write to whatever path they're given — if preview server runs from worktree but agents write to main, must copy files to worktree for preview

## Files Created/Modified

### New Files
- `nano-banana.css` — image placeholder styles
- `nano-banana.js` — image injection engine
- `pages-with-images.html` — image index page
- `narrated-pages.html` — audio narrations index with inline playback
- `.project/image-style-ref.md` — Nano Banana style guide
- `generate-images.mjs` — batch image generation script (utility, not committed)
- `regen-sketch.mjs` — sketch-style regeneration script (utility, not committed)
- 37 PNG images across `*/img/` directories

### Modified Files
- 22 `.dd.html` files — added NB_IMAGES config + nano-banana.js reference
- 4 `.dd.html` files — rebuilt from scratch (ml-blog, poetry-collection, religion-psychology, sophie's-world)
- 1 `.dd.html` file — fixed missing shell.className (poetry-syllabus)
- `index.html` — added links to image + narration index pages
