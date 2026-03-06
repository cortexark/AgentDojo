# TaskPilot Known Bugs and Improvements

## Active Issues

### [FIX-NEXT] BUG-001: Event emission hooks not integrated
- **Severity:** Medium
- **Description:** hooks.json defines event structure but event emission is not integrated with Claude Code execution
- **Impact:** Cannot track skill execution events automatically; relies on manual logging
- **Suggested fix:** Implement hook triggers that emit events to .project/events.jsonl on skill completion

### [FIX-NEXT] BUG-002: Loop tracking not automated
- **Severity:** Medium
- **Description:** .project/loops.md format is defined but not auto-populated when loops occur
- **Impact:** Loop data must be manually recorded; easy to miss loops in long orchestration runs
- **Suggested fix:** Add loop counter to orchestrator state, auto-append to loops.md on each iteration

### [FIX-NEXT] BUG-003: Skill manifest lacks dependency metadata
- **Severity:** Medium
- **Description:** skill-manifest.json exists but individual markdown skills don't reference it or declare dependencies
- **Impact:** Cannot validate skill prerequisite chains automatically
- **Suggested fix:** Add YAML frontmatter to each skill .md file with `depends_on` and `produces` fields

### [IMPROVE] IMP-001: No structured skill scoring
- **Severity:** Low (addressed in v0.1.0)
- **Description:** Skills are prose-based markdown with no machine-readable scoring rubrics or exit criteria
- **Status:** ADDRESSED in v0.1.0 — YAML skill definitions created with scoring rubrics and exit criteria

### [IMPROVE] IMP-002: No simulation or testing framework
- **Severity:** Medium (addressed in v0.1.0)
- **Description:** Cannot test orchestrator behavior against failure scenarios
- **Status:** ADDRESSED in v0.1.0 — Simulation harness created with 5 scenarios

### [IMPROVE] IMP-003: No version isolation
- **Severity:** High (addressed in v0.1.0)
- **Description:** No ACTIVE_VERSION file, no versioned folders for experiments
- **Status:** ADDRESSED in v0.1.0 — ACTIVE_VERSION and v0.1.0/ folder created

### [RESEARCH] RES-001: Phase 7+ end-to-end testing not validated
- **Severity:** Medium
- **Description:** HeartCoach build tested Phases 1-6; Phase 7+ not yet validated with fixes
- **Suggested action:** Run full orchestration with simulation harness to validate Phase 7-9 behavior

### [RESEARCH] RES-002: Extended roles not defined
- **Severity:** Low
- **Description:** Only 5 base roles exist. SKILL.md task spec calls for 8 extended roles (TPM, SEC, PRIV, DATA, RM, SRE, DOC, SUPPORT)
- **Suggested action:** Define extended roles when orchestrator needs them (on-demand creation)

## Resolved Issues
- None yet (first cycle)
