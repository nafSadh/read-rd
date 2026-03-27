# Peer Review: anthro/flag-history

**Reviewer:** Claude (agentic peer review)
**Date:** 2026-03-25

## Overall Assessment

This is a well-executed vexillology project with strong content depth across six per-section deep-dives and one monolithic overview file. The writing is analytical rather than merely descriptive, the synthesis notes identify genuine cross-cutting themes (the "three color families" thesis is particularly compelling), and the literature collection is well-organized with 35+ sources spanning academic vexillology, primary historical texts, and institutional references. The project demonstrates genuine domain expertise and produces engaging, substantive deep-dives with rich SVG diagrams.

However, the project has significant paper-drive compliance gaps: no synthesis papers exist, no slide decks have been built, the index page links all point to the monolithic overview rather than individual section files, Wikipedia-style inline citations are entirely absent from the deep-dives, and the changelog references a `s7-collection.dd.html` that was never created (section 7 content lives only in the monolith). External source links in the deep-dive HTML files total only ~15 unique references (excluding font imports), well short of the 20+ target.

**Grade: B for Content Quality, C+ for Paper-Drive Compliance**

## Completeness Scorecard

| Criterion | Status | Notes |
|-----------|--------|-------|
| Literature collection | ✅ | 35+ sources in `literature-collection.md`, well-organized by section with IDs (V-01, A-01, etc.), URLs for digital sources |
| Source adequacy checks | ⚠️ | Sources listed per section in todo.md (5-7 per section) but no formal adequacy assessment document; sources skew toward Wikipedia and encyclopedias for several sections |
| Deep-dives (6/7 built as standalone) | ⚠️ | s1 through s6 exist as standalone .dd.html files with 7-8 subsections each; s7 (The flags.fyi Collection) exists only inside the monolithic `flag-history.dd.html`, not as a standalone file despite changelog claiming it was created |
| Papers | ❌ | No synthesis papers written; todo.md lists two optional papers ("Flags as Compressed Histories", "The Three Color Families") but neither was started |
| Slides | ❌ | No slide deck exists; listed as optional in todo.md |
| Index deliverable cards | ⚠️ | Index page exists with 7 section cards + source card, stat bar, and theme toggle; however all deep-dive links point to `flag-history.dd.html#section-N` anchors in the monolith rather than linking to the individual section files (s1-origins.dd.html, etc.) |
| .project/ management | ✅ | changelog.md, methodology.md, and todo.md all present and well-maintained; methodology includes limitations section; todo.md serves as hand-off document |
| Citations (Wikipedia-style) | ❌ | No Wikipedia-style inline citations (superscript reference numbers, footnote sections) in any deep-dive file; sources are linked inline as hyperlinks but without formal citation apparatus |
| External source links (20+) | ⚠️ | ~15 unique external source links across all .dd.html files (to Wikipedia, flags.fyi, FIAV, NAVA); literature-collection.md has 20+ URLs but they are not carried through into the deep-dive content |

## Content Quality

The content across all deep-dives is substantive and well-structured. Each section file contains 7-8 subsections with expandable detail panels, stat blocks, feature grids, callout blocks, and timelines. The writing consistently moves beyond description into analysis -- for example, the s1 deep-dive on the Shahdad Standard draws out the distinction between flags as sacred objects versus reproducible symbols, and s4 identifies the tricolor format itself as carrying semantic meaning (popular sovereignty). The monolithic overview file (`flag-history.dd.html`) is particularly rich, containing 41 SVG elements including inline flag renderings and timeline diagrams.

The synthesis notes (`notes/00-synthesis.md`) identify six cross-cutting themes and three tensions that demonstrate genuine intellectual engagement with the material. The "flags as compressed histories" framing is a strong organizing thesis.

## Strengths

- **Analytical depth**: The deep-dives go well beyond encyclopedia-level description. The analysis of material transitions (metal to cloth), the identification of design lineages (Ottoman crescent family, tricolor diffusion), and the treatment of flags as constitutive rather than merely representative are all strong analytical moves.
- **Visual richness**: 63 SVG elements across the project, including inline flag renderings, timeline diagrams, layout pattern taxonomies, and evolution charts. The Afghanistan timeline SVG in the overview is particularly effective.
- **Literature breadth**: Sources span from Eusebius (4th century primary source) and Ferdowsi's Shahnameh to modern scholarly vexillology (Whitney Smith, Michel Pastoureau, Ted Kaye) and institutional references (FIAV, NAVA, Flag Institute).
- **Cross-referencing**: Section files link to related sections (e.g., s1 links forward to s2), creating navigable connections across the project.
- **Methodology transparency**: The methodology.md file includes an honest limitations section acknowledging gaps in East Asian vexillology and sub-national flag coverage.
- **Consistent design system**: All deep-dive files use a shared CSS design system with light/dark theme support, sidebar navigation, and detail panel mechanics.

## Weaknesses

- **Missing papers and slides**: The paper-drive workflow expects synthesis papers (with 20+ source links) and slide decks as deliverables. Neither exists. The two paper topics identified in todo.md ("Flags as Compressed Histories", "The Three Color Families") are strong candidates but remain unstarted.
- **No Wikipedia-style citations**: None of the deep-dive files use superscript reference numbers or footnote sections. Sources appear as inline hyperlinks when present, but most claims go entirely unsourced in the HTML. The literature collection documents the sources but they are not formally cited in the content.
- **Missing s7 standalone file**: The changelog claims `s7-collection.dd.html` was created, but it does not exist on disk. Section 7 content lives only in the monolithic overview.
- **Index links are stale**: The index.html links all 7 sections to `flag-history.dd.html#section-N` rather than to the individual standalone section files (s1-origins.dd.html through s6-design.dd.html). This means the standalone section files are effectively orphaned from the index.
- **Thin external linking in deep-dives**: Only ~15 external source links appear across all .dd.html files combined. Many substantive claims (e.g., specific dates, flag counts, historical events) lack any linked source in the rendered content.
- **No audio transcript or notes**: An `flag-history.mp3` file exists but there is no corresponding transcript or notes file.

## Recommendations

1. **Write at least one synthesis paper** -- "Flags as Compressed Histories" is the strongest candidate, as the thesis is already developed in the synthesis notes. Target 20+ source links drawn from literature-collection.md.
2. **Add Wikipedia-style citations** to all deep-dive files: superscript reference numbers in the text body, with a references section at the bottom of each file linking to the corresponding literature-collection.md entries.
3. **Create s7-collection.dd.html** as a standalone file, or update the changelog to accurately reflect that section 7 remains only in the overview.
4. **Update index.html links** to point to individual section files (s1-origins.dd.html, etc.) rather than monolith anchors.
5. **Increase external source density** in deep-dive content. Many historical claims (Battle of Teutoburg Forest, Battle of Lyndanisse, Arab Revolt) could link to their Wikipedia articles or scholarly references already cataloged in literature-collection.md.
6. **Build a slide deck** with SVG diagrams. The project already has strong visual assets (flag layout taxonomy, Afghanistan timeline, evolution chains) that would translate well to slides.
7. **Consider a formal source adequacy check** document in `.project/` that maps each section's claims to specific sources and identifies any gaps.
