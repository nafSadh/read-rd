# Agentic Peer Review -- The Science of Music

**Reviewer**: Claude Opus 4.6 (automated peer review)
**Date**: 2026-03-25
**Project**: craft/science-of-music

---

## Overall Assessment

**Overall Grade: B+**

This is a well-conceived interdisciplinary research project with strong source selection, genuinely insightful synthesis, and high production quality on the completed sections. The central research question -- why music works the way it does -- is well-framed and the seven-dimension structure covers the topic comprehensively. The two completed deep-dive HTMLs (S1: Physics, S2: Harmony) are excellent: substantively rich, clearly written, and visually polished. The overview deep-dive successfully ties all seven dimensions together. The literature collection is thorough (52 sources across 7 sections) with good disciplinary breadth.

The primary weakness is completion: only 2 of 7 section deep-dives have been built as HTML, with 5 remaining as markdown notes only. There are no synthesis papers and no slide decks. The project infrastructure is also slightly inconsistent -- the changelog claims all 7 deep-dives were built ("Built all section deep-dives (s1 through s7)") but only s1 and s2 exist on disk. The todo.md acknowledges this discrepancy.

---

## Completeness Scorecard

| Component                  | Status       | Grade | Notes |
|----------------------------|-------------|-------|-------|
| Literature collection      | Complete    | A     | 52 sources across 7 sections; good mix of primary research, textbooks, and reference material |
| Source adequacy per section | Complete    | A-    | 6-8 sources per section; S5 has 3 entries without specific URLs (items 4-6 cite "multiple sources") |
| Research notes             | Complete    | A     | All 7 section notes + synthesis notes present and detailed |
| Overview deep-dive         | Complete    | A     | Covers all 7 dimensions with summaries, detail panels, SVG diagrams |
| Section deep-dives (HTML)  | 2 of 7      | C+    | S1 and S2 are excellent; S3-S7 exist only as markdown notes |
| Synthesis paper            | Not started | F     | No synthesis paper exists |
| Slide deck                 | Not started | F     | No slides exist |
| Index page                 | Complete    | A     | Clean design, accurate status tracking, links to all resources |
| Project metadata           | Complete    | A-    | Changelog, methodology, todo all present; changelog has an accuracy issue |
| Cross-references           | Partial     | B     | Good in completed sections (S1 links to S2, S4, S7); absent in unbuilt sections |

---

## Content Quality

### Source Quality: A-

The literature collection demonstrates strong source selection. Highlights include:

- **Primary neuroscience papers**: Salimpoor et al. (2011, Nature Neuroscience), Grahn (2017, Cortex), Cheung et al. (2019, Current Biology) -- these are foundational studies, not derivative reviews.
- **Deliberate inclusion of contradicting evidence**: Huron's prolactin hypothesis (2011) paired with Ladinig et al.'s negative replication (2021). This is good scientific practice.
- **Non-Western sources**: Gamelan tuning (Computer Music Journal, MIT Press), raga/maqam comparative material. The project avoids pure Western-centrism.
- **Recency**: Several 2024-2025 sources (concert hall optimization, AI music market data, lullaby ethnographic review).

Weaknesses: Three entries in S5 (Music & Memory) cite "multiple sources" or "multiple clinical/psychology sources" without specific URLs. These should be pinned to concrete citations. Some sources are lower-tier (Vedantu, Vocal Media, Thermaxx Jackets blog) -- serviceable but not peer-reviewed.

### Analytical Depth: A

The strongest aspect of this project. The synthesis notes demonstrate genuine intellectual integration rather than mere summarization:

- The thread from overtone series (physics) through Pythagorean comma (math) through equal temperament (cultural choice) through gamelan rejection of the octave (cultural divergence) is traced with clarity and rigor.
- The parallel between equal temperament flattening key character and AI flattening genre diversity is an original and insightful observation.
- The BRECVEMA framework discussion correctly distinguishes eight distinct mechanisms rather than treating "emotion" as monolithic.
- Cross-section connections are explicitly mapped (S1 to S2, S2 to S6, S3 to S4, S4 to S5, S5 to S6, S6 to S7, S1 to S7).

### Writing Quality: A-

The completed deep-dives are well-written. Prose is clear and avoids both jargon-heavy academic density and oversimplification. Technical concepts are explained precisely (e.g., the explanation of why a clarinet only produces odd harmonics, the mathematical derivation of the Pythagorean comma). Key insight callouts at the end of each detail section effectively distill the takeaway.

Minor issue: the overview summaries occasionally compress complex arguments to the point where nuance is lost (e.g., the sad music discussion is reduced to a single sentence).

### Visual/Interactive Quality: A

The deep-dive HTML files use a sophisticated three-panel layout (sidebar navigation, summary scroll, detail panel) with:

- SVG diagrams (waveform anatomy, standing waves in tubes, tuning system comparison chart)
- Stat blocks with quantitative data
- Feature grids (BRECVEMA mechanisms, non-Western tuning systems)
- Theme toggle (light/dark) with well-considered color palettes
- Mobile-responsive design with proper breakpoints
- Keyboard navigation (Escape to close detail panel)

---

## Strengths

1. **Interdisciplinary integration is the project's defining strength.** The synthesis notes and cross-references genuinely connect acoustics, neuroscience, music theory, ethnomusicology, and technology. This is not seven separate reports -- it is one argument traced across seven lenses.

2. **Balanced treatment of Western and non-Western perspectives.** The project consistently uses gamelan, raga, and maqam as substantive counterpoints to Western music theory, not as exotic footnotes. The point that equal temperament is a cultural choice, not a physical necessity, is made forcefully and correctly.

3. **Honest treatment of unresolved questions.** The prolactin hypothesis failure, the nature-vs-culture tension in consonance perception, the WEIRD bias in neuroscience research, and the unresolved evolutionary function of music are all acknowledged rather than glossed over.

4. **Source quality for completed sections.** The core neuroscience and musicology citations (Salimpoor, Juslin, Grahn, Mehr, Plomp-Levelt, Helmholtz) are the right papers to cite. The project demonstrates familiarity with the primary literature.

5. **Production quality of completed HTML.** The deep-dive template is visually polished, functionally complete, and consistent across the overview and two section pages.

---

## Weaknesses

1. **Completion gap is the dominant issue.** 5 of 7 section deep-dives are not built. The notes are thorough enough to support building them, but as of now the project delivers only 29% of its planned section coverage in presentation-ready form. No synthesis paper or slide deck exists.

2. **Changelog accuracy.** The changelog states "Built all section deep-dives (s1 through s7) with full detail panels" but only s1-physics.dd.html and s2-harmony.dd.html exist on disk. The todo.md notes this discrepancy, but the changelog itself should be corrected to avoid confusion.

3. **Incomplete source citations in S5.** Three of seven sources in the Music & Memory section lack specific URLs and cite "multiple sources" or "multiple clinical sources." This falls below the project's own standards established in other sections.

4. **No shared CSS/JS.** Each deep-dive HTML file embeds its full CSS and JS inline. The project notes the absence of dd-shared.css and dd-shared.js. This creates maintenance risk -- any design change must be applied to each file independently.

5. **No audio or interactive demonstrations.** For a project about sound and music, the absence of any playable audio examples is a missed opportunity. The overview.mp3 file exists but is not embedded in any HTML page. Interactive demonstrations (e.g., playable intervals for the consonance section, adjustable Fourier synthesis) would significantly strengthen the pedagogical value.

6. **Missing paper-drive artifacts.** The paper-drive methodology calls for source assessment, synthesis papers, and slide decks. None of these higher-order deliverables exist. The project has strong notes and two polished deep-dives but has not yet reached the synthesis/publication stage of the workflow.

---

## Recommendations

### Priority 1: Build remaining deep-dives (S3-S7)

The markdown notes for all five remaining sections are detailed enough to support HTML conversion. S3 (Rhythm) and S4 (Emotion) should be built next -- they have the strongest source bases (7 and 8 sources respectively, all with URLs) and their content connects directly to the completed S1-S2 material.

### Priority 2: Fix literature collection gaps

Pin the three vague citations in S5 to specific papers with URLs. Candidates:
- Alzheimer's music therapy: Sarkamo et al. (2014, Cortex) or Baird & Samson (2015, Music Perception)
- Reminiscence bump: Janata et al. (2007, Cerebral Cortex) or Schulkind et al. (1999, Memory & Cognition)
- Musical mnemonics: Wallace (1994, Journal of Experimental Psychology: Learning, Memory, and Cognition)

### Priority 3: Correct the changelog

Update the changelog entry for "Phase 2: Section Deep-Dives" to accurately reflect that only S1 and S2 were built as HTML, with S3-S7 having notes completed but HTML not yet constructed.

### Priority 4: Extract shared CSS/JS

The deep-dive CSS and JS are identical across the overview, S1, and S2 files. Extracting them to dd-shared.css and dd-shared.js would reduce duplication and make future section builds faster and more consistent.

### Priority 5: Embed audio content

The overview.mp3 file should be embedded in the overview page. Each section deep-dive would benefit from relevant audio examples -- even simple ones (e.g., a pure sine wave vs. a complex tone for S1, a comparison of Pythagorean vs. equal-tempered fifths for S2).

### Priority 6: Write synthesis paper

The synthesis notes (00-synthesis.md) are strong enough to serve as an outline for a full synthesis paper. The cross-section connections and key findings sections could be expanded into a publishable narrative that traces the central argument: music sits at the intersection of physics, neuroscience, and culture, and the tensions between these domains are where the most interesting questions lie.
