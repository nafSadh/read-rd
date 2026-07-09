# read-rd Changelog

## 2026-07-09 (revision)

### social-influence-bias — SVG bug fixes + full de-clinicalizing prose rewrite

User feedback: slides too clinical, SVG bugs in guide.html, writing quality overall.

- **Guide SVG bugs fixed** (root cause: `<marker>` arrowheads scale with stroke-width by default — thick strokes got giant heads, worst on the 16px SAMPLE arrow). All 10 markers converted to fixed `markerUnits="userSpaceOnUse"` sizing; label/path collisions fixed in the asymmetry (crowd-corrects box, no-counter-force), MusicLab (clipped "indep.", W1/W8 dot kisses), inversion (best-song label on bar, quality-climbs-back on curve), and two-step (P(download|listen) split to two lines, fat arrow got a proportionate dedicated head) diagrams. Verified via a temp one-SVG-per-screen viewer (window-scroll pages defeat below-fold screenshots) + programmatic getBBox audit: 0 out-of-bounds, 0 text overlaps across all 8 SVGs. Also nudged the deep-dive confound diagram's "quality path" label off its dashed arrow.
- **Prose rewritten across all four pages** (3 writer + 3 adversarial-verifier agents, #58–60): scene-first openings, findings-as-headlines ("The Crowd Un-Downvotes You", "Tell a lie about popularity. Watch it come true."), staged numbers, aphorism key-ideas ("Praise compounds. Unfair criticism gets bodyguards."). Verifiers confirmed every spec figure verbatim and all four hedges intact; the slides verifier caught and fixed 5 factual drifts the rewrite introduced (invented "~1.7 points" → 5.13%→6.8%; "all seeded" → "a few thousand seeded"; scoped 308,515 ratings; restored the MusicLab verbatim quote; "permanently" → "measurably").
- **Accuracy nit**: corrected van de Rijt et al. 2014 title in deep-dive Sources ("The Field of Success" → "Field experiments of success-breeds-success dynamics").
- **Validated**: HTMLParser + node --check pass on all four files; no console errors; slides/deep-dive/guide spot-checked in browser. Removed the temp `.tmp-svg-viewer.html` that rode along in interim commit 7ee7d0b.

## 2026-07-09

### New study bundle — cog-sci/social-influence-bias ("Why Upvotes Beget Upvotes")

- **New project** on social influence bias / vote herding, built from a verified deep-research synthesis (5 search angles, 21 primary sources, 25 claims each 3-vote adversarially verified against primary full texts). Core studies: Muchnik, Aral & Taylor 2013 (*Science*), Salganik/Dodds/Watts 2006 & Salganik/Watts 2008 (MusicLab), Krumme et al. 2012.
- **Three learning formats** (the read-aid trio), each hand-crafting the same teaching diagrams with a shared color grammar (indigo = upvotes/positive influence, coral = downvotes, amber = crowd correction, teal = quality, purple = popularity/cumulative advantage):
  - `deep-dive.html` — 7 sections + Sources, 8 SVG diagrams, footnoted; house `dd-shared.css` scaffold, both themes.
  - `slides.html` — 27-slide deck (7 chapters), 17 col-2 diagram slides; Crimson Pro deck style, both themes.
  - `guide.html` — cinematic dark animated scrolling guide, 6 sections, 7 animated SVGs (snowball climb, crowd-correction push-back).
  - `index.html` — landing hub with three format cards + a "what the research shows" summary and primary-source links.
- **Built via a 3-agent Workflow** (`sib-build`, agents #55–57 in `claude-agents.md`) off a shared content spec; every empirical figure verified verbatim (32% first-viewer / P=1.0e-6, +25% final / P=2.3e-11, +30% to ≥10, 0.099 vs 0.054 asymmetry, MusicLab Gini/unpredictability, inversion r=0.84 vs 0.16).
- **Verified in browser** (localhost:8090, both themes): deep-dive all 8 diagrams render, fixed one asymmetry-diagram vertical overlap (viewBox 330→400, separated the evidence-bar band); slides deck title/content/dark all clean; guide hero + section content confirmed painting. Registered in the site nav under Cognitive Science. No console errors.

## 2026-07-02

### Paper-blend treatment for nano-banana images (both themes)

- **Images now dissolve into the page** instead of sitting in bordered boxes: the image moved to a `.nb-img-layer` child (so filters never touch the copy-prompt button) with 28px feathered edge masks on all four sides; border and placeholder background clear on load.
- **Sketch art (default)** — light theme: `mix-blend-mode: multiply` sinks the artwork's cream paper into the page; dark theme: `invert(1) hue-rotate(180deg)` + `screen` turns ink light-on-dark while roughly preserving hues (violet accents survive).
- **Photo art (`style: 'photo'` in NB_IMAGES)** — light: multiply + slight desaturation for a printed-plate look; dark: dimmed (`brightness(.88)`) with the same feathered vignette, no inversion. Tagged on flag-history (except sketch-style s6) and project-hail-mary (12 entries).
- **Verified in browser, both themes**: typography overview (sketch hero + detail panels), flag-history s1 (photo hero + aquila detail image inside the right panel). No console errors.

### Restored nano-banana hero/section images on 34 dd pages

- **Root cause**: the `5a8ae9f` inline-HTML refactor stripped every `NB_IMAGES` block + `nano-banana.js` include, so generated images sat unused in `img/` folders (only april-fools-death kept its wiring). Blocks recovered verbatim from `5a8ae9f^` and re-appended to all 33 affected pages; `sci-fi-te/time-travel-fiction/overview.dd.html` (never wired) got a hero entry with its original prompt from `generate-images.mjs`.
- **`nano-banana.js`**: `detail-hero` now injects directly into inline `#detail-{N}` panels (post-refactor structure) at load, falling back to the legacy `openDetail` hook for dynamic pages. Also fixes april-fools-death section images, which previously could only land in the first panel.
- **Path fix**: `sci-fi-te/nonlinear-time.dd.html` hero now points at `../physics/img/nonlinear-time-hero.png` (page moved out of `physics/`, image didn't).
- **13 entries reference not-yet-generated images** (typography s2–s6, cosmos s2–s7, flag s7) — these show the designed shimmer placeholder with copy-prompt button.
- **Verified in browser** (typography overview 7/7 loaded incl. all detail panels, hail-mary `.section-block` targets, nonlinear-time cross-dir path, fermi placeholder, april-fools 4/4): no console errors.

## 2026-06-30

### world-names — added a merged Codes column (ccTLD · ISO-3 · FIFA)

- **One `Codes` column** at the far right: ccTLD, ISO 3166-1 alpha-3, and FIFA — with FIFA shown only where it differs from ISO-3 (Zimbabwe `.zw ZWE ZIM`, Germany `.de DEU GER`); where they match it's hidden (France `.fr FRA`). Native column narrowed (15.5% → 13%) to make room.
- **Data sourced authoritatively, not from memory**: ISO alpha-2/alpha-3 and ccTLD via `pycountry`; FIFA from the RSSSF list (211 members, updated Sept 2025). Zero lookup errors. FIFA differs from ISO-3 for 69 of 206 entries; 5 are FIFA-only (home nations + Kosovo).
- **Edge cases**: home nations show FIFA only (England → `ENG`); the UK shows `.uk GBR` (no FIFA); Kosovo → `KVX`; Ascension → `.ac`; Antarctica → `.aq ATA`; all-absent shows `—`.
- **Draggable + searchable** like the other columns — KEYS now 10; jsdom suite updated (17 assertions) and passing.

### world-names — interactive table features

- **Drag-to-reorder columns** — any column header can be dragged to a new position; the header, colgroup `<col>`, and every row's cells move together. Order persists in `localStorage`; "Reset columns" restores the original layout.
- **Filter by continent** — chip bar (All + 7 continents) with live per-continent counts. Every one of the 260 entries tagged with `data-continent` (verified 260/260; ISO/pycountry convention for transcontinental cases — Russia→Europe, Turkey/Caucasus/Kazakhstan→Asia).
- **Group by continent** — toggle inserts sorted group-header rows with counts; combines with the active continent filter and the search box.
- **Search** — matches any name or script across all columns; live count ("N of 260").
- **Verified** with a jsdom harness — 26 assertions (filter counts, group order, drag reorder + persistence, reset), all passing.
- Styling reuses the page's existing design tokens; no new dependencies, still a single self-contained file.

### Added "What We Call the World" naming atlas (anthro)

- **New page** `anthro/world-names/world-names.html` — comparative naming atlas of 260 countries/territories across English, native script, Bengali, German, French, Spanish, Hindi, and Arabic. Placed under **Anthropology**, next to Flag History.
- **Kept the source's clean light/article styling intact** (not wrapped in the read-rd dark chrome) per preference to iterate on read-rd's UI separately. Added only a minimal on-palette back-link to `read.sadh.app`.
- **Registered in `index.html`** — added leaf under the `anthro` subject with a new `ref` format badge (`.file-fmt.ref`, cyan).
- **Registered in `manifest.json`** — added `world-names` topic under `subjects.anthro.topics` (status: complete).

## 2026-03-23

### Session 10 — Fact-check audit, fixes, and file renames

- **Comprehensive fact-check** of all non-course content pages. Verified ~30+ claims across physics, neuroscience, philosophy, and psychology pages against primary sources.
- **Fixed 2 factual errors in `neuro/brain-energy.dd.html`**:
  - ATP yield per glucose: 37 → 30–32 (modern biochemistry consensus, per J. Chem. Ed. and Wikipedia)
  - Ketone efficiency: 2.6× → ~30% (2.6 was glucose's own P/O ratio, not a ketone multiplier; β-OHB yields ~13 ATP vs ~10 for pyruvate ≈ 30% boost per FASEB J.)
  - OXPHOS stat: 32-34 → 26–28 ATP (OXPHOS portion only, consistent with total ~30-32)
- **Fixed 3 misleading claims**:
  - Palmer affiliation: MIT/Harvard → Harvard Medical School / McLean Hospital (brain-energy, 2 locations)
  - Past Hypothesis attribution: credited to David Albert (2000), Carroll correctly framed as extending the framework (block-universe, 2 locations)
  - ASD diagnosis ratio: 4:1 → 3–4:1 reflecting narrowing estimates (audhd)
- **Added Cialdini's 7th principle** "Unity" from *Pre-Suasion* (2016) to `dark-psychology.dd.html` — summary, detail section, and new subsection
- **Fixed JS SyntaxError** (`Identifier 'details' has already been declared`) in 2 files:
  - `neuro/brain-energy.dd.html` — renamed top-level `const details` query to `detailEls`
  - `philosophy/dark-psychology.dd.html` — same fix (had 3 declarations, 1 global array + 1 function-scoped + 1 top-level query)
- **Renamed all `-deep-dive.html` files to `.dd.html`** (8 files):
  - `papers/trending-ai/trending-ai-deep-dive.html` → `trending-ai.dd.html`
  - `physics/block-universe/block-universe-deep-dive.html` → `block-universe.dd.html`
  - `sci-fi-te/nonlinear-time/nonlinear-time-deep-dive.html` → `nonlinear-time.dd.html`
  - `sci-fi-te/nonlinear-time/time-travel-fiction-deep-dive.html` → `time-travel-fiction.dd.html`
  - `poetry/syllabus/poetry-syllabus-deep-dive.html` → `poetry-syllabus.dd.html`
  - `project-hail-mary-deep-dive.html` → `project-hail-mary.dd.html`
  - `self/audhd/audhd-deep-dive.html` → `audhd.dd.html`
  - `self/how-to-know-a-person/how-to-know-a-person-deep-dive.html` → `how-to-know-a-person.dd.html`
- **Updated all references** in `manifest.json` and `index.html` to use new `.dd.html` paths
- **Added 2 missing files** to manifest.json + index.html:
  - `sci-fi-te/nonlinear-time/time-travel-fiction.dd.html` (was on disk but unindexed)
  - `project-hail-mary.dd.html` (was on disk but unindexed)
- **Updated manifest.json** — physics_of_time journey now includes time-travel-fiction
- **Updated todo.md** — marked rename migration items as done, updated file counts
- **Structural flatten** — removed all nested topic subdirectories:
  - `papers/trending-ai/` + `papers/agentic-llm-survey/` → `ai/` (papers/ dir deleted)
  - `physics/block-universe/` + `sci-fi-te/nonlinear-time/` → `physics/` flat
  - `poetry/syllabus/` → `craft/` (poetry/ dir deleted)
  - `self/audhd/` + `self/how-to-know-a-person/` → `self/` flat
  - `project-hail-mary.dd.html` → `craft/`
  - Removed 4 stale README.md files (papers/, poetry/, physics/, self/)
- **Rebuilt index.html** — new collapsible directory tree layout with canonical deep-dive theming (EB Garamond + Jost + IBM Plex Mono, light/dark themes, grain overlay, gradient effects), expand/collapse all buttons, format badges, planned items
- **Updated todo.md** — reflected actual flat structure, marked all migration items complete

## 2026-03-23

### Session 8b — Structure proposal & canonical verification

- **Verified all 36 .dd.html files** against canonical deep-dive-reference.html — 35/36 passed. Fixed `kv-cache.dd.html` section-block padding (`2em 3em` → `40px 8px`).
- **Proposed new dir structure** — `~c/` (courses), `~d/` (digests) as special dirs; soft reading at root (`ai/`, `physics/`, `philosophy/`, `craft/`, `self/`, `cs/`). Flat files within each (no nested topic dirs).
- **Updated manifest.json** — added `_meta` with proposed structure, `dir` field per subject, planned topics (philosophy: stoicism, religion, brain-energy, dark-psychology; craft: poetry-collection; self: wellbeing, career; ai: ml-blog). File paths still point to current on-disk locations.
- **Updated todo.md** — full proposed tree, migration checklist, open questions, backlog table.

### Session 8 — Housekeeping & gap analysis

- **Updated manifest.json** — all file paths migrated from old structure (`ml/linear-algebra/linear-algebra-deep-dive.html`) to new (`courses/scpd-ml/linear-algebra.dd.html`). All 46 topic entries updated. Journey topic refs kept as logical keys.
- **Removed empty dirs** — `ml/` and `deep-gen-ai/` (files moved to `courses/` by Session 7.5 restructure agent)
- **Created root hub portal** (`index.html`) — condensed single-page with section cards, flat file list (41 items), theme toggle
- **Updated todo.md** — new structure tree, housekeeping checklist, gap analysis from `claude-chat-log/deep-dives/` chat logs
- **Gap analysis** — identified 5 high-value uncovered topics from chat history: brain energy/metabolic theory, agnostic theism, dark psychology, ML blog project, poetry collection

### Session 7 — Style compliance, citations, portal redesign

- **Updated local template** (`deep-dive-template.md`) to match new `deep-dive-reference.html` — light theme colors `--text:#363b48;--dim:#65707a;--bright:#141a1e`, section-block padding `40px 8px`
- **Migrated 6 older files** to new light theme colors via sed (trending-ai, block-universe, nonlinear-time, poetry-syllabus, audhd, how-to-know-a-person)
- **Fixed 5 style compliance issues**:
  - `kv-cache` — added missing `.right.closed::before{opacity:0}` ghost overlay fix for both themes
  - `problem-sets` — added missing sidebar tooltip (CSS + JS)
  - `how-to-know-a-person` — added missing sidebar tooltip
  - `kernel-methods` — replaced static tooltip with dynamic JS creation
  - `xcs229` — replaced static tooltip with dynamic JS creation
- **Comprehensive rewrite of `xcs236-deep-dive.html`** — replaced `.right-outer` flex-basis architecture, grid stat bars, rounded corners with canonical `.right` 50% width pattern
- **Comprehensive rewrite of `kv-cache-deep-dive.html`** — fixed `data-theme` on `<html>`, wrong var names (`--text-muted`/`--secondary`/`--danger`), `shell.classList` → canonical architecture
- **Added citations/references to all 42 deep-dive files** — Section 09 "Sources & References" with arxiv papers, Stanford course URLs, textbook references, Wikipedia links. ~165 unique URLs across all files.
- **Verified citation links** — spot-checked 20+ URLs across arxiv, Stanford, Wikipedia, Lilian Weng, PyTorch, textbook sites. Fixed 3 broken links:
  - `web.stanford.edu/class/cs236/` (404) → `deepgenerativemodels.github.io`
  - `arxiv.org/abs/1912.01301` (wrong paper) → `arxiv.org/abs/2112.07068`
  - `paperswithcode.com` (redirects to HuggingFace) → `huggingface.co/papers`
- **Redesigned index.html portal** — new single-page dashboard layout with subject cards, topic count badges, file type badges, journey progress bars, scroll spy sidebar, theme toggle
- **Updated changelog** — this entry

### Session 6 — Per-topic deep-dives for XCS229 & XCS236

- **Built 29 new deep-dive HTML files** using sierra-leone canonical CSS/JS template:
  - **XCS229 lecture topics (11 files)**: linear-regression, logistic-regression, glm, generative-algorithms, svm-kernels, decision-trees-ensemble, neural-networks, unsupervised, pca-ica, bias-variance, reinforcement-learning
  - **XCS229 problem sets (5 files)**: ps1 (25pts), ps2 (35pts), ps3 (35pts), ps4 (50pts), ps5 (55pts)
  - **XCS236 lecture topics (10 files)**: intro, autoregressive, mle-latent, vae, normalizing-flows, gan, ebm, score-based, diffusion, evaluation
  - **XCS236 problem sets (3 files)**: ps1 (40pts), ps2 (80pts), ps3 (80pts)
- Each file: 8 sections with summaries + expandable detail panels, SVG diagrams, stats, feature grids, timelines, callouts, verdicts. ~800-1000 lines each.
- **Updated manifest.json** — added all 29 new topics, created 4 new journeys (xcs229-lectures, xcs229-problem-sets, xcs236-lectures, xcs236-problem-sets). Total: 46 topics, 11 journeys.
- **Updated .project/todo.md** — full directory tree with all 46 topics, 11 journeys.
- **Updated .project/changelog.md** — this entry.

### Session 5 — Deep-dive template & HTML compliance fix

- **Audited all 12 deep-dive HTML files** against canonical reference (sierra-leone-civil-war-deep-dive.html). Found 3 files with deviations: linear-algebra, poetry-syllabus, xcs236.
- **Fixed ml/linear-algebra/linear-algebra-deep-dive.html** — replaced CSS with canonical (all 40+ CSS variables, border-divided grids, sharp edges), fixed data-theme placement, added ghost overlay fix.
- **Fixed poetry/syllabus/poetry-syllabus-deep-dive.html** — complete rewrite from wrong architecture to canonical 3-panel with sections/summaries/details data arrays, sidebar tooltip, compact header, sticky title.
- **Fixed deep-gen-ai/xcs236/xcs236-deep-dive.html** — comprehensive fix: replaced `.right-outer` flex-basis pattern with canonical `.right` 50% width, replaced all component CSS (stat bars, feat grids, timelines, security boxes, verdict, price grid), removed border-radius from all components, added ghost overlay fix, sidebar tooltip as floating div, compact header, sticky title with topbar glow, ESC handler.
- **Rewrote .project/deep-dive-template.md** — complete rewrite to match canonical reference. Now covers: complete production CSS (both themes with all 40+ variables), HTML shell, JS architecture (data arrays, DOM building, sidebar builder + tooltip, interaction functions, event listeners), all 10 content components, customization checklist, and common-mistakes-to-avoid table. Previous template had wrong CSS variable names, wrong class placement, missing features.
- **Updated .project/changelog.md** — this entry.

### Session 4 — Portal sync

- **Updated index.html** — synced inline manifest data with current manifest.json. All 17 topics now show as complete with file links. Added Deep Generative AI subject (🎨) and SCPD Deep Gen AI journey to sidebar. Subject numbering updated (01–07). Added xcs229, xcs236. All journeys fully populated.
- **Updated .project/todo.md** — marked all topics complete, updated journey status table (all 7/7 journeys complete), removed stale backlog items.
- **Updated .project/changelog.md** — this entry.

### Session 2 (cont.) — Slide decks + final portal update

- **Built ml/cnn-rnn/cnn-rnn-slides.html** — 29 slides (CNNs: convolution, pooling, classic architectures; RNNs: vanishing gradients, LSTM, GRU, seq2seq; Modern context: ViT, transfer learning). 2521 lines.
- **Built ml/transformers/transformers-slides.html** — 22 slides (Architecture, Attention, Multi-head, FFN, Decoder, Training, Modern context). 1603 lines. Worked examples with dmodel=512, dk=64, h=8.
- **Updated manifest.json** — marked cnn-rnn and transformers as complete. All placeholder topics now filled.
- **Rebuilt index.html** — portal updated to reflect all completed topics including Session 3 additions (xcs229, xcs236)

### Session 3 — SCPD course deep-dives from repo

- **Cloned nafSadh/scpd repo** to `/mnt/src/scpd` — private GitHub repo with XCS229 ML and XCS236 Deep Generative Models course materials (syllabi, lecture notes, problem sets, saved notes PDFs)
- **Built ml/xcs229/xcs229-deep-dive.html** — 8 sections (Supervised Foundations, Gen vs Disc, Kernels & SVMs, Deep Learning, Unsupervised, Dimensionality Reduction, Generalization Theory, Course Roadmap). 1101 lines, 77KB. SVG diagrams for regression, GDA, kernel trick, neural nets, K-means/EM, PCA/ICA, bias-variance, VC dimension.
- **Created deep-gen-ai/ subject directory** with xcs236/ subdirectory
- **Built deep-gen-ai/xcs236/xcs236-deep-dive.html** — 8 sections (Generative Foundations, Autoregressive, VAEs, Normalizing Flows, GANs, Energy/Score-Based, Diffusion, Evaluation). 899 lines, 66KB. 13 SVG diagrams including VAE architecture, GAN min-max, flow transformations, diffusion process.
- **Updated manifest.json** — added ml/xcs229, deep-gen-ai subject with xcs236 topic, scpd-deep-gen-ai journey, updated scpd-ml-course journey to include xcs229
- **Updated .project/todo.md** — added xcs229 and xcs236 entries, updated journeys
- **Updated .project/changelog.md** — this entry

## 2026-03-23

### Session 2 — Continued autonomous build

- **Resumed work** — picked up from session 1 context summary
- **Updated manifest.json** — marked linear-algebra, autoencoders, kernel-methods as complete with file paths
- **Created changelog.md** — this file
- **Built physics/block-universe/block-universe-deep-dive.html** — 8 sections (Measurement Problem, Block Universe, Retrocausality, Problem of Time, Time as Emergent, Arrow of Time, CTCs, Verdict). 513 lines with SVG diagrams.
- **Built ml/problem-sets/problem-sets-deep-dive.html** — 8 sections (Gen vs Disc, GDA, Logistic Regression, Naive Bayes, SVMs, Softmax, Decision Boundaries, When to Use What). 859 lines with SVG diagrams.
- **Built self/how-to-know-a-person/how-to-know-a-person-deep-dive.html** — 8 sections (Illuminators, Attention, Conversation, Life Stories, Hard Conversations, Character, Toolkit, Assessment). 898 lines.
- **Updated manifest.json** — marked block-universe, problem-sets, how-to-know-a-person as complete
- **Built poetry/syllabus/poetry-syllabus-deep-dive.html** — 8 sections (Study Plan, Foundations, Modernism, Confessional, Contemporary, Craft, Integration, Resources). 1284 lines. 12 poets, 45-day schedule.
- **Built self/audhd/audhd-deep-dive.html** — 8 sections (Landscape, ADHD, ASD, AuDHD intersection, Executive Function, Sensory/Emotional, Strategies, Identity). 1138 lines. SVG Venn diagram.
- **Built sci-fi-te/nonlinear-time/nonlinear-time-deep-dive.html** — 8 sections (Time Travel Origins, Relativistic Time, Loops, Branching, Subjective, Block Universe, Retrocausality, Convergence). 601 lines. Sci-fi mapped to physics.
- **Updated manifest.json** — marked syllabus, audhd, nonlinear-time as complete
- **Built papers/trending-ai/trending-ai-deep-dive.html** — 8 sections (Landscape, Agentic Benchmarks, Reasoning Models, Multimodal Agents, Architecture, Scaling, Safety, Verdict). 1216 lines. Incorporates user's research topics (FeatureBench, AgentBench, AgentVista, ORZ, GRPO/DRPO, TraceR1, VIGA, MAPG, Ponder & Press).
- **Updated manifest.json** — marked trending-ai as complete

### Session 1 — Structure + first deep dives

- **Created directory structure** — subject-based hierarchy with journey cross-navigation
- **Created manifest.json** — single source of truth for topics, statuses, journeys
- **Rebuilt index.html** — portal with deep-dive design system (EB Garamond + Jost + IBM Plex Mono, blurple theme)
- **Created .project/todo.md** — full backlog with priorities
- **Created .project/deep-dive-template.md** — 1270-line authoritative template reference matching production CSS/JS
- **Moved digests/** — relocated from root with working build_reader.py
- **Created subject READMEs** — ml, papers, physics, poetry, self, digests
- **Built ml/linear-algebra/linear-algebra-deep-dive.html** — 8 sections, 83KB (Vectors, Matrices, Systems, Eigenvalues, SVD, Matrix Calculus, Norms, Decompositions)
- **Built ml/autoencoders/autoencoders-deep-dive.html** — 8 sections (Basic AE through VAEs to diffusion connections)
- **Built ml/kernel-methods/kernel-methods-deep-dive.html** — 7 sections (Feature maps through Mercer's theorem)
- **Added new research topics to backlog** — Agentic Benchmarks, Reasoning Models, Multimodal Agents

## 2026-03-25

### Session 12 — The Cosmos: S2 Big Bang & CMB

- **Built `physics/the-cosmos/s2-bigbang.dd.html`** — 8 sections (Hot Big Bang, Nucleosynthesis, Recombination & CMB, COBE/WMAP/Planck, Seeds of Structure, Inflation, Evidence & Critique, Consensus). ~90KB, 8 SVG diagrams, 51K chars of detail panels. 7 sources synthesized.
- **Updated `physics/the-cosmos/index.html`** — S2 marked done with deep-dive link, counter updated to 2 of 7 sections complete.
- **Created `.project/image-gen-cosmos.md`** — Image generation instructions for Claude Code agents. S2 hero image prompt defined, plus prompts for S3–S7 when built. Gemini API (gemini-2.0-flash-preview-image-generation) could not be reached from this container due to proxy/SSL issues; deferred to Claude Code.
- **Updated `.project/changelog.md`** — this entry.

- **Built `physics/the-cosmos/s3-darkmatter.dd.html`** — 8 sections (Evidence, Rotation Curves, Bullet Cluster, WIMPs & the Search, Axions/PBHs/Exotica, MOND, Detection Crisis, Consensus). ~81KB, 8 SVG diagrams, 43K chars of detail panels. 9 sources synthesized.
- **Updated `physics/the-cosmos/index.html`** — S3 marked done (3 of 7).
