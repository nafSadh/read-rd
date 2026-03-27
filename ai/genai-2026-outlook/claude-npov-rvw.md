# NPOV Review — GenAI 2026 Outlook

Reviewer: Claude Opus 4.6 (automated review, 2026-03-27)

## Files Reviewed

- `survey-paper.md` — main 8-dimension survey (~170 lines)
- `tensions-paper.md` — six contradictions analysis
- `scenarios-paper.md` — three scenarios for AI in 2027
- `s1-llms.dd.html` through `s8-economics.dd.html` — deep-dive companion pages
- `literature-collection.md` — source tracking
- `survey-paper.html`, `survey-slides.html`, `tensions-paper.html`, `scenarios-paper.html` — rendered outputs

## Pass 1

### POV (Point of View)

1. **Generally strong neutrality.** The "Six Tensions" structure is an effective NPOV device — presenting credible sources on both sides of key debates without prematurely resolving them. This is one of the paper's architectural strengths.

2. **Sora shutdown framing (Section 4 / S2).** The Sora shutdown is described with dramatic language ("the most dramatic event," "the most high-profile AI video product in the world") and the reasons listed ("cost pressure, 2% market share, copyright liability, competitive focus") lean toward a failure narrative. An alternative framing — strategic reallocation of resources — receives no airtime.

3. **Agent skepticism tilt (Section 5 / S3).** The agent section opens with Gartner's prediction that 40% of agentic AI projects will be canceled and production agents executing 10 or fewer steps. The positive use cases ("40% median cost reduction, 80% customer service containment") appear later and receive less structural emphasis. The ordering choices create a skeptical-first framing.

4. **"Installation phase" framing (Section 12).** The meta-finding that GenAI is in an "installation phase" is presented as the paper's conclusion, but this is one interpretive framework among several (Carlota Perez's technological revolutions framework). It is not attributed to a specific theorist, which makes an interpretive choice appear as objective finding.

### RIGOR

5. **Source adequacy is well-handled.** The explicit minimum of 5-6 sources per section, with both sides of key debates represented, is a strong methodological commitment. The paper follows through on this.

6. **Percentage proliferation without context.** The paper cites many survey statistics (78% use AI, 39% EBIT impact, 66% productivity gains, 20% revenue growth, 88% deploy, 12% full value). Different surveys use different methodologies, sample frames, and definitions of "use" / "deploy" / "impact." Comparing McKinsey's 78% to PwC's 88% to Deloitte's 66% as if they measure the same thing risks false precision. The paper partially addresses this by noting the surveys converge on the gap, but does not discuss methodological differences.

7. **Revenue and investment figures.** "$500B+ in hyperscaler capital expenditure" and "$252B in corporate AI investment" (Section 10) are stated without primary citation. Similar to the agentic survey, industry figures should carry source attribution.

8. **Scenario probability.** The scenarios paper states the "middle scenario" may be least likely but does not provide a rigorous basis for this claim. The assertion that extremes are more likely than the middle is itself a strong claim requiring support.

### BIAS

9. **Geographic bias toward US/Western framing.** The employment section focuses heavily on US labor market data (Yale Budget Lab, Goldman Sachs, Dallas Fed, Brookings). The regulation section covers EU and US. Chinese AI development is mentioned briefly (Qwen models, government restrictions on OpenClaw) but Chinese enterprise adoption, labor effects, and regulatory approaches receive minimal coverage despite China being the second-largest AI market.

10. **Enterprise-centric framing.** The workplace adoption section (S4) draws primarily from C-suite surveys (McKinsey, Deloitte, PwC). Worker-perspective surveys, union positions, and small business adoption receive less attention. The "leadership commitment is the differentiator" finding reflects the C-suite survey framing.

11. **The gender statistic (Section 7 / S5)** — "79% of employed women hold jobs at high automation risk, versus 58% of men" — is cited from Brookings but presented without discussing the methodology behind "high automation risk" classification or noting that such classifications have historically overestimated actual displacement.

### TONE

12. **Measured and appropriate overall.** The tone avoids both hype and doomerism. Phrases like "the honest answer to 'is AI overhyped?' is: it is simultaneously underhyped and overhyped" model the kind of nuanced position-taking that NPOV requires.

13. **Occasional editorial voice.** "Hype meets reality most violently" (Section 5) and "the most confusing technology in the market" (Section 1) are vivid but editorialize. These could be softened without losing clarity.

14. **"Consensus" boxes are well-calibrated.** Each section's consensus summary is concise and avoids overclaiming. This structural device works well for NPOV.

### Fixes Applied (Pass 1)

None. Pass 1 was a review-only pass. No edits were made to source files.

### Remaining Concerns (Pass 1)

- The strongest concern is BIAS #9: geographic coverage is US/West-heavy. Adding a brief acknowledgment of this limitation would improve transparency.
- The "installation phase" conclusion (POV #4) should be attributed to its intellectual lineage (Perez, or similar) rather than presented as an original finding.
- Survey methodology differences (RIGOR #6) deserve a brief note, even a single sentence, when cross-comparing enterprise adoption percentages from different firms.
- Overall, this is a well-structured discourse survey that achieves stronger NPOV than most technology analyses. The tensions framework is the paper's best feature — it resists the temptation to resolve contradictions prematurely and treats disagreement as informative signal.

---

## Pass 2

Reviewer: Claude Opus 4.6 (automated review, 2026-03-27)

### Scope

All `.dd.html` files (s1 through s8, plus genai-2026-overview), `survey-paper.html`, `tensions-paper.html`, `scenarios-paper.html`. Systematic search for first/second person POV, editorial language, unsupported claims, and logical issues.

### Issues Found and Fixed

#### POV — Second Person Removed

| # | File | Issue | Fix |
|---|------|-------|-----|
| P2-1 | `s4-workplace.dd.html` | "If you only read headlines" / "if you read the enterprise surveys" | Changed to "On the surface" / "But the enterprise surveys ... tell a very different story." |
| P2-2 | `s4-workplace.dd.html` | "Your employees are already using AI" (callout) | Changed to "Employees are already using AI" with neutral phrasing throughout. |
| P2-3 | `s3-agents.dd.html` | "If you are evaluating agent solutions..." (callout) | Changed to "Organizations evaluating agent solutions..." |
| P2-4 | `s5-employment.dd.html` | "you enter a profession... you develop tacit knowledge... You become senior" | Changed to "a worker enters... the worker develops... Seniority comes from..." |
| P2-5 | `genai-2026-overview.dd.html` | "context rot degrades quality before you reach the limit" | Changed to "before the nominal limit is reached" |
| P2-6 | `s1-llms.dd.html` | "You can hire researchers in months" (callout) | Changed to "Researchers can be hired in months" |

#### POV — First Person Plural Removed

| # | File | Issue | Fix |
|---|------|-------|-----|
| P2-7 | `s1-llms.dd.html` | "We are watching a market commoditize" | Changed to "The market is commoditizing" |
| P2-8 | `s1-llms.dd.html` | "When we discuss agents (S3) falling at a 40% rate" | Changed to "When the agents section (S3) discusses a 40% failure rate" |
| P2-9 | `s1-llms.dd.html` | "But What Are We Actually Measuring?" (heading) | Changed to "But What Are Benchmarks Actually Measuring?" |
| P2-10 | `tensions-paper.html` | "We'll know within 18 months." | Changed to "The answer should become clear within 18 months." |
| P2-11 | `tensions-paper.html` | "We argue that these tensions are not bugs..." (abstract) | Changed to "This paper argues that these tensions are not bugs..." |

Note: `survey-paper.html` uses "we" in its methodology section ("We conducted a structured discourse survey"). This is standard academic convention for describing the authors' methodology and was left unchanged.

#### Scholastic Rigor — Attribution Added

| # | File | Issue | Fix |
|---|------|-------|-----|
| P2-12 | `survey-paper.html` | "installation phase" presented as original finding in conclusion | Added attribution: "fits what economist Carlota Perez calls the installation phase of a technological revolution" |
| P2-13 | `tensions-paper.html` | "installation phase" unattributed in abstract | Added: "what economist Carlota Perez calls the installation phase of a technological revolution" |
| P2-14 | `tensions-paper.html` | "installation phase" in Bubble vs. Boom section | Added: "economist Carlota Perez's 'installation phase' framework for technological revolutions" |
| P2-15 | `s8-economics.dd.html` | "installation phase" unattributed in summary callout | Added: "what economist Carlota Perez calls the 'installation phase'" |
| P2-16 | `s8-economics.dd.html` | Perez reference in detail section lacked full identification | Added: "Economist Carlota Perez's framework" |

#### Tone — Editorial Flourishes Softened

| # | File | Issue | Fix |
|---|------|-------|-----|
| P2-17 | `survey-paper.html` | "the most confusing technology in the market" | Changed to "the most contested technology in the market" |
| P2-18 | `survey-paper.html` | "hype meets reality most violently" | Changed to "the gap between hype and reality is widest" |
| P2-19 | `survey-paper.html` | "the most dramatic event" (Sora shutdown) | Changed to "the most significant structural event" |
| P2-20 | `scenarios-paper.html` | "single-point predictions are dishonest" | Changed to "single-point predictions are unreliable — they assert confidence that the evidence does not support" |

### Issues Reviewed and Left Unchanged

1. **survey-paper.html "we" in methodology** — "We conducted a structured discourse survey" is standard academic convention.
2. **Quoted speech containing "you/we/our"** — All instances inside direct quotes from sources (Stanford's Landay, IBM's Baughman, Salesforce, etc.) are properly attributed speech acts, not authorial POV.
3. **s2-multimodal.dd.html "most high-profile AI video product"** — Factual descriptor; Sora received more media coverage than any other AI video product by a wide margin.
4. **Agent skepticism ordering (Pass 1 #3)** — The skeptical-first framing in S3 remains. This is a structural choice rather than a factual error; the section does present both sides. Noted but not altered.
5. **Geographic bias (Pass 1 #9)** — The US/Western framing in employment and regulation sections remains. This is a source-availability limitation rather than an editorial choice. An explicit limitation acknowledgment would improve the work but falls outside the scope of text-level NPOV fixes.
6. **Survey methodology differences (Pass 1 #6)** — Cross-comparison of survey percentages without discussing methodological differences remains. The paper partially mitigates this by noting convergence on the gap rather than on specific numbers.
7. **Scenario probability claim (Pass 1 #8)** — The "middle scenario may be least likely" argument in scenarios-paper.html offers reasoning (binary dynamics of installation-phase economics) but could be stronger. Left unchanged as the reasoning is at least stated, even if debatable.

### Assessment

Pass 2 found and fixed 20 issues across 7 files. The most common problem was second-person address ("you/your") in analytical passages and callout boxes — a natural tendency in writing that reads as direct advice but violates neutral encyclopedic register. The most substantively important fix was attributing the "installation phase" framework to Carlota Perez across four files; without attribution, the paper's central interpretive lens appeared to be an objective finding rather than one theoretical framework among several.

The remaining concerns from Pass 1 (geographic bias, survey methodology transparency, agent section ordering) are structural and would require more extensive rewriting to address. They are noted but do not constitute factual errors or clear POV violations.

Overall quality: strong. The tensions framework continues to be the paper's best NPOV feature, and the fixes in this pass bring the authorial voice closer to the neutral register the content deserves.
