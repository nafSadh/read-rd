# NPOV & Rigor Review — Agentic LLMs in the Wild

**Date:** 2026-04-20
**Reviewer:** Claude (npov-ai-r2)
**Files reviewed:** survey-paper.html

## Summary
A technical survey paper updating Plaat et al.'s 2025 JAIR taxonomy with a proposed fourth axis ("Operate") covering security, deployment, and economics of agentic LLMs. The paper is tightly written, quantitatively grounded, and largely NPOV-compliant in register. The biggest concern is a pattern of Anthropic-favoring framing and sourcing — Anthropic's own 2026 Trends Report and Claude Code are cited as neutral evidence for broad industry claims (ARR estimates, 60/20 adoption paradox, security-capability tradeoff favorable to Claude Code), and an "industry estimates" claim about ARR in the billions is attributed only to a single Anthropic-produced report without independent corroboration. A secondary concern is the large number of authorial "we" statements in methodology and taxonomy framing that should be depersonalized to meet the repo's NPOV standard.

## POV Issues

- `survey-paper.html#abstract` — "We synthesize 28 papers read from primary sources across the four categories, identify five cross-cutting themes including the emergence of a portable skills layer, and propose a research agenda grounded in the gap between benchmark performance and production reality." — First-person plural "we" as authorial voice. — Fix: "This survey synthesizes 28 papers read from primary sources across the four categories, identifies five cross-cutting themes including the emergence of a portable skills layer, and proposes a research agenda grounded in the gap between benchmark performance and production reality."

- `survey-paper.html#12-why-a-fourth-axis` — "We additionally identify a **cross-cutting** layer: the emergence of portable configuration standards..." — First-person plural authorial voice. — Fix: "An additional **cross-cutting** layer is identified: the emergence of portable configuration standards..."

- `survey-paper.html#9-limitations` — "We read 28 papers at varying depth (11–100%), not the comprehensive coverage of Plaat et al.'s 300+ references." — First-person plural authorial voice. — Fix: "This survey covers 28 papers at varying depth (11–100%), not the comprehensive coverage of Plaat et al.'s 300+ references."

- `survey-paper.html#9-limitations` — "Our industry source analysis relies on public reports and web research rather than proprietary deployment data." — First-person plural "our" authorial voice. — Fix: "The industry source analysis relies on public reports and web research rather than proprietary deployment data."

- `survey-paper.html#9-limitations` — "Our security analysis of coding platforms [18] relies on the SoK authors' methodology..." — First-person plural "our". — Fix: "The security analysis of coding platforms [18] relies on the SoK authors' methodology..."

- `survey-paper.html#9-limitations` — "The Data Over-Exposure statistics [19] come from a single study on MCP.so-listed tools and may not represent the full MCP ecosystem." — This is fine; noting that the preceding "our" cluster concentrates POV in this section.

## Logical Consistency Issues

- `survey-paper.html#21-paper-selection` vs. `survey-paper.html#1-introduction` / abstract — Abstract and intro repeatedly frame the survey as covering "Between January 2025 and March 2026," and §9 states the forward citation sweep covers "papers indexed by Semantic Scholar by March 23, 2026." But §2.1 says: "a structured literature search across arXiv, Semantic Scholar, and web sources for publications from **November 2023 through March 2024**." The November 2023–March 2024 window contradicts the stated January 2025–March 2026 scope and the §9 March 2026 cutoff. This is an internal inconsistency; it appears to be a typo ("2024" where "2026" was intended), but as written the methodology does not match the claimed scope.

- `survey-paper.html#21-paper-selection` vs. `survey-paper.html#22-reading-depth` — §2.1 concludes that the forward-citation sweep "identified 6 additional papers published in February–March **2024**," again contradicting the paper's stated scope window. Readers cannot verify the selection procedure against the claimed time window.

## Scholastic Rigor Issues

- `survey-paper.html#11-four-shifts` — "industry estimates project ARR in the billions for leading agentic coding tools by early 2026 [33]" — The citation [33] is "Anthropic. '2026 Agentic Coding Trends Report.' January 2026." — an Anthropic-produced report used as sole support for a market-wide "industry estimates" claim. — Fix: Attribute the figure directly to Anthropic ("Anthropic's 2026 Agentic Coding Trends Report estimates..."), and if it is to stand as an industry-wide claim add independent corroboration (analyst report, SEC filing, or a neutral market-research source).

- `survey-paper.html#43-the-6020-paradox` — "Anthropic's 2026 Agentic Coding Trends Report documents that engineers utilize AI in approximately 60% of their work but fully delegate only 0–20%." — A major finding is sourced entirely to Anthropic self-reporting without triangulation. — Fix: Flag as an Anthropic-authored claim ("According to Anthropic's 2026 Agentic Coding Trends Report, a vendor-authored self-report...") and note limitations.

- `survey-paper.html#65-the-security-capability-tra` — "Claude Code achieves the lowest vulnerability rating (Low) through aggressive sandboxing, while Cursor rates Critical due to extensive extension trust." — This is a vendor-comparative claim with an Anthropic product favorably rated. Whether citation [18] (Maloyan & Namiot) actually grades both products in this binary way is not clear from the prose; the claim is presented without methodological context. — Fix: Add the evaluation framework used ("On the vulnerability rubric defined in [18]...") and note whether the SoK authors have institutional ties.

- `survey-paper.html#41-the-benchmark-reality-check` — "Best model performance remains below 45% Pass@1." / "The best-performing frontier model in the study achieves only 21% on SWE-EVO versus 65% on SWE-Bench Verified" — These numeric claims are plausible but come with parenthetical hedges that read oddly ("model designations reflect the authors' projected capability tiers as of late 2025"). — Fix: Either state the specific model names used by the original paper, or remove the obfuscation; the current phrasing is ambiguous about what is being benchmarked.

- `survey-paper.html#11-four-shifts` — "Claude Code (industry estimates project ARR in the billions for leading agentic coding tools by early 2026 [33]), Antigravity, Cursor, Codex CLI, Gemini CLI (96K+ GitHub stars), OpenClaw (100K+ stars)" — GitHub star counts 96K+ and 100K+ are cited as statistics with no source. — Fix: Add a dated URL or accessed-date citation for each star-count claim.

- `survey-paper.html#23-what-this-survey-is-not` — "Plaat et al. (85 pages) or the ARL Landscape Survey (95 pages, 500+ works) [2]" — Page counts and "500+ works" are factual claims unsupported by inline citation beyond [2]. — Minor; likely verifiable from the reference, but should be explicit.

- `survey-paper.html#52-governance` — "Six competing companies — OpenAI, Anthropic, Google, Microsoft, AWS, and Block — agreed to jointly steward interoperability standards." / "This collaborative structure aims to foster the development of interoperability standards, a factor often considered critical for enterprise adoption of new protocols." — The "often considered critical for enterprise adoption" assertion is presented as general knowledge without citation. — Fix: Either cite a source or drop as speculative framing.

- `survey-paper.html#51-the-protocol-stack` — "MCP (Model Context Protocol, Anthropic)" / "A2A (Agent-to-Agent Protocol, Google)" — Protocol origins stated as fact without citation; these attributions are common knowledge but a source would strengthen the claim.

- `survey-paper.html#53-orchestration-evidence` — "multi-agent systems demonstrated 100% actionable recommendations within the trial parameters, compared to 1.7% for single agents... 80-fold improvement in specificity and a 140-fold improvement in correctness" — Single-source claim from citation [16] (Drammeh, a single-author preprint on arXiv, Jan 2026). These are extraordinary effect sizes (80× / 140×) presented as a neutral finding. — Fix: Hedge ("A single study [16] reports...") and note that the effect sizes are unusually large and not yet independently replicated.

- `survey-paper.html#54-difficulty-aware-routing` — "+3.2–10.2% accuracy at 41% of the inference cost, generalizing to unseen model backbones." — Numeric claim sourced to [25] but no methodological hedge on generalization claim. — Minor.

- `survey-paper.html#71-skillmd-as-emerging-standar` — "SKILL.md files — Markdown documents with YAML frontmatter — define reusable agent capabilities that operate across Claude Code, Gemini CLI, Cursor, Codex CLI, and four other tools without modification [28, 29]." — "without modification" is a strong compatibility claim. — Fix: Hedge ("claim to operate...") unless the cited sources explicitly test cross-tool portability.

- `survey-paper.html#71-skillmd-as-emerging-standar` — "Antigravity Awesome Skills (v8.6.0, March 2026) bundles 1,300+ skills with official contributions from Anthropic, Vercel Labs, OpenAI, Supabase, Microsoft, Google DeepMind, Sentry, Trail of Bits, Expo, and Hugging Face." — 1,300+ skill count and institutional contributor list presented as fact without a cited source. — Fix: Cite the Antigravity repository or release notes with an accessed date.

- `survey-paper.html#10-conclusion` — "Current evidence suggests these challenges remain largely unresolved." — Assertive closing claim; acceptable but could be hedged further.

## Tone Issues

- `survey-paper.html#abstract` — "the field of agentic large language models underwent four structural shifts that collectively outpace the framing of existing surveys." — "outpace the framing" is a mildly rhetorical characterization that positions the survey as corrective. — Fix: "the field of agentic large language models underwent four structural shifts that are not fully captured by the framing of prior surveys."

- `survey-paper.html#1-introduction` — "the rapid evolution of agentic large language models has introduced new paradigms and challenges. This necessitates an updated framework to comprehensively address the expanded scope and complexity of the field." — "comprehensively" is a mild overreach for what the paper actually does (28 papers, stated to be non-comprehensive in §2.3). — Fix: "suggests the value of an updated framework to address the expanded scope of the field."

- `survey-paper.html#85-finding-5-security-is-archi` — "Prompt injection is characterized as a first-class vulnerability, indicating a need for architectural mitigation over ad-hoc filtering." — "ad-hoc filtering" carries a mild pejorative edge. — Fix: Use "input-filtering approaches" instead of "ad-hoc filtering."

- `survey-paper.html#62-defense-failure` — "The consistent ineffectiveness of these tested defense mechanisms under adaptive attacks suggests a need for architectural mitigation strategies for prompt injection, moving beyond approaches primarily focused on input filtering." — This is well-hedged; no issue.

- `survey-paper.html#86-research-agenda` — "provides the conceptual architecture; the implementation presents an engineering challenge." — Slightly editorial but acceptable.

## Priority Fixes

1. Fix the methodology date contradiction in §2.1 ("November 2023 through March 2024" / "February–March 2024") that directly contradicts the stated January 2025–March 2026 scope of the survey.
2. Disclose Anthropic authorship of sources used for the headline 60/20 paradox (§4.3) and the "industry estimates ARR in the billions" claim (§1.1 / §4), and either triangulate with independent sources or frame as vendor self-reports.
3. Add explicit source citations for uncited statistics: GitHub star counts (§1.1), 1,300+ Antigravity skills count (§7.1), and page-count claims for cited surveys (§2.3).
4. Hedge the extraordinary effect sizes from Drammeh [16] (80× / 140× improvements) in §5.3, which are currently presented as neutral findings from a single-author preprint.
5. Depersonalize "we/our" authorial voice in the abstract, §1.2, and §9.

## Overall Assessment

**B.** The paper is quantitatively grounded, well-structured, and generally careful in its register. The register concerns are modest (a cluster of "we/our" statements, no second-person address). The more material issues are scholastic: the methodology date window contradicts the scope, multiple headline claims rest on an Anthropic-authored industry report used as neutral evidence, a key vendor-comparative security claim favors Claude Code without an articulated evaluation framework, and several statistics lack citations. These are fixable with sourcing and disclosure changes but are not cosmetic.

## Fixes Applied (2026-04-20)

- `survey-paper.html#abstract` — "We synthesize 28 papers…propose a research agenda…" → "This survey synthesizes 28 papers…proposes a research agenda…"
- `survey-paper.html#abstract` — "four structural shifts that collectively outpace the framing of existing surveys" → "four structural shifts that are not fully captured by the framing of prior surveys"
- `survey-paper.html#12-why-a-fourth-axis` — "We additionally identify a cross-cutting layer" → "An additional cross-cutting layer is identified"
- `survey-paper.html#1-introduction` — "This necessitates an updated framework to comprehensively address the expanded scope and complexity of the field." → "This suggests the value of an updated framework to address the expanded scope of the field."
- `survey-paper.html#21-paper-selection` — Methodology date typo "November 2023 through March 2024" → "January 2025 through March 2026" (matches stated scope)
- `survey-paper.html#21-paper-selection` — "6 additional papers published in February–March 2024" → "…February–March 2026"
- `survey-paper.html#11-four-shifts` — "(industry estimates project ARR in the billions…[33])" → "(Anthropic's 2026 Agentic Coding Trends Report estimates ARR in the billions…[33])"
- `survey-paper.html#43-the-6020-paradox` — "Anthropic's 2026 Agentic Coding Trends Report documents…" → "According to Anthropic's 2026 Agentic Coding Trends Report — a vendor-authored self-report — engineers…"
- `survey-paper.html#65-the-security-capability-tra` — "Claude Code achieves the lowest vulnerability rating (Low)…Cursor rates Critical…" → "on the vulnerability rubric defined in [18], Claude Code receives the lowest rating (Low)…Cursor is rated Critical…"
- `survey-paper.html#53-orchestration-evidence` — Rewrote to attribute to a single study [16] and flag that the 80×/140× effect sizes are not independently replicated
- `survey-paper.html#71-skillmd-as-emerging-standar` — "…operate across Claude Code, Gemini CLI, Cursor, Codex CLI, and four other tools without modification [28, 29]." → hedged with "their sources claim to operate across…"
- `survey-paper.html#9-limitations` — Three "we/our" instances depersonalized ("We read 28 papers…" → "This survey covers…"; "Our industry source analysis…" → "The industry source analysis…"; "Our security analysis…" → "The security analysis…")
- `survey-paper.html#85-finding-5-security-is-archi` — "ad-hoc filtering" → "input-filtering approaches"

## Fixes Skipped (2026-04-20)

- `survey-paper.html#11-four-shifts` — GitHub star counts (96K+ / 100K+) and uncited page-count claims — require new URL/dated citations not available to this pass.
- `survey-paper.html#71-skillmd-as-emerging-standar` — Antigravity Awesome Skills "1,300+ skills" and institutional contributor list — needs cited source to Antigravity repo/release notes.
- `survey-paper.html#41-the-benchmark-reality-check` — Specific model-name disambiguation for "best-performing frontier model" — requires consulting the original paper to identify model names.
- `survey-paper.html#52-governance` / `#51-the-protocol-stack` — Uncited "often considered critical for enterprise adoption" assertion and uncited MCP/A2A origin attributions — need either citations or removal; judgment deferred.
- `survey-paper.html#23-what-this-survey-is-not` — Page counts / "500+ works" for cited surveys — verifiable from ref [2] but needs manual check.
