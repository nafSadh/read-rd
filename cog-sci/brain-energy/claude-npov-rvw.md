# NPOV Review -- Brain Energy & Metabolic Psychiatry

## Files Reviewed
- `.project/methodology.md`
- `notes/00-synthesis.md`
- `notes/01-metabolic-theory.md`
- `notes/02-mitochondria.md`
- `notes/03-psychiatric-applications.md`
- `notes/04-neuroinflammation.md`
- `notes/05-interventions.md`
- `notes/06-clinical-evidence.md`
- `literature-collection.md` (50 sources)

Note: This project has notes and literature collection but no survey paper HTML yet. Deep-dive HTML files have not been built. Review is based on the notes and literature collection.

## Issues Found

### POV

1. **Framing as "emerging field" is appropriate.** The methodology explicitly treats metabolic psychiatry as an emerging field with limitations, not settled science. This is a neutral and accurate framing.

2. **Palmer is treated as a serious researcher, not a guru.** The notes flag researcher-advocate overlap as a bias risk, which is important given Palmer's dual role as clinician, author, and advocate. The notes avoid hagiographic treatment.

3. **The synthesis notes lean toward the metabolic theory.** Phrases like "strong biology" and the evidence hierarchy listing emphasize what works. The critiques section (S6) has shorter notes than the mechanism sections (S2, S4, S5). This creates a structural imbalance where the evidence for the theory is more developed than the evidence against.

### RIGOR

1. **Literature collection is strong and well-sourced.** 50 sources including meta-analyses, RCTs, systematic reviews, and critical commentary. Source types are clearly labeled.

2. **Evidence hierarchy in synthesis is well-calibrated.** The Strong/Moderate/Emerging/Preliminary gradation is honest and resists the temptation to overstate the clinical evidence.

3. **Notes acknowledge the single-RCT problem.** The JAMA Psychiatry 2025 trial is correctly categorized as "emerging" rather than definitive.

4. **Missing explicit critique sources.** The literature collection has a "Clinical Evidence & Critiques" section (S6) but the critical voices are mainly from within the sympathetic community (Freudenreich, Sarnyai). There is no dedicated skeptic or hostile critic in the collection -- no equivalent of Kagan for attachment theory. This is a gap. Metabolic psychiatry has critics who argue it overextends, and they should be represented.

### BIAS

1. **Ketogenic diet is given disproportionate emphasis.** Of 11 intervention sources, 7 are about ketogenic diets. Exercise, fasting, sleep, and supplements share the remaining 4. This tracks real research output but may give readers the impression that keto is the primary intervention, when exercise has a much larger evidence base for depression.

2. **Industry source inclusion.** Metabolic Mind (source 49) and Behavioral Health Business (source 47) are industry/advocacy sources. Their inclusion is fine for tracking field trajectory, but they should be clearly marked as non-peer-reviewed advocacy, not evidence.

3. **"Stanford 75% recovery" appears in notes without qualification.** This figure from the Stanford pilot (Sethi et al.) is repeated across multiple notes sections. Pilot studies with small samples and self-selected participants routinely produce inflated recovery rates. The notes should flag this more explicitly.

### TONE

1. **Notes are telegraphic and appropriately neutral.** The abbreviation style (bullet points, short lines) avoids editorializing. This is a strength.

2. **The synthesis notes' "BHB is more than fuel" line has an advocacy feel.** It reads as an argument for the theory rather than a neutral summary of findings.

## Fixes Applied

None. The project is in an earlier stage (notes + literature, no survey paper). Issues flagged here should inform the survey paper when it is written.

## Remaining Concerns

- The project needs at least 2-3 sources from explicit critics of the metabolic psychiatry paradigm -- researchers who argue it is reductive, overhyped, or premature.
- The Stanford pilot figure (75% recovery) needs consistent qualification wherever it appears.
- When the survey paper is written, the keto-to-exercise ratio in the interventions section should be rebalanced to reflect the relative maturity of evidence bases.
- The timeline prediction ("2-5yr larger RCTs, 5-10yr possible mainstream") in S6 notes reads as field advocacy rather than neutral assessment.

---

## Pass 2

### Files Reviewed

All .dd.html deep-dive pages and the tensions-paper.html synthesis paper, plus index.html:

- `overview.dd.html`
- `s1-metabolic-theory.dd.html`
- `s2-mitochondria.dd.html`
- `s3-psychiatric-applications.dd.html`
- `s4-neuroinflammation.dd.html`
- `s5-interventions.dd.html`
- `s6-clinical-evidence.dd.html`
- `tensions-paper.html`
- `index.html`

### POV

No first-person or second-person ("you/your/we/our") language found in any file. The deep-dives and tensions paper maintain consistent third-person encyclopedic voice throughout. This is clean.

### Tone: Editorial Flourishes Fixed

The deep-dive pages had several instances of editorial/advocacy language that went beyond neutral description:

1. **"striking"** -- Used 6 times across files to describe pilot results, cross-diagnostic patterns, and psychiatric comorbidity. Replaced with "notable," "high," or removed where the surrounding context already conveyed significance.
   - `overview.dd.html` (x2): "striking" -> "notable"
   - `s3-psychiatric-applications.dd.html` (x2): removed or replaced with neutral phrasing
   - `s2-mitochondria.dd.html` (x2): "striking" -> "high" and "notable"

2. **"dramatic" / "dramatically"** -- Used to describe bipolar oscillations, metabolic syndrome rates, and FMT. Replaced with neutral descriptors.
   - `s3-psychiatric-applications.dd.html`: "dramatic oscillations" -> "oscillations"; "dramatically exceed" -> "substantially exceed"
   - `s1-metabolic-theory.dd.html`: "Dramatically elevated" -> "Elevated"
   - `s4-neuroinflammation.dd.html`: "most dramatic intervention" -> "most direct intervention"

3. **"profoundly"** -- Used to describe dietary effects on brain function. Replaced with "significantly."
   - `s1-metabolic-theory.dd.html`: "profoundly affect" -> "significantly affect"

4. **"remarkably"** -- Describing consistency of animal model findings. Removed as the word adds emphasis rather than information.
   - `s3-psychiatric-applications.dd.html`: "remarkably consistent" -> "consistent"

5. **"vital" / "critical" / "essential"** -- Used where "important" or "necessary" suffices. These words imply indispensability beyond what the evidence warrants.
   - `s3-psychiatric-applications.dd.html`: "critical connecting mechanism" -> "connecting mechanism"; "vital roles" -> "important roles"
   - `s2-mitochondria.dd.html`: "essential" -> "important" (in callout)
   - `s5-interventions.dd.html`: "essential" -> "necessary" (medication monitoring); "essential electron carrier" -> "required electron carrier"
   - `s6-clinical-evidence.dd.html`: "essential for honest assessment" -> "important for honest assessment"

6. **"compelling"** -- Used to describe the biology in a callout box. Replaced with "well-supported."
   - `s6-clinical-evidence.dd.html`: "The biology is compelling" -> "The biology is well-supported"

7. **"demolishes"** -- Used to describe the impact of pre-treatment metabolic findings on the iatrogenic argument. Replaced with "undermines" -- a strong but not absolutist term.
   - `s3-psychiatric-applications.dd.html`: "This demolishes the argument" -> "This undermines the argument"

### Scholastic Rigor: Stanford 75% Qualification

Pass 1 flagged that the Stanford pilot 75% recovery figure was repeated without adequate qualification. Pass 2 found this figure appeared in 4 files across 6+ locations. Fixes applied:

- `overview.dd.html`: Added "(n=21, uncontrolled)" to inline mention; added "no control group" to detailed mention.
- `s1-metabolic-theory.dd.html`: Added "(n=21, uncontrolled)" and changed "75% recovery" to "reported 75% recovery."
- `s3-psychiatric-applications.dd.html` (bipolar section): Replaced editorial assessment ("magnitude was striking") with explicit limitation language: "sample was small (n=21), unblinded, and lacked a control group, so these results should be interpreted as preliminary."
- `s3-psychiatric-applications.dd.html` (schizophrenia section): Rewrote to explicitly note pilot studies with self-selected participants routinely produce inflated effect sizes.
- `overview.dd.html` (superlative claim): "This is the strongest disorder-specific evidence" -> "This represents some of the more direct disorder-specific evidence."

### Scholastic Rigor: Causation Language

- `s6-clinical-evidence.dd.html`: "This finding alone shifts the framing" -> "This finding supports reframing" -- a single finding does not by itself shift an entire field's framing.

### Logical Consistency

No contradictions found between files. The evidence hierarchy is consistent across the overview, deep-dives, and tensions paper. Claims made in the tensions paper are supported by the sources cited in the deep-dives.

### What Was Clean

- **tensions-paper.html**: Well-structured with balanced "why both sides are right" framing. "Paradigm shift" language is correctly attributed to Palmer rather than asserted by the author. The conclusion ("biologically plausible, clinically preliminary, institutionally legitimate, commercially premature") is appropriately hedged.
- **s6-clinical-evidence.dd.html**: The critiques section (theoretical, methodological, implementation) is substantive and gives genuine weight to counterarguments. The "What Remains Uncertain" column in the verdict box is honest.
- **index.html**: Descriptive, no tone issues.
- **No first/second person found anywhere.** All files maintain encyclopedic register.

### Remaining Concerns (carried from Pass 1, still applicable)

- The project still needs 2-3 explicit critic sources (researchers who argue metabolic psychiatry is reductive or overhyped).
- The keto-to-exercise ratio in s5-interventions is still skewed toward keto. Exercise has the deeper evidence base but gets less detailed treatment.
- Industry sources (Metabolic Mind, Behavioral Health Business) are cited in s6 and tensions-paper without explicit non-peer-reviewed labeling.
