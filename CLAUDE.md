# TaskPilot — PM, PE, SDE, QAE & UX Skills

## Overview
TaskPilot is a modular skill system for Claude Code, covering **Product Management**, **Principal Engineering**, **Senior SDE**, **Quality Assurance Engineering**, and **UI/UX Design** domains. 56 skills across 5 domains — each is a standalone agent that can be pointed at any product repository or engineering organization.

## Skills (invoke with `/skill-name`)

| Skill | Command | What It Does |
|-------|---------|-------------|
| Gap Analyst | `/gap-analyst` | Identifies product gaps, deduplicates against backlog, scores with WINNING filter |
| PRD Generator | `/prd-generator [feature]` | Generates structured PRDs and files as GitHub Issues |
| Research Agent | `/research-agent [company]` | Deep competitor profiling with features, pricing, sentiment |
| Discovery Validator | `/discovery-validator [idea]` | Turns ideas into testable hypotheses, designs cheapest experiments |
| Customer Research | `/customer-research [topic]` | Research program design, interview scripts, personas, JTBD |
| Experiment Designer | `/experiment-designer [experiment]` | Hypothesis cards, A/B test plans, cohort analysis, innovation accounting |
| Prioritization Engine | `/prioritization-engine` | RICE/Kano/MoSCoW/ICE scoring, outcome-based roadmaps |
| Stakeholder Communicator | `/stakeholder-communicator [type]` | Status reports, stakeholder maps, decision logs, alignment docs |
| Metrics Advisor | `/metrics-advisor` | North star metrics, metric trees, OKR templates, vanity metric audits |
| Pivot Analyzer | `/pivot-analyzer` | PMF signal assessment, pivot type mapping, decision reports |
| Buyer Psychology | `/buyer-psychology [segment]` | Buyer profiles, cognitive biases, switching forces, churn psychology |

## How Skills Connect

```
Research Agent --> Gap Analyst --> PRD Generator --> GitHub Issues
     |                 |
     |                 +-- uses WINNING Filter (6-criterion scoring)
     |                 +-- deduplicates against existing issues
     |
     +-- writes to pm/competitors/

Discovery Validator --> Experiment Designer --> Metrics Advisor
                                                      |
Customer Research ---------------------------------> feeds all skills

Prioritization Engine <-- reads from gaps, PRDs, metrics
Stakeholder Communicator <-- reads from all outputs
Pivot Analyzer <-- reads metrics, experiments, market data
Buyer Psychology <-- feeds Discovery, PRD, Gap Analysis
```

## Data Directory Convention

All skills read from and write to `pm/` in the working directory:

```
pm/
  product/inventory.md          # Current product features
  product/architecture.md       # Technical constraints
  competitors/[company].md      # Competitor profiles
  gaps/[YYYY-MM-DD]-analysis.md # Gap analysis reports
  prds/[feature-name].md        # PRD documents
  requests/*.md                 # Feature requests / GitHub issue cache
  experiments/*.md              # Experiment briefs and results
  metrics/*.md                  # Metric trees, OKRs, dashboards
  research/*.md                 # Interview guides, personas, JTBD
  stakeholder/*.md              # Status updates, decision logs
  cache/last-updated.json       # Staleness tracker
```

## WINNING Filter (Scoring Framework)

6 dimensions, max 60 points. Hybrid scoring: AI suggests Pain + Timing, user scores Execution + Fit + Revenue + Moat.

| Score | Action | Meaning |
|-------|--------|---------|
| 40-60 | FILE | High conviction — create issue, add to roadmap |
| 25-39 | WAIT | Monitor — revisit next quarter |
| 0-24 | SKIP | Not worth pursuing now |

## PM Conventions
- Skills save outputs to `pm/` subdirectories with descriptive filenames
- Date-based filenames use `YYYY-MM-DD` format
- Competitor profiles include `Last Updated` timestamps
- Every scored opportunity includes evidence for each criterion
- Skills reference each other's outputs (gap analysis references competitor profiles, PRDs reference gap scores)

---

## Principal Engineer Skills (invoke with `/skill-name`)


| Skill | Command | What It Does |
|-------|---------|-------------|
| Tech Strategy | `/tech-strategy [topic]` | Engineering strategy & vision, strategy kernel, bad strategy detection |
| Architecture Reviewer | `/architecture-reviewer [RFC/design]` | RFC review, design quality assessment, ADR writing, rough consensus |
| Technical Quality | `/technical-quality [system]` | 7-tier quality progression, DORA metrics, tech debt management |
| Migration Planner | `/migration-planner [migration]` | De-Risk/Enable/Finish framework for large-scale migrations |
| Leverage Analyzer | `/leverage-analyzer [situation]` | Impact/time analysis, anti-pattern detection, high-leverage activity catalog |
| Org Health | `/org-health [concern]` | Team state diagnosis, sizing rules, chain-link bottleneck analysis |
| Influence Navigator | `/influence-navigator [situation]` | Nemawashi, radiating intent, stakeholder alignment, Three Maps |
| Decision Facilitator | `/decision-facilitator [topic]` | Decision classification, facilitation templates, unstuck techniques |
| Mentorship & Sponsorship | `/mentorship-sponsorship [person]` | Growth plans, sponsorship playbook, feedback frameworks |
| Incident & Reliability | `/incident-reliability [incident]` | Post-mortems, reliability reviews, operational burden reduction |
| Career Navigator | `/career-navigator [goal]` | Staff+ archetypes, promotion packets, career self-assessment |

## How PE Skills Connect

```
tech-strategy --> architecture-reviewer --> decision-facilitator
      |                                          |
      +-- Strategy Kernel                        +-- Rough Consensus
      +-- Bad Strategy Detection                 +-- Unstuck Techniques

technical-quality --> leverage-analyzer --> migration-planner
      |                    |
      +-- 7-Tier Quality   +-- Impact/Time Lens
      +-- DORA Metrics     +-- Anti-Pattern Detection

org-health --> influence-navigator --> decision-facilitator
      |              |
      +-- 4 Team States    +-- Nemawashi
      +-- Chain-Link       +-- Radiating Intent

mentorship-sponsorship --> career-navigator --> leverage-analyzer
      |                         |
      +-- Sponsorship Playbook  +-- 4 Archetypes
      +-- Feedback Framework    +-- Promotion Packets

incident-reliability --> technical-quality --> org-health
```

## PE Data Directory Convention

All PE skills read from and write to `pe/` in the working directory:

```
pe/
  strategy/          # Tech strategy and vision documents
  architecture/      # RFCs, ADRs, design reviews
  quality/           # Quality assessments, DORA metrics, debt inventories
  migrations/        # Migration plans and tracking
  decisions/         # Decision records and facilitation docs
  org/               # Team health assessments, org analysis
  mentorship/        # Mentorship plans, feedback records
  incidents/         # Post-mortems, reliability reviews
  career/            # Promotion packets, self-assessments, growth plans
```

## PE Conventions
- Skills save outputs to `pe/` subdirectories with descriptive filenames
- Templates use markdown with structured tables for assessments
- Skills cross-reference each other (org-health informs leverage-analyzer, etc.)
- Decision records include reasoning, not just outcomes

---

## Senior SDE Skills (invoke with `/sde-*`)


**Core Philosophy: TDD-First.** Every feature starts with a failing test. Every bug fix starts with a test that reproduces it.

| Skill | Command | What It Does |
|-------|---------|-------------|
| Code Craftsman | `/sde-code-craftsman [topic]` | Clean code, DRY, naming, guard clauses, construction quality |
| TDD | `/sde-tdd [feature]` | Red-green-refactor, testing pyramid, test doubles, FIRST principles |
| System Design | `/sde-system-design [system]` | 4-step framework, estimation, CAP theorem, trade-off analysis |
| Architecture | `/sde-architecture [topic]` | SOLID principles, clean architecture layers, dependency rule |
| Data Systems | `/sde-data-systems [topic]` | Data models, replication, partitioning, consistency, batch/stream |
| Requirements | `/sde-requirements [feature]` | Elicitation, specification, validation, traceability matrices |
| Systems Thinking | `/sde-systems-thinking [system]` | Feedback loops, leverage points, system archetypes, Brooks's Law |
| ML Design | `/sde-ml-design [system]` | ML pipelines, feature stores, model serving, monitoring |
| Debugging | `/sde-debugging [bug]` | Systematic debugging, root cause analysis, defensive programming |
| Estimation | `/sde-estimation [project]` | PERT estimation, Brooks's Law, scheduling, risk buffers |
| Code Review | `/sde-code-review [PR]` | Review checklists, quality gates, SOLID compliance, security |

## How SDE Skills Connect

```
sde-tdd ←→ sde-code-craftsman ←→ sde-code-review
  |              |                      |
  |              +-- DRY, Guard Clauses +-- SOLID Compliance
  |              +-- Naming, PPP        +-- Quality Gates
  |
  +-- Red-Green-Refactor drives ALL code writing

sde-system-design --> sde-architecture --> sde-data-systems
       |                    |                    |
       +-- 4-Step Framework +-- Clean Layers     +-- DDIA Patterns
       +-- Estimation       +-- SOLID            +-- Replication/Partitioning

sde-requirements --> sde-estimation --> sde-systems-thinking
       |                  |                  |
       +-- Elicitation    +-- PERT/Brooks   +-- Feedback Loops
       +-- Traceability   +-- Risk Buffers  +-- Leverage Points

sde-ml-design --> sde-system-design --> sde-debugging
```

## SDE Data Directory Convention

All SDE skills read from and write to `sde/` in the working directory:

```
sde/
  code/            # Code quality assessments
  tests/           # Test strategies, TDD session logs
  designs/         # System design documents
  architecture/    # Architecture reviews, ADRs, SOLID assessments
  data-systems/    # Data system designs
  requirements/    # Requirements docs, traceability matrices
  systems/         # Systems thinking analyses
  ml/              # ML system designs
  debugging/       # Bug analysis reports
  estimates/       # Project estimates, velocity tracking
  reviews/         # Code review reports
```

## SDE Conventions
- TDD is the primary way code gets written — every feature starts with a failing test
- All designs must include back-of-envelope estimation — quantify QPS, storage, bandwidth
- Every architecture decision must state the trade-off — what you gain AND what you lose
- Code quality follows the Boy Scout Rule — leave every file cleaner than you found it
- Skills cross-reference each other (TDD feeds code review, system design feeds architecture)

---

## QAE Skills (invoke with `/qae-*`)


**Core Philosophy: Quality is Everyone's Responsibility.** The QAE writes detailed test strategies, test plans, and CI/CD pipelines. Combines automated testing (speed) with exploratory testing (insight).

| Skill | Command | What It Does |
|-------|---------|-------------|
| Test Strategy | `/qae-test-strategy [project]` | Comprehensive test strategies, risk-based approaches, coverage models |
| Test Plan | `/qae-test-plan [release]` | Detailed test plans with scope, entry/exit criteria, deliverables |
| Exploratory Testing | `/qae-exploratory [feature]` | Session-based testing, charters, heuristics, risk-based exploration |
| CI/CD Pipeline | `/qae-cicd-pipeline [project]` | Pipeline design, quality gates, deployment strategies |
| Test Automation | `/qae-automation [project]` | Framework selection, automation pyramid, ROI analysis |
| API Testing | `/qae-api-testing [API]` | REST/GraphQL testing, contract testing, schema validation |
| Performance Testing | `/qae-performance [system]` | Load/stress/soak testing, capacity planning, bottleneck analysis |
| Security Testing | `/qae-security [system]` | OWASP Top 10, STRIDE threat modeling, vulnerability scanning |
| Test Data | `/qae-test-data [project]` | Data generation, masking, synthetic data, environment management |
| Defect Management | `/qae-defect-management [project]` | Bug lifecycle, root cause analysis, severity classification, metrics |
| Quality Metrics | `/qae-quality-metrics [release]` | Test coverage, defect density, dashboards, release readiness |

## How QAE Skills Connect

```
qae-test-strategy --> qae-test-plan --> qae-cicd-pipeline --> qae-automation
       |                    |                   |                   |
       +-- Risk-Based       +-- Entry/Exit     +-- Quality Gates   +-- Pyramid
       +-- Coverage Model   +-- Schedule       +-- Deployment      +-- ROI

qae-test-plan --> qae-exploratory --> qae-defect-management
                       |                      |
                       +-- Charters           +-- 5 Whys RCA
                       +-- SBET              +-- Severity/Priority

qae-api-testing --> qae-automation --> qae-cicd-pipeline
qae-performance --> qae-security --> qae-quality-metrics
       |                |                   |
       +-- Load/Stress  +-- OWASP Top 10   +-- Release Readiness
       +-- Budgets      +-- STRIDE         +-- Dashboards

qae-test-data ←→ qae-cicd-pipeline ←→ qae-automation
```

## QAE Data Directory Convention

All QAE skills read from and write to `qae/` in the working directory:

```
qae/
  strategies/     # Test strategy documents
  plans/          # Detailed test plans
  exploratory/    # Exploratory testing session logs
  pipelines/      # CI/CD pipeline designs
  automation/     # Automation framework plans, ROI analysis
  api/            # API test plans and contracts
  performance/    # Performance test plans and results
  security/       # Security test plans, threat models
  test-data/      # Test data strategies, data plans
  defects/        # Defect reports, RCA documents
  metrics/        # Quality dashboards, KPI reports
```

## QAE Conventions
- Test strategies are written BEFORE development begins
- CI/CD pipelines include quality gates at every stage
- Exploratory testing complements automation — both are required
- Every defect gets root cause analysis (5 Whys for S1/S2)
- Quality metrics drive action — track trends, not snapshots

## Cross-Domain Integration

| SDE Skill | QAE Skill | How They Connect |
|-----------|-----------|-----------------|
| `/sde-tdd` | `/qae-test-strategy` | TDD executes at unit level, strategy defines full scope |
| `/sde-requirements` | `/qae-test-plan` | Test plan traces back to requirements |
| `/sde-code-review` | `/qae-cicd-pipeline` | Pipeline enforces review + test gates |
| `/sde-tdd` | `/qae-automation` | Automation extends TDD to integration/E2E |
| `/sde-system-design` | `/qae-api-testing` | API tests validate system design contracts |
| `/sde-data-systems` | `/qae-performance` | Performance tests validate data system design |
| `/sde-architecture` | `/qae-security` | Security tests validate architecture boundaries |
| `/sde-code-review` | `/qae-quality-metrics` | Metrics inform review priorities |

---

## UI/UX Designer Skills (invoke with `/ux-*`)


**Core Philosophy: Design is Communication.** Every skill contains concrete CSS values, pixel sizes, ratios, and production-ready patterns — not surface-level theory.

| Skill | Command | What It Does |
|-------|---------|-------------|
| Design System | `/ux-design-system [project]` | Atomic Design hierarchy, design tokens, component maturity model |
| Visual Hierarchy | `/ux-visual-hierarchy [page]` | 8pt grid, spacing scales, Gestalt principles, whitespace mastery |
| Typography | `/ux-typography [project]` | Modular type scales, font pairing, clamp() fluid sizing, vertical rhythm |
| Color System | `/ux-color-system [project]` | HSL palettes, WCAG contrast, dark mode tokens, 60-30-10 rule |
| Component Design | `/ux-component-design [component]` | State matrices, button/form/card/modal design, all states + sizes |
| Landing Page | `/ux-landing-page [product]` | Hero patterns, CTA hierarchy, social proof, conversion optimization |
| Interaction Design | `/ux-interaction-design [component]` | Micro-interactions, CSS timing, motion systems, loading states |
| Responsive | `/ux-responsive [page]` | Mobile-first CSS, breakpoints, container queries, touch targets |
| Dashboard | `/ux-dashboard [dashboard]` | Chart selection, KPI cards, data tables, filter patterns |
| Accessibility | `/ux-accessibility [page]` | WCAG 2.2 compliance, keyboard nav, ARIA, focus management |
| Design Review | `/ux-review [design]` | Nielsen's 10 Heuristics, scoring rubrics, critique frameworks |

## How UX Skills Connect

```
ux-design-system --> ux-color-system --> ux-typography --> ux-visual-hierarchy
       |                   |                  |                   |
       +-- Atomic Design   +-- HSL Palettes   +-- Type Scales    +-- 8pt Grid
       +-- Design Tokens   +-- Dark Mode      +-- clamp()       +-- Gestalt

ux-component-design --> ux-interaction-design --> ux-accessibility
       |                        |                       |
       +-- State Matrices      +-- CSS Timing          +-- WCAG 2.2
       +-- All States          +-- Motion              +-- Keyboard Nav

ux-landing-page --> ux-responsive --> ux-dashboard
       |                  |                |
       +-- Hero Patterns  +-- Mobile-First +-- Chart Selection
       +-- CTA/Social     +-- Breakpoints  +-- KPI Cards

ux-review <-- reads from all UX outputs for design critique
```

## UX Data Directory Convention

All UX skills read from and write to `ux/` in the working directory:

```
ux/
  design-systems/    # Token files, component inventories, maturity audits
  layouts/           # Grid templates, spacing analyses, hierarchy maps
  typography/        # Type scales, font audits, pairing decisions
  colors/            # Palette definitions, contrast audits, dark mode tokens
  components/        # Component specs, state matrices, a11y checklists
  landing-pages/     # Hero designs, conversion audits, section blueprints
  interactions/      # Motion specs, timing values, gesture patterns
  responsive/        # Breakpoint systems, device audits, fluid calculations
  dashboards/        # Chart specs, KPI layouts, data table designs
  accessibility/     # WCAG audits, keyboard maps, ARIA implementations
  reviews/           # Design critiques, heuristic scores, debt assessments
```

## UX Conventions
- Every design deliverable includes concrete CSS values — not just visual descriptions
- Accessibility (WCAG 2.2 AA) is a baseline requirement in every component and page design
- Design tokens follow the 3-tier model: Reference → System → Component
- Components always specify all states: default, hover, active, focus, disabled, loading, error, skeleton
- Skills cross-reference each other (design system tokens feed color/typography, components feed accessibility)

---

## Domain Orchestrators (invoke with `/*-orchestrator`)

5 orchestrators that chain domain skills into guided workflows. Each presents a workflow menu, manages data directory context, supports skip/jump, and recommends cross-domain skills.

| Orchestrator | Command | Domain | Skills Chained |
|-------------|---------|--------|---------------|
| PM Orchestrator | `/pm-orchestrator [goal]` | Product Management | 11 PM skills via `pm/` |
| PE Orchestrator | `/pe-orchestrator [goal]` | Principal Engineering | 11 PE skills via `pe/` |
| SDE Orchestrator | `/sde-orchestrator [goal]` | Senior SDE | 11 SDE skills via `sde/` |
| QAE Orchestrator | `/qae-orchestrator [goal]` | Quality Assurance | 11 QAE skills via `qae/` |
| UX Orchestrator | `/ux-orchestrator [goal]` | UI/UX Design | 11 UX skills via `ux/` |

### How Orchestrators Work
1. **Pick a workflow** — each orchestrator offers 5 common workflows (e.g., "Feature Build", "Design Sprint")
2. **Sequential execution** — skills run in order, each skill's output feeds the next via data directories
3. **Skip/jump** — skip completed steps or jump to any skill in the sequence
4. **Cross-domain** — orchestrators recommend skills from other domains when relevant
5. **Session tracking** — progress is displayed as a checklist showing completed/current/pending steps

### Cross-Domain Integration via Orchestrators

```
pm-orchestrator ──→ ux-orchestrator ──→ sde-orchestrator ──→ qae-orchestrator
       |                   |                   |                    |
  PRD defines         UX designs          SDE implements       QAE validates
  requirements        interfaces          features             quality
       |                   |                   |                    |
       └───── pe-orchestrator (strategic oversight, architecture, quality) ─────┘
```

| From | To | When |
|------|----|------|
| PM → UX | After PRD is written | Design the interface for the feature |
| PM → SDE | After PRD + UX design | Implement the feature with TDD |
| UX → SDE | After component specs | Implement components with design tokens |
| UX → QAE | After accessibility audit | Add a11y assertions to test automation |
| SDE → QAE | After implementation | Run test strategy, performance, security |
| QAE → SDE | After defect analysis | Fix bugs with TDD (reproduce → test → fix) |
| PE → All | Strategic decisions | Architecture reviews, tech strategy, migrations |

## Full Skill Inventory

**60 skills across 5 domains + 5 orchestrators:**

| Domain | Prefix | Skills | Orchestrator |
|--------|--------|--------|-------------|
| Product Management | `pm-*` / named | 11 | `/pm-orchestrator` |
| Principal Engineering | `pe-*` / named | 11 | `/pe-orchestrator` |
| Senior SDE | `sde-*` | 11 | `/sde-orchestrator` |
| Quality Assurance | `qae-*` | 11 | `/qae-orchestrator` |
| UI/UX Design | `ux-*` | 11 | `/ux-orchestrator` |
| **Total** | | **55 skills + 5 orchestrators = 60 commands** | |

---

## CRITICAL: Accountability & Transparency Standards

**NEVER conflate different stages of work. Always use these explicit labels in every response:**

### Four Clear States (Use in Every Chat)

| State | Meaning |
|-------|---------|
| **PLAN** | "I will do X" — intention stated but not yet started |
| **IMPLEMENT** | Actively building/creating something right now |
| **COMPLETED** | Work is finished, saved to disk, ready to use |
| **EXECUTED** | Work tested, verified working, output shown |

### Rules for Honest Communication

1. **NEVER say "built"** if you only created config files → that's IMPLEMENT, not COMPLETED
2. **NEVER say "will run"** without actually running it → that's a PLAN you didn't execute
3. **NEVER imply EXECUTED** when you mean COMPLETED → test it first
4. **ALWAYS state gaps immediately** — if something doesn't work, say so upfront
5. **ALWAYS provide todo list** with explicit statuses in every chat response

### Example of Honest Communication

❌ **Wrong:**
> "I built the coordination service and will use it to deliver OAuth2"

✅ **Right:**
```
## Todo — OAuth2 Delivery

**PLAN:** Create coordination service infrastructure and execute master orchestrator

**IMPLEMENT:**
- ✅ Created orchestration/coordination-service.md (452 lines)
- ✅ Created .project/skill-manifest.json (784 lines)
- ✅ Created orchestration/routing-rules.json (291 lines)

**COMPLETED:**
- ✅ All infrastructure files saved to disk and ready
- ⚠️ Master orchestrator skill exists but implementation status UNKNOWN

**EXECUTED:**
- ❌ Master orchestrator NOT YET TESTED with OAuth2
- ⚠️ Individual domain orchestrators (/pm:orchestrator, etc.) confirmed working

**GAPS:**
- Master orchestrator may not be fully implemented
- Need to test before claiming it works
```

### Every Chat Must Include

1. **Clear todo list** with PLAN/IMPLEMENT/COMPLETED/EXECUTED labels
2. **Status indicators** (✅ done, ⏳ in progress, ❌ not started, ⚠️ unknown)
3. **Explicit gaps** — what doesn't work yet
4. **Next steps** — what comes after current work
