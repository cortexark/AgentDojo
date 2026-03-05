# Orchestration Metrics & Interaction Tracking

**Project:** OAuth2 Social Login Feature  
**Tracking Period:** 2026-03-03 → 2026-05-31 (Phases 1-9)  
**Framework:** Measures coordination effectiveness, cross-domain handoffs, and skill interaction quality  

---

## Orchestration Interaction Model

### Interaction Types

| Type | Definition | Example |
|------|-----------|---------|
| **Skill Invocation** | One skill calls another or reads its output | PM prd-generator reads PM gaps output |
| **Cross-Domain Handoff** | Output from one domain feeds input to another | UX components → SDE requirements |
| **Intra-Domain Loop** | Skill within same domain loops back | PM gap-analyst → PM research-agent |
| **Inter-Domain Loop** | Defect/issue routes across domains | QAE defect → SDE debugging |
| **Decision Gate** | Gating condition blocks/allows phase advance | Phase 2→3 gate: experiments SHIP? |
| **Async Dependency** | Output used by multiple downstream skills | PM PRD read by UX, SDE, QAE |

---

## Metrics Framework

### 1. Interaction Density (IxD)
**Definition:** Number of meaningful skill interactions per phase  
**Formula:** Total Skill-to-Skill Interactions / Phase Duration (days)  
**Target:** 1.5-2.5 interactions/day (efficiency + quality balance)  
**Interpretation:**
- <1.0: Under-orchestrated (phases execute in silos)
- 1.5-2.5: Optimal (tight coordination)
- >3.0: Over-orchestrated (excessive back-and-forth, coordination overhead)

### 2. Handoff Quality (HQ)
**Definition:** % of outputs that successfully feed next phase inputs  
**Formula:** (Successful Handoffs / Total Handoffs) × 100  
**Target:** >95% (minimal re-work on handoff failures)  
**Tracking:**
- Handoff successful: Input requirements met, no surprises in next phase
- Handoff failed: Missing data, format mismatch, requirement gap detected
- Partial: Mostly successful but required clarifications

### 3. Loop Ratio (LR)
**Definition:** Feedback loops per phase (should be minimal)  
**Formula:** Total Loops / Total Phases  
**Target:** <0.5 loops/phase (avg <1 loop in 9 phases)  
**Interpretation:**
- 0 loops: Perfect execution (rare, suspicious?)
- 0.5-1.0: Healthy (some rework expected)
- 1.5+: Coordination issues (needs investigation)

### 4. Phase Gate Performance (PGP)
**Definition:** % of phases that advance without gate violations  
**Formula:** (Phases Meeting All Gates / Total Phases) × 100  
**Target:** 100% (gates prevent downstream failures)  
**Tracking:** Did previous phase outputs meet minimum quality for next phase?

### 5. Cross-Domain Coordination Index (CDCI)
**Definition:** Quality of handoffs across PM↔UX↔SDE↔QAE↔PE  
**Formula:** Σ(Handoff Quality per Domain Pair)  
**Target:** All domain pairs >90% handoff quality  
**Key Pairs:**
- PM → UX: Requirements clarity (PRD specifies design needs?)
- UX → SDE: Specification completeness (design specs match code?)
- SDE → QAE: Test coverage (code coverage matches strategy?)
- QAE → PE: Quality metrics (defects tracked for reliability review?)

### 6. Skill Utilization Efficiency (SUE)
**Definition:** Are the right skills being invoked at the right time?  
**Formula:** (Expected Skills Used / Actual Skills Invoked) × 100  
**Target:** 95-105% (allows for optional conditional skills)  
**Interpretation:**
- >110%: Extra skills invoked (possibly unnecessary work)
- 95-105%: Optimal (follows plan with minor flexibility)
- <90%: Skipped critical skills (risk of downstream failures)

### 7. Time-to-Value (TtV)
**Definition:** How long from project start to feature in production  
**Formula:** Phase 8 completion date - Phase 1 start date  
**Target:** <120 days for OAuth2 feature  
**Breakdown:** Track per-phase duration to identify bottlenecks

---

## Tracking Checklist: Every Phase

After EACH phase completion, record:

- [ ] **Phase Name & Duration** — e.g., "Phase 3: Planning (7 days)"
- [ ] **Skills Executed** — list all skills invoked
- [ ] **Interactions Recorded** — count skill-to-skill references
- [ ] **Handoffs Completed** — track domain transitions
- [ ] **Loops Encountered** — any rework? Why?
- [ ] **Decision Gates** — did outputs meet next phase requirements?
- [ ] **Blockers/Issues** — what slowed coordination?
- [ ] **Quality Assessment** — are outputs production-ready?

---

## Phase-by-Phase Tracking Template

### Phase [N]: [Name]

**Start Date:** [Date]  
**End Date:** [Date]  
**Duration:** [Days]  

#### Skills Executed
| Step | Skill | Status | Notes |
|------|-------|--------|-------|
| N.1 | `/[skill-name]` | ✅/⏳/❌ | [Notes] |

#### Interactions
| From | To | Type | Data Flow | Quality |
|------|-----|------|----------|---------|
| [Skill A] | [Skill B] | Handoff/Loop/Dependency | [Files shared] | Good/Partial/Failed |

#### Decision Gates
| Gate | Criteria | Result | Action |
|------|----------|--------|--------|
| [Name] | [Requirement] | Pass/Fail/Warn | [Decision] |

#### Loop Count
| From | To | Reason | Count | Status |
|------|-----|--------|-------|--------|

#### Metrics
- Interaction Density: [X] interactions/day
- Handoff Quality: [X]% successful
- Phase Gate Performance: [Pass/Warn/Fail]

#### Observations
- [What worked well?]
- [What was challenging?]
- [Any coordination failures?]

---

## Expected Baseline (Phases 1-2 Completed)

From our Phase 1-2 execution:

| Metric | Phase 1 | Phase 2 | Combined |
|--------|--------|--------|----------|
| Interaction Density | 0.8/day | 1.2/day | 1.0/day |
| Handoff Quality | 100% | 100% | 100% |
| Loop Ratio | 0 loops | 0 loops | 0/2 = 0 loops/phase |
| Phase Gate Performance | ✅ Pass | ✅ Pass | 100% |
| Cross-Domain CDCI | PM only | PM+PE | ~95% (both experiments SHIP) |
| Skill Utilization | 100% | 100% | 100% |

**Observation:** Phase 1-2 execution was optimal — clean discovery, validated assumptions, zero loops, perfect handoff.

**Projection for Phases 3-9:**
- Expected Interaction Density: 1.5-2.0/day (planning/design/build phases more complex)
- Expected Loops: 1-2 total (some rework in design or QA expected)
- Expected Total Duration: 14 weeks (98 days)
- Success Criteria: HQ >95%, PGP 100%, TtV <120 days

---

## Interaction Quality Assessment (Post-Execution)

This section filled in AFTER all 9 phases complete:

### Overall Metrics
- **Total Interactions:** [N] across 9 phases
- **Average Interaction Density:** [X]/day
- **Overall Handoff Quality:** [X]%
- **Total Loops:** [N] (target <1)
- **Phase Gate Violations:** [N] (target 0)
- **Time-to-Value:** [Days] (target <120)

### Domain Pair Quality
- PM ↔ UX: [Quality %] — [Notes]
- UX ↔ SDE: [Quality %] — [Notes]
- SDE ↔ QAE: [Quality %] — [Notes]
- QAE ↔ PE: [Quality %] — [Notes]

### Orchestration Health Assessment
**Excellent (>95%):** Coordination working smoothly, minimal friction  
**Good (85-95%):** Most handoffs clean, some minor clarifications needed  
**Fair (75-85%):** Noticeable delays, some rework loops  
**Poor (<75%):** Significant coordination failures, substantial rework  

---

## Improvement Recommendations (Post-Delivery)

### Based on Observed Gaps:
1. **If IxD too low:** Skills executing too independently, consider adding more cross-checks
2. **If HQ <95%:** Handoff failures indicate missing requirements, improve gate definitions
3. **If Loops >1/phase:** Rework suggests incomplete planning, strengthen earlier phases
4. **If PGP <100%:** Gates not catching issues early enough, make gates stricter
5. **If TtV >120 days:** Bottleneck identification needed, optimize critical path

### Skill Improvements:
- Which skills need better documentation?
- Which skill outputs are frequently misinterpreted?
- Which hand-offs create most friction?
- Could any skills be combined or split?

### Orchestration Rules Refinement:
- Did Rule 4 (Phase Gates) prevent issues?
- Did Rule 6 (Skip/Jump) get misused?
- Should any gates be stricter?
- Should any optional skills become conditional (not optional)?

