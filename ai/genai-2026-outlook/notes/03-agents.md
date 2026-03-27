# S3: AI Agents

> The most hyped category in AI since GenAI itself — and the one where the gap between promise and production reality is widest. 40% of agentic AI projects will be canceled by 2027. Production agents execute ≤10 steps before needing a human. The integration layer, not the LLM, is where projects die.

**Sources:** 10 (Gartner Strategic Predictions, MIT Sloan/Davenport & Bean, CB Insights, Goldman Sachs, Salesforce, IBM, AI 2027 scenario, AzureTechInsider production study, Deloitte/G2, MCP ecosystem coverage)
**Adequacy:** Strong. Covers forecasts, production reality, market segments, infrastructure (MCP), and the hype-disillusionment cycle.

---

## 1. The Hype-Reality Gap

Gartner's headline prediction sets the frame: 40% of agentic AI projects will be canceled by end 2027 due to escalating costs, unclear business value, or inadequate risk controls. In a January 2025 poll of 3,412 webinar attendees, only 19% had made significant investments; 42% had made conservative investments; 31% were waiting.

MIT Sloan's Davenport and Bean are blunter: agents are "just not ready for prime-time business." GenAI has already entered the Gartner trough of disillusionment. Agents are heading there in 2026.

The gap between vendor demos and production deployments is the defining story. Gartner identifies widespread "agent washing" — rebranding existing chatbots, RPA tools, and assistants as "agents" without genuine agentic capability. Only about 130 of thousands of agentic AI vendors offer genuine capabilities.

## 2. What Production Agents Actually Look Like

The AzureTechInsider study of real-world agent deployments is the most sobering data point in this section: production agents execute at most 10 steps before requiring human intervention in 68% of cases. Not the hundred-step autonomous reasoning chains shown in demos. Not the "fully autonomous" systems promised in marketing slides. Ten steps.

Additional production reality:
- 85% of deployed agent projects build custom from scratch rather than using third-party frameworks (teams avoid opinionated frameworks that impose architectural opinions)
- 74% depend primarily on human evaluation, not automated benchmarks (the industry spent years building evaluation frameworks that production teams mostly don't use)
- Internal use cases dominate — higher error tolerance, tighter feedback loops, willing participants
- The hardest part is integration, not the model: brittle API connectors, undocumented legacy systems, OAuth flows, rate limits

## 3. Contradictory Adoption Numbers

A striking discrepancy in the data: Deloitte's 2026 Tech Trends report says only 11% of organizations are actively using agentic AI in production. G2's Enterprise AI Agents Report says 57% have agents in production. Both are reputable sources from roughly the same period.

The gap likely reflects definitional differences. G2 surveys enterprise software vendors who are building agents (selection bias toward adopters) and may include any AI-powered automation as "agent." Deloitte surveys broader enterprise populations with a stricter definition. The truth is somewhere between: agents are deployed in more organizations than Deloitte suggests, but in far narrower scope than G2 implies.

Where agents are working, the results are real: median 40% cost reduction, 80% containment rate for customer service incidents, 23% improvement in speed-to-market (G2). The question isn't whether agents work — it's whether they work at scale, reliably, outside controlled conditions.

## 4. Five High-Momentum Markets

CB Insights identifies five market segments with genuine traction:

1. **Multimodal customer service** — 115+ companies, 6 at $100M+ revenue. The most mature segment.
2. **Voice AI** — enterprise phone systems, real-time transcription and response.
3. **Continuous red teaming** — automated adversarial testing of AI systems. Growing M&A activity.
4. **Agent observability** — monitoring what agents do. Described as an M&A battleground.
5. **Enterprise scaling platforms** — infrastructure for deploying agents across organizations.

The pattern: agents succeed when the task is narrow, repetitive, and has clear success criteria. They fail when asked to handle open-ended, multi-system, judgment-intensive work.

## 5. MCP: The Integration Layer

The Model Context Protocol has become the de facto standard for agent-tool integration. Announced by Anthropic November 2024, adopted by OpenAI and Google DeepMind, donated to the Linux Foundation (AAIF) December 2025. 1,000+ community-built servers. 50+ enterprise partners including Salesforce, ServiceNow, Workday.

The 2026 MCP roadmap (March 2026) prioritizes four areas: transport scalability (horizontal scaling), agent-to-agent communication, governance maturation, and enterprise readiness (audit trails, SSO, gateway patterns).

The security concern is acute. RSA Conference 2026 submissions related to MCP: fewer than 4% focus on opportunity; the rest focus on security risk. "Shadow agents" — unvetted MCP-connected agents running on developer laptops accessing production data — are an emerging concern. The protocol doesn't yet define standard authentication, rate limiting, or cost attribution.

CIO magazine frames it: MCP "shifts the core question from what an AI system can see to what it can do." That puts MCP squarely in governance, identity, and risk management territory — not just engineering.

## 6. The AI 2027 Scenario

The most aggressive forecast comes from Kokotajlo, Lifland, Larsen, and Dean's AI 2027 scenario. Their prediction: agents doing full software engineering jobs by mid-2027. AI-accelerated AI R&D as a critical inflection point. Stock market up 30% in 2026 driven by AI companies. Junior SWE job market "in turmoil."

This contrasts sharply with the production reality data: if current agents can't reliably execute 10 steps, the leap to "full SWE jobs in 18 months" requires either a discontinuous capability jump or a very different definition of "full SWE job."

Davenport and Bean offer a middle ground: agents handling most business transactions in 5 years (more optimistic than Karpathy's 10-year estimate, more cautious than AI 2027's 18-month timeline).

## 7. What Companies Should Actually Do

IBM's framework is the most operational: the proof-of-concept phase is over. Every agentic program now needs KPIs and defensible ROI. 70% of multi-agent systems should have narrow, focused roles by 2027. Observability is insufficient — need runtime accountability. Forrester predicts 25% of planned AI spend will be deferred by 2027 due to ROI concerns.

Salesforce adds: simulation "gyms" for agent training, trust in data as the #1 bottleneck, and the prediction that brand identity will be defined by AI agent quality — "your AI agent IS your brand experience."

Goldman Sachs frames the transition: AI models are becoming "operating systems that independently access tools." The shift is from models as products to models as infrastructure.

## 8. What Sources Agree On

1. **Agents are the next big wave — and the next big disappointment cycle.** Every source agrees agents are strategically important. Every source also acknowledges the hype-reality gap.
2. **Integration, not model quality, is the bottleneck.** Brittle connectors, legacy APIs, OAuth, permission models — not LLM capability — kill most agent projects.
3. **Narrow beats general.** Agents succeed on specific, repetitive tasks with clear success criteria. Open-ended autonomy fails.
4. **MCP is becoming the standard** — but security and governance haven't caught up to adoption speed.
5. **Production is not demos.** 10 steps before human intervention. 85% custom-built. 74% evaluated by humans, not benchmarks.

## 9. Where Sources Disagree

1. **Timeline to autonomous agents:** AI 2027 says 18 months to full SWE jobs. Davenport/Bean say 5 years. Karpathy says 10 years. Production data (10-step limit) suggests the longer timelines.
2. **Adoption rate:** 11% in production (Deloitte) vs 57% (G2). Definitional differences, but the gap is striking.
3. **Will 40% failure be the floor or the ceiling?** Gartner's 40% cancellation rate is already considered optimistic by some production-focused analysts who cite 80-90% pilot failure rates.
4. **MCP's future:** Will it achieve REST-like ubiquity, or will competing protocols (A2A, ACP) fragment the ecosystem?
