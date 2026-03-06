# Cycle Plan — v0.1.0 (2026-03-06)

## Baseline: v0.0.0 (initial state, no versioning)

## Priority List (max 5 items)

### 1. [FIX-NOW] Create baseline infrastructure
- **Problem:** No ACTIVE_VERSION, no bugs file, no version isolation, no improvement history
- **Action:** Create ACTIVE_VERSION pointer, TASKPILOT-KNOWN-BUGS-AND-IMPROVEMENTS.md, v0.1.0 folder structure
- **KPI impact:** Enables all future KPI measurement (prerequisite)

### 2. [IMPROVE] Add YAML skill definitions with exit criteria
- **Problem:** Skills are markdown files with no structured scoring rubrics, exit criteria, or test hooks. Cannot measure skill_completion_rate KPI
- **Action:** Create YAML skill definitions for all 5 base roles (50 skills) with scoring_rubric, exit_criteria, anti_patterns, test_hooks
- **KPI impact:** skill_completion_rate (new metric, target ≥ 0.85), artifact_correctness (enables measurement)
- **Research-backed:** Informed by CrewAI guardrail pattern (PATTERN_006) and MetaGPT SOP-driven approach (PATTERN_METAGPT_001)

### 3. [IMPROVE] Create simulation harness
- **Problem:** No way to test orchestrator behavior against failure scenarios. Cannot measure defect_detection_rate, defect_escape_rate, or orchestration_reliability
- **Action:** Build YAML scenario files (5 scenarios) + Python simulation runner with KPI computation
- **KPI impact:** Enables measurement of defect_detection_rate, defect_escape_rate, test_coverage, orchestration_reliability
- **Research-backed:** Informed by AgentBench evaluation framework (Paper #10) and LangGraph checkpoint pattern (PATTERN_015)

### 4. [IMPROVE] Add challenge rules policy
- **Problem:** Inter-role challenges described in SKILL.md but not formalized in machine-readable format
- **Action:** Create policies/challenge_rules.yaml with triggers, evidence, SLA, escalation
- **KPI impact:** human_intervention_rate (target ≤ 0.15), defect_escape_rate (target ≤ 0.10)
- **Research-backed:** Informed by MetaGPT publish-subscribe pattern (PATTERN_METAGPT_003) and multi-agent failure taxonomy (Paper #1)

### 5. [IMPROVE] Add orchestration graph schema
- **Problem:** State machine exists in SKILL.md prose but not in structured, machine-readable format
- **Action:** Create schemas/orchestration_graph.yaml with entity definitions, state transitions, checkpoint specs
- **KPI impact:** orchestration_reliability (target ≥ 0.95), time_to_go_no_go_min (target ≤ 30)
- **Research-backed:** Informed by LangGraph state machine (PATTERN_013) and TEA Protocol (Paper #7)

## Items NOT addressed this cycle
- Extended roles (TPM, SEC, PRIV, DATA, RM, SRE, DOC, SUPPORT) — deferred to v0.2.0
- Event emission hooks integration — deferred, routing engine not needed per current assessment
- Loop tracking automation — deferred, manual tracking via .project/loops.md is sufficient for now
- Skill manifest dependency metadata — deferred to v0.2.0
- End-to-end Phase 7+ testing — requires simulation harness first (built this cycle)
