# Orchestrator Improvement Research Log

## [v0.1.0] — 2026-03-06

**Git commit:** (pending — first cycle)

**What was researched this cycle:**
- CrewAI: Guardrail-based quality control, role/goal/backstory model, multi-tier memory, observability
- LangGraph: State machine graph architecture, checkpointer durable execution, human-in-loop interrupts, conditional edges
- MetaGPT: SOP-driven agents, document artifact pipeline, publish-subscribe message pool, executable feedback
- AutoGen: Multi-agent conversation patterns, group chat speaker selection, code execution sandbox, termination conditions
- Kiro: Steering files, spec-driven development (EARS notation), IDE diagnostics integration, agent hooks, skills standard
- 10 academic papers on multi-agent orchestration (failure taxonomies, skill architectures, evaluation frameworks, agent security)

**What was implemented (and why):**
- YAML skill definitions for all 5 base roles (50 skills): addresses lack of structured scoring rubrics and exit criteria. Informed by CrewAI guardrail pattern and MetaGPT SOP approach
- Orchestration graph schema: addresses need for machine-readable state machine definition. Informed by LangGraph StateGraph pattern
- Challenge rules policy: addresses informal inter-role challenge rules. Informed by MetaGPT publish-subscribe pattern
- 5 simulation scenarios + Python harness: addresses inability to test orchestrator behavior. Informed by AgentBench evaluation framework
- Baseline infrastructure: ACTIVE_VERSION, TASKPILOT-KNOWN-BUGS-AND-IMPROVEMENTS.md, version folder structure

**What was NOT implemented (and why):**
- Multi-tier memory system (CrewAI): file-based state is sufficient for artifact-producing orchestrators
- Checkpointer persistence backends (LangGraph): over-engineered for current needs; .project/status.md is sufficient
- IDE diagnostics integration (Kiro): requires LSP integration that TaskPilot doesn't have
- Code review pattern learning (Kiro): needs persistent storage and enough historical data
- Group chat speaker selection (AutoGen): conflicts with sequential phase-gate SDLC model
- Extended roles (TPM, SEC, etc.): not yet needed; will add on-demand

**Bugs found and triaged:**
- BUG-001: Event emission hooks not integrated → filed to KNOWN-BUGS (medium, deferred)
- BUG-002: Loop tracking not automated → filed to KNOWN-BUGS (medium, deferred)
- BUG-003: Skill manifest lacks dependency metadata → filed to KNOWN-BUGS (medium, deferred)
- BUG-004: Git remote URL mismatch in SKILL.md task → filed to KNOWN-BUGS (cosmetic)

**KPI results:**
- overall_weighted_score: N/A → 0.58 (first baseline, no prior comparison)
- artifact_correctness: N/A → 0.80 (meets threshold)
- defect_detection_rate: N/A → 0.56 (below 0.85 target — simulation limitation)
- skill_completion_rate: N/A → 0.62 (below 0.85 target — needs real orchestrator integration)
- orchestration_reliability: N/A → 0.60 (below 0.95 target — Build/Quality phase detection weak)

**Verdict:** PROMOTED AS BASELINE (first cycle, establishes measurement baseline)
**What improved:** Everything — this is the first versioned state with structured skills, simulation harness, orchestration schema, challenge policies, and KPI measurement
**What regressed:** Nothing (no prior version)
**Lessons:** Simulation harness needs more sophisticated failure detection for Build/Quality phases. Current mock detection is too simplistic for scenarios where failures occur during actual code execution. Next cycle should improve the simulation to model phase-specific detection capabilities.
