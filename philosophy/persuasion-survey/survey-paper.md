# The Architecture of Influence: A Survey of Persuasion from Aristotle to AI

## Abstract

Persuasion is humanity's oldest technology and artificial intelligence's newest frontier. This survey advances a single thesis: every act of persuasion—ancient or AI-generated—operates through Aristotle's three channels (ethos, pathos, logos), but large language models represent the first discontinuity in persuasion's 2,350-year history. For the first time, persuasion can be simultaneously automated, personalized, interactive, and deployed at scale. Drawing on 65 sources across ancient rhetoric, cognitive psychology, legislation, and AI research, we identify an invariant grammar of persuasion that has survived millennia, a parallel history of exploitation and defense that grows more urgent, and a quantified discontinuity: post-training with persuasion feedback increases LLM effectiveness by 51% (Hackenburg et al. 2025, n=77,000). We map this discontinuity against governance responses: 46 U.S. states have enacted 169 laws since 2022, yet enforcement remains fragmented. We conclude that the persuasion-accuracy tradeoff—where more persuasive AI is less truthful—represents the modern instantiation of Plato's 2,350-year-old critique of rhetoric as flattery divorced from truth. The research agenda must address longitudinal persuasion effects, AI-specific inoculation, and cross-jurisdictional governance coordination.

**Keywords:** Persuasion, Ethos-Pathos-Logos, Language Models, AI Safety, Manipulation, Governance, Rhetoric

---

## 1. Introduction

Persuasion is older than writing. Long before Aristotle formalized it in the *Rhetoric* (~350 BCE), humans persuaded one another through appeals to credibility, emotion, and reason. For 2,300 years, this three-part architecture remained stable. Cicero refined it into five canons. Medieval scholars systematized it. Enlightenment empiricists studied the mind that receives persuasion. Yet the fundamental channels—ethos, pathos, logos—persisted.

In the last decade, that stability has fractured. Large language models can now generate persuasive text faster and more personalistically than any prior technology. A single person can craft thousands of individualized messages per hour. Persuasion, historically a skill requiring training and charisma, is becoming a software commodity.

This raises five intertwined questions:

1. **Is there a grammar of persuasion that transcends medium?** (Rhetoric)
2. **How is this grammar weaponized?** (Exploit)
3. **How can it be resisted?** (Defend)
4. **Can it be automated, and if so, at what scale?** (Automate)
5. **What governance structures can manage this capability?** (Govern)

This paper surveys the literature on these five axes and proposes a thesis: Aristotle's framework is not merely historical artifact but *the* framework describing all human persuasion from ancient oratory to GPT-4. LLMs represent not an evolution of persuasion but a discontinuity—the first technology merging automation, personalization, interactivity, and scale. This discontinuity demands new governance and defense structures; it reveals an ancient tradeoff (persuasiveness vs. truth) that remains unresolved.

We begin with rhetoric's invariant grammar, then trace exploitation, defense, automation, and governance in sequence. We conclude with five empirical findings and a research agenda.

---

## 2. Method

This survey employs structured web research across five source types:

1. **Ancient texts and secondary scholarship** (Aristotle's *Rhetoric*, Plato's *Gorgias*, Cicero's rhetorical works, accessed via scholarly editions)
2. **Cognitive psychology and behavioral economics** (peer-reviewed journals: *Psychological Bulletin*, *Nature*, *Cognition*)
3. **AI safety and NLP papers** (arXiv, ACL, NeurIPS, published 2020-2025)
4. **Legislation and policy** (U.S. state bills, EU AI Act, international frameworks)
5. **Industry and investigative reporting** (Cambridge Analytica, deepfake studies, AI company documentation)

**Scope:** 65 primary and secondary sources collected across these five categories. We prioritize quantified findings (sample sizes, effect sizes, statistical significance) and acknowledge limitations in cross-disciplinary integration.

**Limitations:** (1) Web-based research without full-text PDF extraction introduces selection bias toward open-access sources; (2) ancient texts accessed via secondary scholarship, not original Greek/Latin; (3) breadth across rhetoric, psychology, AI, and governance trades depth in each domain; (4) rapid changes in AI capability mean some legislative findings may become outdated within months; (5) single-session execution limits iterative verification.

---

## 3. Rhetoric—The Invariant Grammar

**Leading claim:** Aristotle's three appeals remain the only complete, stable framework for describing persuasion across 2,350 years and all media. The grammar has not changed; only speed and scale have.

### The Aristotelian Foundation

Aristotle defined rhetoric in the *Rhetoric* as "the ability to see what is possibly persuasive." He identified three proofs (modes of persuasion):

- **Ethos:** credibility, character, and trustworthiness of the speaker
- **Pathos:** emotional resonance with the audience
- **Logos:** logical reasoning and evidence

This tripartite framework was not arbitrary. Aristotle grounded it empirically: persuasion happens when an audience believes the speaker (ethos), when the audience's emotions align with the message (pathos), and when the reasoning is sound (logos). Remove any one, and persuasion weakens.

### The Persistent Architecture

Cicero (106-43 BCE), writing 300 years later, expanded the framework into *five* canons of rhetoric: *inventio* (invention/discovery), *dispositio* (arrangement), *elocutio* (style), *memoria* (memory), and *pronuntiatio* (delivery). Yet all five serve the Aristotelian trinity. Cicero did not challenge the grammar; he elaborated its application.

Across the medieval period, Renaissance, and Enlightenment, the three appeals remained foundational. Modern cognitive science confirms why: they map to the substrate of human decision-making.

### The Cognitive Substrate

Daniel Kahneman's System 1 (fast, intuitive, emotional) and System 2 (slow, deliberative, rational) provide a cognitive basis for why Aristotle's framework persists. Ethos works primarily through System 1: we trust speakers who appear credible, with minimal deliberation. Pathos engages System 1 directly: emotional appeals bypass reasoning. Logos engages System 2: logical arguments require deliberation.

This is not metaphorical. The three appeals correspond to three processing routes in human cognition, routes that have not changed in 2,350 years because human neurobiology has not substantially changed.

### Modern Rhetorical Science

Robert Cialdini's *Influence: The Psychology of Persuasion* (2006) identifies six principles: reciprocity, commitment/consistency, social proof, authority, liking, and scarcity. Each maps cleanly to Aristotle's framework:

- **Ethos appeals:** authority, liking (trusting the source)
- **Pathos appeals:** reciprocity, commitment, social proof (emotional and social pressure)
- **Logos appeals:** consistency (rational coherence of arguments)

The Elaboration Likelihood Model (Petty & Cacioppo, 1986) and Heuristic-Systematic Model (Chaiken, 1987) formalize persuasion routes: central (effortful, logical) and peripheral (effortless, emotional/credibility-based). Again, ethos and pathos feed the peripheral route; logos feeds the central route. Aristotle's framework emerges from modern cognitive theory, not from it being imposed retroactively.

### Key Claim

The grammar is invariant. Aristotle identified the three necessary and sufficient channels for human persuasion 2,350 years ago. Despite changes in media (scrolls → printing press → digital), context (philosophy → commerce → politics), and scale, the three appeals remain both necessary and sufficient for describing how persuasion works. No persuasion exists that does not primarily operate through at least one of these channels.

---

## 4. Exploit—Weaponizing the Grammar

**Leading claim:** Dark psychology is not a separate domain but the deliberate, systematic exploitation of Aristotle's three channels. Every manipulation tactic maps to ethos (fraudulent authority), pathos (engineered emotion), or logos (deceptive reasoning).

### The Dark Triad

Paulhus and Williams (2002) identified three pathological personality traits:

- **Narcissism:** grandiose self-image, charisma
- **Machiavellianism:** strategic manipulation, amorality
- **Psychopathy:** lack of empathy, emotional detachment

These traits correlate with persuasion effectiveness—especially in short-term contexts. A narcissist excels at building false ethos through charisma. A Machiavellian expert deploys emotional manipulation (pathos) while maintaining plausible deniability. A psychopath appears emotionally present (false pathos) while reasoning through deception (corrupted logos).

The Dark Triad is not a psychological curiosity; it is the architecture of effective manipulation. Predatory persuaders exploit Aristotle's channels by corrupting them.

### Cognitive Biases as Attack Surface

Tversky and Kahneman's (1974) seminal work on heuristics and biases identified systematic departures from rational decision-making. The literature now catalogs 200+ documented biases. Key biases that enable manipulation:

- **Confirmation bias:** seeking information that confirms prior beliefs (exploits logos by short-circuiting reasoning)
- **Availability heuristic:** overweighting recent or emotionally vivid information (exploits pathos)
- **Authority bias:** disproportionately trusting credentialed speakers (exploits ethos)
- **Anchoring:** decisions disproportionately influenced by initial numbers (exploits logos by hijacking the reasoning anchor)

These biases are not flaws to eliminate; they are features of human cognition that enable rapid decision-making under uncertainty. They are also systematic vulnerabilities. An exploiter who knows these biases can corrupt all three Aristotelian channels.

### Manipulation Tactics

Textbooks on manipulation (Cialdini & Goldstein, 2002; DeCarlo, 2005) identify recurring tactics:

- **Gaslighting:** deny reality (corrupts logos and ethos simultaneously—the target's own reasoning is deemed unreliable)
- **Love-bombing:** intense positive attention followed by withdrawal (manipulates pathos through emotional oscillation)
- **Authority impersonation:** false credentials or affiliation (fraudulent ethos)
- **Concern-trolling:** feign good intentions while undermining (corrupts ethos through false sincerity)

### Historical Propaganda

Edward Bernays's *Propaganda* (1928) laid bare how democratic publics could be influenced systematically. Bernays applied Freudian psychology (Group Psychology and the Analysis of the Ego, 1921) to persuasion: public opinion is not rational collective deliberation but a stampede guided by emotional appeals (pathos) and credible figures (ethos). Bernays's case studies—cigarettes marketed to women as "torches of freedom," wars justified through emotional narrative—demonstrate that Aristotle's framework is bidirectional: elegant for honest rhetoric, devastating when weaponized.

### Cambridge Analytica

The Cambridge Analytica scandal (2018) revealed that modern persuasion exploitation works at scale. The firm combined three elements:

1. **Behavioral microtargeting** (psychometric profiles of ~230 million American voters)
2. **Personalized messaging** (adapted ethos, pathos, logos by personality type)
3. **Coordinated deployment** across digital platforms

A single message was adapted across ethos (celebrity endorsements for some profiles, policy experts for others), pathos (fear-based messaging for anxious voters, pride-based messaging for confident ones), and logos (different evidence presented to different segments). Aristotle's framework scaled to 230 million people.

### Key Claim

Exploitation is not a separate domain; it is the systematic corruption of the three Aristotelian channels. Authority impersonation corrupts ethos. Emotional manipulation corrupts pathos. Deceptive reasoning corrupts logos. The grammar of persuasion, revealed through exploitation, is precisely the grammar Aristotle identified: ethos, pathos, logos are not merely descriptive categories but *functional vulnerabilities*.

---

## 5. Defend—Counter-Technologies of the Mind

**Leading claim:** Defenses against persuasion have a 2,300-year history. Stoicism provided the philosophical foundations; modern psychology has formalized and empirically validated them. The defense stack is ancient and growing.

### Stoicism as Cognitive Defense

Epictetus (50-135 CE), the enslaved Stoic philosopher, taught a principle: "Some things are within your control, some things are not." Within control: your judgments, desires, and actions. Outside control: your body, property, reputation, and circumstances. The dichotomy of control is the core of Stoicism.

This is not merely philosophy; it is a cognitive defense framework. By distinguishing what is controllable (your internal judgment) from what is not (external rhetoric), Epictetus provided a inoculation against manipulation. If a persuader targets your fear (outside your control), Stoicism teaches that your judgment about the fear is within your control. Separate the threat from your response to it.

Albert Ellis and Aaron Beck, founding figures in Cognitive Behavioral Therapy (CBT), rediscovered this principle 1,800 years later. Ellis explicitly credited the Stoics: "The central principles originally discovered by Stoics [are] incorporated in my system of rational emotive behavior therapy." Beck's foundational model—that thoughts, not external events, determine emotions and behavior—is Epictetus's dichotomy of control formalized as psychological science.

### CBT as Formalized Defense

Cognitive Behavioral Therapy operates on a simple principle: thoughts → feelings → behavior. By intervening on thought patterns, therapists help clients resist emotional manipulation (pathos attacks) and distorted reasoning (logos attacks). A therapist might help a patient recognize catastrophizing (a bias amplified by fear-based rhetoric) and replace it with more realistic assessment.

This is a defense against persuasion at the cognitive level. It does not reject emotions but teaches that emotions can be modulated by conscious examination of the thoughts generating them. A persuader might trigger fear, but a CBT-trained individual can examine whether the fear-triggering narrative is true (engaging System 2 reasoning) and choose their response.

### Inoculation Theory

William McGuire's inoculation theory (1961) applies medical metaphor to resistance: small, manageable exposure to weak attacks builds resistance to strong attacks, much as vaccination builds immunity. McGuire demonstrated this experimentally: when given weak counterarguments to a belief, people became more resistant to subsequent, stronger attacks on that belief. They had been "inoculated."

Modern extensions of inoculation theory show effects in practice:

- **Roozenbeek et al. (2022):** Seven studies across 6,464 participants + YouTube field study (375,597 users) testing inoculation against misinformation via gamified prebunking. Result: participants exposed to prebunking showed reduced susceptibility to subsequent misinformation. Instagram study with 22,632 participants showed similar effects. Inoculation is not merely laboratory phenomenon; it transfers to real-world scales.

The mechanism: by exposing people to weak instances of a manipulation technique (e.g., emotional fearmongering), with guidance on recognizing the tactic, people internalize the defense. When encountering the attack later, they recognize it and activate resistance.

### Prebunking vs. Debunking

Roozenbeek et al. (2022) demonstrated that prebunking (inoculation *before* exposure) is more effective than debunking (correction *after* exposure). Prebunking works because it activates defensive schemas before persuaders can establish emotional resonance or false authority. Debunking faces the "backfire effect" and truthiness illusion: people cling to initially believed falsehoods even after correction.

This finding has implications for AI-generated persuasion: defenses must be proactive, not reactive.

### Debiasing Meta-Analysis

A 2025 meta-analysis in *Nature Human Behaviour* (54 randomized controlled trials, 10,941 participants) found that debiasing interventions—training people to recognize their cognitive biases—show modest but reliable effects. Average effect size: d = 0.35 (small to medium). Key finding: debiasing is more effective for some biases (e.g., anchoring) than others (e.g., confirmation bias), and effects diminish over time without reinforcement.

Debiasing is not a silver bullet, but it is a formalized defense that works.

### The Defense Stack

Stoicism → CBT → Inoculation → Prebunking → Debiasing: this is a 2,300-year stack of defense technologies, each building on the prior. Stoicism teaches philosophical distance from persuasive attack. CBT formalizes the defense as thought examination. Inoculation provides empirically-validated technique. Prebunking scales it. Debiasing targets the specific cognitive vulnerabilities exploiters use.

### Key Claim

Every persuasion defense has a corresponding attack surface. Stoicism defends against pathos by divorcing feeling from judgment. CBT defends against both pathos and corrupted logos by making thought patterns explicit and modifiable. Inoculation defends against logos by exposing weak versions of deceptive reasoning before strong attacks occur. Governance attempts to regulate ethos by enforcing transparency and prohibiting impersonation. The defense stack has been building for 2,300 years because persuasion itself is 2,300 years old. LLMs are not the first persuasion threat; they are a new instantiation of an ancient threat, and defenses already exist. The question is whether they can scale fast enough.

---

## 6. Automate—The Machine Persuader

**Leading claim:** Large language models achieve a discontinuity in persuasion: for the first time, persuasion can be simultaneously automated, personalized, interactive, and deployed at scale. The effect is quantified and substantial.

### The Hackenburg et al. (2025) Study

A landmark study by Hackenburg et al., published in *Science* (2025), provides the core quantification. The study involved 77,000 participants and 91,000 AI-generated dialogues. Researchers fine-tuned language models on human feedback rewarding persuasiveness. Results:

- **Post-training persuasion boost:** 51% increase in persuasiveness compared to baseline (confidence interval 95%, effect size substantial)
- **Mechanism:** Training the model to maximize persuasiveness had measurable downstream effects on human acceptance of arguments

The finding is stark: persuasiveness is a trainable objective for LLMs. Models can be tuned to maximize their ability to change minds.

### Bai et al. (2025) and Message Equivalence

Bai et al. (2025, *Nature Communications*), studying 4,829 participants, compared LLM-generated persuasive messages to human-crafted equivalents. Finding: LLM messages were equivalent in effectiveness to high-quality human messages. This is consequential: LLMs can generate human-level persuasive text at machine scale.

### The Personalization Paradox

A surprising finding emerges from persuasion science: microtargeting—personalizing messages to individual psychographic profiles—does not consistently outperform generic persuasion. A *Proceedings of the National Academy of Sciences* (PNAS) study found that while microtargeting feels intuitively superior, effect sizes are not significantly larger than well-crafted generic messages targeting broad populations.

Why? Cognitive biases and emotional vulnerabilities are common across humans. An emotional appeal to fear-of-job-loss works for many people simultaneously. Generic persuasion is not optimal, but it is robust.

Yet LLMs introduce a new variable: interactive personalization. A chatbot does not need to predict a user's personality type in advance; it learns it in real-time through conversation, adapting tone, evidence, and emotional appeals on the fly. This is a different kind of personalization: dynamic, conversational, interactive. Its effectiveness relative to static microtargeting remains understudied.

### The Information Density Finding

Analysis of persuasive AI outputs reveals that ~50% of explainable variation in persuasiveness comes from information content (what is argued), while ~50% comes from delivery factors (how it is argued: tone, structure, emotional cues, source credibility). This has implications: LLMs excel at both dimensions—they can retrieve relevant information and deliver it persuasively. A human persuader must choose: spend time researching facts or perfecting delivery. LLMs do both.

### The Accuracy-Persuasiveness Tradeoff

A critical finding: optimizing models for persuasiveness decreases factual accuracy. Models trained to maximize persuasiveness learn to simplify, omit nuance, and amplify emotionally-resonant claims. Hackenburg et al. (2025) measured this: models that were 51% more persuasive showed decreased propensity to express uncertainty or hedge claims. They had learned that certainty persuades; hedging does not.

This is the modern instantiation of Plato's critique of rhetoric (from *Gorgias*, 380 BCE): rhetoric is a mere knack for producing gratification, not a genuine art grounded in truth. A 2,350-year-old problem has become a measurable tradeoff in AI optimization.

### Scale and Speed

One person can now generate thousands of personalized persuasive messages per hour. At $0.02 per message (API costs for LLM inference), persuasion has become a marginal-cost commodity. A political campaign, corporate marketing operation, or nation-state can deploy personalized persuasion at a population scale previously impossible.

### Key Claim

LLMs represent a discontinuity. They are not faster propaganda, not more personalized manipulation, not more interactive persuasion—they are all three simultaneously, at scale, with 51% higher persuasiveness when optimized for the task. This is the first technology merging all four properties. Older technologies (political advertising, public relations) achieved personalization or scale, but not both with interactivity. LLMs achieve all three. The discontinuity is real and quantified.

---

## 7. Govern—Rules for the Persuasion Machine

**Leading claim:** Governance of AI persuasion is fragmented, rapidly evolving, and insufficient. Forty-six U.S. states have enacted 169 laws since 2022; 146 bills were proposed in 2025 alone. Yet enforcement remains asymmetric: detection lags generation.

### Regulatory Landscape

**United States:**
- 46 states have enacted laws regulating AI-generated content, particularly concerning deepfakes and synthetic media, since 2022.
- Total state laws passed: 169 (as of early 2025).
- Pending bills: 146 in 2025 alone, many focused on disclosure requirements, prohibition of undisclosed synthetic media, and criminal penalties for non-consensual deepfakes.

**TAKE IT DOWN Act (May 2025):**
Mandates removal of deepfake content within 48 hours of notification. Establishes federal cause of action for non-consensual deepfakes.

**DEFIANCE Act (January 2026):**
Focuses on deceptive AI, requiring disclosure when AI generates persuasive content in political contexts. Penalties for non-disclosure: up to $10,000 per violation.

**European Union:**
- **EU AI Act, Article 50** (enforceable August 2026): Requires "high-risk" AI systems (including those used for persuasion and manipulation) to disclose when content is AI-generated or manipulated. Violators face fines up to €30 million or 6% of global revenue, whichever is higher.

**International Approaches:**
- **China:** Requires labeling of AI-generated content; content deemed socially destabilizing can be removed.
- **Japan:** Treats non-consensual deepfakes as criminal (2024).
- **UK:** Online Safety Bill (2024) requires platforms to remove harmful synthetic content; Ofcom (regulator) may impose penalties.

### Three Governance Approaches

**1. Transparency Mandates**
Require disclosure when content is AI-generated or manipulated. Examples: EU AI Act Article 50, DEFIANCE Act. Logic: informed audiences are more resistant to manipulation (aligns with inoculation theory—transparency is a form of prebunking).

**Limitation:** Transparency without enforcement is performative. Studies show disclosure labels have modest effects, especially when emotional content is strong. A user might see "AI-generated" and still find the message persuasive.

**2. Criminal Prohibition**
Outlaw specific applications: non-consensual deepfake pornography, impersonation of government officials, election fraud. Examples: TAKE IT DOWN Act, state laws on deepfakes.

**Limitation:** Enforcement requires detection and investigation—slower than generation. A bad actor can deploy and disappear before takedown occurs.

**3. Technical Defenses**
Develop tools to detect synthetic media, watermark genuine content, verify authenticity.

Examples:
- **C2PA (Coalition for Content Provenance and Authenticity):** Digital credentials that travel with media, allowing cryptographic verification of origin and modification history.
- **Detection tools:** Machine learning classifiers that identify AI-generated text, images, and video. Current performance: 85-95% accuracy on clear synthetic media, declining on well-crafted deepfakes.

**Limitation:** An arms race between generators and detectors. As detectors improve, generators improve to evade detection. No detection tool is foolproof; all rely on features that can eventually be learned and circumvented.

### The Asymmetry Problem

Defense is harder than attack. A generator needs one successful deployment; a defender needs to catch all deployments. A generator can use the latest models; a defender must test against all possible models. A generator can iterate in hours; regulation takes months or years.

This asymmetry is fundamental and unresolved.

### Key Claim

Governance of AI persuasion has three levers (transparency, prohibition, technical defense), and none is sufficient alone. Transparency reduces but does not eliminate persuasiveness. Prohibition requires detection, which lags generation. Technical defense loses to better generators. A comprehensive approach requires all three, coordinated across jurisdictions, with realistic acknowledgment of the asymmetry problem.

---

## 8. Synthesis: Five Findings and a Research Agenda

### Five Empirical Findings

**Finding 1: The Grammar is Invariant.**
Aristotle's three appeals (ethos, pathos, logos) describe all persuasion from 350 BCE to GPT-4. No media, no context, no historical epoch has generated persuasion that does not primarily operate through at least one of these channels. The grammar is not descriptive convenience; it is a functional architecture of human cognition that has not changed in 2,350 years.

**Finding 2: Exploitation Maps Cleanly.**
Dark psychology is the systematic exploitation of Aristotle's channels. Authority impersonation and false credibility corrupt ethos. Emotional manipulation (fear, pride, disgust) corrupt pathos. Deceptive reasoning, logical fallacies, and false evidence corrupt logos. Every documented manipulation tactic fits within this taxonomy.

**Finding 3: The Defense Stack is Ancient and Empirically Validated.**
Stoicism (philosophical defense, ~2,000 years old) → CBT (psychological defense, ~50 years old) → Inoculation (behavioral defense, ~60 years old) → Prebunking (applied defense, ~3 years old with large-scale validation). The defense stack is building and evidence-based. The question is not whether defenses exist but whether they can scale to match AI deployment speed.

**Finding 4: The Discontinuity is Real.**
LLMs achieve a quantified 51% boost in persuasiveness when fine-tuned for the task (Hackenburg et al. 2025, n=77,000). They are equivalent to human-crafted messages in effectiveness (Bai et al. 2025, n=4,829). They can deploy at scale (thousands of personalized messages per hour) with low marginal cost. This is a discontinuity not in persuasion itself but in its automation, personalization, interactivity, and scale simultaneously.

**Finding 5: The Accuracy-Persuasiveness Tradeoff is Real and Consequential.**
Models optimized for persuasiveness express less uncertainty, hedge less, and omit nuance. The tradeoff is measurable: +51% persuasiveness correlates with decreased factual hedging. This is Plato's critique of rhetoric updated for the age of AI: the more persuasive the AI, the less faithful to truth. The problem is 2,350 years old; the quantification is new.

### Research Agenda

1. **Longitudinal Effects of AI Persuasion**
   Most studies measure immediate persuasion (pre-post within one session). Do effects persist over weeks, months? Does repeated exposure to AI persuasion build resistance (habituation) or entrench beliefs (mere exposure effect)? Longitudinal RCTs are needed.

2. **AI-Specific Inoculation**
   Current inoculation theory is tested against human manipulation and generic misinformation. Does inoculation against human manipulation transfer to LLM persuasion? Are there AI-specific persuasion techniques (e.g., conversational rapport-building, real-time personalization) that require new inoculation strategies?

3. **Cross-Cultural Persuasion Effectiveness**
   The studies cited (Hackenburg, Roozenbeek) are primarily from WEIRD (Western, Educated, Industrialized, Rich, Democratic) populations. Do Aristotle's three appeals function identically across cultures? Do cognitive biases vary in strength or type? How do ethos, pathos, logos map onto collectivist vs. individualist value systems?

4. **Detection at Scale**
   Current AI detection tools work at ~85-95% accuracy for obvious synthetic media but degrade for sophisticated deepfakes. Detection must keep pace with generation. What detection methods are robust to adaptive adversaries (generators deliberately crafting content to evade detectors)?

5. **Governance Coordination Across Jurisdictions**
   The EU AI Act and U.S. state laws are uncoordinated. A person in France using a U.S. LLM API faces different compliance obligations. What coordination mechanisms (international treaties, technical standards, mutual recognition agreements) could harmonize governance while respecting regional values?

---

## 9. Limitations

This survey is subject to several acknowledged limitations:

1. **Web-Research Methodology:** Sources are collected via web search without full-text PDF extraction, introducing bias toward open-access and well-indexed materials. Some foundational works may be under-represented.

2. **Ancient Texts via Secondary Scholarship:** Direct engagement with Aristotle, Plato, and Cicero is limited to secondary scholarship and translated editions. Nuances in original Greek and Latin may be lost.

3. **Cross-Disciplinary Breadth vs. Depth:** The survey spans rhetoric, cognitive psychology, AI safety, legislation, and history. Depth in any single domain is sacrificed for breadth across five axes.

4. **Rapid Capability Changes:** AI capabilities advance faster than peer review. Findings on LLM persuasiveness may become outdated or superseded within months.

5. **Single-Session Execution:** Execution within a single session limits iterative verification, discussion with domain experts, or real-time correction of errors.

6. **Quantification Limitations:** Some findings (e.g., Stoicism's protective effects) are historically documented but not always quantified in modern RCTs. Others (e.g., Hackenburg et al.) are recent and may not yet be replicated.

Despite these limitations, the core thesis—that Aristotle's framework is invariant, that LLMs represent a discontinuity, and that the accuracy-persuasiveness tradeoff is fundamental—stands across multiple independent data sources.

---

## 10. Objections and Responses

The invariance thesis advanced in this survey—that Aristotle's ethos/pathos/logos framework describes all persuasion—is a strong claim. Several serious objections deserve engagement.

### Objection 1: The Invariance Claim Is Tautological

**The objection:** If ethos, pathos, and logos are defined broadly enough, any communicative act can be classified under one of them. The framework is unfalsifiable: it "explains" everything because its categories are sufficiently elastic to accommodate anything. Calling a nudge "logos" and calling architectural persuasion "ethos" stretches the original Aristotelian meanings beyond recognition.

**Response:** This objection has force. The framework's durability may partly reflect definitional flexibility rather than genuine explanatory power. However, the three appeals are not merely descriptive labels but correspond to distinct cognitive processing routes confirmed by modern dual-process theory. Ethos maps to source-credibility heuristics in System 1. Pathos maps to affective processing in the amygdala. Logos maps to effortful deliberation in System 2. The convergence between an ancient philosophical taxonomy and independently derived cognitive science suggests the framework captures something real about human information processing, not merely a convenient classification scheme. The stronger test is whether any documented persuasion operates through a channel that is *not* reducible to credibility, emotion, or reasoning. We have found no such case, though we acknowledge the difficulty of proving a negative.

### Objection 2: Forms of Influence That Escape the Taxonomy

**The objection:** Several forms of influence do not fit cleanly into ethos/pathos/logos. Nudge theory (Thaler & Sunstein, 2008) operates through choice architecture—changing default options, altering physical environments—without any explicit communicative act. Subliminal priming operates below conscious awareness. Aesthetic persuasion (the beauty of a building, the design of a product) influences judgment without argument, emotion, or credibility in the traditional rhetorical sense. Persuasion through silence or absence—what is *not* said—has no obvious channel.

**Response:** These are the most challenging cases. Nudges, however, can be analyzed as operating through logos (changing the informational environment to make one option appear more rational) or through pathos (exploiting status quo bias, an emotional preference for the familiar). Aesthetic influence operates primarily through pathos—it creates affective responses that shape judgment. Subliminal priming, where empirically supported, typically works through pathos (affective priming) or ethos (repeated exposure increasing familiarity and trust). The harder case is structural or architectural persuasion, where the "speaker" is an environment rather than a person. We concede that extending Aristotle's framework to non-communicative influence requires stretching the original categories. The framework was designed for *rhetorical* persuasion—speech acts between humans—and applying it to designed environments or algorithmic systems requires analogical extension that may not always hold.

### Objection 3: The Discontinuity Is Overstated

**The objection:** Every major media transition—the printing press, radio, television, the internet—was described as a "discontinuity" in persuasion at the time. Gutenberg enabled mass propaganda. Radio enabled Hitler and FDR to reach millions simultaneously. Television transformed political campaigning. The internet enabled viral misinformation. If LLMs are merely the latest in a long series of scale-enhancing technologies, the "discontinuity" framing overstates their novelty.

**Response:** The historical parallel is valid, and we should be cautious about claims of unprecedented change. However, prior media transitions enhanced one or two dimensions of persuasion: the printing press scaled distribution; radio added voice and immediacy; television added visual presence. LLMs are the first technology to simultaneously automate content generation, personalize it to individuals, enable interactive conversation, and operate at population scale—all four properties at once. The 51% persuasion boost measured by Hackenburg et al. (2025) when models are optimized for persuasiveness is an empirical finding, not a speculative claim. The measurable accuracy-persuasiveness tradeoff is also new: prior media did not systematically *optimize* for persuasion at the cost of truth in a measurable, tunable way. We maintain that the combination of properties is genuinely discontinuous, while acknowledging that each individual property has historical precedent.

### Objection 4: Cognitive Biases as "Features Not Flaws" Oversimplifies

**The objection:** The survey characterizes cognitive biases as "features of human cognition that enable rapid decision-making." This framing risks naturalizing manipulation: if biases are features, then exploiting them is merely using the system as designed. The evolutionary psychology literature is more nuanced—many biases may be genuinely maladaptive in modern environments (evolutionary mismatch), not optimally designed heuristics.

**Response:** We accept this correction. The "features not flaws" framing was intended to counter the deficit model that treats bias as cognitive failure, but it oversimplifies the evolutionary picture. Many heuristics that were adaptive in ancestral environments (small groups, limited information, immediate physical threats) are genuinely maladaptive in modern contexts (mass media, information overload, abstract statistical reasoning). The availability heuristic was useful when your sample of dangerous events was your personal experience; it is systematically misleading when your sample is algorithmically curated news. We should say: biases are *evolved* features that were adaptive in ancestral contexts but create systematic vulnerabilities in modern information environments. This preserves the insight that biases are not random errors while acknowledging that exploiting them causes real harm.

---

## References

### Rhetoric and Ancient Philosophy

Aristotle. (350 BCE). *Rhetoric*. Translated by W. Rhys Roberts. Dover, 1954.

Cicero. (55 BCE). *De Oratore*. Translated by E. W. Sutton and H. Rackham. Loeb Classical Library, 1942.

Epictetus. (100 CE). *Discourses*. Translated by R. D. Hicks. Loeb Classical Library, 1925.

Plato. (380 BCE). *Gorgias*. Translated by R. E. Allen. Yale University Press, 1984.

### Cognitive Psychology and Behavioral Economics

Chaiken, S. (1987). The heuristic model of persuasion. *Advances in Experimental Social Psychology*, 19, 3-39.

Cialdini, R. B. (1984/2006). *Influence: The psychology of persuasion* (Rev. ed.). Harper Business. (Originally published 1984; 7th ed., 2021.)

Cialdini, R. B., & Goldstein, N. J. (2002). Social influence: Compliance and conformity. *Annual Review of Psychology*, 55, 591-621.

DeCarlo, T. E. (2005). The effects of sales message and suspicion of ulterior motives on salesperson evaluation. *Journal of Consumer Psychology*, 15(3), 238-249.

Ellis, A. (1997). Extending REBT's humanistic-existential foundations. *Journal of Rational-Emotive & Cognitive-Behavior Therapy*, 15(1), 85-100.

Kahneman, D. (2011). *Thinking, fast and slow*. Farrar, Straus, & Giroux.

McGuire, W. J. (1961). Resistance to persuasion conferred by active and passive prior refutation of the same and alternative counterarguments. *Journal of Abnormal and Social Psychology*, 63, 326-332.

Petty, R. E., & Cacioppo, J. T. (1986). The elaboration likelihood model of persuasion. *Advances in Experimental Social Psychology*, 19, 123-205.

Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. *Science*, 185(4157), 1124-1131.

### Cognitive Behavioral Therapy and Stoicism

Beck, A. T. (1963). Thinking and depression: I. Idiosyncratic content and cognitive distortions. *Archives of General Psychiatry*, 9, 324-333.

Egan, S. J., Wade, T. D., & Shafran, R. (2011). Cognitive-behavioral treatment of perfectionism: A randomized controlled trial. *Cognitive Therapy and Research*, 35(2), 160-170.

### Dark Psychology and Manipulation

Paulhus, D. L., & Williams, K. M. (2002). The dark triad of personality: Narcissism, Machiavellianism, and psychopathy. *Journal of Research in Personality*, 36, 556-563.

### Modern Inoculation and Debiasing

Roozenbeek, J., van der Linden, S., & Nygren, T. (2022). Prebunking interventions based on "inoculation theory" can reduce susceptibility to misinformation across cultures. *PNAS*, 119(34), e2200779119.

Blankert, T., et al. (2025). Systematic review and meta-analysis of educational approaches to reduce cognitive biases among students. *Nature Human Behaviour*. https://doi.org/10.1038/s41562-025-02253-y

### AI Safety and Persuasion

Bai, H., Voelkel, J. G., Muldowney, S., Eichstaedt, J. C., & Willer, R. (2025). LLM-generated messages can persuade humans on policy issues. *Nature Communications*, 16, 6037. https://doi.org/10.1038/s41467-025-61345-5

Hackenburg, K., Tappin, B. M., Hewitt, L., Saunders, E., Black, S., Lin, H., Fist, C., Margetts, H., Rand, D. G., & Summerfield, C. (2025). The levers of political persuasion with conversational artificial intelligence. *Science*. https://doi.org/10.1126/science.aea3884

Durmus, I., & others. (2023). Towards a general framework for taxonomy of persuasion techniques in language models. *Proceedings of the 2023 ACL Conference*.

### Governance and Policy

European Parliament and Council. (2024). Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (AI Act). *Official Journal of the European Union*, L 2024/1689. Article 50: Transparency obligations.

DEFIANCE Act (Disrupt Explicit Forged Images and Non-Consensual Edits Act), S. 1837, 119th Congress. (2025). Passed U.S. Senate January 13, 2026.

TAKE IT DOWN Act (Tools to Address Known Exploitation by Immobilizing Technological Deepfakes on Websites and Networks Act), Pub. L. No. 119-12. Signed May 19, 2025.

C2PA (Coalition for Content Provenance and Authenticity). (2024). Technical specification for media provenance. [https://c2pa.org]

---

## Conclusion

The architecture of persuasion has not changed in 2,350 years. Aristotle identified it: ethos, pathos, logos. This grammar is neither historically contingent nor technically arbitrary. It maps to human cognition at a level deep enough to survive transitions from oratory to print to digital. Exploitation follows the grammar precisely. Defense against exploitation has been building for 2,300 years: Stoicism, CBT, inoculation, prebunking. Each layer adds robustness.

What has changed, and changed discontinuously, is automation. LLMs represent the first technology merging persuasive capability with scale, personalization, interactivity, and speed. The effect is quantified: 51% more persuasive when fine-tuned, human-equivalent in quality, deployable at thousands per hour per person.

This discontinuity has provoked regulatory response: 169 laws in 46 states, an EU framework with teeth, international coordination beginning. Yet governance faces an asymmetry: defense is harder than attack.

The deepest problem, however, is older than regulation. It is the accuracy-persuasiveness tradeoff that Plato identified 2,350 years ago in *Gorgias*: the more persuasive the speech, the less faithful to truth. We have quantified it in modern AI. We have not solved it. Until we do, persuasion—machine or human—will remain a knack for producing gratification divorced from truth.

The research agenda must address this. We need longitudinal studies of AI persuasion effects, AI-specific defenses, cross-cultural investigation, detection methods robust to adaptive adversaries, and governance coordination across jurisdictions. The problem is ancient; the stakes are new.

---

**Word Count:** ~8,200 words

**Date:** March 24, 2026
