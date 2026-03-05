# Master Orchestrator: Single Command End-to-End Execution

**Goal:** Run entire 9-phase feature delivery with ONE command  
**Time:** ~100 days for full delivery (98 days observed for OAuth2)  
**Prerequisites:** Git repo, 2+ engineers, clear PRD

---

## Quick Start: The One Command

```bash
/taskpilot:master-orchestrator Build OAuth2 social login with privacy-first and passwordless-first positioning. Phase 1 discovery through Phase 9 feedback. Full lifecycle with detailed interaction tracking.
```

That's it! The orchestrator will:
1. ✅ Create `.project/` directory structure
2. ✅ Execute all 9 phases in sequence
3. ✅ Track interactions at each phase
4. ✅ Gate advances between phases
5. ✅ Generate final delivery report

---

## Command Syntax

### Full Command Structure

```
/taskpilot:master-orchestrator [PROJECT_NAME]: [DETAILED_DESCRIPTION]
```

### Example: OAuth2

```
/taskpilot:master-orchestrator OAuth2 Social Login Feature:
Build OAuth2 social login supporting Google, Apple, GitHub, and passwordless (passkeys).
- Privacy-first positioning (transparent audits, open-source)
- Passwordless-first (2-hour integration for developers)
- Target: 12 weeks, multi-domain feature
- Start: Phase 1 Discovery
- End: Phase 9 Feedback & Retrospective
```

### Example: Payment Processing

```
/taskpilot:master-orchestrator Payment Processing MVP:
Build payment processing for Stripe integration.
- Phase 1: Market research on payment providers
- Phase 4: Design checkout flow UX
- Phase 6: Implement Stripe SDK
- Phase 7: Full security audit (PCI compliance)
- Phase 8: Launch with feature flags
```

### Example: Mobile App Redesign

```
/taskpilot:master-orchestrator Mobile App v2.0 Redesign:
Complete redesign of iOS/Android mobile app.
- Phase 1: User research (what's broken?)
- Phase 4: New design system (components, spacing, typography)
- Phase 5: Architecture for cross-platform code sharing
- Phase 6: Implement in React Native
- Phase 7: Performance testing on low-end devices
- Phase 8: Beta launch
```

---

## What Happens When You Run the Command

### Auto-Execution Flow

```
You run ONE command:
  ↓
Master Orchestrator initializes
  ↓
Scans for existing work (.pm/, .sde/, .ux/, .qae/, .pe/)
  ↓
Determines starting phase (defaults Phase 1, skips if work exists)
  ↓
Phase 1 → Invokes all PM skills
  ├─ Research Agent (competitors)
  ├─ Gap Analyst (scored gaps)
  ├─ Buyer Psychology (segments)
  └─ Experiment Designer (hypotheses)
  ↓
[After Phase 1 complete] → Phase 2 → Invokes PM + PE validation skills
  ├─ Discovery Validator
  ├─ Experiment Designer
  ├─ Tech Strategy
  └─ Leverage Analyzer
  ↓
[Phase gate check] → Does Phase 2 pass? (yes/no)
  ├─ If YES → Advance to Phase 3
  └─ If NO → Loop or escalate to user
  ↓
Phase 3 → Phase 9 [same pattern for each phase]
  ↓
✅ COMPLETE → Generates final orchestration report
```

---

## Real Example: Running OAuth2 End-to-End

### Step 1: Copy and Paste This Command

```
/taskpilot:master-orchestrator OAuth2 Social Login Feature with Privacy-First & Passwordless-First Positioning:
Build complete OAuth2 social login system supporting Google, Apple, GitHub, and WebAuthn passkeys.

POSITIONING:
- Developer: Fast setup (<2 hours), minimal SDK bloat, clear errors
- Enterprise: Privacy auditable (SOC2, open-source SDK), transparent data handling

SCOPE:
- Phase 1: Research Google, Apple, GitHub, passkeys market (80% of auth)
- Phase 2: Validate passwordless works for developers, privacy resonates with enterprises
- Phase 3: Plan with RICE scoring, estimate 10-week timeline, 2-engineer team
- Phase 4: Design privacy-first UI, passwordless-first flow, accessibility audit
- Phase 5: Architecture OAuth2 server, credential storage, token strategy
- Phase 6: Implement with TDD (220 tests minimum), code review
- Phase 7: Test strategy (55% unit, 30% integration, 15% E2E), security scan, performance
- Phase 8: Launch readiness (quality gates, CI/CD pipeline, reliability SLOs)
- Phase 9: Measure adoption, switching intent, plan v1.1

EXPECTED TIMELINE: 98-120 days
TEAM: 2 engineers, 1 designer, 1 QAE, 1 PM
SUCCESS: <2hr integration time, 3.5+ switching intent score, 99.5% uptime
```

### Step 2: Orchestrator Auto-Executes

**Week 1-2 (Phase 1: Discovery)**
```
✅ Phase 1.1 - Research Agent executes
   → Creates .pm/competitors/google-sign-in.md (75% market share)
   → Creates .pm/competitors/apple-sign-in.md (73% growth)
   → Creates .pm/competitors/github-oauth.md
   → Creates .pm/competitors/oauth-market-trends.md

✅ Phase 1.2 - Gap Analyst executes
   → Reads competitors + product inventory
   → Creates .pm/gaps/2026-03-03-oauth-gaps.md
   → Scores 8 gaps with WINNING filter
   → Identifies 4 FILE gaps (45-57 score)

✅ Phase 1.3 - Buyer Psychology executes
   → Creates .pm/research/buyer-profile-privacy-conscious.md
   → Creates .pm/research/buyer-profile-developer-first.md
   → Maps switching forces, cognitive biases

✅ Phase 1.4 - Experiment Designer executes
   → Creates hypothesis cards for passwordless + privacy
   → Designs A/B test with sample size calculations
   → Defines success criteria (SHIP/ITERATE/KILL)

⏳ Phase 1 Gate Check
   ├─ Are competitor profiles complete? ✓
   ├─ Are gaps scored? ✓
   ├─ Are buyer profiles created? ✓
   └─ Are experiments designed? ✓
   
   → GATE PASSED → Advance to Phase 2
```

**Week 3-4 (Phase 2: Validation)**
```
✅ Phase 2.1 - Discovery Validator executes
   → Maps assumptions (passwordless works, privacy matters)
   → Creates testable hypotheses

✅ Phase 2.2 - Experiment Designer executes
   → Runs A/B test on passwordless-first messaging
   → Sample: 2000 developers, 4 weeks
   → Result: +16% conversion (SHIP decision)

✅ Phase 2.3 - Tech Strategy executes
   → Evaluates OAuth2 server feasibility
   → Identifies architecture options

✅ Phase 2.4 - Leverage Analyzer executes
   → Assesses impact/effort trade-offs

⏳ Phase 2 Gate Check
   ├─ Both experiments SHIP or clear signal? ✓ (Both SHIP)
   ├─ Technical feasibility confirmed? ✓
   └─ Ready for planning? ✓
   
   → GATE PASSED → Advance to Phase 3
```

**Week 5-7 (Phase 3: Planning)**
```
✅ Phase 3.1-3.6 executes in sequence
   → Prioritization Engine (4 FILE gaps → features)
   → PRD Generator (comprehensive PRD)
   → Metrics Advisor (OKRs, success criteria)
   → SDE Requirements (technical specs)
   → SDE Estimation (PERT: 355 hours, 8.9 weeks)
   → Stakeholder Communicator (kickoff brief)

⏳ Phase 3 Gate Check
   ├─ PRD approved? ✓
   ├─ Timeline realistic? ✓ (10 weeks estimate)
   └─ Team aligned? ✓
   
   → GATE PASSED → Advance to Phase 4
```

**Week 8-9 (Phase 4: Design)**
```
✅ Phase 4.1-4.8 executes in sequence
   → UX Design System (tokens, components)
   → UX Color System (palette, contrast)
   → UX Typography (type scale, pairing)
   → UX Visual Hierarchy (8pt grid, spacing)
   → UX Component Design (all states)
   → UX Interaction Design (animations)
   → UX Responsive (mobile-first CSS)
   → UX Accessibility (WCAG audit)

⏳ Design phase complete
   → GATE PASSED → Advance to Phase 5
```

**Week 10-11 (Phase 5: Architecture)**
```
✅ Phase 5.1-5.6 executes in sequence
   → SDE System Design (OAuth2 flow, capacity)
   → SDE Architecture (clean layers, SOLID)
   → SDE Data Systems (credential storage)
   → Architecture Reviewer (RFC review, ADRs)
   → Decision Facilitator (token strategy consensus)
   → SDE Systems Thinking (feedback loops)

⏳ Architecture complete + reviewed
   → GATE PASSED → Advance to Phase 6
```

**Week 12-13 (Phase 6: Build)**
```
✅ Phase 6.1-6.4 executes in sequence
   → QAE Test Strategy (risk-based approach)
   → SDE TDD (220 tests, red-green-refactor)
   → SDE Code Craftsman (clean code, DRY)
   → SDE Code Review (SOLID compliance)

⏳ Build complete with tests passing
   → GATE PASSED → Advance to Phase 7
```

**Week 14 (Phase 7: Quality)**
```
✅ Phase 7.1-7.9 executes in sequence
   → QAE Test Plan (detailed test plan)
   → QAE Test Data (synthetic data, scenarios)
   → QAE Automation (test pyramid, CI/CD)
   → QAE API Testing (contract tests)
   → QAE Performance (load test 1000 users)
   → QAE Security (OWASP scan, finds XSS)
   → QAE Exploratory (session-based testing)
   → UX Review (Nielsen heuristics)
   → QAE Defect Management (triages 12 defects)

⏳ Quality gate check
   ├─ All tests passing? ✓ (92% coverage)
   ├─ Security issues resolved? ✓ (XSS fixed)
   ├─ Performance acceptable? ✓ (p95=320ms)
   └─ Zero critical defects? ✓
   
   → GATE PASSED → Advance to Phase 8
```

**Week 15 (Phase 8: Launch)**
```
✅ Phase 8.1-8.5 executes in sequence
   → QAE Quality Metrics (readiness scorecard: 98/100)
   → QAE CI/CD Pipeline (GitHub Actions, gates)
   → PE Technical Quality (DORA metrics)
   → PE Incident Reliability (SLOs, runbooks)
   → PM Stakeholder Communicator (launch comms)

⏳ Launch decision
   ├─ Quality: 98/100 ✓
   ├─ Security: Passed ✓
   ├─ Performance: Passed ✓
   └─ Readiness: GO ✓
   
   → LAUNCH APPROVED → Ship to production
```

**Week 16+ (Phase 9: Feedback)**
```
✅ Phase 9.1-9.4 executes
   → PM Metrics Advisor (track OKRs, north star)
   → PM Pivot Analyzer (PMF signal, persevere/pivot)
   → PM Customer Research (user feedback)
   → PM Stakeholder Communicator (retrospective)

⏳ Post-launch metrics
   ├─ Developer integration: 1.8 hours (target 2) ✓ Better!
   ├─ Enterprise switching intent: 3.6 (target 3.5) ✓ Better!
   ├─ Passwordless enrollment: 34% (target 30%) ✓ Better!
   ├─ System uptime: 99.8% (target 99.5%) ✓ Excellent!
   └─ Critical defects: 0 (target 0) ✓ Perfect!
   
   → DECISION: PERSEVERE (all metrics exceeded)
   → NEXT: Plan v1.1 features
```

---

## Output: What You Get When It Completes

### Automatic Deliverables

**`.project/` Directory (Status & Tracking)**
- ✅ `.project/status.md` — Complete lifecycle checklist, 9 phases, all steps marked complete
- ✅ `.project/deliverables.md` — Cross-domain deliverable map
- ✅ `.project/loops.md` — Loop tracking (3 loops documented)
- ✅ `.project/orchestration-metrics.md` — Interaction metrics, handoff quality
- ✅ `.project/FINAL-ORCHESTRATION-REPORT.md` — Executive summary (8.6/10 score)

**`.pm/` Directory (Product)**
- ✅ `.pm/competitors/*.md` (5 files)
- ✅ `.pm/gaps/2026-03-03-oauth-gaps.md`
- ✅ `.pm/research/*.md` (buyer profiles, personas)
- ✅ `.pm/experiments/*.md` (hypothesis + results)
- ✅ `.pm/prds/oauth2-social-login.md` (285 lines)
- ✅ `.pm/metrics/oauth2-okrs.md`

**`.ux/` Directory (Design)**
- ✅ `.ux/design-systems/` (tokens, hierarchy)
- ✅ `.ux/colors/` (palette, tokens)
- ✅ `.ux/components/` (60 component specs)
- ✅ `.ux/typography/` (type scale, pairing)
- ✅ `.ux/accessibility/` (WCAG audit results)

**`.sde/` Directory (Engineering)**
- ✅ `.sde/requirements/oauth2-detailed-specs.md`
- ✅ `.sde/designs/oauth2-system-design.md`
- ✅ `.sde/architecture/oauth2-adr.md`
- ✅ `.sde/estimates/oauth2-pert-estimate.md`

**`.qae/` Directory (Quality)**
- ✅ `.qae/strategies/oauth2-test-strategy.md`
- ✅ `.qae/plans/oauth2-test-plan.md`
- ✅ `.qae/automation/` (test pyramid)
- ✅ `.qae/metrics/oauth2-quality-scorecard.md` (98/100)

**`.pe/` Directory (Principal Engineering)**
- ✅ `.pe/strategy/oauth2-tech-strategy.md`
- ✅ `.pe/architecture/oauth2-adr.md`
- ✅ `.pe/decisions/` (decision records)
- ✅ `.pe/incidents/oauth2-reliability-review.md`

---

## Variations: Custom Starting Points

### Start from Phase 3 (Skip Discovery/Validation)

```
/taskpilot:master-orchestrator OAuth2 Social Login Feature: 
[Same description]

Note: Starting Phase 3 (Planning) — validation already complete
```

**What happens:**
- Orchestrator scans `.pm/gaps/`, `.pm/experiments/` — finds them
- Skips Phase 1-2
- Starts Phase 3 (Planning) directly
- Saves 4 weeks

### Start from Phase 4 (Design)

```
/taskpilot:master-orchestrator OAuth2 Social Login Feature:
[Description]

Note: Starting Phase 4 (Design) — PRD and requirements already done
```

**What happens:**
- Skips Phase 1-3
- Reads `.pm/prds/oauth2-social-login.md`
- Starts Phase 4 (Design)
- Saves 7 weeks

### Skip a Specific Phase

```
/taskpilot:master-orchestrator OAuth2 Social Login Feature:
[Description]

Skip Phase 2 (validation) — feature already validated in market
```

**What happens:**
- Normal flow until Phase 2
- Skips Phase 2 entirely
- Continues Phase 3→9
- Saves 2 weeks

---

## Monitoring Orchestration Progress

### Real-Time Status

While orchestrator is running, check:

```bash
# Check current phase
cat .project/status.md

# See latest activities
tail -50 .project/loops.md

# Monitor deliverables
ls -la .pm/ .ux/ .sde/ .qae/ .pe/
```

### Pause & Resume

If you need to pause:

```
[Orchestrator running...]
Press Ctrl+C to pause

# Later, resume from where it left off:
/taskpilot:master-orchestrator [same command]
[Scans .project/status.md, continues from current phase]
```

---

## Conditional Behaviors: Gates & Decisions

### Phase Gate Failures (Automatic Decisions)

The orchestrator automatically handles gate failures:

```
Phase 2 Gate Check: Do experiments SHIP?
├─ IF experiments SHIP → Advance to Phase 3 ✓
├─ IF experiments ITERATE → Loop back to Phase 2, re-experiment
└─ IF experiments KILL → Escalate to PM (may pivot feature)
```

### Architecture Review Issues

```
Phase 5 Gate: Did architecture review pass?
├─ IF approved → Advance to Phase 6 ✓
├─ IF issues found → Create ADR, resolve, re-review
└─ IF critical → Escalate to CTO (may redesign)
```

### Quality Gate Failures

```
Phase 7 Gate: Did quality metrics pass?
├─ IF all green → Advance to Phase 8 ✓
├─ IF warnings → Fix defects, re-test
└─ IF critical failures → Block launch (iterate code)
```

---

## Error Handling

If orchestrator encounters an error:

```
❌ Phase 4.5 - UX Component Design failed
   Reason: "Cannot find design tokens in .ux/design-systems/"
   
Action:
   Option 1: Run Phase 4.1 (Design System) first
   Option 2: Manually provide design tokens, resume
   Option 3: Adjust orchestrator parameters
```

The orchestrator PAUSES and waits for your decision. You can:
- `resume` — Continue with workaround
- `retry` — Re-run same phase
- `restart` — Start from previous phase
- `skip` — Skip this phase, continue

---

## Summary: One Command End-to-End

**The Command:**
```
/taskpilot:master-orchestrator [PROJECT_NAME]: [DETAILED_DESCRIPTION]
```

**What It Does:**
```
Phase 1 (Discovery) ✓
    ↓
Phase 2 (Validation) ✓
    ↓
Phase 3 (Planning) ✓
    ↓
Phase 4 (Design) ✓
    ↓
Phase 5 (Architecture) ✓
    ↓
Phase 6 (Build) ✓
    ↓
Phase 7 (Quality) ✓
    ↓
Phase 8 (Launch) ✓
    ↓
Phase 9 (Feedback) ✓
    ↓
✅ COMPLETE: Production feature + full documentation
```

**Timeline:** 98-120 days  
**Output:** 50+ files across `.pm/`, `.ux/`, `.sde/`, `.qae/`, `.pe/`  
**Orchestration Score:** 8.6/10 (excellent coordination)

**Try it now! Use this exact command:**

```
/taskpilot:master-orchestrator [Your Feature Name]: [Your Description]
```

The orchestrator handles the rest automatically. 🚀
