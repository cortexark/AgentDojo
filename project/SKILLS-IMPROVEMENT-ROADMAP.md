# Skills Improvement Roadmap: Fixing the Gaps

**Goal:** Fix high-priority skill gaps identified in critical assessment  
**Timeline:** 3 phases over 6 weeks  
**Success Criteria:** 15% improvement in defect prevention, 20% faster testing cycles

---

## Phase 1: HIGH PRIORITY (Weeks 1-2)

### Fix #1: Move Accessibility Testing Earlier 🔴

**Current State:** Phase 4.8 (final design step) — too late for changes  
**Problem:** Color contrast issue found late, required rework loop  
**Target State:** Phase 4.2 (after color system defined) — guides palette choices

#### Implementation Plan

**Step 1: Refactor UX Accessibility Skill**
- Split into 2 skills:
  - `ux-accessibility:foundational` (Phase 4.2) — WCAG basics, contrast validation, keyboard nav
  - `ux-accessibility:audit` (Phase 4.8) — Final audit, edge cases, assistive tech testing
- Add early validation in Phase 4.2 to catch color contrast before design finalized

**Step 2: Create Accessibility Checklist**
- WCAG 2.2 AA baseline checklist (30 items)
- Executable in Phase 4.2 (before components designed)
- Feeds into color system refinement

**Step 3: Add Screen Reader Testing Early**
- Phase 4.2: Test with NVDA/JAWS on prototype components
- Catch keyboard nav issues before components finalized
- Currently (Phase 4.8): Only WCAG audit, no assistive tech

**Effort:** 8 hours (split skill, create checklist, add testing)  
**Ownership:** UX + QAE collaboration  
**Expected Benefit:** Prevent 1-2 accessibility loops

---

### Fix #2: Expand Performance Testing 🔴

**Current State:** Load test only (1000 users, p95=320ms)  
**Problem:** Missing chaos/stress/soak scenarios — will fail at scale  
**Target State:** Comprehensive testing (load + stress + chaos + soak)

#### Implementation Plan

**Step 1: Add Chaos Testing Framework**
- Implement network failure scenarios:
  - Connection timeout (simulate network loss)
  - Slow responses (simulate 3G latency)
  - Partial failures (some OAuth providers down)
- Tool: `tc` (traffic control) for latency injection
- Requirement: Tests must pass with 10% failure rate

**Step 2: Add Stress Testing**
- Push beyond normal load (1000 → 5000 users)
- Identify breaking point
- Current: No stress testing (gap)
- Expected result: Should handle 2x peak load

**Step 3: Add Soak Testing**
- Run load test for 24+ hours
- Identify memory leaks, connection pool exhaustion
- Current: Load test runs 2 hours max
- Expected: No performance degradation after 24h

**Step 4: Add Spike Testing**
- Simulate sudden traffic surge (100 → 5000 users in 5 minutes)
- Test auto-scaling, rate limiting
- Expected: Graceful degradation, no crashes

**Effort:** 40 hours (framework setup, scenario design, execution)  
**Ownership:** QAE Performance + DevOps  
**Timeline:** Week 2-3  
**Expected Benefit:** Catch 2-3 scalability issues before production

---

### Fix #3: Start Mobile Testing in Phase 4 (Not Phase 7) 🔴

**Current State:** Phase 7 (build complete) — too late to affect design  
**Problem:** Passkey overflow on mobile found in production  
**Target State:** Phase 4.6 (responsive design phase) — validates mobile UX early

#### Implementation Plan

**Step 1: Create Mobile Testing Checklist**
- 8+ device sizes (not 3):
  - iPhone 12 mini (320px)
  - iPhone 12 (375px)
  - iPhone 12 Pro Max (428px)
  - Android small (360px)
  - Android large (480px)
  - Tablet (768px)
  - iPad (1024px)
  - iPad Pro (1366px)
- 4+ browsers (not 2):
  - Safari (iOS)
  - Chrome (iOS)
  - Chrome (Android)
  - Firefox (Android)

**Step 2: Set Up Mobile Device Lab**
- Real devices (not simulators):
  - 2x iPhone (latest, one generation old)
  - 2x Android (Samsung, Google Pixel)
  - 1x Tablet
  - BrowserStack for additional device coverage
- Cost: ~$500 one-time, $50/month
- Expected: Catch mobile-specific issues (scrolling, touch targets, etc.)

**Step 3: Run Mobile Testing in Phase 4**
- Phase 4.6: Test responsive layouts on real devices
- Check: Touch targets (44px minimum), landscape rotation, keyboard appearance
- Current: Done in Phase 7, found issues too late
- New: Done in Phase 4, can adjust design

**Step 4: Add Mobile Performance Testing**
- Test on slow networks (3G, LTE)
- Test on low-end devices (older iPhone, budget Android)
- Current: No mobile-specific performance testing
- Expected: Identify slow-loading components, battery drain

**Effort:** 30 hours setup + 8 hours per testing cycle  
**Ownership:** QAE + Design  
**Timeline:** Week 2 (setup), Week 3+ (ongoing)  
**Expected Benefit:** Catch 2-3 mobile-specific issues earlier

---

## Phase 2: MEDIUM PRIORITY (Weeks 2-4)

### Fix #4: Coordinate Security Testing 🟡

**Current State:** SDE threat modeling (Phase 5) + QAE scanning (Phase 7) — duplicated  
**Problem:** Overlap, inconsistent coverage, wasted effort  
**Target State:** Single security strategy (threat model → validation → verification)

#### Implementation Plan

**Step 1: Create Shared THREAT-MODEL.md**
- Phase 5 `/sde-security:threat-modeling` creates: `THREAT-MODEL.md`
- Documents STRIDE analysis for each component:
  - Spoofing: Can attacker impersonate user? (OAuth flows)
  - Tampering: Can attacker modify credentials? (token storage)
  - Repudiation: Can user deny actions? (audit logs)
  - Information Disclosure: Can attacker read data? (encryption)
  - Denial of Service: Can attacker crash system? (rate limiting)
  - Elevation of Privilege: Can attacker escalate access? (session handling)

**Step 2: Phase 7 `/qae-security:validation` reads threat model**
- Don't rediscover threats
- Instead: Validate that each threat is mitigated
- Create test scenarios for each threat:
  - Spoofing: Try invalid tokens, expired tokens
  - Tampering: Try modified tokens, wrong credentials
  - Etc.

**Step 3: Merge Threat Modeling + Scanning**
- Phase 5: High-level threat modeling (architecture level)
- Phase 7: Low-level security testing (code level)
- Both contribute to `THREAT-MODEL.md`
- No duplication

**Effort:** 12 hours (create artifact, coordinate workflows, write tests)  
**Ownership:** SDE Security + QAE Security  
**Timeline:** Week 2  
**Expected Benefit:** Reduce Phase 5-7 duration by 1 day, eliminate duplication

---

### Fix #5: Expand API Testing (Error Paths) 🟡

**Current State:** Happy path only (valid requests)  
**Problem:** 401/403 errors, rate limiting, abuse scenarios not tested  
**Target State:** Comprehensive API testing (happy + unhappy paths)

#### Implementation Plan

**Step 1: Add Error Path Tests**
- Create test scenarios for each error case:
  - 400 (invalid request): missing fields, wrong types, invalid values
  - 401 (unauthorized): missing token, expired token, invalid token
  - 403 (forbidden): valid token but insufficient scope
  - 429 (rate limited): too many requests
  - 500 (server error): database down, external service down

**Step 2: Add Abuse Scenario Tests**
- Token replay: Can attacker reuse expired token?
- Credential stuffing: Can attacker brute force passwords? (rate limiting)
- CSRF: Can attacker forge requests? (state validation)
- API parameter tampering: Can attacker modify request parameters?

**Step 3: Contract Testing**
- Define API contract (request/response schema)
- Test: Does response always match contract?
- Catch: Breaking changes, unexpected fields

**Effort:** 16 hours (write tests, run scenarios, document)  
**Ownership:** QAE API Testing  
**Timeline:** Week 2-3  
**Expected Benefit:** Catch 1-2 API security/validation issues

---

### Fix #6: Expand Test Automation Scope 🟡

**Current State:** 95 tests (unit + integration), 15 E2E scenarios, no chaos  
**Problem:** Only happy path automated, edge cases manual-only  
**Target State:** 120+ tests, 20+ E2E scenarios, chaos scenarios included

#### Implementation Plan

**Step 1: Add E2E Scenario Tests**
- Current: 15 scenarios (happy path only)
- Add:
  - Passkey enrollment → logout → Google login (5 scenarios)
  - Error recovery flows (password reset, session expiry) (5 scenarios)
  - Cross-browser flows (Safari → Chrome) (2 scenarios)
- Target: 20-25 E2E scenarios

**Step 2: Add Regression Testing**
- For each bug fixed (12 defects found), create regression test
- Prevent bug from reoccurring
- Current: No regression tests
- Expected: Catch regressions early

**Step 3: Add Performance Regression Tests**
- Track p95 latency over time
- Alert if p95 > 350ms (current 320ms)
- Prevent performance degradation

**Effort:** 24 hours (write tests, integrate into CI/CD)  
**Ownership:** QAE Automation  
**Timeline:** Week 3  
**Expected Benefit:** Catch 1-2 regressions early

---

## Phase 3: LOW PRIORITY (Weeks 4-6)

### Fix #7: Deprecate/Redesign Low-Value Skills 🟢

#### Leverage Analyzer (Deprecate)
**Current:** Generic, output unused  
**Action:** Remove from standard toolkit
**Effort:** 2 hours (update documentation)  
**Timeline:** Week 4

#### Migration Planner (Make Conditional)
**Current:** Required even for greenfield projects  
**Action:** Mark as "conditional — skip for greenfield"
**Effort:** 1 hour  
**Timeline:** Week 4

#### Discovery Validator (Redesign)
**Current:** Shallow assumption mapping  
**Action:** Redesign as workshop + automated analysis
- Workshop: Team brainstorms assumptions (1 hour)
- Automated: Tool identifies most critical assumptions
- Output: Ranked list of testable hypotheses
**Effort:** 20 hours (redesign, testing)  
**Timeline:** Week 5  
**Expected Benefit:** Better hypothesis prioritization

#### Influence Navigator (Make Optional)
**Current:** Unnecessary for technical projects  
**Action:** Skip by default, use only if org friction detected
**Effort:** 1 hour  
**Timeline:** Week 4

---

### Fix #8: Add New Skills (Or Enhance Existing)

#### Add `/qae-chaos-testing` Skill
**Purpose:** Chaos scenario generation, network failure simulation  
**Effort:** 40 hours (design, implement, test)  
**Timeline:** Week 5-6  
**Expected Impact:** Identify 1-2 resilience issues

#### Enhance `ux-accessibility` with Assistive Tech Testing
**Current:** WCAG audit only  
**Enhanced:** + Screen reader testing (NVDA, JAWS, VoiceOver)
**Effort:** 16 hours  
**Timeline:** Week 4-5  
**Expected Impact:** Catch 1-2 assistive tech issues

---

## Summary: Work Breakdown

| Week | Task | Effort | Owner | Deliverable |
|------|------|--------|-------|------------|
| **Week 1** | Accessibility refactor | 8h | UX+QAE | 2-skill split, checklist |
| **Week 1-2** | Performance testing framework | 40h | QAE | Chaos, stress, soak tests |
| **Week 2** | Mobile device lab setup | 30h | QAE | Real device lab operational |
| **Week 2** | Security coordination | 12h | SDE+QAE | THREAT-MODEL.md artifact |
| **Week 2-3** | API error path tests | 16h | QAE | Error scenarios automated |
| **Week 3** | Expand test automation | 24h | QAE | 20+ E2E, regression tests |
| **Week 4** | Low-priority deprecations | 4h | PM | Updated toolkit docs |
| **Week 4-5** | Accessibility + assistive tech | 16h | UX+QAE | Screen reader testing |
| **Week 5-6** | Chaos testing skill | 40h | QAE | New skill, integrated |
| **Week 6** | Testing & validation | 20h | All | Verify improvements |
| | **TOTAL** | **210 hours** | **Cross-functional** | **All improvements shipped** |

---

## Implementation Sequence (Critical Path)

```
Week 1:
  ├─ Accessibility refactor (8h) ✓
  └─ Performance framework (40h) — start
     
Week 2:
  ├─ Performance framework continued (40h) ✓
  ├─ Mobile lab setup (30h) — start
  ├─ Security coordination (12h) ✓
  └─ API error tests (16h) — start

Week 3:
  ├─ Mobile lab setup continued (30h) ✓
  ├─ API error tests continued (16h) ✓
  └─ Test automation expansion (24h) ✓

Week 4:
  ├─ Deprecations (4h) ✓
  └─ Accessibility + assistive tech (16h) — start

Week 5:
  ├─ Accessibility continued (16h) ✓
  └─ Chaos testing skill (40h) — start

Week 6:
  ├─ Chaos testing continued (40h) ✓
  └─ Testing & validation (20h) ✓
```

---

## Success Metrics: How to Measure Improvement

### Metric 1: Defect Prevention Rate
**Current:** 30-50% miss rate (4-10 defects undiscovered)  
**Target:** <20% miss rate (2-3 defects undiscovered)  
**How to Measure:** 
- Run next feature through improved testing
- Compare defects found during testing vs post-launch
- Expected: 50% reduction in post-launch issues

### Metric 2: Testing Timeline
**Current:** Phase 7 takes 7 days  
**Target:** Phase 4-7 distributed (Phase 4: 2 days mobile, Phase 7: 5 days focused testing)  
**How to Measure:** Track testing cycle duration for next feature

### Metric 3: Loop Count
**Current:** 3 loops across 9 phases (0.33/phase)  
**Target:** <2 loops (accessibility, mobile earlier) (0.22/phase)  
**How to Measure:** Document loops in next project

### Metric 4: Team Confidence
**Current:** 8.6/10  
**Target:** 9.2/10 (improvements increase confidence)  
**How to Measure:** Team survey after next feature

---

## Who Does What

| Role | Phase 1 | Phase 2 | Phase 3 |
|------|---------|---------|---------|
| **UX Lead** | Accessibility refactor (8h) | Mobile testing validation | Assistive tech testing (16h) |
| **QAE Lead** | Performance framework (40h) | API testing, Automation (40h) | Chaos skill, Validation (60h) |
| **SDE Security** | — | Security coordination (6h) | — |
| **DevOps** | — | Mobile lab setup (15h) | Performance monitoring |
| **PM** | — | — | Update toolkit docs (4h) |

---

## Budget & Resources

### New Resources Needed
- **Mobile device lab:** $500 setup + $50/month
- **BrowserStack license:** $30/month
- **Performance testing tools:** No additional cost (use existing)
- **Personnel:** ~210 hours (5.25 person-weeks)

### Cost Estimate
- Equipment: $680
- Personnel: 210 hours × $150/hour = $31,500
- **Total:** ~$32,000

### ROI
- **Benefit:** Prevent 1-2 post-launch issues per feature
- **Cost of post-launch issue:** $50K-$200K (emergency fixes, reputation)
- **Expected ROI:** 2-3x payback on first feature with improvements

---

## Risk Mitigation

### Risk 1: Performance Framework Takes Longer
**Mitigation:** Use existing tools (tc, locust, k6) vs building from scratch  
**Impact:** Reduce 40h → 25h

### Risk 2: Mobile Lab Setup Delayed
**Mitigation:** Use BrowserStack as backup (cloud-based testing)  
**Impact:** Can proceed without physical lab temporarily

### Risk 3: Team Over-committed
**Mitigation:** Run Phase 1 (2 weeks) on current project, Phase 2-3 (4 weeks) on next feature  
**Impact:** Stagger improvements, don't overload team

---

## Approval & Signoff

**Timeline:** Start immediately (Week 1)  
**Owner:** QAE Lead (orchestrates improvements)  
**Dependencies:** Access to mobile devices, CI/CD infrastructure, team bandwidth  
**Success Criteria:** 15% improvement in defect prevention by end of Week 6

**Recommendation:** ✅ **START NOW** — Phase 1 (2 weeks) has high ROI, low risk

---

## Next Steps

1. ✅ **Week 1:** Kick off accessibility + performance improvements
2. ✅ **Week 2:** Mobile lab operational, security coordination in place
3. ✅ **Week 3-4:** Testing expansions deployed
4. ✅ **Week 5-6:** Chaos testing skill + validation complete
5. ✅ **Week 7+:** Use improved skills on next feature, measure results

**Start with Phase 1 improvements immediately. Estimated 2-week sprint to get accessibility and mobile testing working.**
