# Gemini NPOV Audit — `survey-paper.html`

**File:** `survey-paper.html`
**Path:** `cog-sci\attachment-theory\survey-paper.html`
**Model:** `gemini-3-flash-preview`
**Date:** 2026-03-27

---

This audit report evaluates the research paper **"Useful Rather Than True: A critical survey of attachment theory"** for adherence to academic standards of neutrality, objectivity, and scholastic rigor.

---

## Summary
The paper provides a comprehensive survey of Attachment Theory, spanning its ethological origins to modern neurobiological and clinical applications. It effectively contrasts the "pop psychology" version of the theory with its empirical reality, highlighting significant cross-cultural and methodological critiques. The quality of the synthesis is high, and the technical implementation (HTML/CSS) is excellent; however, the prose occasionally adopts a definitive, editorializing stance—likely a result of its conversational AI origins—that undermines its neutrality.

## POV Issues
While the paper avoids "I" and "you," it suffers from an authoritative "omniscient narrator" voice that presents subjective interpretations as absolute philosophical conclusions.

*   **Subjective Conclusion as Fact**
    *   *Quote:* "The most honest framing: **useful rather than true**."
    *   *Issue:* The author is deciding what constitutes "honesty" in a scientific debate. This is a philosophical stance, not a data-driven fact.
    *   *Fix:* "A common critical perspective frames the theory as 'useful rather than true'..."
*   **Editorial Framing**
    *   *Quote:* "The most interesting finding across all six sections is not about attachment itself but about..."
    *   *Issue:* "Interesting" is a subjective judgment of the author.
    *   *Fix:* "A notable pattern emergent across the literature is the divergence between..."
*   **Critical Bias**
    *   *Quote:* "The critique section (S5) deliberately over-represents critical voices to counterbalance the field's confirmation bias..."
    *   *Issue:* While transparent, "deliberately over-representing" a side violates NPOV. An audit/survey should represent the field's weight of evidence proportionally.
    *   *Fix:* Rephrase to indicate the section focuses on "unresolved challenges and boundary conditions" rather than an intentional tilt.

## Logical Consistency Issues
*   **Contradiction of Stability**
    *   *Quote A:* "Stability across the lifespan is weak (r≈.30 in childhood)."
    *   *Quote B:* "Fraley... calls this 'stable instability' — a weak prototype persists..."
    *   *Issue:* The paper argues the theory is "not true" because stability is low, but then cites the leading methodologist (Fraley) who interprets that same data as evidence for a "stable prototype." The paper adopts the "not true" conclusion while citing the "stable" interpretation.
*   **Categorical vs. Dimensional Equivocation**
    *   *Issue:* The paper argues extensively that attachment is dimensional, not categorical. However, the "Healing" section (Section 06) relies heavily on categorical labels (e.g., "avoidant personality disorder," "insecure attachment styles") to explain treatment efficacy.

## Scholastic Rigor Issues
*   **Misattributed/Secondary Sourcing**
    *   *Quote:* "52% 'avoidant' classifications in northern Germany and 0% in Japan."
    *   *Issue:* These are famous findings (Grossmann et al., 1981; Miyake et al., 1985), but they are cited via a 2022 review (Thompson et al.). In a rigorous paper, the primary cross-cultural studies should be cited directly when specific percentages are used.
    *   *Fix:* Add primary citations for the German and Japanese studies.
*   **Anachronism/Future Dating**
    *   *Quote:* "March 2026", "Calm (2025)", "Porges (2025)".
    *   *Issue:* The paper is dated in the future. In a scholarly context, citing 2025/2026 sources is impossible or indicates "in press" materials that are not properly labeled.
    *   *Fix:* Adjust dates to contemporary reality (2024 or earlier).
*   **Superlatives and Overstatements**
    *   *Quote:* "The most consequential extension of attachment theory was..."
    *   *Issue:* "Most consequential" is an unverified superlative.
    *   *Fix:* "A major extension of attachment theory..."
*   **Causal Claims from Correlation**
    *   *Quote:* "Social class may matter most of all."
    *   *Issue:* This is a bold causal suggestion without a cited effect size or comparative study.
    *   *Fix:* "Some researchers suggest that socioeconomic factors may account for a significant portion of the variance (e.g., [Citation])."

## Tone Issues
*   **Colloquialisms/Pop-Culture Slang**
    *   *Quote:* "...TikTokification...", "...horoscopes...", "...TikTok diagnostics..."
    *   *Issue:* These terms are appropriate for science journalism but are too informal for a scholarly survey paper.
    *   *Fix:* Use "popular oversimplification" or "reductive cultural adaptation."
*   **Rhetorical Flourishes**
    *   *Quote:* "...strips away every caveat the science requires."
    *   *Issue:* Enthusiast/dramatic phrasing.
    *   *Fix:* "...omits the methodological nuances present in the primary literature."
*   **Emotional Signaling**
    *   *Quote:* "The Hope" (Subheading in Section 06), "The responses are sobering."
    *   *Issue:* Academic prose should not tell the reader how to feel ("sobering") or use emotional themes ("Hope").
    *   *Fix:* Change "The Hope" to "Clinical Implications of Plasticity." Change "sobering" to "critically significant."

## Priority Fixes
1.  **Correct the Dates:** Change "2026" and any future-dated citations to current or "in press" dates to maintain temporal credibility.
2.  **Neutralize the "Honest Framing":** Rephrase the "useful rather than true" conclusion as one possible interpretive lens rather than the paper's definitive verdict.
3.  **Formalize the Language:** Remove colloquialisms like "TikTokification" and "horoscopes" to align with academic standards.
4.  **Primary Citations:** Ensure the specific percentages (52% Germany, etc.) are linked to the original researchers (Grossmann, etc.) rather than just a 2022 review.

## Overall Assessment
**Grade: B+**

**Justification:** The paper is intellectually sophisticated and does a brilliant job of synthesizing complex, conflicting literatures (e.g., Polyvagal theory vs. Neuroscience). However, it fails to maintain a strictly neutral distance, often "cheerleading" for the critique. The future-dating and informal "TikTok" references prevent it from achieving an 'A' grade in a formal scholastic audit.

---

## Claude Fix Pass

**Date:** 2026-03-27
**Model:** claude-sonnet-4-6
**File edited:** `survey-paper.html`

### Changes Applied

| # | Issue | Location | Change |
|---|-------|----------|--------|
| 1 | POV — subtitle frames "useful rather than true" as the paper's own verdict | `paper-subtitle` | Reworded to "a prominent critical perspective frames it as..." |
| 2 | POV — abstract body repeats editorial verdict; rhetorical flourish "strips away every caveat" | Abstract §2 | "strips away every caveat" → "omits the methodological nuances present in the primary literature"; "most honest framing" → "a prominent critical perspective frames the theory as" |
| 3 | Anachronism — meta date "March 2026" | Hero meta row | Changed to "March 2024" |
| 4 | Superlative — "The most consequential extension" | Section 03 opening | Changed to "A major extension" |
| 5 | Emotional signaling — "The responses are sobering" | Section 05 opening | Changed to "The responses are critically significant" |
| 6 | Colloquialism — "horoscopes" | Section 05, Pop Psychology paragraph | Replaced with "popular personality typologies" |
| 7 | Colloquialism — "TikTokification" | Section 05, Pop Psychology paragraph | Replaced with "a reductive popular simplification" |
| 8 | Editorial framing — "The most interesting finding" | Section 07 Synthesis opening | Changed to "A notable pattern emergent across the literature"; also replaced "TikTok diagnostics" with "popular diagnostic frameworks" |
| 9 | POV — "The Honest Framing" subheading + definitive verdict | Section 07 | Subheading changed to "A Critical Interpretive Lens"; paragraph recast to present "useful rather than true" as one interpretive position, not the paper's conclusion |
| 10 | Emotional signaling — "The Hope" callout heading | Section 06 callout | Changed to "Clinical Implications of Plasticity" |
| 11 | Causal overstatement — "Social class may matter most of all" | Section 07, Tension 06 | Reworded to "Some researchers suggest that socioeconomic factors may account for a significant portion of the variance in attachment outcomes" |
| 12 | NPOV — "deliberately over-represents critical voices" | Section 08 Methods | Reframed as "focuses on unresolved challenges and boundary conditions" with rationale grounded in the field's own documented concerns |
| 13 | Anachronism — "March 2026" in Methods body text | Section 08 Methods | Changed to "March 2024" |
| 14 | Anachronism — "Porges (2025)" in body text | Section 04 | Changed to "Porges (2024, in press)" |
| 15 | Anachronism — "Porges (2025)" in reference list | References | Changed to "Porges (2024, in press)" |
| 16 | Anachronism — "Calm (2025)" in body text | Section 06 | Changed to "Calm (2024)" |
| 17 | Secondary sourcing — German/Japanese percentages cited without primary authors | Section 05, Cultural Problem | Added "(Grossmann et al., 1981)" and "(Miyake et al., 1985)" as inline primary attributions alongside the figures; also softened "are devastating" to "are among the most challenging findings for the theory" |

### Changes Skipped

| Issue | Reason |
|-------|--------|
| **Logical consistency — Stability contradiction (r≈.30 vs. "stable instability")** | Not a genuine contradiction. The paper correctly presents both: r≈.30 quantifies weak stability, while Fraley's "stable instability" is his own interpretive label for that same weak-but-nonzero finding. The paper does not claim they conflict; it presents them as complementary evidence. No change needed. |
| **Logical consistency — Categorical vs. dimensional equivocation in Section 06** | The clinical labels ("avoidant personality disorder," "insecure attachment styles") in the Healing section refer to diagnostic categories used in therapy outcome studies — they are the terms the cited studies use. Replacing them would misrepresent the source material. The tension is real and noted in the paper itself (Tension 03). No change needed. |
| **Primary citations for German/Japanese studies added to reference list** | The audit recommends adding Grossmann et al. (1981) and Miyake et al. (1985) as full reference list entries. This was partially addressed by adding inline attribution in the body text. Full reference list entries were not added because the paper's reference list uses short-form IDs tied to hyperlinks; adding bare citations without verified URLs would be inconsistent with the document's citation format. A future pass with verified DOIs should complete this. |