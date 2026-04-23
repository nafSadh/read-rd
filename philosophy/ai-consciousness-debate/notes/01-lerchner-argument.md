# S1: Lerchner's Argument — *The Abstraction Fallacy*

> Framed as the target of the survey: the argument that counter-arguments and similar contemporary arguments respond to. What the paper claims, how it claims it, and which moves invite pushback.

**Sources:** 2 primary (L1-1 Lerchner preprint via PhilPapers; L1-2 companion slide deck at repo root). Historical anchors: Putnam 1988, Searle 1990.
**Adequacy:** Adequate for a framing summary. Not a critical peer review — that happens in S2–S8.

---

## 1. Historical Roots

Lerchner's argument sits in a specific lineage. Two classical works frame almost every contemporary discussion of whether consciousness can be computational, and both anticipate the paper's central move.

**Putnam (1988)**, in *Representation and Reality*, proves what became known as the triviality theorem: under a permissive enough mapping, every physical system implements every finite-state automaton. The wall in a room, interpreted the right way, implements word processing software. Putnam took this as a reductio — computational functionalism, if taken literally, cannot be a theory of anything determinate, because computation is not intrinsic to physics.

**Searle (1990)**, in "Is the Brain a Digital Computer?" (his APA Presidential Address), pushes a kindred observation in a different key. Syntax is observer-relative. A physical process becomes a computation only under an interpretation assigned from outside. "The wall behind my back is right now implementing the WordStar program, because there is some pattern of molecule movements that is isomorphic with the formal structure of WordStar. But if the wall is implementing WordStar, then if it is a big enough wall it is implementing any program, including any program implemented in the brain."

Lerchner's *Abstraction Fallacy* reworks this observation into an argument specifically about consciousness. The novelty is not the triviality result itself but the causal gloss: if computation is observer-dependent, and consciousness is taken to be identical with computation, then the observer becomes a hidden precondition of consciousness — a circularity the functionalist programme cannot tolerate.

---

## 2. The Target: Computational Functionalism

The position Lerchner sets out to undermine has a precise shape. Computational functionalism holds:

- **Substrate independence.** What matters for consciousness is the abstract causal topology, not the physical realizer. The same computation run on silicon, biological tissue, photonics, or an exotic substrate would be conscious.
- **Realization relation.** Physics realizes computation, computation realizes (or is identical with) consciousness. The chain is: *physics → computation → consciousness*.
- **Practical implication.** AGI systems, whatever their substrate, are candidates for moral patiency once their computational profile approximates that of a conscious organism.

This is the programme that the [Butlin–Long report (S4)](s4-butlin-long.dd.html) operationalizes into "indicator properties." It is also the position Chalmers (2023) cautiously defends in "Could a Large Language Model Be Conscious?" (S2, S4). Lerchner's paper identifies this programme as the target.

---

## 3. The Implementation Equation

The paper's central formal move is compressed into a commutative relation:

- Let `p` be a physical state and `p'` its successor.
- Let `f` be a mapping function from physical states to abstract states.
- Let `A = f(p)` and `A' = f(p')` be the corresponding abstract states.

The functionalist picture requires that the transition `p → p'` (physics) commute with the transition `A → A'` (computation) via `f`. That is, the physical dynamics, viewed through `f`, look like the right abstract computation.

Lerchner's key claim: **`f` is the mapmaker's choice, not a fact about the physics.** For any physical dynamics, infinitely many maps `f` are permissible — some yielding one computation, some another, some none. The mapping is not inscribed in the electrons or neurons; it is imposed by an interpreting observer.

This is the first move in the circularity argument. If `f` is observer-chosen, then the abstract state `A` is observer-dependent. And if consciousness is identified with `A`, then consciousness is observer-dependent.

---

## 4. Map vs. Territory

Lerchner spends several sections on the ontology of abstract states. Two readings are rejected:

**Abstract states are not Platonic ideals.** Nothing in the paper commits to a separate realm of forms in which `A` exists independently.

**Abstract states are not metaphysical entities.** They are not causal substances sitting alongside the physical ones.

**Abstract states are neurophysiological constructs.** Specifically, they are equivalence classes carved out by an experiencing brain or other learning system. The organism encounters a diversity of physical configurations, learns that certain configurations matter the same way for its goals, and groups them conceptually. The abstraction is epistemic — a tool of the mapmaker — not ontic.

This is where the paper's title earns its bite. The fallacy it names is treating an abstraction (the map) as though it were a feature of the territory (the physics). Maps are useful. They are also imposed. Substrate-independent consciousness, on this diagnosis, mistakes a useful projection for a causal structure.

---

## 5. The Causal Circularity

With `f` observer-chosen and abstract states identified as epistemic constructs, the standard functionalist chain reverses.

**Standard chain (functionalist):** physics → computation → consciousness.

**Revised chain (Lerchner):** consciousness (mapmaker) → computation (selected `f`) → physics (interpreted through the map).

The paper puts this as an *ontological inversion*. The computational description, which the functionalist takes to be caused by physics, is instead produced by an already-conscious interpreter. To then derive consciousness from that computational description is to let the conclusion smuggle itself into the premise.

This is the core charge: computational functionalism is not false because consciousness cannot be computational — it is *underdetermined*, because the computational description it starts from requires consciousness to be picked out in the first place.

---

## 6. Simulation versus Instantiation

Several analogies carry the argument's intuition from formal terrain into everyday reasoning. Each contrasts a simulation of some process with an instantiation of it.

**The Heart.** A computer simulation of the heart does not pump blood. The simulation represents the causal structure of pumping; it does not realize it. Blood pumping requires muscle, vessels, and pressure differentials. Analogously (Lerchner argues), a simulation of consciousness may represent its computational structure without instantiating the experience.

**The GPU and Photosynthesis.** A GPU simulating the quantum chemistry of photosynthesis does not make sugar. The chemistry requires specific molecular arrangements in leaves, not patterns of floating-point arithmetic that track them. The worry generalizes: the pattern-tracking is not the phenomenon.

**The Melody Paradox.** A melody is an abstract pattern of pitches and intervals. It can be played on piano, guitar, or synthesizer, and remains the same melody. But "melody" is a category of musical experience, not a force that causes vibrations. The musicians, not the melody, cause the sound. Consciousness-as-abstract-pattern, Lerchner argues, conflates the pattern with the physical causes.

These analogies are the paper's most contested moves. Defenders of functionalism reply that consciousness is unlike pumping, unlike photosynthesis, and unlike melodies in the relevant respect: it *is* the computational pattern, not merely represented by one. This is precisely where [Chalmers' "dancing qualia" strategy (S2)](s2-ai-architects.dd.html) and the [Butlin–Long indicator framework (S4)](s4-butlin-long.dd.html) do their work.

---

## 7. AGI as Non-Sentient Tool

The paper's practical conclusion is framed as relief rather than loss. If computational functionalism fails, the prospect of AGI raises different worries than the ones currently dominating AI safety discourse. On Lerchner's account:

- AGI systems, however capable, are not candidates for phenomenal consciousness merely by virtue of their computational profile.
- Moral patiency concerns tied to substrate-independent consciousness (S3) have no foothold if substrate-independence itself is incoherent.
- The remaining concerns are behavioural and agential: powerful non-sentient optimizers can still cause catastrophic harm without having experiences.

The framing is significant. Lerchner does not argue that AGI cannot be conscious in principle — he argues that the specific theoretical route from "sufficiently advanced computation" to "phenomenal experience" is blocked. An AGI that happened to be conscious would need to be conscious *for some other reason* (biological substrate, substrate-sensitive causal structure, embodiment, etc.), not by the functionalist route.

This conclusion is where the contemporary AI-welfare discourse (S3) has the most direct stake. If Lerchner is right, the [Butlin–Long recommendations (S4)](s4-butlin-long.dd.html) to assess AI systems for consciousness indicators are tracking the wrong thing. If Lerchner is wrong, the whole welfare programme retains its motivation.

---

## 8. Where the Argument Invites Pushback

The paper is constructed so that several moves are vulnerable by design. Each becomes a pivot point for a different section of this survey.

- **The mapmaker move (→ S7).** Does observer-dependence of `f` actually follow from the formal triviality result, or can a non-trivial theory of implementation (Chalmers 1996, Piccinini 2015) restrict `f` to a principled subset? This is the contemporary pancomputationalism debate in direct form.

- **The biological alternative (→ S5).** Lerchner argues computational functionalism fails, but what succeeds it? Seth (2024) and Godfrey-Smith (2024) offer biological naturalism; Lerchner's argument is compatible with theirs but does not endorse it.

- **The practitioner view (→ S2).** What do the people building these systems think? Hinton and Sutskever believe current systems may already be conscious; LeCun rejects the possibility; Shanahan argues the question is malformed. The lab voices intersect Lerchner's claims at many angles.

- **The welfare implication (→ S3).** If Lerchner is right, is the Anthropic model-welfare programme philosophically confused? Or does it hedge responsibly under uncertainty, regardless of the underlying theory?

- **The indicator framework (→ S4).** The Butlin–Long report is the explicit target. Its defenders argue indicator properties are agnostic about the metaphysics; Lerchner argues the indicators presuppose the metaphysics.

- **The embodiment response (→ S6).** Thompson's enactivism and Wiese/Friston's FEP argue for substrate- and body-sensitivity on grounds distinct from Lerchner's. The three positions converge on a rejection of strong functionalism from different directions.

- **The illusionist dissolution (→ S8).** If Frankish and Kammerer are right that phenomenal consciousness is itself illusory, the question Lerchner is asking may not have a determinate answer. The theory wars become the frame in which his argument is evaluated.

---

## 9. Summary of the Argument

1. Computational functionalism claims substrate-independent consciousness via the chain *physics → computation → consciousness*.
2. Computation is formally a mapping `f(p) = A` from physical states to abstract states.
3. The mapping `f` is observer-chosen; infinitely many `f` are permissible for any given physics.
4. Abstract states are therefore epistemic (constructed by a mapmaker), not ontic (features of physics).
5. If consciousness is identified with abstract computational states, consciousness inherits the observer-dependence.
6. Therefore the functionalist derivation of consciousness from computation is circular: the computational description requires an interpreter who is already conscious.
7. Practical conclusion: AGI is best understood as a non-sentient tool; phenomenal consciousness, if possible in artificial systems, requires a non-functionalist account.

---

*Lerchner's *Abstraction Fallacy* is the survey's target, not its endorsed position. Subsequent sections examine how contemporary counter-arguments respond and how similar contemporary arguments reach related conclusions from different starting points.*
