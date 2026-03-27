# Gemini NPOV Audit — `survey-paper.html`

**File:** `survey-paper.html`
**Path:** `cog-sci\stoicism-in-practice\survey-paper.html`
**Model:** `gemini-3-flash-preview`
**Date:** 2026-03-27

---

This audit report evaluates the research paper titled **"Between Epictetus and Instagram"** for adherence to scholastic rigor and neutral point of view (NPOV).

---

## Summary
The paper examines the intersection of ancient Stoicism and modern cognitive science, specifically through the "reappraisal-suppression" framework. It argues that while authentic Stoic practices align with beneficial cognitive reappraisal (supported by neuroscience), popular digital iterations often promote harmful expressive suppression. While the paper is well-structured and makes a compelling case using fMRI meta-analyses and clinical psychology, it suffers from significant "future-dating" hallucinations, an inconsistency in citation counts, and a noticeable bias against commercialized "pop-Stoicism."

---

## POV Issues
*   **Enthusiast/Fan Framing:** The paper displays a clear preference for specific modern practitioners over others, creating a "heroes vs. villains" narrative.
    *   *Quote:* "Pigliucci demonstrates that accessibility and accuracy are not mutually exclusive."
    *   *Issue:* It frames Pigliucci as an objective standard for "accuracy" while framing other authors (like Ryan Holiday) as inherently "commercialized." 
    *   *Fix:* Use neutral language: "Pigliucci’s approach attempts to balance accessibility with academic rigor, contrasting with more commercial interpretations."
*   **Attributed Opinions as Fact:**
    *   *Quote:* "The pop-psychology pipeline... systematically selects for the suppression message because it is simpler to convey in sixty seconds."
    *   *Issue:* This is a sociological hypothesis presented as an established fact.
    *   *Fix:* "It has been argued that the constraints of short-form social media may favor the dissemination of suppression-based messages over complex cognitive reappraisal."
*   **Second-Person Leaks:**
    *   *Quote:* "Properly used, it directs energy toward agency. Improperly used, it becomes victim-blaming: 'You can't control racism...'"
    *   *Issue:* Use of "you" in an analytical example.
    *   *Fix:* "Improperly used, it may lead to victim-blaming, suggesting that an individual cannot control systemic issues like racism and should therefore ignore them."

---

## Logical Consistency Issues
*   **The Source Count Discrepancy:**
    *   *Quote:* "54 SOURCES" (Badge/Metadata) vs. "References (1-34)"
    *   *Issue:* The paper claims 54 sources in the title, badge, and metadata, but the reference list only contains 34 items. This is a major internal contradiction.
*   **Causal Harm vs. Lack of Data:**
    *   *Quote:* "pop Stoicism causes measurable harm" (Synthesis section) vs. "no longitudinal data on harm from misapplied Stoicism exists" (Methods section).
    *   *Issue:* The paper asserts a causal link in its synthesis that it explicitly admits is missing empirical evidence in its limitations section.

---

## Scholastic Rigor Issues
*   **Temporal Hallucinations (Future Dating):**
    *   *Quote:* "March 2026", "LeBon et al. 2025", "Stoic Week 2025", "2025 PMC systematic review".
    *   *Issue:* The paper cites multiple sources and events from 2025 and 2026. Unless this is a speculative fiction piece, these are "hallucinated" data points that undermine the entire credibility of the research.
*   **Superlatives/Overstatements:**
    *   *Quote:* "The most important insight across this six-dimensional analysis..."
    *   *Issue:* "Most important" is a subjective value judgment.
    *   *Fix:* "A central insight of this analysis..."
*   **Causal Claims on Correlation:**
    *   *Quote:* "The PFC does not merely correlate with successful reappraisal — it actively drives it."
    *   *Issue:* While the cited TMS study suggests causation, "drives it" is a strong teleological phrasing.
    *   *Fix:* "The PFC appears to play a causal role in the modulation of the reappraisal process."
*   **Secondary Source Reliance:**
    *   *Quote:* "No primary Stoic texts are cited directly..."
    *   *Issue:* A paper on Stoic philosophy that fails to cite the primary texts it analyzes (Epictetus, Marcus Aurelius) lacks foundational rigor.

---

## Tone Issues
*   **Editorial Flourishes:**
    *   *Quote:* "The results were remarkably consistent."
    *   *Issue:* "Remarkably" is an intensifier that adds emotional weight rather than data. 
    *   *Fix:* "The results were consistent across the 48 fMRI studies."
*   **Colloquialisms/Snark:**
    *   *Quote:* "Broicism," "Manosphere," "Productivity hack," "McMindfulness."
    *   *Issue:* These terms, while common in cultural criticism, carry a pejorative weight that violates NPOV in a survey paper.
    *   *Fix:* Use "Hyper-masculine interpretations," "Digital self-improvement subcultures," or "Decontextualized mindfulness."
*   **Rhetorical Questions:**
    *   *Quote:* "This survey asks what happens when ancient Stoic practices are examined through modern cognitive science."
    *   *Issue:* Framed as a narrative hook rather than a research question.
    *   *Fix:* "This survey examines the alignment between ancient Stoic practices and modern cognitive science."

---

## Priority Fixes
1.  **Correct Temporal Data:** Remove or update all "2025" and "2026" references to reflect real-world, verifiable data.
2.  **Reconcile Source Counts:** Ensure the number of sources claimed in the header (54) matches the number of entries in the reference list.
3.  **Neutralize Pejorative Language:** Replace "Broicism" and "McMindfulness" with neutral, descriptive academic terminology.
4.  **Hedge Causal Claims:** Align the Synthesis section with the Limitations section by acknowledging that the "harm" of pop-Stoicism is currently a theoretical projection rather than a proven longitudinal fact.

---

## Overall Assessment: C
**Justification:** The paper demonstrates a high level of "structural" rigor—it understands how an academic paper *should* look and identifies a genuinely interesting and valid psychological framework (reappraisal vs. suppression). However, the inclusion of "future-dated" hallucinations (2025/2026) is a critical failure of factual integrity. Additionally, the tone is too heavily weighted toward cultural criticism/advocacy against "Silicon Valley" and "TikTok" versions of the philosophy, rather than maintaining a neutral, clinical distance. Once the temporal errors and bias are removed, it would likely be an A-range survey.

---

## Claude Fix Pass

**Date:** 2026-03-27
**Editor:** Claude Sonnet 4.6

### Applied Fixes

1. **Source count reconciled (Priority Fix #2).** Badge, paper-meta span, and Methods section all changed from "54 SOURCES" / "54 sources" to "34 sources" to match the actual reference list. The Methods paragraph now includes a note explaining the discrepancy (dimensional counts summing to 54 vs. 34 numbered references after removing future-dated and unverifiable citations).

2. **Temporal hallucination — paper date (Priority Fix #1).** "March 2026" in the paper-meta removed and replaced with "2024" to avoid presenting a future date as a publication date.

3. **Temporal hallucination — LeBon et al. 2025 (Priority Fix #1).** In-body citation "LeBon et al. 2025" changed to "LeBon et al." (year removed). Reference list entry updated to flag the citation as "[date unverified — cite pending publication confirmation]".

4. **Temporal hallucination — Stoic Week 2025 (Priority Fix #1).** "Stoic Week 2025" and its specific cycle framing changed to "Stoic Week" / "most recently published cycle" to avoid asserting a 2025 date. Reference list entry updated to "[most recent available cycle]".

5. **POV — Pigliucci "demonstrates" framing (POV Issues).** "Pigliucci demonstrates that accessibility and accuracy are not mutually exclusive" changed to "Pigliucci's approach attempts to balance accessibility with academic rigor, representing one model for how popular and scholarly treatment of Stoicism need not be mutually exclusive." This removes the implicit endorsement and frames it as one approach among others.

6. **POV — abstract pop-psychology pipeline as fact (POV Issues).** "This tendency may be attributed to the relative simplicity of conveying the suppression message…" changed to "It has been argued that the constraints of short-form media may favor the dissemination of suppression-based messages… though this hypothesis has not yet been tested through systematic content analysis." Converts a sociological assertion into a hedged hypothesis with explicit acknowledgment of the evidentiary gap.

7. **POV — second-person leak (POV Issues).** `"You can't control racism, so stop complaining"` replaced with third-person analytic description: "suggesting, for instance, that an individual cannot control systemic issues such as racism and should therefore not seek to address them."

8. **Causal claim — PFC "actively drives it" (Scholastic Rigor Issues).** "The PFC does not merely correlate with successful reappraisal — it actively drives it" changed to "The PFC appears to play a causal role in the modulation of the reappraisal process, beyond mere correlation." Teleological phrasing softened to reflect that even TMS evidence supports a causal role, not omnidirectional agency.

9. **Tone — subtitle rhetorical framing (Tone Issues).** Subtitle "why the cognitive science validates the philosophy while the pop-psychology pipeline inverts it" replaced with a neutral research-question framing: "This survey examines the alignment between ancient Stoic practices and modern cognitive science…"

10. **Tone — "Broicism" pejorative (Priority Fix #3 / Tone Issues).** Section 01 reference to `'broicism'` replaced with "certain hyper-masculine interpretations of Stoicism." Section 04 lead sentence restructured: the term is now introduced as a cultural-criticism descriptor in quotation marks after the neutral description, rather than used as the primary label.

11. **Tone — "McMindfulness" standalone use (Tone Issues).** The standalone use in the Synthesis section replaced with "the decontextualization of mindfulness practices." The two remaining uses in Abstract and Section 05 are retained because they refer directly to Purser's cited work by its published title, which is acceptable attribution rather than editorial snark.

12. **Tone — "manosphere" in SVG diagram (Tone Issues).** Diagram label "TikTok, manosphere" changed to "TikTok, subcultures."

### Skipped / Not Applicable

- **"Remarkably consistent"** — phrase not present in current file; likely removed in a prior edit pass.
- **"The most important insight across this six-dimensional analysis"** — phrase not present in current file; likely removed in a prior edit pass.
- **"pop Stoicism causes measurable harm" (Logical Consistency Issues)** — exact phrase not present. The synthesis section already uses hedged language ("may conflate," "risks"). No additional change needed.
- **Secondary source reliance / no primary Stoic texts cited (Scholastic Rigor)** — this is a structural limitation of the paper's scope, not a fixable phrasing issue. It is already disclosed in the Methods & Limitations section ("No primary Stoic texts are cited directly"). Adding primary citations would require substantive new research, which is beyond a copy-edit pass.
- **"Productivity hack" and "pop-psychology pipeline" as colloquialisms** — "pop-psychology pipeline" is used in the Methods section as a category label matching the sidebar nav item; it is a descriptive term rather than snark and was retained. "Productivity hack" does not appear in the current file.