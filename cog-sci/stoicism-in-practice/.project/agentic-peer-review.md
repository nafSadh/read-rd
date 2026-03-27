# Peer Review -- Stoicism in Practice: Between Epictetus and Instagram

**Reviewer:** Agentic peer review (automated)
**Date:** 2026-03-26
**Round:** 2
**Project path:** `cog-sci/stoicism-in-practice/`

---

## Overall Assessment

| Criterion | Grade |
|-----------|-------|
| **Completeness** | A |
| **Source Quality** | B+ |
| **Analytical Depth** | A |
| **Structural Integrity** | A |
| **Presentation / UX** | A- |
| **Overall** | **A-** |

Since the round 1 review (2026-03-25), the project has added a survey paper (`survey-paper.html`) with 34 cited sources and a sidebar-navigated academic layout. The index page now links to this paper and to an audio overview. All six section deep-dives remain complete and substantive. The central analytical framework -- mapping the Gross & John reappraisal/suppression distinction onto authentic vs. toxic Stoicism -- continues to be the project's strongest element, and it is now articulated most fully in the survey paper. The main unresolved issues from round 1 persist: no primary Stoic text citations, thin empirical base for harm claims in S4, and the overview deep-dive still uses inline CSS rather than the shared stylesheet.

---

## Completeness Scorecard

| # | Deliverable | Status | Notes |
|---|-------------|--------|-------|
| 1 | `literature-collection.md` | Done | 54 sources across 6 sections, with gap analysis and tensions table |
| 2 | `index.html` | Done | Project hub with section links, status badges, key tensions; now links to survey paper and audio |
| 3 | Overview deep-dive (`overview.dd.html`) | Done | 6 subsections covering all dimensions; uses inline CSS (852 lines), not shared stylesheet |
| 4 | S1: Science of Stoic Practice (`s1-science.dd.html`) | Done | 9 sources, 8 subsections, uses `dd-shared.css` + `dd-shared.js` |
| 5 | S2: Cognitive Mechanisms (`s2-mechanisms.dd.html`) | Done | 8 sources, 8 subsections, best-sourced section with strong neuroscience evidence |
| 6 | S3: Evidence-Based Stoicism (`s3-evidence.dd.html`) | Done | 10 sources, 8 subsections, effective timeline component |
| 7 | S4: Misuse & Toxic Stoicism (`s4-misuse.dd.html`) | Done | 9 sources, 8 subsections, sharp cultural criticism |
| 8 | S5: Pop-Psychology Pipeline (`s5-pipeline.dd.html`) | Done | 8 sources, 8 subsections, McMindfulness parallel well-developed |
| 9 | S6: Integration & Clinical (`s6-integration.dd.html`) | Done | 10 sources, 8 subsections, Stockdale and Robertson material compelling |
| 10 | Survey paper (`survey-paper.html`) | Done (new since round 1) | 34 cited sources, 8 sections + abstract + references, sidebar navigation, academic layout |
| 11 | Research notes (`notes/00` -- `06`) | Done | Synthesis note + 6 section notes with subsection plans |
| 12 | `.project/methodology.md` | Done | Research question, scope, source strategy, deliverables checklist |
| 13 | `.project/changelog.md` | Done | Session 1 record with decisions |
| 14 | `.project/todo.md` | Done | Hand-off document with next steps |
| 15 | `dd-shared.css` + `dd-shared.js` | Done | Shared scaffold for S1--S6 deep-dives (15 + 122 lines) |
| 16 | Audio overview (`overview.mp3`) | Present | Audio file exists on disk |
| -- | Slide deck | Not started | Listed as optional |
| -- | Hero images (`img/`) | Not started | Prompts documented in `image-banana-claude.md` |

---

## Content Quality

### Analytical Framework (A)

The reappraisal-suppression framework remains the project's central contribution. With the addition of the survey paper, it now has a standalone articulation that integrates material from S2 (neuroscience), S4 (misuse), and S5 (pipeline) into a single argument. The framework is:

- Empirically grounded in the 48-study Buhle et al. (2014) fMRI meta-analysis and the 2023 TMS causal evidence
- Philosophically literate, distinguishing apatheia from emotional flatness and pathos from eupatheiai
- Culturally applied through the McMindfulness parallel and the "What Gets Lost" analysis
- Consistently threaded across all deliverables from notes through deep-dives through survey paper

The five "Key Tensions" on the index page are well-chosen: reappraisal vs. suppression, philosophy vs. therapy, dichotomy of control as tool vs. weapon, evidence quality, and the accessibility paradox. These are genuine unresolved questions, not manufactured controversy.

### Source Adequacy (B+)

54 sources remains adequate for this scope. The survey paper cites 34 of them with numbered references and hoverable footnotes. The tier breakdown is unchanged from round 1:

- **Peer-reviewed primary research:** ~12 sources (Buhle et al., Gross & John, Butler et al., LeBon et al. SABS, TMS-fMRI 2023, amygdala-PFC studies, ACT review, gratitude/journaling meta-analyses, masculinity norms PMC 2025). Solid empirical base.
- **Practitioner/bridge literature:** ~8 sources (Robertson, Ellis/Beck lineage, Stockdale). Good clinical integration coverage.
- **Cultural criticism and commentary:** ~15 sources (Trill Mag, Paideia Institute, Medium, The Conversation, Quartz). Adequate for cultural analysis but journalistic, not systematic.
- **Primary Stoic texts:** 0 explicit citations. Epictetus, Seneca, Marcus Aurelius, and Chrysippus are discussed extensively but never cited with specific works, passages, or translations.
- **Modern Stoicism org data:** ~6 sources (Stoic Week reports, SABS, SMRT).

The source gaps remain honestly identified: no Stoicism-specific RCTs, no fMRI of Stoic practitioners, no systematic content analysis of social media accuracy, no longitudinal harm data.

### Survey Paper Quality (A-)

The survey paper is the major addition since round 1 and addresses the round 1 recommendation to write a synthesis. It is well-structured with 8 sections plus abstract and references, uses a sidebar-navigated academic layout with inline footnotes, and sustains a coherent argument across its full length. It includes SVG diagrams (e.g., the reappraisal-suppression circuit diagram) and statistical callouts. The prose is clear and the citations are well-integrated with hoverable tooltips linking back to the literature collection.

Weaknesses of the survey paper: it uses its own inline CSS (not shared with any other page), the reference list uses the project's internal source IDs (e.g., "CM3 Gross & John") rather than standard academic citation format, and it does not cite any primary Stoic texts.

### Section-Level Quality (unchanged from round 1, brief updates)

**S1 (Science):** Strong on SABS and Stoic Week data. Self-selection and control-group limitations correctly identified. SMRT outcomes still underexplored.

**S2 (Mechanisms):** Best-sourced section. The Stoic practice-to-neural-mechanism mapping table is a genuine contribution. TMS causal evidence well-highlighted. Still missing predictive processing literature for premeditatio malorum.

**S3 (Evidence):** Excellent Epictetus-Ellis-Beck-ACT lineage. Timeline component effective. "Components vs. Package" gap analysis admirably honest.

**S4 (Misuse):** Culturally urgent, writing is sharp. "Broicism Takes/Leaves Behind" verdict table and "Social Media vs. Real Stoicism" comparison are effective. Empirical base for harm remains thin (single PMC 2025 study plus general suppression research).

**S5 (Pipeline):** McMindfulness parallel is the strongest analytical move. "What Gets Lost" analysis (physics, logic, ethics stripped sequentially) is well-structured. Holiday critique still built from reviews/opinion pieces rather than systematic content analysis.

**S6 (Integration):** Stockdale material compelling. Robertson's clinical bridge well-covered. Future research agenda concrete. Military resilience section still lacks deeper engagement with the critique that these programs reduce philosophy to endurance training.

### Presentation Quality (A-)

- S1--S6 deep-dives use `dd-shared.css` (15 lines, minified) + `dd-shared.js` (122 lines), providing a consistent three-panel layout with sidebar, main scroll, and expandable detail panel
- Survey paper has its own polished academic layout with sidebar navigation and intersection-observer-based active section tracking
- Index page has its own clean inline styling with theme toggle
- Overview deep-dive uses 852 lines of inline CSS duplicating the shared stylesheet -- this remains a maintenance inconsistency
- Theme toggle works across all pages (light/dark) but uses different localStorage keys (`theme` on index, `sip-theme` on survey paper) -- theme choice does not persist across pages consistently
- All deep-dives include hoverable footnote tooltips linking sources
- Mobile-responsive at 1000px (deep-dives) and 900px (survey paper) breakpoints

---

## Strengths

1. **Strong central thesis with standalone articulation.** The reappraisal-suppression framework now lives in a dedicated survey paper as well as being threaded through all six section deep-dives. This gives the project's core argument both a concise, citable form and a detailed, evidence-rich backing.

2. **Balanced critical lens.** The project gives equal weight to evidence supporting Stoic practices (S1, S2, S3) and to evidence of their distortion and misuse (S4, S5). It neither advocates for nor dismisses Stoicism; it maps the evidence landscape.

3. **Honest about evidence gaps.** The project consistently distinguishes between evidence for components of Stoic practice (reappraisal, gratitude, journaling) and the untested Stoic package as a whole. The SABS is correctly positioned as a measurement milestone, not proof of efficacy.

4. **Complete deliverable set.** All standard paper-drive deliverables are present: literature collection, overview deep-dive, 6 section deep-dives, research notes, project metadata, index page. The survey paper and audio overview go beyond minimum requirements.

5. **Rich interactive presentation.** The deep-dive scaffold (three-panel layout with expandable detail views, hoverable footnote tooltips, theme toggle, sidebar navigation) provides a polished reading experience that rewards engagement.

6. **Effective use of comparative analysis.** The McMindfulness parallel, the "Broicism Takes/Leaves Behind" verdict table, and the Stoic practice-to-neural-mechanism mapping table are analytical devices that do genuine intellectual work, not just visual decoration.

---

## Weaknesses

1. **No primary Stoic text citations (persists from round 1).** The project discusses Epictetus, Seneca, Marcus Aurelius, and Chrysippus extensively but never cites specific works, passages, editions, or translations. For a project whose core claim is that pop culture distorts what the Stoics "actually taught," the absence of direct textual evidence is a credibility gap.

2. **Thin empirical base for harm claims in S4 (persists from round 1).** The argument that pop Stoicism causes measurable psychological harm rests on one PMC 2025 study on masculinity norms plus general suppression research from Gross & John and Butler et al. The project correctly flags this gap, but it remains the weakest empirical link in the chain.

3. **Overview deep-dive uses inline CSS (persists from round 1).** `overview.dd.html` duplicates the full CSS/JS scaffold (852 lines) inline rather than referencing `dd-shared.css` and `dd-shared.js`. If shared styles are updated, the overview will diverge.

4. **Inconsistent theme persistence across pages.** The index page uses `localStorage.getItem('theme')`, the survey paper uses `localStorage.getItem('sip-theme')`, and the deep-dives use the shared JS scaffold's own key. A user toggling dark mode on one page will not see it persist when navigating to another page type.

5. **Survey paper uses non-standard citation format.** References are listed as internal source IDs (e.g., "CM3 Gross & John") rather than standard academic citation format (APA, Chicago, etc.). This limits the paper's utility as a standalone academic artifact.

6. **Cultural criticism sections (S4, S5) lack systematic methodology (persists from round 1).** These sections draw on journalistic sources and opinion pieces. The Holiday critique in S5 is built from reviews rather than systematic analysis of his actual published content. The TikTok analysis cites aggregate view counts but no systematic content coding.

---

## Recommendations

1. **Add primary text citations.** Include specific references to Epictetus (*Discourses* 1.1, *Enchiridion* 1, 5), Seneca (*Letters* 9, 63, 77; *On Anger* 2.36; consolation letters), Marcus Aurelius (*Meditations* 2.1, 4.3, 8.49), and Chrysippus fragments (via Long & Sedley *The Hellenistic Philosophers* or SVF). Even 10--15 targeted textual anchors would materially strengthen the project's authority.

2. **Standardize theme persistence.** Use a single localStorage key (e.g., `sip-theme`) across all pages -- index, overview, survey paper, and deep-dives. This requires updating `index.html`, `overview.dd.html`, and `dd-shared.js` to share the same key.

3. **Refactor overview.dd.html to use shared CSS/JS.** Replace the 852 lines of inline CSS with `<link rel="stylesheet" href="dd-shared.css">` and `<script src="dd-shared.js"></script>`, matching the S1--S6 pattern. This was recommended in round 1 and remains unaddressed.

4. **Convert survey paper references to standard academic format.** Replace internal IDs with proper citations (e.g., "Gross, J.J. & John, O.P. (2003). Individual differences in two emotion regulation processes. *Journal of Personality and Social Psychology*, 85(2), 348--362."). This would make the survey paper a more credible standalone document.

5. **Strengthen S4 with additional empirical sources.** Search for research on alexithymia prevalence in male populations, grief complication from avoidant coping styles, emotional suppression and suicidality, and any emerging studies on philosophy-exposure effects via social media. Even 3--4 additional empirical sources would substantially strengthen the harm argument.

6. **Add hero images.** The `image-banana-claude.md` file contains well-crafted prompts for 4 hero images. Generating and placing these would enhance the visual identity of the project's most-visited pages.
