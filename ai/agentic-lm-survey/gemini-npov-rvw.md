# Gemini NPOV Audit — `survey-paper.html`

**File:** `survey-paper.html`
**Path:** `ai\agentic-lm-survey\survey-paper.html`
**Model:** `gemini-3-flash-preview`
**Date:** 2026-03-27

---

This audit report evaluates the research paper titled **"Agentic LLMs in the Wild: Reasoning, Acting, Interacting, and Operating"** for adherence to NPOV standards and scholastic rigor.

## Summary
The paper provides a structured update to the 2025 Plaat et al. taxonomy of agentic LLMs, proposing a fourth analytical axis: "Operate." It synthesizes recent (post-2025) developments in reinforcement learning (RL) internalized reasoning, the expansion of agentic coding, the standardization of agent protocols (MCP/A2A), and the emergent security risks of production deployment. While the paper is sophisticated and well-structured, it is written from a "future-dated" perspective (March 2026), which leads to the inclusion of speculative data (e.g., GPT-5 performance, 2026 ARR figures) and occasional lapses into advocacy for specific architectural shifts.

## POV Issues
- **First-person voice as personal narrative:** 
    - *Quote:* "We are explicit about this because the field is moving faster than any individual can read comprehensively, and intellectual honesty about coverage depth is itself a contribution."
    - *Issue:* This shifts from a description of methodology to a personal defense of the author's limitations.
    - *Fix:* Remove the justification. "Given the rapid pace of publication in the field, this study prioritizes depth of argument over exhaustive breadth."
- **Second-person address:** 
    - *Quote:* "Teams don't need massive unique RL datasets."
    - *Issue:* Uses "you" (implied) to address the reader/practitioner directly.
    - *Fix:* Use third-person: "Large-scale unique RL datasets may not be a prerequisite for effective model optimization."
- **Personal opinions stated as fact:** 
    - *Quote:* "The paper needs a reframing."
    - *Issue:* Authorial directive rather than an evidence-based conclusion.
    - *Fix:* "These shifts suggest that a new taxonomic framework is required to capture the current state of the field."
- **Enthusiast/Advocacy framing:** 
    - *Quote:* "The winning approach must find an asymmetric advantage..."
    - *Issue:* Prescriptive language ("must") and competitive framing ("winning") more suited to a strategy memo than a survey.
    - *Fix:* "Future development will likely focus on balancing capability with architectural security."

## Logical Consistency Issues
- **Category Conflict:** 
    - *Quote:* "This is not a comprehensive survey... It is an argument paper." vs Title: "Survey Paper."
    - *Issue:* The paper identifies as a "Survey Paper" in the title and metadata, but Section 2.3 explicitly disclaims being a survey. This creates an internal contradiction regarding the paper's genre and intended contribution.
- **Premise-Conclusion Gap:**
    - *Quote:* "77.4% on SWE-bench Verified... while self-play training on raw codebases eliminates the need for human-curated data entirely."
    - *Issue:* The conclusion that human data is "entirely" eliminated is not supported by the later admission in Section 4.2 that a "minimum model capability threshold" (initially trained on massive human data) is required for this to work.

## Scholastic Rigor Issues
- **Factual claims (Future-dating):** 
    - *Quote:* "GPT-5 drops from 25.9% to 8.4%." / "Claude 4.5 Sonnet shows +22.6% improvement."
    - *Issue:* These models and their specific performance metrics do not exist as of the current real-world date. In a scholarly context, citing speculative future models as empirical evidence is a critical rigor failure.
    - *Fix:* Attribute these to "projected capabilities" or use currently available frontier models (e.g., GPT-4o, Claude 3.5).
- **Statistics without primary sourcing:** 
    - *Quote:* "Claude Code (reported $2.5B ARR by March 2026)."
    - *Issue:* Financial projections are stated as historical facts without a specific citation to a financial report or news source.
    - *Fix:* "Industry reports estimate revenue growth for agentic tools in the billions (Anthropic, 2026)."
- **Causal claims vs. Correlation:** 
    - *Quote:* "training agents to judge which action is better... produces genuine self-reflection rather than imitated reflection."
    - *Issue:* "Genuine" vs. "imitated" is a philosophical/mechanistic distinction that the cited RL paper likely cannot prove.
    - *Fix:* Use: "...produces behaviors statistically indistinguishable from deliberative self-reflection."
- **Teleological Language:** 
    - *Quote:* "The trend toward learned rather than engineered agent capabilities..."
    - *Issue:* Implies an inevitable evolutionary direction.
    - *Fix:* "The current research trajectory favors learned over hand-engineered capabilities."

## Tone Issues
- **Editorial Flourishes:** 
    - *Quote:* "unprecedented act of co-governance," "stunning result," "virtuous cycle."
    - *Issue:* Hyperbolic adjectives that bias the reader toward the author’s excitement.
    - *Fix:* Replace "unprecedented" with "rare" or "notable"; replace "stunning" with "significant."
- **Rhetorical Questions:** 
    - *Quote:* "The field is no longer asking 'can agents reason...?' It is asking 'can we make them do so safely...?'"
    - *Issue:* Used to create a dramatic narrative rather than provide analysis.
    - *Fix:* "The research focus has shifted from basic feasibility to safety and reliability at scale."
- **Informal phrasing:** 
    - *Quote:* "The winning approach must find an asymmetric advantage — high capability with architectural security, not capability restriction."
    - *Issue:* "Winning approach" is colloquial and lacks nuance.
    - *Fix:* "The most viable long-term strategy involves..."

## Priority Fixes
1.  **Temporal Realignment:** The paper is written from the perspective of March 2026. Unless this is for a "speculative fiction" journal, all references to GPT-5, Claude 4.5, and 2026 financial data must be removed or clearly labeled as hypothetical projections.
2.  **Genre Clarification:** Resolve the contradiction in Section 2.3. Either commit to being a "Critical Review/Perspective" or expand the "Survey" to be comprehensive.
3.  **Removal of Personal Voice:** Strip the "Method and Scope" section of its defensive tone. Rephrase Section 2.2 to state the inclusion criteria neutrally.
4.  **Hedge Causal Claims:** Soften the language around "self-improvement" and "genuine reasoning." The paper currently presents RL-driven emergent behavior as a solved mechanistic fact.

## Overall Assessment
**Grade: B-**

**Justification:** The paper is intellectually ambitious and provides a highly useful synthesis of the "Operate" axis, which is indeed missing from many current taxonomies. The technical understanding of POMDPs and the protocol stack (MCP/A2A) is excellent. However, the "future-history" conceit severely undermines its scholastic rigor, and the tone occasionally slips into industry cheerleading. With temporal realignment and a more neutral authorial voice, this would be an A-level contribution.