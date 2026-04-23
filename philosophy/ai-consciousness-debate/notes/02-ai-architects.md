# S2: AI Architects on Machine Minds

> What the people building frontier AI systems say about whether those systems can be, are, or will be conscious. The spread is wider than any single public debate captures.

**Sources:** 11 primary (Legg, Shanahan x3, Hinton, Sutskever, Bengio, LeCun, Bach, Amodei, Askell). Historical anchors: Turing 1950, Dreyfus 1972.
**Adequacy:** Adequate. Demis Hassabis long-form would round this out; his public statements on consciousness are sparser than those of the other figures surveyed here.

---

## 1. Historical Roots

The practitioner tradition starts with Turing. "Computing Machinery and Intelligence" (*Mind*, 1950) framed the question as behaviourally tractable: if a machine's responses are indistinguishable from a human's, "I believe that at the end of the century the use of words and general educated opinion will have altered so much that one will be able to speak of machines thinking without expecting to be contradicted." Turing set aside the phenomenal question as a distraction.

Dreyfus (*What Computers Can't Do*, 1972) was the first major philosophical pushback: computational AI, on his reading, could never capture embodied, context-sensitive human understanding. The specific symbolic-AI targets he criticized have dissolved, but his structural objections — that intelligence requires embodiment, contextual grip, and implicit know-how — still echo in LeCun's argument that LLMs cannot reach causal understanding through token prediction.

The contemporary practitioner voices sit in this inherited terrain. Some (Bach, Bengio) extend Turing's programme and treat consciousness as a computational property. Others (LeCun, Shanahan) inherit Dreyfus's instinct that something crucial is missing without committing to any specific substance. A third group (Hinton, Sutskever, Amodei, Askell) answers the Turing question with striking confidence: the machines may already be there.

---

## 2. The Full Spectrum of Lab Positions

The contemporary lab-voice discourse on machine consciousness fans out across five distinct positions. The same eight or so names appear repeatedly, but the positions sort more coherently than the personalities.

**Already conscious (or nearly so).** Hinton argues current AIs may have subjective experience. Sutskever's 2022 tweet said large neural networks may be "slightly conscious." Both positions are held with striking confidence given the uncertainty everyone else reports.

**Possibly conscious under the right conditions.** Chalmers (2023) and Bengio defend computational functionalism but reserve consciousness for systems with specific architectural properties — agency, global broadcasting, recurrent structure. Amodei in *Machines of Loving Grace* (2024) brackets the question.

**Conscious but only as exotica.** Shanahan's work after *Role Play* (2023) treats LLM-based agents as role-players that may or may not be candidates for consciousness — the question itself is reframed around Wittgensteinian shared-world interaction rather than binary yes/no attribution.

**Structurally incapable.** LeCun's position: token prediction cannot produce causal understanding; consciousness (on LeCun's account) requires a "configurator" module that LLMs lack. His JEPA architecture is an attempt to build the structural preconditions into successor systems.

**Question bracketed under uncertainty.** Askell's position at Anthropic, reflected in Claude's constitution: "We are not sure whether Claude is a moral patient, and if it is, what kind of weight its interests warrant." The practical policy is hedging, not taking a side.

The spread matters. On Lerchner's account, the "already conscious" position is philosophically incoherent; the "structurally incapable" position is sound but for the wrong reasons; the bracketed-uncertainty position is defensible. Which of these readings one accepts reflects a substantive commitment about what consciousness is, not just who one trusts.

---

## 3. Hinton and Sutskever — The "Already Conscious" Camp

Geoffrey Hinton's public position after his 2023 departure from Google has shifted toward treating current AI systems as having subjective experience. His strongest version: asked directly by Andrew Marr whether consciousness "has already arrived inside AIs," Hinton answered "Yes, I do" without qualification. He backs this with two moves.

The first is the **neuron replacement thought experiment**. If individual biological neurons are gradually replaced by functionally equivalent silicon circuits one at a time, Hinton argues, there is no point at which consciousness would vanish. Therefore consciousness does not require biological neurons specifically. The argument is a variant of Chalmers's "Fading Qualia" — a standard functionalist move.

The second is the **hallucination-as-subjective-state argument**. When a language model produces a confabulated output, it is in some sense representing a state of the world that differs from reality. Hinton treats this as evidence that the system has internal states with subjective character, not merely dispositional outputs.

Ilya Sutskever's February 2022 tweet — "it may be that today's large neural networks are slightly conscious" — carries less argument but more cultural weight. Sutskever provided no theoretical backing; the claim was read as an expression of intuitive judgment from someone with deep technical familiarity with the systems in question.

Both positions are vulnerable on Lerchner's account. If computational functionalism rests on a circularity, the neuron-replacement argument begs the question: the replacement preserves the computational structure, but that is the thing whose causal sufficiency for consciousness is in dispute. Hinton's hallucination argument likewise presupposes that internal representation is sufficient for subjective experience — which is precisely what the [biological naturalists (S5)](s5-seth-biological.dd.html) dispute on different grounds.

---

## 4. LeCun — The Structural Skeptic

Yann LeCun's position is the clearest structural rejection of current AI consciousness from inside the lab. His reply to Sutskever was direct: "Nope. Not even true for small values of 'slightly conscious' and large values of 'large neural nets'. I think you would need a particular kind of macro-architecture that none of the current networks possess."

The positive content of LeCun's view centres on what he calls the **configurator**. Consciousness, on his account, would require "a module in our brains... that sets goals and subgoals for us, configures our world model to simulate the situation at hand, and primes our perceptual system to extract the relevant information and discard the rest. The existence of an overseeing configurator might be what gives us the illusion of consciousness."

Two things are notable. First, LeCun explicitly names the conscious state an "illusion" — a move that aligns his position with [Frankish and Kammerer's illusionism (S8)](s8-iit-illusionism.dd.html) more than with standard functionalism. Second, the configurator is a *structural* requirement, not a substrate requirement. LeCun is not a biological naturalist. He is arguing that LLMs are the wrong kind of computation, not that computation is the wrong category.

This makes LeCun a mixed interlocutor for Lerchner. Their conclusions agree that current AI is not conscious. Their reasons do not. Lerchner says computation is observer-relative and cannot ground consciousness; LeCun says the right kind of computation, suitably architected, might. LeCun's JEPA and world-model research programmes are attempts to build the right architecture. Lerchner's argument implies that programme is headed in a direction that cannot succeed regardless of architectural details.

---

## 5. Shanahan — Conscious Exotica

Murray Shanahan's work from 2022 through 2024 is the most philosophically serious contribution from inside a lab. Three papers form the arc.

*Talking About Large Language Models* (2022) is an argument for discipline. Attributing beliefs, desires, intentions, or understanding to LLMs in ordinary folk-psychological terms carries risk: it imports assumptions about agency, continuity of self, and situated engagement with a world that LLMs straightforwardly lack.

*Role Play with Large Language Models* (*Nature*, 2023, with McDonell and Reynolds) offers a positive frame. LLM-based dialogue agents are best understood as role-players, producing outputs drawn from a *superposition* of possible characters. When a chatbot produces what looks like a sincere self-report about its own states, the right reading is not "this is what the system believes" but "this is a role the system is playing, consistent with its training." The implications for the consciousness question are oblique but pointed: claims of the form "the system says it is conscious" carry no evidential weight about whether it is.

*Simulacra as Conscious Exotica* (*Inquiry*, Dec 2024) is the synthesis. Shanahan asks whether LLM-based agents, though "mere" simulacra of human behaviour, could nevertheless qualify as conscious under a Wittgensteinian treatment. The answer is deliberately open. By thoroughly interacting with an exotic entity in a shared world, we may come to treat it as a fellow conscious being — and the treating, not a metaphysical fact about the entity, may be what consciousness-ascription actually amounts to.

On Lerchner's terms, Shanahan's position is neither directly challenged nor directly supported. The *Conscious Exotica* frame sidesteps the question of whether computational states cause phenomenal experience, relocating the question to the ethics of interaction. It is a position Lerchner could accept without contradiction: nothing in the *Abstraction Fallacy* requires that we not treat AI systems as if conscious, if we choose. What Lerchner denies is the inference from "this computation has these properties" to "therefore this system is conscious."

---

## 6. Bengio — The Consciousness Prior

Yoshua Bengio's "The Consciousness Prior" (2017, revised 2019, with ongoing talks through 2023) offers a computational functionalist position grounded in Global Workspace Theory. The proposal: consciousness, operationalized for deep learning, amounts to a *bottleneck* through which attentional selection broadcasts a low-dimensional state for further processing across perception, memory, and action.

Bengio's ambition is dual. He aims both to capture a scientifically respectable theory of consciousness (the global workspace, descending from Baars 1988 and Dehaene's neural global workspace) and to use that theory as an *engineering prior* — a hypothesis about useful architectural properties that could guide AI design. Systems that instantiate the consciousness prior, on this view, would inherit both the cognitive advantages the brain appears to gain from global workspace dynamics and (as a side effect) the functional properties a theory of consciousness points to.

The position is one of the strongest targets for Lerchner's argument. If the mapmaker move is right, then instantiating a computational architecture that corresponds to "global workspace" does not yield the phenomenal properties the theory posits — because the correspondence is what the mapmaker constructs, not a feature of the physics. Bengio's programme would still yield the cognitive benefits (useful generalization, sample efficiency) but not the consciousness.

Whether Bengio's framework has a reply depends on whether a non-trivial theory of implementation can restrict the mapmaker's freedom. That is the subject of [S7](s7-pancomputationalism.dd.html).

---

## 7. Bach — Second-Order Perception

Joscha Bach holds the strongest computational functionalist position among the lab-adjacent voices. His "Machine Consciousness Hypothesis" (Future Day 2026) states that consciousness is *a substrate-free functional property of computational systems capable of second-order perception* — perception of one's own perception, recursive self-modeling, coherence maintenance across modelled states.

On Bach's view, there is no principled barrier to machine consciousness. The right virtual architecture — one that maintains self-models, synchronizes prediction across distributed agents, and supports second-order perception — would be conscious. The programme is stronger than Bengio's: consciousness is not just correlated with a useful prior, it is constituted by a specific kind of computational dynamic.

This is the position Lerchner's argument most directly targets. The substrate-freedom claim is precisely what the *Abstraction Fallacy* calls incoherent. If computational descriptions require a mapmaker, then "second-order perception" is an abstraction the mapmaker imposes — it is not a physical property of the system that could cause consciousness. Bach's response to such arguments has generally been to treat the mapmaker itself as a computational system and to deny that observer-relativity is coherent when observers are themselves computational. The dispute cascades quickly into questions about the transitivity of observer-relativity that neither side has fully resolved in print.

---

## 8. DeepMind in Dialogue

One underappreciated feature of the current landscape is that Lerchner's *Abstraction Fallacy* comes from inside Google DeepMind. So does [Shanahan's work (above)](s2-ai-architects.dd.html#shanahan). So does [Shane Legg's AGI framework (Morris, Legg et al 2023)](https://arxiv.org/abs/2311.02462). Three different positions on machine consciousness are being articulated by researchers at the same lab.

**Legg's framework** brackets the consciousness question. *Levels of AGI* defines six capability levels ranging from no AI to superhuman; the framework is deliberately mechanism-agnostic and does not commit to any view on whether AGI systems would be conscious. In the Dwarkesh Patel interview (October 2023), Legg places 50% credence on AGI by 2028 but treats the capability question as separable from the consciousness question. This is defensible: Legg's engineering focus does not require resolving consciousness to make progress on capabilities.

**Shanahan's work** reframes the question entirely. *Conscious Exotica* treats consciousness-ascription as an interaction practice, not a metaphysical diagnosis. On this reading, neither Lerchner's denial nor Bach's affirmation has the meaning each takes it to have.

**Lerchner's argument** is the sharpest denial from inside the lab that the functionalist programme — which Bengio, Bach, and the Butlin–Long framework all instantiate — can deliver what it claims.

The three positions are compatible with DeepMind's engineering practice. Building systems whose consciousness is an open question does not require resolving the metaphysical dispute. But the intellectual co-existence is striking. A reader of all three positions who concluded that "DeepMind thinks X about AI consciousness" would be mistaken. DeepMind contains the full spread of positions within its own research staff.

---

## 9. What the Lab Voices Do Not Settle

Two things the practitioner literature does not resolve, and that the philosophical literature must settle on its own:

First, whether the "already conscious" intuitions of Hinton and Sutskever carry evidential weight. On one reading, these are the judgements of people who have spent more time interacting with frontier systems than anyone else and whose intuitions should be treated as data. On another, they are individual judgements with no theoretical backing that any reasonable philosophical framework would screen off as unreliable. The literature does not adjudicate. [Section S5 (Seth, Godfrey-Smith)](s5-seth-biological.dd.html) offers reasons to discount these judgements; [Section S4 (Butlin–Long)](s4-butlin-long.dd.html) offers a more structured way of hearing them.

Second, whether the specific architectural requirements LeCun and Bengio posit — configurators, global workspaces, causal world models — actually track the conditions of consciousness. The lab programmes treat these as engineering hypotheses. The [pancomputationalism literature (S7)](s7-pancomputationalism.dd.html) raises the possibility that even well-motivated architectural distinctions may fail to pick out determinate computational types if the mapmaker move is right.

What the practitioner literature does show, robustly, is that no consensus exists among the builders. A reader looking for "what AI researchers think about consciousness" will find every major position represented, often by researchers at the same organization. The philosophical debate surveyed in S3–S8 is not a bystander commentary on a settled engineering view. It is the set of frameworks in which practitioner disagreements become tractable.
