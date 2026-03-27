# Peer Review -- Stoicism in Practice: Between Epictetus and Instagram

**Reviewer:** Agentic peer review (automated)
**Date:** 2026-03-25
**Project path:** `cog-sci/stoicism-in-practice/`

---

## Overall Assessment

| Criterion | Grade |
|-----------|-------|
| **Completeness** | A |
| **Source Quality** | B+ |
| **Analytical Depth** | A |
| **Structural Integrity** | A |
| **Presentation / UX** | A |
| **Overall** | **A-** |

This is a strong, well-executed paper-drive project that delivers all standard deliverables (literature collection, overview deep-dive, 6 section deep-dives, research notes, project metadata, index page) in a single session. The central analytical framework -- mapping the reappraisal/suppression distinction onto authentic vs. toxic Stoicism -- is genuinely insightful and sustained across every section. The main limitations are source-level: heavy reliance on secondary/popular commentary in the critical sections (S4, S5), a moderate but not deep primary-literature base in the neuroscience section (S2), and the absence of a synthesis paper or slide deck.

---

## Completeness Scorecard

| Deliverable | Status | Notes |
|-------------|--------|-------|
| `literature-collection.md` | Done | 54 sources across 6 sections, with gap analysis per section |
| `index.html` | Done | Clean project hub with section links, status badges, key tensions |
| Overview deep-dive (`overview.dd.html`) | Done | 6 subsections covering all dimensions; inline CSS (not shared) |
| S1: Science of Stoic Practice (`s1-science.dd.html`) | Done | 9 sources, 8 subsections |
| S2: Cognitive Mechanisms (`s2-mechanisms.dd.html`) | Done | 8 sources, 8 subsections |
| S3: Evidence-Based Stoicism (`s3-evidence.dd.html`) | Done | 10 sources, 8 subsections |
| S4: Misuse & Toxic Stoicism (`s4-misuse.dd.html`) | Done | 9 sources, 8 subsections |
| S5: Pop-Psychology Pipeline (`s5-pipeline.dd.html`) | Done | 8 sources, 8 subsections |
| S6: Integration & Clinical (`s6-integration.dd.html`) | Done | 10 sources, 8 subsections |
| Research notes (`notes/00` -- `06`) | Done | Synthesis note + 6 section notes with subsection plans |
| `.project/methodology.md` | Done | Research question, scope, source strategy, deliverables |
| `.project/changelog.md` | Done | Session 1 record with decisions |
| `.project/todo.md` | Done | Hand-off document with next steps |
| `dd-shared.css` + `dd-shared.js` | Done | Shared scaffold for S1--S6 deep-dives |
| Synthesis paper | Not started | Listed as optional in todo |
| Slide deck | Not started | Listed as optional in todo |
| Audio overview (`overview.mp3`) | Present | Audio file exists on disk |

---

## Content Quality

### Analytical Framework (A)

The project's central thesis -- that the Gross & John (2003) reappraisal/suppression distinction maps onto the difference between authentic Stoic practice and its toxic cultural derivatives -- is the strongest element. This framing is:

- Empirically grounded (48-study fMRI meta-analysis, TMS causal evidence)
- Philosophically literate (correctly distinguishing apatheia from emotional flatness, pathos from eupatheiai)
- Culturally applied (explaining how social media format selects for suppression messaging)
- Consistently threaded across all six sections

The synthesis note (`notes/00-synthesis.md`) clearly articulates both the reappraisal-suppression framework and the McMindfulness commercialization parallel. The five "Key Tensions" on the index page are well-chosen and non-trivial.

### Source Adequacy (B+)

54 sources is adequate for this scope. Breakdown by quality tier:

- **Peer-reviewed primary research:** ~12 sources (Buhle et al. 2014, Gross & John 2003, Butler et al. 2003, LeBon et al. 2025, TMS-fMRI 2023, amygdala-PFC studies, ACT review, gratitude meta-analyses, journaling meta-analysis, masculinity norms PMC 2025). Solid base.
- **Practitioner/bridge literature:** ~8 sources (Robertson's books and toolkit, Ellis/Beck lineage pieces, Stockdale). Good coverage of the clinical integration angle.
- **Cultural criticism and commentary:** ~15 sources (Trill Mag, Paideia Institute, Medium critiques, The Conversation, Quartz, Philosophy blogs). Adequate for cultural analysis, but these are journalistic or opinion pieces, not systematic studies.
- **Primary Stoic texts or scholarly editions:** 0 explicit citations. The project discusses Seneca, Epictetus, Marcus Aurelius, and Chrysippus extensively but never cites specific works or translations directly.
- **Modern Stoicism org data:** ~6 sources (Stoic Week reports, SABS, SMRT). Good use of the main empirical source for Stoic practice outcomes.

**Source gaps identified by the project itself (honest and accurate):**
- No RCTs testing Stoic practice as a complete package
- No fMRI studies of people specifically practicing Stoic exercises
- No systematic content analysis of social media Stoic accuracy
- No longitudinal harm data from misapplied Stoicism

### Section-Level Quality

**S1 (Science):** Strongest on SABS and Stoic Week data. Correctly identifies the self-selection and lack-of-control-group limitations. Could benefit from more detail on SMRT outcomes.

**S2 (Mechanisms):** The best-sourced section. The Stoic practice-to-neural-mechanism mapping table is a genuine contribution. The TMS causal evidence is well-highlighted. Missing: direct engagement with the predictive processing literature for premeditatio malorum.

**S3 (Evidence):** Excellent historical lineage (Epictetus to Ellis to Beck to ACT). The timeline component in the deep-dive is effective. The "Evidence Gap: Components vs. Package" subsection is admirably honest about what the evidence does and does not show.

**S4 (Misuse):** Culturally the most urgent section and the writing is sharp. The "Broicism Takes / Leaves Behind" comparison and the "Social Media vs. Real Stoicism" table are effective devices. Weakness: relies heavily on journalistic sources; the PMC 2025 masculinity norms study is the only primary empirical source on harm.

**S5 (Pipeline):** The McMindfulness parallel is the strongest analytical move. The "What Gets Lost" analysis (physics, logic, ethics sequentially stripped) is well-structured. The Silicon Valley adoption angle adds useful context. Weakness: the critique of Holiday is built primarily from reviews and opinion pieces rather than systematic analysis of his actual content.

**S6 (Integration):** The Stockdale material is compelling and well-used. Robertson's clinical bridge work is well-covered. The future research agenda (RCTs, longitudinal SMRT, neuroimaging of practitioners) is concrete and actionable. The military resilience section (CSF/MRT) could engage more deeply with the critique that these programs reduce philosophy to endurance training.

### Presentation Quality (A)

- The `dd-shared.css` and `dd-shared.js` scaffold provides a consistent, polished reading experience across all section deep-dives
- Light/dark theme toggle works correctly
- The overview uses inline CSS (duplicating the shared styles) -- minor inconsistency but functional
- Rich UI components used throughout: stat bars, feature grids, verdict tables, timelines, callout boxes, security boxes, chip tags
- Mobile-responsive layout with media queries at 1000px breakpoint
- Index page is clean and navigable with status badges and section descriptions

---

## Strengths

1. **Strong central thesis:** The reappraisal/suppression framework gives the entire project analytical coherence. It is not just a survey of "what people say about Stoicism" but an argument about *why* the pop version causes harm, grounded in neuroscience.

2. **Balanced critical lens:** Sections S4 and S5 are given equal weight to the positive evidence in S1 and S3. The project does not advocate for or against Stoicism; it maps the evidence landscape honestly.

3. **Honest about evidence gaps:** The project repeatedly acknowledges that most evidence supports components of Stoic practice (reappraisal, gratitude, journaling) rather than the integrated Stoic package. The SABS is correctly identified as a milestone that makes future RCTs possible, not as proof that Stoicism works.

4. **Full deliverable set in one session:** All standard paper-drive deliverables are present and complete. The project did not leave partial deep-dives or stub pages.

5. **Effective use of the Tensions framework:** The literature collection identifies genuine unresolved tensions (reappraisal vs. suppression, philosophy vs. therapy, accessibility paradox) rather than manufactured disagreements.

6. **Good companion project awareness:** The todo notes the relationship with `philosophy/stoicism-landscape`, correctly placing this project in the cognitive science / clinical psychology lane.

---

## Weaknesses

1. **No primary Stoic text citations:** The project discusses Epictetus, Seneca, Marcus Aurelius, and Chrysippus extensively but never cites specific works, passages, or translations. For a project claiming to distinguish authentic from distorted Stoicism, direct textual engagement would strengthen the authority of those claims.

2. **Thin empirical base for harm claims (S4):** The argument that pop Stoicism causes measurable harm is central to the project's critical lens, but it rests on a single PMC study on masculinity norms plus general suppression research (Gross & John, Butler et al.). The project correctly flags this gap but the gap is significant.

3. **Overview deep-dive uses inline CSS:** The overview.dd.html duplicates the entire CSS/JS scaffold inline rather than referencing `dd-shared.css` and `dd-shared.js`. This creates a maintenance inconsistency -- if the shared styles are updated, the overview will drift.

4. **No synthesis paper:** The project's analytical framework (reappraisal-suppression mapping, McMindfulness parallel, evidence gap analysis) is strong enough to warrant a standalone paper. Currently this analysis lives only in the deep-dives and notes.

5. **Cultural criticism sections lack systematic methodology:** S4 and S5 draw on journalistic sources and opinion pieces. A more rigorous approach would include systematic content analysis (e.g., coding a sample of TikTok Stoicism videos) or at minimum would frame the journalistic sources as illustrative rather than evidentiary.

6. **Source overlap between S3 and S6:** Several sources (Robertson's work, the CBT lineage material) appear across both sections. While some overlap is natural, the two sections could be more clearly delineated -- S3 as historical lineage and evidence, S6 as forward-looking clinical applications.

---

## Recommendations

1. **Add primary text citations:** Include specific citations to Epictetus (*Discourses*, *Enchiridion*), Seneca (*Letters*, *On Anger*, consolation letters), Marcus Aurelius (*Meditations*), and Chrysippus (fragments via Long & Sedley or similar). Even brief textual anchors would significantly strengthen the project's philosophical credibility.

2. **Write the synthesis paper:** The analytical framework is strong enough. A paper titled something like "Between Epictetus and Instagram: The Reappraisal-Suppression Framework for Understanding Modern Stoicism" could integrate the best material from S2, S4, and S5 into a coherent argument.

3. **Refactor overview.dd.html to use shared CSS/JS:** Align with the S1--S6 pattern by moving the overview to `<link rel="stylesheet" href="dd-shared.css">` and `<script src="dd-shared.js"></script>`.

4. **Strengthen S4 with additional empirical sources:** Search for research on alexithymia and emotional suppression in male populations, grief complication from avoidant coping, and any emerging studies on social media philosophy exposure effects. This would move the harm argument from plausible to well-evidenced.

5. **Consider a "What the Stoics Actually Said" reference section:** A brief appendix or supplementary page with key passages from primary texts would serve as a corrective reference -- the reader could verify claims about "what Stoicism actually teaches" against the source material.

6. **Add a slide deck for the core argument:** The reappraisal-suppression framework, the McMindfulness parallel, and the 5 key tensions would make a compelling 15-slide deck suitable for academic or professional presentation.
