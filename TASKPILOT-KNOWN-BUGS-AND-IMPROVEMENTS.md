# TaskPilot — Known Bugs and Improvements

## Active Items

### [IMPROVEMENT] 14 skills have vague exit criteria (64% pass rate)
**Severity:** P2
**What happened:** Exit criteria validator (v0.4.0) detected 14 of 39 skills with criteria lacking measurable assertion verbs. Examples: "P95 latency within SLO threshold" (no specific threshold), "Breaking changes called out explicitly" (no artifact verification).
**Expected behavior:** All exit criteria should pass the exit_criteria_validator with measurable patterns.
**Suggested fix:** Rewrite failing criteria to include explicit thresholds, artifact names, or binary predicates. Target: >= 90% pass rate.
**Found in phase:** PHASE 4 (TEST — v0.4.0 exit criteria validation)

### [IMPROVEMENT] 4 of 20 MAST failure modes uncovered by simulations
**Severity:** P2
**What happened:** FailureMode enum defines 20 modes. 16 are exercised by SIM_001-SIM_011. Missing: hallucination, infinite_loop, context_loss, tool_misuse (the original MAST canonical modes that no scenario exercises).
**Expected behavior:** All 20 defined failure modes should have at least one scenario.
**Suggested fix:** Add SIM_012 (hallucination) and SIM_013 (tool_misuse) in v0.5.0.
**Found in phase:** PHASE 4 (TEST — v0.4.0 MAST coverage = 0.80 = 16/20)

### [IMPROVEMENT] Event chain tracing not yet validated at runtime
**Severity:** P3
**What happened:** `caused_by_event_id` field added to event emissions (PATTERN_037), but no runtime enforcement validates that the field is populated correctly.
**Expected behavior:** Every gate_blocked event should have a caused_by_event_id linking to the triggering failure event.
**Suggested fix:** Add validation in simulation harness or event bus to verify cause chains.
**Found in phase:** PHASE 3 (BUILD — v0.4.0 orchestration graph)

## Resolved Items (v0.4.0 — 2026-03-10)

### [RESOLVED] BUG-005 — Simulation harness naive string matching
**Original severity:** P3
**Resolution:** Replaced `_is_failure_detected()` with `StructuredOutcomeValidator` class using `FailureMode` enum (20 modes), `DetectionVerdict` enum, and `DetectionAssertion` dataclass. Validation now checks detector role + skill against skill catalog exit criteria instead of substring matching. All 11 scenarios pass with structured validation.
**Resolved in:** v0.4.0, PHASE 3

### [RESOLVED] BUG-006 — No binary exit criteria validation
**Original severity:** P3
**Resolution:** Created `exit_criteria_validator.py` with 18 measurable patterns (regex) and 7 vague word patterns. Validator scans all skills/*.yaml and reports pass rate. Current pass rate: 64.10% (25/39 valid). Validator works correctly — failing criteria are genuinely vague and flagged for improvement.
**Resolved in:** v0.4.0, PHASE 3

### [RESOLVED] Memory system is query-by-filter only — no semantic search
**Original severity:** P2
**Resolution:** Created `memory_search.py` with BM25 keyword search (k1=1.5, b=0.75) over JSONL event logs. Pure Python, zero dependencies. Searches over `rationale`, `notes`, `finding`, `description` fields.
**Resolved in:** v0.4.0, PHASE 3

### [RESOLVED] 6 of 14 MAST failure modes not yet in simulations
**Original severity:** P2
**Resolution:** MAST coverage expanded from 10/14 to 16/20 (expanded taxonomy). Added SIM_010 (reward_hacking) and SIM_011 (verification_gaming). Extended FailureMode enum to 20 modes.
**Resolved in:** v0.4.0, PHASE 3

## Resolved Items (v0.2.0 — 2026-03-10)

### [RESOLVED] SEC skill gap in key rotation auditing
**Original severity:** P2
**Resolution:** Added key lifecycle audit to SKILL_SEC_DATA_HANDLING exit criteria. SIM_005 now fully detected. SIM_006 added for partial re-encryption variant.
**Resolved in:** v0.2.0, PHASE 3

### [RESOLVED] Extended role skills need deeper exit criteria
**Original severity:** P2
**Resolution:** All 9 extended role skills now have 4+ binary, verifiable exit criteria. skill_completion_rate: 0.83→0.93.
**Resolved in:** v0.2.0, PHASE 3

### [RESOLVED] defect_detection_rate below threshold (0.80 vs 0.85)
**Original severity:** P1
**Resolution:** Enhanced SEC skills + expanded simulation suite (5→7). defect_detection_rate: 0.80→1.00. defect_escape_rate: 0.20→0.00.
**Resolved in:** v0.2.0, PHASE 3+4

### [RESOLVED] No persistent memory across cycles
**Original severity:** P2
**Resolution:** Implemented JSONL event store with bi-temporal timestamps. MEMORY_CONSULT state added to orchestration graph.
**Resolved in:** v0.2.0, PHASE 3
