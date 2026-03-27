# NPOV Review: Sleep & Dreams

**Reviewer:** Claude (automated NPOV audit)
**Date:** 2026-03-27
**Scope:** All content files in `cog-sci/sleep-and-dreams/`

## Files Reviewed

- `index.html` -- project landing page
- `overview.dd.html` -- comprehensive overview deep-dive
- `s1-why-we-sleep.dd.html` -- sleep architecture, evolution, Walker's framework
- `s2-sleeping-brain.dd.html` -- replay, spindles, glymphatic system, SHY
- `s3-dream-theories.dd.html` -- Freud through predictive processing
- `s4-lucid-dreaming.dd.html` -- LaBerge, neuroscience, PTSD applications
- `s5-deprivation.dd.html` -- Gardner, cognitive effects, blue light, shift work
- `s6-disorders.dd.html` -- insomnia, apnea, narcolepsy, FFI, parasomnias, TMR
- `literature-collection.md` -- 57 sources across 6 sections
- `survey-paper.html` -- synthesized survey
- `tensions-paper.html` -- six tensions analysis

## Pass 1

**Date:** 2026-03-27
**Status:** Read-only audit, no changes applied.

### Issues Found

#### POV
- None significant. Content maintains a neutral, survey-style voice. Competing theories presented side by side.

#### RIGOR
- S1/Walker section handles Guzey critique well.
- S2/Glymphatic controversy section commendable (flags limited human evidence).
- S3/Dream theories fairly notes evidence level for each theory.
- S4/Lucid dreaming PTSD 85% figure presented without sample size caveat.
- S5/Blue light section well-balanced.
- S5/Disaster attributions need hedging (multi-causal events).
- Literature collection gaps honestly documented.

#### BIAS
- Slight pro-CBT-I framing in S6 summary: "the speed of writing a script" carries editorial tone.
- No commercial bias detected.
- Source diversity adequate.

#### TONE
- S5 subtitle "The cognitive crisis hiding in plain sight" slightly alarmist.
- FFI described as "the most terrifying disease in medicine" in survey-paper (subjective).
- "Staggering evolutionary cost" (S1, overview) slightly loaded.
- S3 detail sec 04: "arguably the most theoretically sophisticated" is evaluative.

### Remaining Concerns (from Pass 1)
1. Lucid dreaming PTSD 85% figure should note sample size.
2. Disaster section causality language needs multi-causal acknowledgment.
3. Minor tone items at boundary between neutrality and accessible writing.
4. Survey-paper and tensions-paper needed full text review (only CSS reviewed in Pass 1).

---

## Pass 2

**Date:** 2026-03-27
**Status:** Full text review of all files including survey-paper.html and tensions-paper.html. Fixes applied.

### Issues Found and Fixed

#### 1. Loaded language: "staggering evolutionary cost"
- **Files:** `s1-why-we-sleep.dd.html`, `overview.dd.html`
- **Fix:** Changed "staggering" to "substantial" in both files.

#### 2. Alarmist subtitle in S5
- **File:** `s5-deprivation.dd.html`
- **Fix:** Changed subtitle from "The cognitive crisis hiding in plain sight" to "Cognitive effects, modern disruptions, and the sleep economy".

#### 3. Editorial tone in CBT-I framing
- **Files:** `s6-disorders.dd.html`, `overview.dd.html`
- **Fix (s6):** Changed "due to provider shortages and the speed of writing a script" to "largely due to a shortage of trained CBT-I providers and the logistical demands of an 8-session therapy compared to a brief medication visit."
- **Fix (overview):** Changed "due to provider shortages, cost barriers, and the speed of writing a prescription versus delivering an 8-session therapy" to "largely due to a shortage of trained CBT-I providers, variable insurance coverage, and the logistical demands of an 8-session therapy compared to a brief medication visit."

#### 4. PTSD 85% figure without sample size caveat
- **Files:** `s4-lucid-dreaming.dd.html`, `survey-paper.html`, `overview.dd.html`
- **Fix:** Added "though the sample was small" (s4), "in a small sample" (survey-paper, overview) to qualify the 85% figure.

#### 5. Multi-causal disaster acknowledgment
- **File:** `s5-deprivation.dd.html`
- **Fix:** Changed "Sleep deprivation has been implicated in some of the twentieth century's worst industrial disasters" to "Sleep deprivation has been implicated as a contributing factor in some of the twentieth century's worst industrial disasters. The Exxon Valdez, Chernobyl, Challenger, and Three Mile Island incidents were multi-causal events, but all involved..."

#### 6. Evaluative language in S3 predictive processing detail
- **File:** `s3-dream-theories.dd.html`
- **Fix:** Changed "This is arguably the most theoretically sophisticated current account" to "This is among the more theoretically developed current accounts".

#### 7. Subjective FFI description in survey paper
- **File:** `survey-paper.html`
- **Fix:** Changed "describes the most terrifying sleep disorder" to "describes one of the rarest and most clinically devastating sleep disorders".

#### 8. First-person "We" in survey paper abstract
- **File:** `survey-paper.html`
- **Fix:** Changed "We spend roughly a third of our lives asleep" to "Humans spend roughly a third of their lives asleep".

#### 9. "Hiding in plain sight" advocacy language
- **Files:** `survey-paper.html` (deprivation section), `s6-disorders.dd.html` (apnea detail)
- **Fix (survey):** Changed "a public health crisis hiding in plain sight" to "a widespread public health concern with well-documented consequences."
- **Fix (s6 apnea):** Changed "hiding in plain sight" to "that often goes unrecognized."

### Items Reviewed and Left Unchanged

- **First/second person in tensions-paper.html:** Uses "we" in several places ("we cannot agree," "we sleep," "we eat") but in the inclusive academic sense referring to the scientific community or humanity, not as personal POV injection. This is standard academic register for a tensions-analysis paper and does not compromise neutrality.
- **"Hiding in plain sight" in survey-slides.html and notes/05-deprivation.md:** These are companion/source files, not the primary published content. Left unchanged to avoid scope creep; the primary content files are the priority.
- **S2 "The Controversy" callout** ("science working as it should"): Mildly editorializing but defensible as a methodological observation about the scientific process. Left unchanged.
- **S4 detail "Results were striking":** Minor editorial flourish in detail-level text. Left unchanged as it is followed by appropriate caveats.
- **S6 FFI detail "among the most clinically devastating diseases known":** Factually defensible characterization given 100% fatality rate and no treatment. Left unchanged.

### New Issues Found in Pass 2 (survey-paper.html, tensions-paper.html)

These files were only structurally reviewed in Pass 1. Full text review in Pass 2 found:
- The survey paper and tensions paper are well-sourced with inline citations throughout.
- No unsupported claims detected -- all major assertions link to specific references.
- Competing positions are consistently presented in paired tension-card or tension-vs format.
- No systematic bias toward any single theory or position.
- The tensions paper's meta-tension section ("sleep resists simple explanation") is appropriately hedged and does not overstate conclusions.

## Overall Assessment (Post-Pass 2)

All actionable issues from Pass 1 have been addressed. The content now:
- Uses neutral, descriptive language where it previously used loaded or alarmist phrasing
- Qualifies the PTSD 85% finding with sample-size context across all files where it appears
- Acknowledges multi-causality in the disaster section
- Removes editorial tone from the CBT-I access gap discussion
- Replaces subjective superlatives with factual characterizations

The Sleep & Dreams project maintains strong NPOV standards. The remaining minor stylistic choices (occasional "striking," inclusive academic "we") are within normal bounds for educational survey writing and do not compromise the scientific neutrality of the content.
