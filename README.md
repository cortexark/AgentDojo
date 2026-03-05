# AgentDojo

**56 AI skills across 5 domains for Claude Code** — Product Management, Principal Engineering, Senior SDE, Quality Assurance, and UI/UX Design.

One person. Entire engineering org.

```
/sde-tdd my-feature          # Write code test-first
/gap-analyst                 # Find product gaps competitors have
/ux-design-system            # Build a full design system
/qae-security                # OWASP Top 10 security scan
/pe-tech-strategy scaling    # Write engineering strategy
/orchestrator                # Run the full 9-phase SDLC
```

---

## What Is This?

AgentDojo is a skill system for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Each skill is a standalone agent — type a slash command and it reads your codebase, analyzes the problem, and produces real output (code, docs, designs, test plans).

**Not a framework. Not a library. Just skills you install and use.**

---

## Quick Start

```bash
# Clone
git clone https://github.com/mission-agi/AgentDojo.git

# Copy slash commands to Claude
cp -r AgentDojo/claude/commands/ ~/.claude/commands/

# Copy orchestrator
mkdir -p ~/.claude/skills/orchestrator
cp AgentDojo/orchestrator/SKILL.md ~/.claude/skills/orchestrator/SKILL.md

# Copy domain agents
mkdir -p ~/.claude/skills/agents
cp AgentDojo/agents/*.md ~/.claude/skills/agents/

# Done. Open Claude Code and type any skill command.
```

### Verify It Works

```bash
claude
# Then type:
/sde-tdd my-feature
```

If the skill loads, you're good.

### Requirements

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI
- A project repository to work in

---

## All 60 Commands

### Product Management (11 skills)

| Command | What It Does |
|---------|-------------|
| `/gap-analyst` | Find product gaps, deduplicate against backlog, score with WINNING filter |
| `/prd-generator [feature]` | Generate structured PRDs, file as GitHub Issues |
| `/research-agent [company]` | Deep competitor profiling — features, pricing, sentiment |
| `/discovery-validator [idea]` | Turn ideas into testable hypotheses |
| `/customer-research [topic]` | Interview scripts, personas, jobs-to-be-done |
| `/experiment-designer [experiment]` | A/B test plans, hypothesis cards, cohort analysis |
| `/prioritization-engine` | RICE/Kano/MoSCoW/ICE scoring, outcome-based roadmaps |
| `/stakeholder-communicator [type]` | Status reports, stakeholder maps, decision logs |
| `/metrics-advisor` | North star metrics, metric trees, OKR templates |
| `/pivot-analyzer` | PMF signal assessment, pivot type mapping |
| `/buyer-psychology [segment]` | Buyer profiles, cognitive biases, switching forces |

### Principal Engineering (11 skills)

| Command | What It Does |
|---------|-------------|
| `/tech-strategy [topic]` | Engineering strategy & vision, strategy kernel |
| `/architecture-reviewer [RFC]` | RFC review, ADR writing, design quality assessment |
| `/technical-quality [system]` | 7-tier quality progression, DORA metrics, tech debt |
| `/migration-planner [migration]` | De-Risk/Enable/Finish framework for migrations |
| `/leverage-analyzer [situation]` | Impact/time analysis, anti-pattern detection |
| `/org-health [concern]` | Team state diagnosis, chain-link bottleneck analysis |
| `/influence-navigator [situation]` | Nemawashi, radiating intent, stakeholder alignment |
| `/decision-facilitator [topic]` | Decision classification, facilitation templates |
| `/mentorship-sponsorship [person]` | Growth plans, sponsorship playbook, feedback |
| `/incident-reliability [incident]` | Post-mortems, reliability reviews, on-call optimization |
| `/career-navigator [goal]` | Staff+ archetypes, promotion packets |

### Senior SDE (11 skills)

| Command | What It Does |
|---------|-------------|
| `/sde-tdd [feature]` | Red-green-refactor, testing pyramid, test doubles |
| `/sde-code-craftsman [topic]` | Clean code, DRY, naming, guard clauses |
| `/sde-system-design [system]` | 4-step framework, CAP theorem, trade-off analysis |
| `/sde-architecture [topic]` | SOLID principles, clean architecture layers |
| `/sde-data-systems [topic]` | Data models, replication, partitioning, consistency |
| `/sde-requirements [feature]` | Elicitation, specification, traceability matrices |
| `/sde-systems-thinking [system]` | Feedback loops, leverage points, system archetypes |
| `/sde-ml-design [system]` | ML pipelines, feature stores, model serving |
| `/sde-debugging [bug]` | Systematic debugging, root cause analysis |
| `/sde-estimation [project]` | PERT estimation, Brooks's Law, risk buffers |
| `/sde-code-review [PR]` | Review checklists, SOLID compliance, security |

### Quality Assurance (11 skills)

| Command | What It Does |
|---------|-------------|
| `/qae-test-strategy [project]` | Risk-based test strategies, coverage models |
| `/qae-test-plan [release]` | Test plans with entry/exit criteria |
| `/qae-exploratory [feature]` | Session-based exploratory testing, charters |
| `/qae-cicd-pipeline [project]` | Pipeline design, quality gates, deployment strategies |
| `/qae-automation [project]` | Framework selection, automation pyramid, ROI |
| `/qae-api-testing [API]` | REST/GraphQL testing, contract testing |
| `/qae-performance [system]` | Load/stress/soak testing, capacity planning |
| `/qae-security [system]` | OWASP Top 10, STRIDE threat modeling |
| `/qae-test-data [project]` | Data generation, masking, synthetic data |
| `/qae-defect-management [project]` | Bug lifecycle, root cause analysis (5 Whys) |
| `/qae-quality-metrics [release]` | Coverage metrics, defect density, release readiness |

### UI/UX Design (11 skills)

| Command | What It Does |
|---------|-------------|
| `/ux-design-system [project]` | Atomic Design, design tokens, component maturity |
| `/ux-visual-hierarchy [page]` | 8pt grid, spacing scales, Gestalt principles |
| `/ux-typography [project]` | Type scales, font pairing, clamp() fluid sizing |
| `/ux-color-system [project]` | HSL palettes, WCAG contrast, dark mode tokens |
| `/ux-component-design [component]` | State matrices, all states + sizes |
| `/ux-landing-page [product]` | Hero patterns, CTA hierarchy, conversion optimization |
| `/ux-interaction-design [component]` | Micro-interactions, CSS timing, motion systems |
| `/ux-responsive [page]` | Mobile-first CSS, breakpoints, container queries |
| `/ux-dashboard [dashboard]` | Chart selection, KPI cards, data tables |
| `/ux-accessibility [page]` | WCAG 2.2 compliance, keyboard nav, ARIA |
| `/ux-review [design]` | Nielsen's 10 Heuristics, scoring rubrics |

### Orchestrators (5 commands)

| Command | What It Does |
|---------|-------------|
| `/pm-orchestrator [goal]` | Chain all 11 PM skills in sequence |
| `/pe-orchestrator [goal]` | Chain all 11 PE skills in sequence |
| `/sde-orchestrator [goal]` | Chain all 11 SDE skills in sequence |
| `/qae-orchestrator [goal]` | Chain all 11 QAE skills in sequence |
| `/ux-orchestrator [goal]` | Chain all 11 UX skills in sequence |
| `/orchestrator [feature]` | **Master Orchestrator** — 9-phase SDLC across all domains |

---

## How It Works

### Skills Read Your Code

Every skill reads your actual codebase. `/sde-code-review` reads your PR diffs. `/qae-security` scans your source files. `/ux-accessibility` audits your HTML. No dummy output — real analysis of real code.

### Skills Write Real Output

Skills produce files in domain-specific directories:

```
pm/    — PRDs, gap analyses, competitor profiles, experiment briefs
pe/    — Strategy docs, ADRs, quality assessments, migration plans
sde/   — Architecture reviews, TDD sessions, system designs
qae/   — Test strategies, CI/CD configs, security reports
ux/    — Design tokens, component specs, accessibility audits
```

### Skills Chain Together

Output from one skill feeds the next:

```
Research Agent → Gap Analyst → PRD Generator → GitHub Issues
                                    ↓
                        UX Design System → Component Design
                                    ↓
                           SDE TDD → Code Review
                                    ↓
                        QAE Test Strategy → CI/CD Pipeline
```

### Master Orchestrator

The `/orchestrator` command runs the full product lifecycle in 9 phases:

```
Phase 1: Discovery        — PM research, gap analysis
Phase 2: Strategy          — PE tech strategy, UX design system
Phase 3: Architecture      — PE architecture review
Phase 4: Requirements      — PM PRD, SDE requirements
Phase 5: Design            — UX components, SDE system design
Phase 6: Implementation    — SDE TDD, code craftsman (with quality gates)
Phase 7: Quality           — QAE test strategy, security, performance
Phase 8: Integration       — Cross-domain validation
Phase 9: Launch            — Metrics, monitoring, retrospective
```

4 user decision gates at strategic boundaries. Automatic skill loop exit criteria. Cross-domain feedback loops (SDE finds bugs → QAE validates → SDE fixes).

---

## Alternative Installation

### As a Claude Plugin

```bash
git clone https://github.com/mission-agi/AgentDojo.git
mkdir -p ~/.claude/plugins/cache/local/agentdojo/1.0.0
cp -r AgentDojo/* ~/.claude/plugins/cache/local/agentdojo/1.0.0/
```

### Directly in a Project

```bash
git clone https://github.com/mission-agi/AgentDojo.git .agentdojo
cp -r .agentdojo/claude/commands/ .claude/commands/
```

---

## Project Structure

```
CLAUDE.md            — Project instructions for Claude Code (loaded automatically)
README.md            — This file (for humans on GitHub)
agents/              — Domain agent definitions (pm, pe, sde, qae, ux, orchestrator)
claude/commands/     — 60 slash commands (one per skill + orchestrators)
orchestrator/        — Master orchestrator engine (SKILL.md, routing, coordination)
pm/                  — Product Management skills + example outputs
pe/                  — Principal Engineering skills
sde/                 — Senior SDE skills
qae/                 — Quality Assurance skills
ux/                  — UI/UX Design skills
```

### About CLAUDE.md

`CLAUDE.md` is a special file that Claude Code reads automatically when working in a project. It contains the skill conventions, data directory rules, domain integration maps, and accountability standards that Claude needs to use the skills correctly.

- **README.md** = for you, reading on GitHub
- **CLAUDE.md** = for Claude Code, loaded as project context

Both are needed. Don't delete CLAUDE.md — without it, Claude won't know how to use the skills properly.

---

## License

All Rights Reserved. See [LICENSE](LICENSE).
