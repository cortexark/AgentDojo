# 🎯 COMPREHENSIVE TEST SCENARIO: Multi-Hop Feature Build

**Objective:** Build a new "User Authentication" feature from discovery through release  
**Expected Hops:** 12+ skill transitions across 5 domains  
**Intra-Domain Loops:** 2 (code-review severity, accessibility WCAG)  
**Inter-Domain Loops:** 1 (HIGH severity defect)  
**Total Phases:** 9 (Discovery → Feedback)

---

## 📋 Use Case: User Authentication Feature

**Feature:** Add OAuth2 social login (Google, GitHub)  
**Scope:** Web app + mobile  
**Timeline:** Q2 2026

---

## 🎬 EXECUTION FLOW WITH COORDINATION

```
START: /master-orchestrator [goal: build oauth-feature]
  |
  ├─── PHASE 1: DISCOVERY
  |     └─ Run: /pm:research-agent [oauth market analysis]
  |        Output: .pm/competitors/oauth-analysis.md
  |        Status: PASS
  |        ↓
  |     Next: /pm:gap-analyst
  |
  ├─── PHASE 2: VALIDATION
  |     └─ Run: /pm:gap-analyst [analyze oauth gaps]
  |        Output: .pm/gaps/2026-03-03-oauth-gaps.md
  |        Quality Gates: 
  |          ✅ evidence_required: YES
  |          ✅ user_confirmation: YES
  |        Status: PASS
  |        ↓
  |     Routing: gap-analyst PASS → prd-generator
  |
  ├─── PHASE 3: PLANNING
  |     ├─ Run: /pm:prd-generator [write OAuth spec]
  |     |  Output: .pm/prds/oauth-login.md
  |     |  Quality Gates:
  |     |    ✅ structure_complete: YES
  |     |    ✅ user_review: APPROVED
  |     |  Status: PASS
  |     |  ↓
  |     | Routing: prd-generator PASS → ux:design-system
  |     |
  |     └─ Optional: /pm:discovery-validator [validate assumptions]
  |        (skipped: requirements clear)
  |
  ├─── PHASE 4: DESIGN
  |     ├─ Run: /ux:design-system [OAuth tokens, flows]
  |     |  Output: .ux/design-systems/oauth-tokens.md
  |     |  Quality Gates:
  |     |    ✅ tokens_defined: YES
  |     |  Status: PASS
  |     |  ↓
  |     | Routes to: color-system, typography, component-design (parallel)
  |     |
  |     ├─ Run: /ux:color-system [OAuth button colors]
  |     |  Status: PASS → component-design
  |     |
  |     ├─ Run: /ux:typography [Login form typography]
  |     |  Status: PASS → component-design
  |     |
  |     ├─ Run: /ux:component-design [Login form, OAuth buttons]
  |     |  Output: .ux/components/oauth-form.md
  |     |  Quality Gates:
  |     |    ✅ all_states_specified: 
  |     |       • default
  |     |       • hover
  |     |       • active
  |     |       • loading
  |     |       • error
  |     |       • disabled
  |     |  Status: PASS
  |     |  ↓
  |     | Routes to: interaction-design
  |     |
  |     ├─ Run: /ux:interaction-design [OAuth flow animations]
  |     |  Output: .ux/interactions/oauth-transitions.md
  |     |  Quality Gates:
  |     |    ✅ motion_specs_complete: YES
  |     |  Status: PASS
  |     |  ↓
  |     | Routes to: responsive
  |     |
  |     ├─ Run: /ux:responsive [Mobile OAuth form]
  |     |  Output: .ux/responsive/oauth-mobile.md
  |     |  Quality Gates:
  |     |    ✅ mobile_first_verified: YES
  |     |  Status: PASS
  |     |  ↓
  |     | Routes to: accessibility
  |     |
  |     └─ Run: /ux:accessibility [WCAG compliance check]
  |        Output: .ux/accessibility/oauth-audit.md
  |        Quality Gates:
  |          ❌ wcag_aa_compliant: NO (3 violations found)
  |             • Login button contrast ratio 3.5:1 (need 4.5:1)
  |             • Form label not associated with input
  |             • Missing focus indicator
  |        Status: FAIL
  |        ↓
  |     ⚠️  LOOP DETECTED (1/5 in Phase 4)
  |     Routes back to: component-design (fix violations)
  |     Reason: WCAG violations found, redesign needed
  |
  |     └─ LOOP: Re-run /ux:component-design [fix contrast, labels, focus]
  |        Quality Gates:
  |          ✅ all_states_specified: YES (with focus state)
  |        Status: PASS
  |        ↓
  |     Re-run /ux:accessibility [verify fixes]
  |     Quality Gates:
  |       ✅ wcag_aa_compliant: YES
  |     Status: PASS ✅ (Loop 1/5 RESOLVED)
  |     ↓
  |     Routes to: sde:system-design
  |
  ├─── PHASE 5: ARCHITECTURE
  |     ├─ Run: /sde:system-design [OAuth flow architecture]
  |     |  Output: .sde/designs/oauth-architecture.md
  |     |  Quality Gates:
  |     |    ✅ design_complete: YES
  |     |      • OAuth2 flow diagram
  |     |      • Token storage strategy
  |     |      • Refresh token flow
  |     |      • Session management
  |     |  Status: PASS
  |     |  ↓
  |     | Routes to: architecture
  |     |
  |     ├─ Run: /sde:architecture [check SOLID compliance]
  |     |  Output: .sde/architecture/oauth-design.md
  |     |  Quality Gates:
  |     |    ✅ solid_compliant: YES
  |     |      • Single Responsibility (AuthService)
  |     |      • Open/Closed (extensible providers)
  |     |      • Liskov Substitution (provider interface)
  |     |  Status: PASS
  |     |  ↓
  |     | Routes to: requirements
  |     |
  |     └─ Run: /sde:requirements [trace requirements]
  |        Output: .sde/requirements/oauth-spec.md
  |        Quality Gates:
  |          ✅ traceability_complete: YES
  |        Status: PASS
  |        ↓
  |     Routes to: tdd
  |
  ├─── PHASE 6: BUILD
  |     ├─ Run: /sde:tdd [write failing tests]
  |     |  Output: .sde/tests/oauth.test.js
  |     |  Quality Gates:
  |     |    ✅ tests_pass: YES
  |     |  Status: PASS
  |     |  ↓
  |     | Routes to: code-craftsman
  |     |
  |     ├─ Run: /sde:code-craftsman [implement OAuth]
  |     |  Output: .sde/code/oauth-handler.js
  |     |  Status: PASS
  |     |  ↓
  |     | Routes to: code-review
  |     |
  |     └─ Run: /sde:code-review [review implementation]
  |        Output: .sde/reviews/oauth-pr-456.md
  |        Quality Gates:
  |          ❌ review_severity: HIGH (2 critical issues)
  |             • Missing CSRF token validation
  |             • State parameter not verified
  |             • Insufficient test coverage (62%)
  |        Status: FAIL
  |        ↓
  |     ⚠️  LOOP DETECTED (1/5 in Phase 6)
  |     Routes back to: code-craftsman (fix security issues)
  |     Reason: review_severity >= HIGH
  |
  |     └─ LOOP: Re-run /sde:code-craftsman [add CSRF, state validation]
  |        ├─ Add CSRF token middleware
  |        ├─ Add state parameter verification
  |        ├─ Add 12 more unit tests
  |        Status: PASS
  |        ↓
  |     Re-run /sde:code-review [verify fixes]
  |     Quality Gates:
  |       ✅ review_severity: LOW
  |       ✅ test_coverage: 87%
  |     Status: PASS ✅ (Loop 1/5 RESOLVED)
  |     ↓
  |     Routes to: qae:test-strategy
  |
  ├─── PHASE 7: QUALITY
  |     ├─ Run: /qae:test-strategy [QA strategy]
  |     |  Output: .qae/strategies/oauth-test-strategy.md
  |     |  Quality Gates:
  |     |    ✅ coverage_defined: YES
  |     |  Status: PASS
  |     |  ↓
  |     | Routes to: test-plan
  |     |
  |     ├─ Run: /qae:test-plan [detailed test plan]
  |     |  Output: .qae/plans/oauth-test-plan.md
  |     |  Quality Gates:
  |     |    ✅ scope_clear: YES
  |     |  Status: PASS
  |     |  ↓
  |     | Routes to: automation
  |     |
  |     ├─ Run: /qae:automation [write tests]
  |     |  Output: .qae/automation/oauth.e2e.js
  |     |  Quality Gates:
  |     |    ✅ coverage_adequate: 91%
  |     |  Status: PASS
  |     |  ↓
  |     | Routes to: cicd-pipeline
  |     |
  |     ├─ Run: /qae:cicd-pipeline [set up gates]
  |     |  Output: .qae/pipelines/oauth-gates.yml
  |     |  Quality Gates:
  |     |    ✅ gates_defined: YES
  |     |  Status: PASS
  |     |  ↓
  |     | Routes to: defect-management
  |     |
  |     └─ Run: /qae:defect-management [run tests, find defects]
  |        Output: .qae/defects/oauth-defects-2026-03-03.md
  |        Defects Found: 2
  |          1. HIGH: User can bypass OAuth callback verification
  |             Root cause: URL redirect validation missing
  |             Severity: CRITICAL
  |        Quality Gates:
  |          ❌ severity >= HIGH: YES
  |        Status: FAIL
  |        ↓
  |     ⚠️  CROSS-DOMAIN LOOP DETECTED (1/5 across domains)
  |     Routes to: sde:debugging (HIGH severity defect)
  |     Reason: severity >= HIGH → cross-domain loop
  |
  |     └─ LOOP: Cross-domain handoff to SDE
  |        Run: /sde:debugging [root cause analysis]
  |        ├─ Trace redirect validation flow
  |        ├─ Identify missing URL whitelist check
  |        ├─ Write test that reproduces bug
  |        Status: PASS (root cause found)
  |        ↓
  |     Re-run /sde:tdd [write failing test]
  |     • Test: redirect to untrusted domain should fail
  |     Status: PASS (test fails as expected)
  |     ↓
  |     Re-run /sde:code-craftsman [add URL validation]
  |     • Add redirect whitelist to config
  |     • Validate redirect URL against whitelist
  |     • Add 4 more tests
  |     Status: PASS
  |     ↓
  |     Re-run /sde:code-review [verify security fix]
  |     Quality Gates:
  |       ✅ review_severity: LOW
  |       ✅ test_coverage: 89%
  |     Status: PASS
  |     ↓
  |     Re-run /qae:automation [re-run tests]
  |     Quality Gates:
  |       ✅ coverage_adequate: 93%
  |     Status: PASS
  |     ↓
  |     Re-run /qae:defect-management [verify fix]
  |     Quality Gates:
  |       ✅ severity < HIGH: YES (defect resolved)
  |     Status: PASS ✅ (Cross-domain loop 1/5 RESOLVED)
  |     ↓
  |     Routes to: quality-metrics
  |
  |     └─ Run: /qae:quality-metrics [measure readiness]
  |        Output: .qae/metrics/oauth-readiness.md
  |        Metrics:
  |          ✅ Test Coverage: 93%
  |          ✅ Defect Density: 0
  |          ✅ Performance: <200ms OAuth flow
  |          ✅ Security: Audit passed
  |        Status: PASS
  |        ↓
  |     Routes to: pe:architecture-reviewer (Phase 8)
  |
  ├─── PHASE 8: REFINEMENT
  |     └─ Run: /pe:architecture-reviewer [RFC review]
  |        Output: .pe/architecture/oauth-adr.md
  |        Quality Gates:
  |          ✅ rfc_approved: YES
  |        Status: PASS
  |        ↓
  |     Routes to: pm:stakeholder-communicator
  |
  ├─── PHASE 9: FEEDBACK
  |     └─ Run: /pm:stakeholder-communicator [release notes]
  |        Output: .pm/stakeholder/oauth-release.md
  |        Status: PASS
  |        ↓
  |     ✅ FEATURE COMPLETE & READY FOR RELEASE
  |
  └─── END: /master-orchestrator [feature delivered]
```

---

## 📊 Coordination Metrics

| Metric | Value |
|--------|-------|
| Total Skills Invoked | 27 |
| Domains Traversed | 5 (PM→UX→SDE→QAE→PE) |
| Intra-Domain Hops | 22 (same domain routing) |
| Inter-Domain Handoffs | 4 (cross-domain routing) |
| **Intra-Domain Loops** | 1 (UX accessibility) |
| **Inter-Domain Loops** | 1 (QAE→SDE defect) |
| Total Loops | 2 |
| Loop Counter - Phase 4 | 1/5 |
| Loop Counter - Phase 6 | 1/5 |
| Loop Counter - Cross-Domain | 1/5 |
| Phases Traversed | 9/9 (100%) |
| Quality Gates Checked | 22+ |
| Quality Gates Failed → Looped | 3 |
| Quality Gates Passed | 19+ |

---

## 🔄 Loop Details

### Loop 1: Intra-Domain (UX - Accessibility)
```
Phase 4: Design
  component-design → interaction-design → responsive → accessibility
                                                           ↓ WCAG violations
                                                    Loop back to component-design
  Reason: WCAG AA violations (contrast, labels, focus)
  Loop #: 1/5
  Resolution: Fix contrast ratios, add ARIA labels, add focus indicators
  Status: RESOLVED ✅
```

### Loop 2: Intra-Domain (SDE - Code Review)
```
Phase 6: Build
  tdd → code-craftsman → code-review
                            ↓ Severity HIGH (CSRF, state validation)
                       Loop back to code-craftsman
  Reason: Missing CSRF token validation, state not verified
  Loop #: 1/5
  Resolution: Add CSRF middleware, add state parameter verification
  Status: RESOLVED ✅
```

### Loop 3: Cross-Domain (QAE → SDE)
```
Phase 7: Quality → Phase 6: Build (Cross-domain loop)
  defect-management (HIGH severity found)
                            ↓
                     sde:debugging (root cause)
                            ↓
                     sde:tdd (reproduce bug)
                            ↓
                     sde:code-craftsman (fix)
                            ↓
                     sde:code-review (verify)
                            ↓
                     qae:automation (re-test)
                            ↓
                     qae:defect-management (verify resolution)
  Reason: HIGH severity defect (OAuth redirect validation missing)
  Loop #: 1/5 (cross-domain)
  Resolution: Add URL whitelist, validate redirects
  Status: RESOLVED ✅
```

---

## ✅ Success Criteria

- [x] Started in PM (research)
- [x] Transitioned to UX (design)
- [x] Handed off to SDE (architecture → build)
- [x] Escalated to QAE (quality)
- [x] Reviewed by PE (architecture)
- [x] Returned to PM (stakeholder communication)
- [x] **Intra-domain loop** in UX (accessibility fixes)
- [x] **Intra-domain loop** in SDE (code review severity)
- [x] **Cross-domain loop** from QAE to SDE (defect fix)
- [x] All 9 phases completed
- [x] Loop limits enforced (max 5 per phase)
- [x] Quality gates applied throughout
- [x] Events tracked in `.project/events.jsonl`
- [x] Loops recorded in `.project/loops.md`

---

## 📈 Journey Summary

```
OAUTH FEATURE BUILD: Multi-Hop Coordination Test
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Phase 1: Discovery       ✅ research-agent
Phase 2: Validation      ✅ gap-analyst → prd-generator
Phase 3: Planning        ✅ (PRD ready)
Phase 4: Design          ↩️  design-system → component-design 
                            (Loop 1/5: WCAG fixes) ✅ RESOLVED
                         ✅ accessibility → responsive
Phase 5: Architecture    ✅ system-design → architecture
Phase 6: Build           ↩️  tdd → code-craftsman 
                            (Loop 1/5: Security fixes) ✅ RESOLVED
                         ✅ code-review PASS
Phase 7: Quality         ↩️  automation → defect-management
                            ⟲ Cross-domain to sde:debugging
                            (Loop 1/5: Defect fix) ✅ RESOLVED
                         ✅ quality-metrics PASS
Phase 8: Refinement      ✅ architecture-reviewer
Phase 9: Feedback        ✅ stakeholder-communicator

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESULT: ✅ FEATURE READY FOR RELEASE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Total Skills: 27/56
Total Hops: 26+ (including loop re-runs)
Loops: 3 (1 UX, 1 SDE, 1 cross-domain)
Status: ALL QUALITY GATES PASSED
```
