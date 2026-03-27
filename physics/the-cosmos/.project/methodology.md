# The Cosmos — Methodology

## Paper-Drive Approach

This project follows the paper-drive methodology: sources first, assessment second, writing third.

### Phase 1: Literature Collection
Compile sources across all planned sections before writing any deep-dive. Each source is assigned an ID (e.g., BB-01, DM-05) and catalogued with key data points and publication date. Sources include peer-reviewed papers, observatory press releases, review articles, Wikipedia summaries, and science journalism.

### Phase 2: Source Adequacy Assessment
Each section's source pool is evaluated for coverage, recency, and diversity of perspective. A section is marked adequate when it covers the core claims, key data points, named researchers, and active controversies. Minimum 6 sources per section; target 7-10.

### Phase 3: Notes Synthesis
For each section, sources are synthesized into structured markdown notes organized by sub-topic. Notes include specific numbers, named experiments, dates, and source attribution. Notes conclude with "What sources agree on" and "Where sources disagree" sections to identify consensus and tensions.

### Phase 4: Deep-Dive Construction
Each deep-dive is built as a single-file HTML application using the shared template system. Target: 8 sections per deep-dive, 7-9 SVG diagrams, 5-10K characters per detail panel. The template uses CSS custom properties for theming (light/dark) and JavaScript DOM building for the three-panel layout (sidebar, summary scroll, detail panel).

### Phase 5: Citations and Cross-References
Wikipedia-style inline citations using `<sup class="fn">` with tooltip previews linking to external sources. Cross-reference links between section deep-dives where topics connect.

### Phase 6: Synthesis and Deliverables
Synthesis paper drawing on all sections and the cross-cutting tensions framework. Slide deck for presentation. Index page with status tracking.

## Template System

- **CSS:** Identical across all section deep-dives. Variables control theme (light/dark), typography, spacing. Inline in each file (no shared CSS file for this project).
- **JS:** DOM builder creates sidebar navigation, summary scroll, and detail panel. Each file defines `sections`, `summaries`, and `details` arrays. The `shell` innerHTML provides hero markers (badge, title, subtitle, sidebar logo).
- **SVGs:** Inline SVG diagrams using CSS variables for theme compatibility. Labeled with IBM Plex Mono. Background fills use theme-aware rgba values.
- **Nano Banana:** Hero image system. `NB_IMAGES` config array + `nano-banana.js` script for image loading.

## Quality Standards

- Claims cite specific numbers, named researchers, and concrete experimental results
- Tensions and open questions treated as first-class content
- Detail panels run 5-10K characters with embedded diagrams
- Callout boxes highlight key insights
- Feature grids compare alternatives
- Verdict/consensus sections use pro/con format
