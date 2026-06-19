# DS Final Decisions — 8 Papers + Full Code

DECISION: Do NOT ship [Labs] in v0.3.0.
EVIDENCE: Paper 2 (SAST-Genius) explicitly warns that LLMs generating new findings cause FP explosion. Our [Labs] module currently generates additional vulnerability reports beyond SAST flags, and evaluation shows only 1 of 5 agents works reliably (swallowed_exception 3/3). Other agents are blocked by DS API JSON parse errors, indicating systemic instability.
RATIONALE: Shipping a broken, risk-prone module with a known FP explosion risk three days before launch would undermine trust and create negative reviews. We must prioritize reliability over feature breadth. Retire [Labs] from this release; fix and validate it for the next iteration with a confirmation-only design per Paper 2's best practice.

DECISION: Ship v0.3.0 with core pipeline only: 34 rules + Bandit 100+ → ML filter → DS Review (TP/FP) → Auto-fix (10/17 rules) with explicit user opt-in and warning about potential new bugs (per Paper 5).
EVIDENCE: Papers 4 (path feasibility) and 2 (confirmation-only) show that reducing FPs without generating new findings is achievable and safe. The core pipeline already cuts ~40% FPs via ML filter and DS Review. Auto-fix for 10/17 rules can be offered as an opt-in beta, with a clear disclaimer.
RATIONALE: A clean, stable release that delivers tangible value—FP reduction and automated fixes for common issues—is better than a buggy experimental module. This builds credibility for the June 23 launch and sets a foundation for future enhancements.

DECISION: Build ONE thing today: a confirmation-only wrapper for the swallowed_exception agent that converts it from generating new findings to only confirming/rejecting existing SAST flags (aligned with Paper 2). Fix JSON parse errors for other agents later.
EVIDENCE: Paper 1 (QASecClaw) shows specialized multi-agent LLMs can reduce FPs when used correctly. The swallowed_exception agent already works (3/3 confidence 1.0). Paper 2’s warning is about generation, not confirmation.
RATIONALE: Delivering a single validated agent that improves FP reduction without risk demonstrates progress and can be highlighted as a "Labs preview" in the release. Other agents require deeper debugging; deferring them avoids shipping broken code.

DECISION: ProductHunt tagline: "Open-source Python SAST scanner with AI-powered false positive reduction and safe auto-fix."
EVIDENCE: The core value proposition—reducing noise from SAST tools and enabling automated remediation—is directly supported by Papers 1, 2, 4, and 5. Avoid claiming "multi-agent LLM" until [Labs] is stable.
RATIONALE: Honest, clear positioning builds trust. Mentions "AI-powered" (ML filter + DS Review) without overpromising on experimental features. Include a tag for "safe auto-fix" with disclaimer.

DECISION: Long-term roadmap ranking (highest to lowest priority):
1. Fine-tune small local models for high-recall CWE detection (Papers 6, 8) – outperforms prompting, privacy-preserving.
2. Integrate path feasibility analysis (Paper 4) – directly cuts FPs by ~40%.
3. Develop agentic secure code review for pre-commit detection of partial API misuse (Paper 7) – catches what SAST misses.
4. Build secure auto-fix pipeline with self-validation loop (Paper 5) – fixes without introducing new bugs.
5. Enhance LLM false positive reduction with confirmation-only multi-agent system (Papers 1, 2) – after fine-tuning and validation.
EVIDENCE: Papers 8 and 6 show fine-tuning beats prompting; Paper 4 offers immediate FP reduction; Paper 7 expands coverage; Paper 5 enables safe repair; Paper 1/2 refine the FP reduction approach after foundational improvements.
RATIONALE: This sequence maximizes impact while minimizing risk. Start with local models (privacy, reliability), then add deterministic FP reduction, then expand coverage, then automate fixes, then reintroduce LLM agents only when robust.