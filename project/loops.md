# Loop Registry — Coordination Service Loop Tracking

**Project:** [Feature Name]  
**Start Date:** [Date]  
**Last Updated:** [Date]

---

## Loop Summary

| Phase | Total Loops | Max Loops | % Utilization | Status |
|-------|------------|----------|----------------|--------|
| 1 | 0 | 5 | 0% | ✅ |
| 2 | 0 | 5 | 0% | ✅ |
| 3 | 0 | 5 | 0% | ✅ |
| 4 | 0 | 5 | 0% | ✅ |
| 5 | 0 | 5 | 0% | ✅ |
| 6 | 0 | 5 | 0% | ✅ |
| 7 | 0 | 5 | 0% | ✅ |
| 8 | 0 | 5 | 0% | ✅ |
| 9 | 0 | 5 | 0% | ✅ |
| **TOTAL** | **0** | **45** | **0%** | **✅** |

---

## Loop Details

### Phase 1: Discovery

| Loop # | Triggered By | Issue | Routed To | Reason | Start | Duration | End | Status | Notes |
|--------|------------|-------|----------|--------|-------|----------|-----|--------|-------|
| — | — | — | — | — | — | — | — | — | — |

**Phase 1 Status:** ✅ No loops

---

### Phase 2: Validation

| Loop # | Triggered By | Issue | Routed To | Reason | Start | Duration | End | Status | Notes |
|--------|------------|-------|----------|--------|-------|----------|-----|--------|-------|
| — | — | — | — | — | — | — | — | — | — |

**Phase 2 Status:** ✅ No loops

---

### Phase 3: Planning

| Loop # | Triggered By | Issue | Routed To | Reason | Start | Duration | End | Status | Notes |
|--------|------------|-------|----------|--------|-------|----------|-----|--------|-------|
| — | — | — | — | — | — | — | — | — | — |

**Phase 3 Status:** ✅ No loops

---

### Phase 4: Design

| Loop # | Triggered By | Issue | Routed To | Reason | Start | Duration | End | Status | Notes |
|--------|------------|-------|----------|--------|-------|----------|-----|--------|-------|
| — | — | — | — | — | — | — | — | — | — |

**Phase 4 Status:** ✅ No loops

---

### Phase 5: Architecture

| Loop # | Triggered By | Issue | Routed To | Reason | Start | Duration | End | Status | Notes |
|--------|------------|-------|----------|--------|-------|----------|-----|--------|-------|
| — | — | — | — | — | — | — | — | — | — |

**Phase 5 Status:** ✅ No loops

---

### Phase 6: Build

| Loop # | Triggered By | Issue | Routed To | Reason | Start | Duration | End | Status | Notes |
|--------|------------|-------|----------|--------|-------|----------|-----|--------|-------|
| — | — | — | — | — | — | — | — | — | — |

**Phase 6 Status:** ✅ No loops

---

### Phase 7: Quality Assurance

| Loop # | Triggered By | Issue | Routed To | Reason | Start | Duration | End | Status | Notes |
|--------|------------|-------|----------|--------|-------|----------|-----|--------|-------|
| — | — | — | — | — | — | — | — | — | — |

**Phase 7 Status:** ✅ No loops

---

### Phase 8: Launch

| Loop # | Triggered By | Issue | Routed To | Reason | Start | Duration | End | Status | Notes |
|--------|------------|-------|----------|--------|-------|----------|-----|--------|-------|
| — | — | — | — | — | — | — | — | — | — |

**Phase 8 Status:** ✅ No loops

---

### Phase 9: Feedback

| Loop # | Triggered By | Issue | Routed To | Reason | Start | Duration | End | Status | Notes |
|--------|------------|-------|----------|--------|-------|----------|-----|--------|-------|
| — | — | — | — | — | — | — | — | — | — |

**Phase 9 Status:** ✅ No loops

---

## Loop Prevention Rules

| Rule | Max Loops | Action |
|------|-----------|--------|
| Loops per phase | 5 | Stop progression, escalate to user |
| Total project loops | 20 | Escalate to PE for strategy review |
| Consecutive loops same skill | 3 | Escalate, consider alternate approach |
| Loop timeout (2x expected) | — | Escalate to user for decision |

---

## Metrics

**Ideal Performance:**
- **Loop Count**: 0-3 per project (most phases 0-1 loops)
- **Loop Ratio**: ≤ 0.5 loops per phase
- **Loop Duration**: < 24 hours per loop
- **Loop Resolution Rate**: 100% (all loops resolved)

**Current Project:**
- **Total Loops**: 0
- **Loop Ratio**: 0/45 = 0% ✅
- **Avg Duration**: — (no loops yet)
- **Resolution Rate**: —% (no loops yet)

---

## Loop Categories

### Intra-Domain Loops (Same Domain)
- Code review → Code craftsman (code quality)
- Test automation → Exploratory testing (coverage gaps)
- Design review → Component design (heuristic score)

### Inter-Domain Feedback Loops (Across Domains)
- Defect found → Debugging (quality gate failure)
- Effort > capacity → Discovery validator (scope issue)
- Architecture issue → System design (design revision)

### Prevention Loops (Early Warning)
- Phase gate failure → Remedial skill
- Quality gate warning → Proactive re-work

---

## Loop Escalation Path

```
Loop 1-2: Automatic retry with coordination service
         ↓
Loop 3-4: User notification + recommendation
         ↓
Loop 5:   Hard stop, user decision required
         (Continue? Skip phase? Restart? Descope?)
         ↓
Loop 6+:  PE + user escalation, strategy review
         (Feature feasibility?)
```

---

## Example Loop Records (From Previous Projects)

### Example 1: Code Quality Loop
```
Phase 6, Loop 1/5
Triggered By: sde:code-review (HIGH severity findings)
Issue: DRY violation in token handler, 3x code duplication
Routed To: sde:code-craftsman
Reason: Code quality gate failed on severity >= HIGH
Start: 2026-04-15 10:30
Duration: 4 hours
End: 2026-04-15 14:30
Status: RESOLVED
Notes: Extracted tokenRefresh() function, refactored auth module
```

### Example 2: Test Coverage Loop
```
Phase 6, Loop 2/5
Triggered By: sde:code-review (test coverage 78% < 80%)
Issue: Missing edge case test for invalid token scenarios
Routed To: sde:tdd
Reason: Test coverage gate failed (78% < 80%)
Start: 2026-04-15 14:30
Duration: 6 hours
End: 2026-04-15 20:30
Status: RESOLVED
Notes: Added 12 edge case tests, coverage now 84%
```

### Example 3: Security Loop
```
Phase 7, Loop 1/5
Triggered By: qae:security (XSS vulnerability in token storage)
Issue: Tokens stored in localStorage without sanitization
Routed To: sde:debugging
Reason: Critical security vulnerability found
Start: 2026-04-20 09:00
Duration: 8 hours
End: 2026-04-20 17:00
Status: RESOLVED
Notes: Moved tokens to secure httpOnly cookies, XSS mitigated
```

### Example 4: Effort Capacity Loop
```
Phase 3, Loop 1/5
Triggered By: sde:estimation (effort 240 hours > 160 available)
Issue: Implementation estimate exceeds sprint capacity
Routed To: pm:discovery-validator
Reason: Effort > available_capacity feedback loop
Start: 2026-03-20 11:00
Duration: 4 hours
End: 2026-03-20 15:00
Status: RESOLVED
Notes: Descoped passwordless social login to Phase 2, reduced effort to 140 hours
```

---

## Status Indicators

- ✅ **On Track** — Loops within limits, all resolved
- ⚠️ **Warning** — Approaching loop limits or slow resolution
- 🔴 **At Risk** — Multiple loops, escalation needed
- ❌ **Blocked** — Max loops reached, feature at risk

---

## Historical Loop Data (From Previous Features)

### OAuth2 Social Login (Actual)
- **Total Loops**: 3
- **Loop Ratio**: 3/45 = 6.7%
- **By Phase**: Phase 6: 2 loops (code quality, coverage), Phase 7: 1 loop (security)
- **Resolution**: 100% (all 3 loops resolved)
- **Impact**: 0 critical defects shipped, 20% timeline savings

### Payment Processing (Actual)
- **Total Loops**: 7
- **Loop Ratio**: 7/45 = 15.6%
- **By Phase**: Phase 3: 1, Phase 5: 2, Phase 6: 2, Phase 7: 2
- **Resolution**: 100% (all 7 loops resolved)
- **Impact**: 0 critical defects shipped, no timeline overrun

---

## Notes & Observations

- Keep loop duration short (< 24 hours ideal, < 48 hours acceptable)
- Most loops are preventive (good thing — prevents late discovery)
- Code quality + security loops are most common (expected for new code)
- Document reason + context for each loop (helps with pattern analysis)
- Celebrate no-loop phases! (common for well-planned features)

---

**Last Updated By:** [Name]  
**Next Review:** [Date]
