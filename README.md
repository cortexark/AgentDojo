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
AgentDojo/
├── CLAUDE.md              # Claude Code project instructions (auto-loaded)
├── README.md              # This file
├── LICENSE                # All Rights Reserved
│
├── claude/commands/       # Slash commands (the skills you type)
│   ├── sde-tdd.md         #   /sde-tdd
│   ├── gap-analyst.md     #   /gap-analyst
│   ├── ux-design-system.md#   /ux-design-system
│   └── ... (60 files)     #   one file per skill + orchestrator
│
├── agents/                # Domain agent definitions
│   ├── pm.md              #   PM agent — routes to 11 PM skills
│   ├── pe.md              #   PE agent — routes to 11 PE skills
│   ├── sde.md             #   SDE agent — routes to 11 SDE skills
│   ├── qae.md             #   QAE agent — routes to 11 QAE skills
│   ├── ux.md              #   UX agent — routes to 11 UX skills
│   └── orchestrator.md    #   Master orchestrator agent
│
├── orchestrator/          # Master orchestrator engine
│   ├── SKILL.md           #   9-phase SDLC logic, gates, skill selection
│   ├── routing-rules.json #   Phase transitions, loop exit criteria
│   └── coordination-service.md  # Cross-domain handoff protocols
│
├── pm/                    # Product Management skill definitions
├── pe/                    # Principal Engineering skill definitions
├── sde/                   # Senior SDE skill definitions
├── qae/                   # Quality Assurance skill definitions
└── ux/                    # UI/UX Design skill definitions
```

### What Each Part Does

| Folder/File | What It Is | When You Need It | How To Use It |
|-------------|-----------|-------------------|---------------|
| `claude/commands/` | The slash commands themselves | **Always** — this is the core | Copy to `~/.claude/commands/` and type `/sde-tdd` in Claude Code |
| `CLAUDE.md` | Project context Claude reads automatically | **Always** — tells Claude the conventions | Lives in project root, Claude loads it on startup |
| `agents/` | Agent definitions for multi-skill orchestration | When using orchestrators (`/pm-orchestrator`, `/orchestrator`) | Copy to `~/.claude/skills/agents/` |
| `orchestrator/` | Master orchestrator engine | When running the full 9-phase SDLC (`/orchestrator`) | Copy to `~/.claude/skills/orchestrator/` |
| `pm/` `pe/` `sde/` `qae/` `ux/` | Skill definitions + example outputs | Reference — see how each skill is structured | Skills are read by the commands in `claude/commands/` |
| `project/` | Skill manifest | Internal routing metadata | Used by the orchestrator for skill dependency tracking |

### What You Actually Install

For most users, you only need to copy **3 things**:

```bash
# 1. Slash commands (required)
cp -r claude/commands/ ~/.claude/commands/

# 2. Orchestrator skill (if you want /orchestrator)
mkdir -p ~/.claude/skills/orchestrator
cp orchestrator/SKILL.md ~/.claude/skills/orchestrator/SKILL.md

# 3. Domain agents (if you want /pm-orchestrator, /sde-orchestrator, etc.)
mkdir -p ~/.claude/skills/agents
cp agents/*.md ~/.claude/skills/agents/
```

If you only want individual skills (like `/sde-tdd` or `/gap-analyst`), step 1 alone is enough.

---

## License

All Rights Reserved. See [LICENSE](LICENSE).
