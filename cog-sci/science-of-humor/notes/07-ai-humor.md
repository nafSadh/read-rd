# S7: AI & Computational Humor — Notes

## Why Humor Is AI-Hard

### What Humor Requires (All Simultaneously)
1. **Theory of mind**: knowing what the audience expects, believes, values
2. **Cultural knowledge**: shared references, taboo boundaries, social norms
3. **Timing**: not just when to speak but when NOT to speak
4. **Creative subversion**: generating something genuinely unexpected
5. **Evaluation**: knowing whether the subversion is funny vs merely random

### Why Each Is Hard for AI
- **Theory of mind**: LLMs can approximate this but don't truly model other minds
- **Cultural knowledge**: available in training data but not organized for comedic use
- **Timing**: no concept of real-time audience response (text-based models)
- **Creative subversion**: LLMs predict the most likely next token — comedy requires the UNLIKELY token that still makes sense
- **Evaluation**: models can't tell if something is funny because they don't experience humor

## The Current State (2025-2026)

### What LLMs Can Do
- Recognize joke structure (setup/punchline format)
- Generate jokes that follow templates (puns, knock-knock, etc.)
- Explain why jokes are funny (post-hoc analysis)
- Produce humor-adjacent content that's mildly amusing
- Users rate humor-trained LLM captions "nearly on par" with top human humor (ACM, 2025)

### What LLMs Can't Do
- Generate genuinely surprising, original humor
- Time delivery for maximum effect
- Read the room (adapt to audience)
- Produce the kind of humor that makes someone spit out their coffee
- Be funny about being unfunny (meta-humor requires self-awareness)
- On HumorBench-hard: no LLM exceeds 60% accuracy

### The Formulaic Problem
- LLMs produce humor that's technically correct but lacks spark
- "ChatGPT is fun, but it is not funny" (ArXiv, 2023)
- Models tend toward safe, predictable outputs — the opposite of what comedy requires
- Next-token prediction fundamentally biases toward the expected
- Comedy is what happens when you predict correctly and then swerve

## Computational Humor Research (Pre-LLM)

### Historical Approaches
- JAPE (Joke Analysis and Production Engine) — automatic pun generation
- HAHAcronym — humorous acronym generation
- Colton's Computational Creativity framework
- These systems could produce wordplay but nothing broader

### The Pun Problem
- Puns are the one type of humor that is partially computable
- They require: semantic ambiguity + phonological overlap + unexpected interpretation
- All of these can be represented in knowledge graphs
- But puns are the lowest form of humor (and that's not just snobbery — they require the fewest cognitive skills)

## Humor as the Turing Test of Comedy

### The Argument (Thomas Smith, Medium)
- Humor tests cultural knowledge, timing, audience modeling, and creative subversion simultaneously
- No other benchmark requires all four
- If an AI can be genuinely, consistently, originally funny, it probably has achieved general intelligence
- Progress in humor may be the best proxy for progress toward understanding

### The Counter-Argument
- Humor is culturally specific — an AI that's funny in English may not be funny in Japanese
- The bar is actually low: we laugh at many things that aren't objectively funny
- Social laughter (Provine) is the majority of human laughter and has nothing to do with humor generation
- An AI that generates good puns is not close to AGI

## When AI Humor Accidentally Works

### Why It's Funny When AI Fails
- AI-generated humor that's accidentally funny exploits the "uncanny valley" of comedy
- The incongruity between the AI's confident delivery and the output's absurdity IS the joke
- We laugh at AI humor the way we laugh at malapropisms — the error reveals something
- The most genuinely funny AI outputs are the unintentional ones

### Implications
- Current AI humor is best understood as a new GENRE of comedy, not as human comedy
- AI as comic foil (the butt of the joke) vs AI as comedian (the teller of the joke)
- The gap between these two is the gap between current AI and AGI

## Key Insight
Humor may be the truest test of AI understanding — not because it's the hardest task, but because it requires the broadest competence. A system that can be genuinely funny must understand people, culture, expectations, and surprise simultaneously. The current failure of AI humor isn't a bug — it's diagnostic. It tells us precisely what's missing from current AI: the ability to hold multiple frames simultaneously and choose the surprising one that still makes sense.

## Key Sources
- AI-01 through AI-07 in literature collection
- HumorBench (2025) is the most rigorous current evaluation
- "ChatGPT is fun but not funny" (2023) captures the core challenge
- The fitness-indicator framing connects to evolutionary psychology of humor
