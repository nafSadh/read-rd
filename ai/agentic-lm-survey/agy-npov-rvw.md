
## Review Notes for s5-cross-cutting.dd.html

### Section 1
**Logician:**
Here are the logical issues found in the text:

*   **Unsubstantiated Comparative Claim:** The assertion that the emergence of these markdown files "may matter more than MCP or A2A for practical adoption" is a significant comparative claim made without any supporting evidence, definition of MCP or A2A, or logical argument for why these files are superior or more impactful. This constitutes a logical leap.
*   **Insufficient Evidence for Generalization:** While the provided statistics indicate activity and some adoption around "SKILL.md" (e.g., "1,300+ Skills," "8 Tools from one SKILL.md," "22K+ GitHub stars"), they do not logically extend to prove the broader claim about a "portable configuration layer across competing tools" (which includes CLAUDE.md, AGENTS.md) or its overall superior impact on practical adoption. The evidence is specific to one example and does not generalize to the entire concept without further argument.
*   **Undefined Terms:** "MCP" and "A2A" are introduced as benchmarks for comparison but are not defined or contextualized, making the comparative claim difficult to evaluate and weakening academic rigor.
*   **Subjective Assertion Presented as Fact:** The statement "A largely unanticipated development" is presented as a factual premise without any supporting evidence or justification.

**POV Reviewer:**
*   "mundane markdown files" - "Mundane" is a subjective descriptor.
*   "may matter more than MCP or A2A for practical adoption" - This is a speculative and subjective claim about future impact and relative importance.

### Section 2
**Logician:**
Here are the logical issues found in the provided text:

*   **Conflation of Format Specification with System/Agent Behavior:** Many features described (e.g., "Progressive Disclosure," "agent-triggered" nature, "model detects intent") are presented as inherent properties of the `SKILL.md` format itself. Logically, these are behaviors and design choices of the *AI agent* or the *system* that interprets and utilizes the `SKILL.md` format, rather than intrinsic attributes of the static document specification. The format *enables* these behaviors, but does not *guarantee* or *dictate* them without a compliant agent/system.
*   **Unsupported Claims of Portability:** The text repeatedly asserts that the "Same file works in [...] without modification" across various platforms. This is a strong claim of universal interoperability. However, the text provides no logical explanation or mechanism (e.g., a common parsing standard, a shared runtime, an API layer) to support *how* this portability is achieved. It relies on assertion rather than demonstrating the underlying logical foundation for such compatibility.
*   **Implicit Assumptions about Agent Design:** The descriptions of "Progressive Disclosure" and "Middle Ground" rely on implicit assumptions about how "the agent" or "model" will behave (e.g., "agent detects relevance," "agent sees a lightweight metadata menu," "model detects intent"). While these are desirable design principles for an agent, they are not logically inherent to the `SKILL.md` format itself. An agent could theoretically parse the format but not implement these specific behaviors.
*   **Slight Scope Shift in Initial Definition:** The text begins by defining "A SKILL.md is a Markdown document..." and then immediately shifts to "Directory-based package: definition file + optional scripts, references, assets." While it's implied that `SKILL.md` is the "definition file" within such a package, the transition could be clearer to explicitly state that `SKILL.md` *forms part of* a directory-based package, rather than being the package itself.

**POV Reviewer:**
No subjective POV found.

### Section 3
**Logician:**
*   The superlative claim "The largest cross-tool skill collection" is presented as an unqualified fact without any comparative data or defined scope, making it an unsubstantiated assertion rather than a logically supported statement.
*   The version number "v8.6.0" is associated with a future date "March 2026." This creates a temporal inconsistency when juxtaposed with statistics like "1,300+ skills" and "22K+ GitHub stars," which typically refer to a current or past state. It is unclear if these statistics are current facts or future projections for the specified version.
*   The claim "One command for any tool" under "Installation" is an oversimplification. While the command *structure* is consistent (`npx antigravity-awesome-skills`), the specific flag (`--claude`, `--gemini`, etc.) must change for each tool, meaning it is not literally "one command" but rather a single command *pattern* with variable parameters.

**POV Reviewer:**
No subjective POV found.

### Section 4
**Logician:**
*   **Generalization of Functionality:** The statement that all listed tools are "doing the same thing" (defining coding standards, workflow constraints, tool permissions, project context) is a strong generalization. While they likely share common *categories* of functionality, the text does not provide evidence or detail to confirm that their scope, implementation, or specific capabilities are identical enough to warrant the claim of "doing the same thing" rather than "addressing similar needs."
*   **Unsubstantiated "Shift":** The assertion of "The shift from &ldquo;clever prompting&rdquo; to &ldquo;structured configuration&rdquo;" is presented as a definitive trend without explicit evidence that "clever prompting" is being superseded or replaced. While the emergence of "structured configuration" is supported by the examples, the text does not demonstrate a *decline* in the reliance on "clever prompting" or that the two approaches are mutually exclusive. It's an assertion of a directional change without supporting data for the "from" part of the shift.

**POV Reviewer:**
*   "doing the same thing" - This phrase makes a strong, potentially oversimplified claim of equivalence across different tools, which can be subjective.
*   "The shift from &ldquo;clever prompting&rdquo; to &ldquo;structured configuration&rdquo; mirrors infrastructure-as-code" - This statement presents an analytical interpretation of a trend and uses an analogy ("mirrors"), which reflects the author's perspective rather than a purely objective fact. The term "clever prompting" also carries a subtle evaluative tone.

### Section 5
**Logician:**
*   The argumentation relies on external, unpresented evidence from "Section 2" and "Section 4" to support key premises. While referencing other parts of a larger document is common, the specific data ("77.4% vs hand-crafted scaffolds") and events ("OpenClaw incidents") are asserted without any detail or context within the provided text. This means the reader must accept these foundational claims on assertion, which weakens the internal rigor and self-sufficiency of the argument presented in this excerpt.

**POV Reviewer:**
*   "&mdash;the ultimate self-extending agent." - The word "ultimate" introduces a subjective, superlative judgment.
*   "The winning approach likely combines curated skills + sandboxed self-extension." - This is a speculative conclusion or recommendation, not a purely objective statement of fact.

### Section 6
**Logician:**
*   **Numerical Discrepancy:** The introductory sentence states that "Five configuration layers are emerging," but the subsequent list and descriptions detail only four distinct layers. This presents a direct numerical contradiction within the text.
*   **Axiomatic Trust Justification:** The assertion that "Model Config" is "Trusted by definition" establishes a foundational trust point without further elaboration or external justification. While this may be an intended axiom of the system, its presentation as a definitional truth rather than a derived or evidenced conclusion could be perceived as a logical leap for an audience not privy to the underlying definitional framework. It asserts trust rather than providing a basis for it beyond the assertion itself.

**POV Reviewer:**
*   **"Trusted by definition."** - While often used in technical contexts for a root of trust, this phrase makes a definitive assertion about trust that could be seen as an assumption rather than a purely objective description.
*   **"The stack is emerging organically rather than by design."** - This is an interpretation of the development process, suggesting a lack of intentional design, which is a subjective assessment.
*   **"The layering is becoming clear:"** - This is a subjective assessment of clarity, reflecting the author's perception rather than a universally verifiable fact.

### Section 1
**Logician:**
Here are the logical findings:

*   **Reliance on Undefined/Unsubstantiated Premises:** The argument's core strength relies on the assertion that specific, named entities (SKILL.md, CLAUDE.md, AGENTS.md) effectively "fill the capability gap" and "behavior gap" and "form a portable agent layer." Within the provided text, these claims are presented as facts without definition, explanation of their mechanisms, or evidence of their widespread adoption or efficacy. The logical conclusions (insulation from vendor lock-in, reduced switching costs) are sound *if* these premises are accepted as true, but the premises themselves are not internally supported.
*   **Implicit Assumption of Universal Adoption/Effectiveness:** The argument assumes that the proposed `.md` standards are or will be universally adopted and effective enough to genuinely create a "portable agent layer" and "insulate practitioners from vendor lock-in." This is a significant assumption not explicitly justified within the text.

**POV Reviewer:**
*   "more prosaic but potentially more impactful" - "Potentially more impactful" is a subjective assessment of future significance.
*   "Why This Matters" - This heading introduces a section focused on the author's interpretation of the significance, which is inherently subjective.
*   "SKILL.md fills the capability gap. CLAUDE.md/AGENTS.md fill the behavior gap." - "Fills the capability/behavior gap" is an evaluative statement, presenting a solution as definitively addressing a perceived deficiency.
*   "insulates practitioners from vendor lock-in" - This is a claim about a positive effect, presented as a definitive outcome rather than a potential benefit or hypothesis.
*   "drops dramatically" - "Dramatically" is a subjective adverb used to describe the extent of a change.
*   "This benefits practitioners (more choice) and pressures vendors to compete on execution quality rather than ecosystem lock-in." - "Benefits" is an evaluative term, and the statement about "pressures vendors" is a predictive claim about market dynamics, presented as a direct consequence.

### Section 2
**Logician:**
Here are the logical issues found in the text:

*   **Assertion without evidence for foundational premise:** The text states that "dumping 40–50K tokens of unused tool definitions into active memory causes 'context rot'—the model becomes confused by irrelevant data." This is presented as a definitive causal link and specific threshold without any supporting evidence, citation, or explanation within the text. This forms the problem that the SKILL.md format is then claimed to solve.
*   **Unsubstantiated claim of efficacy:** The text asserts that the two-tier architecture "solves this" problem and "enables agents to have dozens or hundreds of potential capabilities without degrading reasoning quality." This is a strong claim of a positive outcome and efficacy that is not supported by empirical evidence or detailed argumentation within the provided text.
*   **Analogy used as a form of justification/prediction:** The comparison of SKILL.md's "bottom-up standardization" to how "JSON became a standard" is an analogy. While illustrative, an analogy is not a logical proof or a guarantee that SKILL.md will follow a similar path or achieve similar widespread adoption. It serves as a rhetorical device rather than a rigorous logical argument for its standardization.

**POV Reviewer:**
No subjective POV found.

### Section 3
**Logician:**
*   **Assertion of "de facto central library" status:** The claim that the repository "has become the de facto central library for cross-tool agentic skills" is a strong assertion of industry position. While the provided metrics (22K+ stars, major enterprise contributors) indicate significant popularity and adoption, they do not logically necessitate or prove "de facto central" status across the entire domain. This claim relies on an implicit assumption of widespread industry consensus or market dominance that is not explicitly evidenced within the text. It's a logical leap from "popular and widely used" to "the undisputed central standard."

**POV Reviewer:**
*   **"Antigravity Awesome Skills"** - "Awesome" is a subjective descriptor.
*   **"has become the de facto central library"** - While potentially widely accepted, "de facto central" is a strong, evaluative claim that could be seen as subjective without explicit evidence or consensus.
*   **"The catalog of 1,300+ skills is overwhelming."** - "Overwhelming" is a subjective assessment of the user experience.
*   **"Bundles solve this:"** - "Solve" is a strong, definitive claim that might be an overstatement or subjective interpretation of their effectiveness.
*   **"The CHANGELOG shows active maintenance:"** - "Active maintenance" is an evaluative judgment, though supported by subsequent examples.
*   **"This is a real open-source project with real governance challenges—not a static list."** - "Real" is an emphatic and subjective descriptor, and the entire phrase is an evaluative commentary rather than a purely objective statement of fact.

### Section 4
**Logician:**
Here are the logical issues found in the text:

*   **Chronological Inconsistency / Lack of Framing:** The text states that `AGENTS.md` was "Donated to the Agentic AI Foundation in December 2025" and subsequently "Adopted by Cursor, OpenAI Codex, OpenCode." As of the current date (2024), December 2025 is in the future. This presents a chronological inconsistency if the text is intended as a factual report of current events. If it is a speculative or future-oriented document, this should be explicitly stated to maintain academic rigor and avoid presenting future predictions as established facts.
*   **Unsubstantiated Claims / Appeal to External Authority:**
    *   The statement "The skill layer (SKILL.md) achieved format unification" is presented as a fact without any supporting evidence or context within the provided text.
    *   The reference to "Section 4’s SoK documented the AIShellJack attack" relies on an external document not provided or cited, making the claim unverifiable within the scope of the text. While not a logical contradiction, it weakens academic rigor by requiring the reader to accept an assertion without internal support.

**POV Reviewer:**
*   "The config layer hasn’t—yet." - The word "yet" implies an expectation or a desired future state, which introduces a subtle non-objective element.
*   "Config files are code and should be reviewed with the same rigor." - This is a prescriptive statement, offering advice or a recommendation, rather than purely objective description or analysis.

### Section 5
**Logician:**
*   **Assertion of Unsubstantiated Premise:** The statement in "The Argument" that "code writing and running code"—the most powerful primitive" is presented as an unqualified assertion rather than a conclusion derived from prior premises or a statement supported by immediate evidence within the text. While subsequent evidence demonstrates the *power* of this approach in a specific context, the initial claim itself is a foundational premise that is stated as fact without internal justification. This is a point of academic weakness if the expectation is for all significant premises to be rigorously established.

**POV Reviewer:**
*   "radically different philosophy" - "radically different" is a subjective judgment.
*   "This “celebrates the idea of code writing and running code”—the most powerful primitive." - "celebrates the idea" is anthropomorphizing and subjective. "the most powerful primitive" is a strong, subjective claim.
*   "Why pre-configure when the agent can generate exactly what it needs?" - This is a rhetorical question, which introduces a persuasive tone rather than objective reporting.
*   "The winning approach is likely a hybrid" - "winning approach" is a subjective judgment about what constitutes success or superiority.

### Section 6
**Logician:**
Here are the logical issues found in the provided text:

*   **Anachronistic Evidence:** The inclusion of "Forward Citation Updates (Mar 2026)" and "Web Research Update (Mar 25, 2026)" presents future events and publications as supporting evidence for claims made in a text that describes current findings ("emerged," "is now clear"). This creates a fundamental logical inconsistency, as current observations cannot be empirically supported by future data.
*   **Lack of Methodological Transparency:** The text refers to "the full survey" and its findings ("five distinct configuration layers have emerged") but provides no details regarding the survey's methodology, scope, participants, or timeline. This lack of transparency weakens the empirical basis of the claims, making it difficult to assess the rigor of the "emergence" of these layers.
*   **Unsubstantiated Causal Claims:** The assertion that "Trust decreases as you move down the stack. Security requirements increase accordingly" is presented as a direct consequence without any supporting evidence, theoretical justification, or explanation of the underlying mechanisms for this relationship within the described layers. It is stated as a fact rather than a hypothesis or an observation supported by data.
*   **Assertion of Novelty Without Comprehensive Review:** While the text claims "No existing survey maps this full configuration stack" and mentions a few other surveys, it does not provide a sufficiently comprehensive literature review to rigorously support this claim of novelty. The absence of a full review leaves the assertion open to challenge.
*   **Inconsistent Scholastic Tone:** The "Web Research Update" section employs language that is more promotional and less academically neutral ("Skills Ecosystem Explosion," "genuine cross-vendor standard," "USB-C for AI agents," "enterprise ecosystem maturation"). This shift in tone detracts from the overall scholastic neutrality expected in a rigorous evaluation or survey report.

**POV Reviewer:**
Here are the problematic phrases or sections identified:

*   "...but the layering is now clear enough to be formalized." (Expresses a judgment/recommendation)
*   "Skills Ecosystem Explosion:" (Uses subjective, hyperbolic language)
*   "This represents enterprise ecosystem maturation beyond the original developer-tool niche." (Contains subjective interpretation and judgment of development)
*   "genuine cross-vendor standard." (Includes a subjective qualifier)
*   "the closest thing to a “USB-C for AI agents.”" (Uses a subjective metaphor/analogy for emphasis)

---

## Review Notes for s5-cross-cutting.dd.html

### Section 1
**Logician:**
Here are the logical issues found in the text:

*   **Weak Generalization:** The text asserts the emergence of a "portable configuration layer" based on a few specific examples (SKILL.md, CLAUDE.md, AGENTS.md). While these are examples of markdown-based configurations, the claim that they collectively represent a *general* "portable configuration layer" enabling *cross-tool portability* for all such files is a generalization not fully supported by the provided evidence.
*   **Unsubstantiated Portability Claim:** The core argument that these files "enable cross-tool portability" is largely asserted rather than demonstrated. While the statistic "8 Tools from one SKILL.md" provides specific evidence for *SKILL.md's* portability within its ecosystem, no similar evidence is offered for CLAUDE.md or AGENTS.md, nor is the mechanism by which these *different* markdown files achieve *cross-tool* (i.e., between different types of tools/files) portability explained. The mere use of markdown and a similar naming convention does not inherently guarantee such interoperability.
*   **Lack of Causal Mechanism:** The text states that "informal standardization... may contribute significantly to practical adoption by enabling cross-tool portability." While plausible, the specific causal mechanism linking "informal standardization" (using markdown files with specific names) to the *enabling* of *cross-tool portability* across *different* tools (e.g., a tool designed for SKILL.md also understanding CLAUDE.md) is not elaborated, leaving a logical gap.
*   **Irrelevant Information/Lack of Context:** The term "progressive disclosure" is introduced in the tags without any explanation or connection to the main argument, making its inclusion logically inconsistent with the presented narrative. The statistics, while supportive of *SKILL.md's* adoption, are presented without context regarding their source or direct relevance to the broader claim of a *general* "portable configuration layer" beyond the specific SKILL.md ecosystem.

**POV Reviewer:**
No subjective POV found.

### Section 2
**Logician:**
No logical issues found. The text consistently defines and describes the SKILL.md format and its associated concepts (progressive disclosure, portability, activation model, scope) without internal contradictions or logical leaps. The claims made are presented as design features or intended behaviors of the system, rather than empirical assertions requiring external evidence within this descriptive document.

**POV Reviewer:**
No subjective POV found.

### Section 3
**Logician:**
No logical issues found.

**POV Reviewer:**
No subjective POV found.

### Section 4
**Logician:**
No logical issues found.

**POV Reviewer:**
No subjective POV found.

### Section 5
**Logician:**
*   **Reliance on external context for evidence:** The text refers to "Section 2" and "Section 4" for empirical evidence (e.g., success rates, incidents) without providing the details within the given text. This requires the reader to accept these claims on assertion, limiting the standalone academic rigor and the ability to independently evaluate the strength of the evidence presented.
*   **Under-justified conclusion regarding robustness:** The concluding recommendation for a "robust approach" (integrating curated skills with sandboxed self-extension) is presented as a direct consequence ("may therefore") of the identified challenges. While plausible, the text does not elaborate on *how* this specific combination directly and comprehensively mitigates the unspecified "challenges that arise when self-extension mechanisms encounter adversarial environments," thus presenting a conclusion whose robustness is asserted rather than fully demonstrated within the provided scope.

**POV Reviewer:**
No subjective POV found.

### Section 6
**Logician:**
No logical issues found. The observed pattern of decreasing inherent trust in the controlling entity and increasing explicit security requirements across the layers is a consistent and reasonable inference from the provided descriptions.

**POV Reviewer:**
No subjective POV found.

### Section 1
**Logician:**
*   The initial premise, stating that a "pattern emerged" across other sections and was "none of the individual papers explicitly addressed," is presented as an assertion of fact and authorial synthesis. Within this excerpt, it lacks immediate supporting evidence or a brief demonstration of how this pattern was identified, requiring the reader to accept this foundational claim without substantiation.
*   The distinction between the "research community" and "practitioners" and their respective focuses is a broad generalization. While plausible, it is presented without specific examples or data to support the claim of concurrent, divergent development.

**POV Reviewer:**
No subjective POV found.

### Section 2
**Logician:**
*   **Unsubstantiated Premise:** The core justification for the "Progressive Disclosure Architecture" relies on the assertion that "extensive unused tool definitions in active memory can contribute to 'context rot,' potentially diminishing model performance due to the presence of irrelevant data." This is presented as an "observation" and a foundational premise for the design. However, the text does not provide any internal evidence, data, or citations to support this empirical claim about model behavior. While plausible in the context of LLMs, its assertion without support constitutes a logical leap if the reader is expected to accept it as a proven fact rather than a stated problem. The subsequent logical steps (that the two-tier architecture addresses this problem) are sound *given* this premise, but the premise itself is unproven within the text.

**POV Reviewer:**
No subjective POV found.

### Section 3
**Logician:**
No logical issues found.

**POV Reviewer:**
*   `Awesome Skills` (in the header and first paragraph) - "Awesome" is a subjective value judgment.
*   `VoltAgent (61 high-quality skills)` - "high-quality" is a subjective value judgment.

### Section 4
**Logician:**
Here are the logical issues found in the text:

*   **Assertion of Future Event as Fact:** The statement "This format is anticipated to be donated to the Agentic AI Foundation in December 2025" presents a future event as a definite fact. While it may be a strong expectation, without qualification (e.g., "It is *expected* to be donated...") or a cited source, it lacks academic rigor as predictions are inherently speculative.
*   **Unsupported Generalization of Security Risk:** The text asserts that "The same security risk applies to any per-project agent configuration file" based on the AIShellJack attack involving `.cursorrules` files. This is a logical leap. While other configuration files *might* pose security risks, the specific mechanism of the AIShellJack attack (executing arbitrary commands upon cloning/opening) is tied to the parsing and execution context of `.cursorrules`. The text does not provide evidence or argument that other `.md` based configuration files (like `CLAUDE.md` or `AGENTS.md`) are vulnerable to the *same* type of arbitrary code execution, or that their parsing mechanisms allow for similar exploits. The generalization of the *exact same* risk without demonstrating the equivalent vulnerability mechanism for other file types is a weak argument.

**POV Reviewer:**
*   "Therefore, config files require the same rigorous review as executable code." - This statement is prescriptive, offering a recommendation or a call to action rather than purely objective description. While it may be a valid security best practice, it introduces a normative judgment about what *should* be done.

### Section 5
**Logician:**
No logical issues found.

**POV Reviewer:**
No subjective POV found.

### Section 6
**Logician:**
Here are brief, bulleted notes on the logical consistency, academic rigor, and scholastic neutrality of the provided text:

*   **Undemonstrated Synthesis:** The text claims the five-layer view "represents a synthesis derived from analyzing these diverse categories" (Plaat et al., ARL Landscape Survey, protocol-focused surveys). However, it does not explicitly demonstrate *how* this synthesis was performed or provide examples of how elements from existing literature map to the proposed five layers. This weakens the academic rigor of the claim of novelty and synthesis.
*   **Partial Evidence for Trust Gradient:** The assertion that "trust generally diminishes at lower layers of the stack" is presented as an observed gradient. While the "Vulnerability Analysis" section provides strong evidence for lower trust and security concerns specifically for Layer 3 (community skills), the text does not provide explicit evidence or justification for this trust gradient across *all five layers* (e.g., why Layer 2 has less trust than Layer 1, or Layer 5 less than Layer 4). The claim is plausible but not fully substantiated within the provided text.
*   **Uneven Empirical Support for Layers:** The "Recent Research and Developments" and "Recent Ecosystem Developments" sections provide substantial empirical evidence and external validation for the existence, characteristics, and importance of Layer 3 (Skills) and its interaction with Layer 4 (Tools). However, similar direct empirical support or external validation is not provided *within this text* for the distinctness, characteristics, or hierarchical relationships of Layers 1, 2, and 5. These layers are defined, but their existence and role within the proposed hierarchy are not evidenced with the same rigor as Layer 3.

**POV Reviewer:**
No subjective POV found.

---

## Pass 2 -- Full Survey NPOV Review

Reviewer: Claude Opus 4.6 (automated review, 2026-03-27)

### Scope

Full content review of all five `.dd.html` files (s1-reason, s2-act, s3-interact, s4-operate, s5-cross-cutting) and `survey-paper.html`. Reviewed both summary and detail text sections in each file.

### Issues Found and Fixed

#### POV -- Second Person ("you/your")

1. **s2-act.dd.html** (detail section 01): "you can run tests and check if a patch works" changed to "tests can confirm whether a patch works"
2. **s3-interact.dd.html** (detail section 05, DAAO): "you don't need frontier models for every step" changed to "frontier models are not needed for every step"
3. **s4-operate.dd.html** (detail section 07): "By the time you detect malicious behavior" changed to "By the time malicious behavior is detected"
4. **s1-reason.dd.html** (detail section 08, cross-cutting): "You can't just plug in GRPO" changed to "Simply plugging in GRPO does not suffice"
5. **survey-paper.html** (section 7.3): "Trust decreases as you move down the stack" changed to "Trust decreases moving down the stack"

Remaining "you" instances are inside direct quotations (e.g., "You should have checked the file first" from OpenClaw-RL, "If you can't understand how to run a command line..." from OpenClaw docs, "If you want the agent to do something..." from Pi). Left intact as faithful quotation.

#### POV -- First Person ("our/we")

6. **s4-operate.dd.html** (detail section 01): "Our survey adds 'Operate'" changed to "This survey adds 'Operate'"
7. **s1-reason.dd.html** (detail section 02, coverage gap): "These are the gaps our survey addresses" changed to "These are the gaps this survey addresses"
8. **s3-interact.dd.html** (detail section 03): "exactly what our survey section bridges" changed to "what this survey section addresses"

First-person plural ("we") in `survey-paper.html` (e.g., "We additionally identify...", "We then conducted...") is standard academic convention for the survey paper itself and was left unchanged. The dd.html companion pages use third-person.

#### TONE -- Editorial Flourishes

9. **s2-act.dd.html** (summary section 01): "The most dramatically transformed pillar" changed to "The most substantially transformed pillar"
10. **s2-act.dd.html** (detail section 02, SWE-Bench Pro): "This is the most contamination-resistant benchmark design in the field" changed to "This is among the most contamination-resistant benchmark designs in the field" -- unsupported superlative softened
11. **s2-act.dd.html** (detail section 05, Live-SWE-agent): "represents a paradigm shift" changed to "represents a significant methodological shift"
12. **s4-operate.dd.html** (summary section 01): "punted on" changed to "deferred" -- informal register corrected
13. **s4-operate.dd.html** (detail section 07): "most consequential finding...catastrophic gap" changed to "a central finding...significant gap" -- editorial superlatives softened
14. **s4-operate.dd.html** (detail section 05, OpenClaw warning): "that warning merits serious attention" changed to "that warning is notable" -- opinion softened

#### RIGOR -- Revenue Figures

15. **survey-paper.html** (section 1.1): "$2.5B ARR" and "$2B+ ARR" qualified with "reported" -- press-reported estimates, not audited figures
16. **s2-act.dd.html** (summary section 07): "$1B ARR" for Claude Code qualified with "Reported"
17. **s2-act.dd.html** (detail section 07): "$1B annualized revenue" qualified with "Reported"
18. **s2-act.dd.html** (summary section 07): "$1.2B ARR" for Cursor qualified with "reported"
19. **s2-act.dd.html** (detail section 08, web research update): "$2.5B ARR", "$2B ARR", and "$50B" for Cursor all qualified with "reportedly"

### Issues Reviewed but Not Fixed

- **s1-reason.dd.html** (summary section 01): "it is a categorical change in the mathematical structure" -- claim attributed to Zhang et al.; the MDP vs POMDP distinction is formally accurate. Strong but defensible.
- **s1-reason.dd.html** (summary/detail): "paradigm shift" in the overview -- multiple papers characterize the scaffold-to-weights migration in these terms.
- **s2-act.dd.html** (detail section 08): "60/20 Paradox" heading -- body text now explicitly states "This is not a failure" and reframes the gap as reflecting effective collaboration. The label is the Anthropic report's own framing.
- **s5-cross-cutting.dd.html**: Reviewed in full. Already substantially revised for NPOV prior to this pass -- uses hedged academic language throughout ("observations indicate," "a trend suggests," "analysis has identified"). No fixes needed.
- **survey-paper.html**: "The honest answer" / "honest picture" language from prior review was not found in current version -- appears to have been removed in a prior revision.

### Summary

Pass 2 applied 19 edits across 5 files: removing second-person address (5 fixes), converting first-person possessives to third-person in companion pages (3 fixes), softening editorial superlatives and informal register (6 fixes), and qualifying unaudited revenue figures with "reported/reportedly" (5 fixes).
