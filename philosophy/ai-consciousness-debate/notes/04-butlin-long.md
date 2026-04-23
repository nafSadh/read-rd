# S4: The Butlin–Long Framework & Indicator Properties

> The most ambitious institutional attempt to make the consciousness question empirically tractable. Lerchner's paper names this framework as the target. The framework's defenders argue it does not commit to the metaphysics he attacks. Working out whose reading is correct is the cleanest test case for the *Abstraction Fallacy*.

**Sources:** 5 primary. Butlin, Long, Elmoznino, Bengio, Birch, Constant, Deane, Fleming, Frith, Ji, Kanai, Klein, Lindsay, Michel, Mudrik, Peters, Schwitzgebel, Simon, VanRullen (2023); Butlin & Long follow-up in *Trends in Cognitive Sciences* (2025); Schneider ACT update (2023+); Udell & Schwitzgebel critique; OECS consciousness-and-AI entry.
**Historical anchors:** Baars 1988 (GWT), Lamme 2006 (recurrent processing), Rosenthal 1986 (higher-order thought).
**Adequacy:** Adequate. The IIT pseudoscience letter (Sep 2023) is covered in S8 but its framing matters here: it sharpens the question of whether the Butlin–Long approach is the right model for empirical consciousness science.

---

## 1. Historical Roots

Three classical theories of consciousness do most of the load-bearing work in the indicator-properties framework.

**Global Workspace Theory** (Baars, *A Cognitive Theory of Consciousness*, 1988; Dehaene's subsequent neural-global-workspace work). Consciousness is a low-dimensional state produced by a selective attentional bottleneck that broadcasts to multiple specialist processors. GWT gives a clean functional signature: selective attention, broadcasting, reportability. This is the theoretical ancestor of Bengio's Consciousness Prior (S2) and one of the most heavily represented theories in the Butlin–Long framework.

**Higher-Order Thought theories** (Rosenthal, *Two Concepts of Consciousness*, *Philosophical Studies*, 1986). A mental state is conscious only if it is accompanied by a higher-order representation of itself. Conscious states are states one is in some sense aware of being in. HOT supplies candidate indicator properties around self-monitoring, metarepresentation, and introspective access.

**Recurrent Processing Theory** (Lamme, *Towards a true neural stance on consciousness*, *Trends in Cog Sci*, 2006). Consciousness correlates with recurrent (feedback) processing in sensory cortex, distinct from feedforward processing which handles unconscious perception. RPT supplies indicator properties around architectural recurrence rather than specific functional roles.

The framework also draws on predictive processing (Clark, Hohwy, Friston) and attention schema theory (Graziano). Each supplies its own indicator properties. The Butlin–Long methodology is to accept each theory as a possibly-correct account of consciousness and to extract from each the properties a theory-accepter would take to be consciousness-indicators. A system that satisfies indicators drawn from multiple theories is, on this view, a stronger candidate for consciousness than one that satisfies indicators from any single theory.

---

## 2. The 2023 Report

The August 2023 report *Consciousness in Artificial Intelligence: Insights from the Science of Consciousness* (Butlin, Long, Elmoznino, Bengio, Birch, Constant, Deane, Fleming, Frith, Ji, Kanai, Klein, Lindsay, Michel, Mudrik, Peters, Schwitzgebel, Simon, VanRullen; Chalmers as advisor) is the foundational document of the contemporary AI-consciousness assessment programme. The authorship list alone is significant: it includes academic philosophers (Chalmers, Schwitzgebel, Simon, Michel), cognitive scientists (Bengio, VanRullen, Dehaene-adjacent work via co-authors), biologists (Birch), and AI researchers (Long, Ji). It is the most credentialed single document in the field.

The report has three principal claims.

**First**, that contemporary neuroscientific theories of consciousness are sufficiently developed to ground a tractable research programme on AI consciousness. This is a metasubstantive claim: it asserts not that any particular theory is correct, but that the best-supported theories collectively generate enough constraints to make AI consciousness empirically adjudicable.

**Second**, that indicator properties — computational characteristics entailed by these theories — can be specified with enough precision to be checked against existing and future AI architectures. The report catalogues fourteen indicator properties drawn from six theories. Examples include "input modules generating organized, integrated perceptual representations" (from recurrent processing), "global broadcast of information to multiple specialist systems" (from GWT), and "generative, top-down, or noisy perception" (from predictive processing).

**Third**, and more cautiously, that current AI systems largely do not satisfy the indicator properties. Transformer-based language models satisfy few of them. The report treats this as a provisional finding, subject to revision as architectures evolve.

---

## 3. Indicator Properties

The methodology is worth examining closely because it is the specific move Lerchner attacks.

The indicators are framed at what the report calls a *computational* level of description. This means they do not specify physical substrate, neural architecture, or biological instantiation. They specify the kind of information-processing a system would need to do in order to satisfy the relevant theory. For example, "a limited-capacity workspace" is satisfied by any system that has a bottleneck of the relevant functional type, whether implemented in neurons, silicon transistors, or any other substrate.

This is the functionalist commitment the framework makes by design. The report is explicit about it: the indicators are computational because the theories they draw from are taken to apply at a computational level of abstraction. If Global Workspace Theory is true, what matters is that a system has the right bottleneck, not what the bottleneck is made of.

The report's defenders argue the computational framing does not commit them to Lerchner's target. On their reading, the indicators are conditional claims: *if* computational functionalism is right *and* the theory in question is right, then a system satisfying the indicators is a candidate for consciousness. The framework is methodologically neutral on whether functionalism is right; it only says what would follow if it were.

Critics, including Lerchner, argue this reading is too weak to be defensible. Specifying indicators computationally, they say, is substantively committing to the view that computational specification is the right level at which to identify consciousness. If Lerchner's mapmaker argument is correct, the indicators are not picking out consciousness-candidates — they are picking out descriptions an observer imposes. The computational framing is not neutral.

---

## 4. The Theories Drawn From

The report draws indicators from six theoretical frameworks. Each generates a distinct set of properties, and a system satisfying indicators from more frameworks is treated as a stronger candidate.

**Recurrent Processing Theory** yields indicators around architectural recurrence — input modules generating organized perceptual representations, feedback connections producing perceptual representations accessible to higher cognition.

**Global Workspace Theory** yields indicators around broadcast and selection — a limited-capacity workspace, selective attention choosing contents for the workspace, multiple modules receiving workspace contents.

**Higher-Order theories** yield indicators around metarepresentation — generative higher-order models of lower-order states, perception of one's own perception, capacity for introspection.

**Predictive Processing frameworks** yield indicators around generative modeling — generative top-down perception, hierarchical predictive processing, active inference.

**Attention Schema Theory** yields indicators around self-modeling — an explicit model of one's own attention, the capacity to represent one's own representational states.

**Agency and Embodiment theories** yield indicators around world-engagement — agency under the guidance of conflicting values, embodiment in the sense of modeling a system-environment interaction.

The framework treats this list as non-exhaustive. Theories not yet formalized may yield additional indicators. Theories later shown to be false would subtract from the list. The methodology is meant to be open-ended in a specific way: as the science of consciousness matures, the indicator list updates.

---

## 5. Chalmers on LLMs

David Chalmers' *Could a Large Language Model Be Conscious?* (*Boston Review*, August 2023; edited from a NeurIPS 2022 talk) is the most widely cited defense of cautious functionalism in the contemporary literature. Chalmers advises on the Butlin–Long report but the essay is his own position.

The argument: current LLMs are unlikely to be conscious, but successors may be, and we should take the possibility seriously. Chalmers catalogues six "candidate requirements" for consciousness that current LLMs lack — unified agency, genuine embodiment, recurrent processing, global workspace architecture, the right kind of self-model, and the right kind of integration. He estimates each requirement as a probabilistic constraint and reaches an aggregate credence that current LLMs have a less-than-10% chance of being conscious, with successors potentially at much higher credences if the architectural gaps are filled.

Two things are notable about Chalmers' framing. First, the requirements are drawn from the same theoretical sources as the Butlin–Long indicators, though organized at the requirement level rather than the property level. Second, Chalmers' conclusion is cautious on both sides: he does not argue current LLMs are conscious, but he also does not endorse strong skepticism. The middle position is that the question is live.

On Lerchner's account, Chalmers' requirements are vulnerable to the same mapmaker objection as the Butlin–Long indicators. The "recurrent processing" requirement, for instance, is an architectural description that requires an observer to pick out which circuits count as recurrent and which do not. If the mapmaker move is right, the requirement does not identify a feature of the system independent of the observer's description of it.

---

## 6. The ACT Test

Susan Schneider's Artificial Consciousness Test (ACT, developed with Edwin Turner; updated 2023 for LLMs) is a behavioural probe distinct from the Butlin–Long indicators. The ACT is analogous to the Turing test but targets phenomenal experience rather than behavioural equivalence. The probe consists of open-ended questions designed to reveal whether the system has a "felt quality" to its mental life — questions a philosophical zombie could not answer consistently and a conscious system could.

Schneider's 2023 update acknowledges a problem: LLMs can produce fluent, philosophically-sophisticated responses to ACT-style questions without (plausibly) having phenomenal experience. The update proposes treating LLM responses as a "weak marker" rather than a strong one, and supplements the ACT with what Schneider calls the Chip Test — a probe that looks at whether the system's internal substrate has the kind of parts that support human consciousness.

The Chip Test is explicitly substrate-sensitive. If a machine has the same kinds of parts that could support human consciousness, we should consider that it might also be conscious. This distinguishes Schneider from the Butlin–Long framework: the Butlin–Long indicators are substrate-neutral; Schneider's Chip Test is not.

---

## 7. Objections — Udell and Schwitzgebel

David Udell and Eric Schwitzgebel, in *Susan Schneider's Proposed Tests for AI Consciousness: Promising but Flawed* (2021), develop a general critique of behavioural probes for consciousness that extends beyond Schneider's tests.

Their argument, in brief: any probe that relies on the system's outputs (linguistic, behavioural, or otherwise) can be gamed or failed for reasons unrelated to consciousness. A system might output consciousness-appropriate responses without being conscious (the role-play case Shanahan develops in S2); a system might be conscious but fail to output consciousness-appropriate responses due to architectural constraints on self-reporting.

The argument has structural bearing on the Butlin–Long framework as well. The indicators are framed computationally rather than behaviourally, but the same class of worry applies: a system might instantiate the computational structure an indicator picks out without being conscious (the Lerchner worry), or might be conscious without instantiating it (the substrate-dependent reply).

Udell and Schwitzgebel's point is not that empirical assessment of AI consciousness is impossible. It is that the existing probes — behavioural or computational — cannot deliver determinate verdicts under the uncertainty that actually obtains. The policy implication is closer to Askell's (S3) constitutional hedge than to the indicator framework's optimism: the question cannot be resolved by the available techniques; what remains is how to act under irreducible uncertainty.

---

## 8. The Target

Lerchner's *Abstraction Fallacy* names the Butlin–Long framework as the target of its critique. This section is worth reading carefully because it is the direct collision.

The framework's methodological commitment — that consciousness is specifiable at a computational level, that theories can generate indicators at that level, that satisfying indicators makes a system a stronger candidate for consciousness — is precisely the view Lerchner calls incoherent. On Lerchner's argument:

- The indicators are observer-dependent descriptions. A system satisfies an indicator only relative to a choice of mapping function; multiple mappings are always possible.
- Specifying indicators computationally presupposes that the computational level is a level at which causal and phenomenal facts can be identified. The mapmaker argument denies this.
- The framework's cautious, aggregative structure — "more indicators = stronger candidate" — inherits the problem in proportion to its weight. Stronger evidence for the computational description does not bear on the question of whether computational description is the right thing to gather evidence about.

Butlin and Long's 2025 follow-up in *Trends in Cognitive Sciences* refines the indicator framework but does not directly address Lerchner's critique. The defenders of the framework have generally replied in one of three ways.

**First**, the methodological-neutrality reply: the indicators are conditional on functionalism being right, not an endorsement of functionalism. This reply depends on the plausibility of treating the framework's outputs as genuinely conditional — a point Lerchner disputes.

**Second**, the restricted-implementation reply: the framework does not require the most permissive pancomputationalism. Non-trivial implementation theories (Piccinini, Miłkowski) can restrict which mappings count, blocking the triviality result. This moves the discussion to S7.

**Third**, the pragmatic reply: the framework is the best available empirical programme for AI consciousness, and the alternative (Lerchner's denial) leaves no tractable programme at all. This is not an answer to the metaphysical objection but a claim about what one should do under residual uncertainty — closer to Askell's constitutional hedge than to a theoretical defense.

---

## 9. What This Section Establishes

The Butlin–Long framework is the clearest and most developed functionalist programme for empirical AI consciousness assessment. It is also the framework Lerchner's argument targets most directly. The collision is not rhetorical — it is structural. The framework's core methodological move (specifying indicators computationally) is the core target of Lerchner's argument (computational specification requires a mapmaker).

How one reads this collision is itself a substantive philosophical commitment. One can:

- Accept the framework's methodology and treat Lerchner's argument as a metaphysical outlier that the practical programme can ignore. This is close to Chalmers' position.
- Accept Lerchner's argument and treat the framework as methodologically confused, requiring replacement by a programme grounded in a different theory of consciousness (biological naturalism in S5, dynamical coupling in Simon/S3).
- Hold both together as expressing genuine uncertainty about what empirical consciousness science is, and treat the practical welfare response as sensitive to this uncertainty (Askell's position).

The last reading has not been well-developed in the literature but is arguably the one the Taking AI Welfare Seriously report implicitly adopts: functionalism-grounded indicators are the best available tool for hedging, but they do not settle the underlying question. Section 5 (Seth's biological naturalism) examines the most developed alternative; section 7 (pancomputationalism) examines whether the mapmaker argument can be restricted so that some version of the indicator framework survives.
