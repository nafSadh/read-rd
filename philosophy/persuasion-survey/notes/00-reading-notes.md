# Reading Notes — The Architecture of Influence

> Iterative reading notes per source. Each entry records what was read, key extractions, and connections to the taxonomy.

---

## SECTION 1: RHETORIC

### R-01: Aristotle, *Rhetoric* (via Stanford Encyclopedia of Philosophy)
**Source:** plato.stanford.edu/entries/aristotle-rhetoric/
**Coverage:** Comprehensive scholarly article (~15,000 words)

**Key extractions:**

1. **Definition:** "the ability to see what is possibly persuasive in every given case" (I.2, 1355b26f.). Not defined by product (speeches) or success (convincing) — defined by *capacity to analyze*.

2. **Three Appeals (with Aristotle's own framing):**
   - **Ethos:** Speaker must display phronêsis (practical intelligence), virtue, and good will. "People follow the trustworthy speaker more easily and more quickly on almost all subjects" (I.2, 1356a6–8). Critical: speaker must *appear* virtuous through the speech itself, not possess prior reputation.
   - **Pathos:** Emotions modify judgment. "Those things due to which people, by undergoing a change, differ in their judgements" (II.1, 1378a20–30). Aristotle catalogs specific emotions with trigger conditions — anger defined as "desire, accompanied with pain, for conspicuous revenge for a conspicuous slight" (II.2, 1378a31–33).
   - **Logos:** The probative means — "people are most or most easily persuaded, when they suppose something to have been proven" (I.1, 1355a3f.). The enthymeme (rhetorical syllogism) is the "body of persuasion."

3. **Rhetoric ↔ Dialectic:** Rhetoric is "counterpart" (antistrophos) to dialectic. Both address uncertain topics using accepted premises. By linking rhetoric to dialectic, Aristotle defends it as genuine art (technê) vs. Plato's dismissal.

4. **Moral neutrality:** Rhetoric is internally neutral but externally purposeful. "The art of rhetoric can be misused, since most goods (wealth, beauty) can be used better or worse." But: "easier to convince someone of the just and good than of their opposites."

5. **The Enthymeme:** Rhetorical equivalent of logical proof — deductive argument from premises audience already accepts. Sometimes premises implicit. Can be real (valid) or merely apparent (fallacious).

6. **Structure:** 3 books, 60 chapters total. Three genres: deliberative (future, assemblies), judicial (past, courts), epideictic (present, ceremonies).

**Connections:** This is the foundation. Every section of the survey maps back here — EXPLOIT weaponizes these three appeals, DEFEND builds resistance to them, AUTOMATE deploys them via machines, GOVERN tries to regulate their automated use.

---

### R-08/R-04 (Durmus et al.): "Persuasion with Large Language Models: a Survey" (arXiv 2411.06837)
**Source:** arxiv.org/html/2411.06837v1 (full HTML)
**Coverage:** Full survey read

**Key extractions:**

1. **Taxonomy:** Six configurable factors for LLM persuasion: interaction approach, model scale, AI source labeling, prompt design, personalization, authority appeals.

2. **Domain results:**
   - Public health: ~20% reduction in conspiracy beliefs via personalized dialogues (Costello et al.)
   - Politics: GPT-3 propaganda achieved 43.5% agreement vs 47.4% for human (Goldstein et al.)
   - E-commerce: 1,203-participant study on content paradigms (Zhang & Gosline)
   - Super-human persuasiveness documented in: debates (Breum et al.), vaccine messaging (Karinshak et al.), political issues (Hackenburg et al.)

3. **Personalization finding:** Personality-matching increases effectiveness; effect sizes small but robust even when AI authorship disclosed (Matz et al.).

4. **Interactive vs static:** "Active engagement typically achieves stronger persuasive effects than passive information delivery, particularly for complex topics requiring sustained attitude change."

5. **Ethical risks:** Monopolization of trusted information, AI-enabled censorship, echo chamber exacerbation, privacy exploitation, manipulation without designer intent.

6. **Measurement framework:** 7 categories — opinion change, agreement/accuracy, behavioral intent, engagement, perceived effectiveness, technical metrics, temporal patterns.

7. **Critical gap:** Most studies measure immediate effects only. Costello et al. and Altay et al. rare exceptions with 10-day and 2-month follow-ups.

**Connections:** This paper provides the conceptual framework for AUTOMATE section. Its six-factor model maps cleanly to our taxonomy — interaction approach and personalization are the key drivers, not model scale.

---

## SECTION 3: DEFEND

### D-08/D-09: Roozenbeek et al. 2022, "Psychological inoculation improves resilience against misinformation on social media" (Science Advances)
**Source:** Web search results + PubMed abstract
**Coverage:** Key findings via secondary sources

**Key extractions:**

1. **Design:** 7 preregistered studies — 6 RCTs (n = 6,464) + 1 YouTube field study (n = 22,632). Total N ≈ 29,000.

2. **Intervention:** 5 short inoculation videos targeting manipulation techniques: emotionally manipulative language, incoherence, false dichotomies, scapegoating, ad hominem attacks.

3. **Results:** Videos improved: manipulation technique recognition, confidence in spotting techniques, ability to discern trustworthy from untrustworthy content, quality of sharing decisions.

4. **Robustness:** Effects robust across political spectrum and wide variety of covariates.

5. **Practical form:** Short videos deliverable via social media platforms — scalable intervention.

**Connections:** This is the key evidence for DEFEND section's "inoculation at scale" subsection. The YouTube field study (22,632 participants) shows inoculation can work as platform-level intervention, not just individual therapy.

---

### D-04/D-05: Robertson, "Stoic Philosophy as Cognitive Behavioral Therapy"
**Source:** Web search results + book descriptions
**Coverage:** Key claims via secondary sources

**Key extractions:**

1. **CBT founders' explicit credit:**
   - Albert Ellis: "some of the central principles of REBT were originally discovered and stated by the Stoics"
   - Aaron Beck: "the philosophical origins of cognitive therapy can be traced back to the Stoic philosophers"

2. **Key parallels:**
   - Stoic praemeditatio malorum = CBT rational-emotive imagery (REI): repeatedly picturing future setbacks to reduce anxiety
   - Epictetus's dichotomy of control = CBT's cognitive restructuring: distinguishing what you can control from what you can't
   - Stoic prosoche (self-monitoring) = CBT self-monitoring and thought diaries

3. **Preventative vs therapeutic:** Stoicism has a more preventative orientation than CBT. CBT treats existing problems; Stoicism trains resilience *before* problems arise. This is exactly the inoculation model.

4. **The core insight:** Epictetus: "It's not things that disturb us, but our judgments about things." This is the CBT cognitive model in one sentence, 2,000 years early.

**Connections:** This bridges RHETORIC → DEFEND. The Stoics understood that persuasion operates through judgments (logos/pathos), and built defenses by training judgment itself. CBT formalized this; inoculation theory scaled it.

---

## SECTION 4: AUTOMATE

### A-02: Bai et al. 2025, "LLM-generated messages can persuade humans on policy issues" (Nature Communications)
**Source:** Web search results + Stanford GSB page
**Coverage:** Key findings

**Key extractions:**

1. **Design:** 3 pre-registered experiments, total N = 4,829.
2. **Policy topics:** Assault weapons ban, carbon tax, paid parental leave (deliberately polarized).
3. **Key finding:** LLM-generated persuasive messages produced significantly more attitude change than control. LLM messages "similarly effective" as human-crafted messages.
4. **Mechanism:** LLM messages considered persuasive due to "logical reasoning and clear presentation of facts."
5. **Effect size:** Small but significant — LLMs make production of political messaging more efficient while shifting opinions by a small percentage.

**Connections:** Evidence for AUTOMATE's claim that LLMs match human persuasiveness. The "small effect" finding connects to PNAS diminishing returns paper — the power isn't in individual message impact but in scalability.

---

### A-03: Hackenburg et al. 2025, "The levers of political persuasion with conversational AI" (Science)
**Source:** Oxford University press release + EurekAlert + arXiv
**Coverage:** Key findings via multiple secondary sources

**Key extractions:**

1. **Design:** 3 large-scale experiments, 76,977 participants, 19 LLMs, 707 political issues, 91,000 AI dialogues. UK participants.

2. **Key levers:**
   - Post-training methods boosted persuasiveness by up to **51%**
   - Prompting methods boosted by up to **27%**
   - Personalization and model scale had **smaller effects** than expected

3. **The information density factor:** Most persuasive AI systems produced information-dense arguments (fact-checkable claims). "Roughly half of the explainable variation in persuasion across models" traced to information density alone.

4. **The accuracy tradeoff:** Information-dense LLMs produced the most inaccurate claims. "Where these methods increased AI persuasiveness, they also systematically decreased factual accuracy." 466,769 LLM claims fact-checked.

5. **Scale:** Largest study of AI persuasion to date by a significant margin (77K vs typical 500–5,000 participant studies).

**Connections:** This is the centerpiece of AUTOMATE. The persuasion-accuracy tradeoff is the key finding — more persuasive = less truthful. This directly connects to RHETORIC (Plato's concern about rhetoric without truth) and GOVERN (why regulation must address accuracy, not just transparency).

---

## SECTION 5: GOVERN

### G-01: TAKE IT DOWN Act (Public Law 119-12, May 2025)
**Source:** Web search results + legal analysis
**Coverage:** Key provisions

**Key extractions:**
1. Criminalizes publishing non-consensual intimate deepfakes
2. Penalties: up to 2 years imprisonment (3 years for minors)
3. Platforms must remove content within 48 hours of valid takedown notice
4. Compliance procedures required by May 2026
5. First major federal legislation specifically targeting AI-generated harmful content

### G-04: State-Level Deepfake Legislation
**Source:** Deepfake Legislation Tracker + Wiley analysis
**Coverage:** Aggregate statistics

**Key extractions:**
1. 46 states have enacted deepfake legislation (as of Feb 2026)
2. 169 laws enacted since 2022
3. 146 bills introduced in 2025 alone
4. Colorado AI Act: risk/impact assessments, enforcement Feb 2026
5. Regulatory approach varies wildly: criminal penalties, civil liability, transparency requirements

### G-06: EU AI Act Article 50
**Source:** TechPolicy.Press + EU AI Act Newsletter
**Coverage:** Key provisions

**Key extractions:**
1. Transparency obligations for AI-generated content
2. Enforceable August 2026
3. Code of Practice draft published December 2025
4. Requirements: labeling, watermarking, metadata
5. Most comprehensive global framework

**Connections:** The governance landscape is exactly as fragmented as claimed — criminal prohibitions (TAKE IT DOWN), transparency mandates (EU AI Act), and technical standards (C2PA) operating in parallel without coordination.

---

## Cross-Section Synthesis Notes

**The throughline:** Aristotle identified three channels of persuasion (ethos, pathos, logos). Every subsequent development maps onto these:
- **Dark Triad exploits ethos** (authority impersonation, false credibility)
- **Cognitive biases exploit logos** (framing, anchoring, false reasoning)
- **Emotional manipulation exploits pathos** (fear, love-bombing, intermittent reinforcement)
- **LLMs deploy all three simultaneously** at scale, with information density (logos) explaining ~50% of variation
- **Inoculation theory defends logos** (teaching people to spot bad reasoning)
- **Stoicism/CBT defends pathos** (training emotional resilience)
- **Governance attempts to regulate ethos** (transparency, disclosure, authenticity)

**The asymmetry:** The Hackenburg et al. finding that persuasion and accuracy trade off is the modern version of Plato's original concern — that rhetoric divorced from truth is dangerous. The Stoic solution (train the audience's judgment) maps directly to inoculation theory. The governance solution (mandate transparency) maps to Quintilian's "good man speaking well." None alone is sufficient.
