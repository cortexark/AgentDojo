# Research Log — v0.1.0 (2026-03-06)

## 1. Adopted Patterns

### PATTERN_006: Guardrail-Based Quality Control (from CrewAI)
- **Source:** CrewAI guardrails — https://docs.crewai.com/en/concepts/tasks
- **Applied to:** Skill exit criteria and scoring rubrics
- **Implementation:** Each skill YAML definition includes `exit_criteria` (binary pass/fail conditions) and `scoring_rubric` (weighted criteria with scales). Exit criteria function as guardrails — a skill that runs but doesn't meet exit criteria is logged as SKILL_INCOMPLETE
- **Expected KPI impact:** skill_completion_rate ≥ 0.85 (new metric)

### PATTERN_013: State Machine Graph Architecture (from LangGraph)
- **Source:** LangGraph StateGraph — https://docs.langchain.com/oss/python/langgraph/graph-api
- **Applied to:** orchestration_graph.yaml schema
- **Implementation:** 9-phase state machine with explicit transitions, conditions, checkpoint definitions, and human-in-the-loop interrupt points. Entities defined with standard fields (id, created_at, version, parent_version, status, metadata)
- **Expected KPI impact:** orchestration_reliability ≥ 0.95

### PATTERN_METAGPT_002: Document Artifact Generation Pipeline (from MetaGPT)
- **Source:** MetaGPT — https://arxiv.org/html/2308.00352v6
- **Applied to:** Skill artifacts_produced and evidence_required fields
- **Implementation:** Every skill YAML explicitly declares what artifacts it produces and what evidence proves execution. This enforces MetaGPT's principle of structured intermediate outputs rather than relying on dialogue
- **Expected KPI impact:** artifact_correctness ≥ 0.80

### PATTERN_METAGPT_003: Publish-Subscribe Challenge Model (from MetaGPT)
- **Source:** MetaGPT message pool — https://docs.deepwisdom.ai/main/en/guide/in_depth_guides/agent_communication.html
- **Applied to:** challenge_rules.yaml policy
- **Implementation:** Roles subscribe to challenge triggers from other roles. Challenge triggers include specific thresholds, required evidence, escalation ladders with SLA hours, and human-in-the-loop flags
- **Expected KPI impact:** defect_escape_rate ≤ 0.10

### Failure Taxonomy (from Paper: "Why Do Multi-Agent LLM Systems Fail?")
- **Source:** https://arxiv.org/abs/2503.13657
- **Applied to:** Simulation scenario design, bug taxonomy categories
- **Implementation:** Scenarios use failure categories from the paper's taxonomy: hallucination, infinite_loop, context_loss, tool_misuse, goal_drift, coordination_deadlock. Each scenario injects failures and tests orchestrator response
- **Expected KPI impact:** defect_detection_rate ≥ 0.85

## 2. Studied but Not Adopted

### PATTERN_005: Multi-Tier Memory System (CrewAI)
- **Reason:** TaskPilot uses file-based state (.project/ directories) rather than in-memory objects. The file-based approach provides natural persistence and version control. Memory system patterns more relevant for conversation-based agents, not artifact-producing orchestrators

### PATTERN_015: Checkpointer-Based Durable Execution (LangGraph)
- **Reason:** Full checkpoint persistence (DynamoDB, Postgres) is over-engineered for current needs. TaskPilot already uses .project/status.md as single source of truth for phase status. Worth revisiting when orchestrator runs become long-lived (>1 hour)

### PATTERN_017: Interrupt-Based Human-in-the-Loop (LangGraph)
- **Reason:** TaskPilot already has AskUserQuestion-based gates at phases 3, 4, 7, and pre-commit. The LangGraph interrupt() pattern requires node re-execution on resume, which adds complexity. Current gate approach is simpler and sufficient

### PATTERN_020: Supervisor Multi-Agent Orchestration (LangGraph)
- **Reason:** TaskPilot already has a master orchestrator that coordinates domain agents. The supervisor pattern would add a layer of indirection without clear KPI benefit. Current direct-coordination model is working

### PATTERN_AUTOGEN_004: Group Chat with Dynamic Speaker Selection (AutoGen)
- **Reason:** TaskPilot skills execute sequentially within phases, not as free-form group conversations. Speaker selection adds non-determinism that conflicts with the SDLC phase gate model

### PATTERN_KIRO_003: IDE Diagnostics for Failure Detection (Kiro)
- **Reason:** Excellent pattern (29% reduction in command executions) but requires LSP integration that TaskPilot doesn't have. Worth investigating for Phase 6 Build improvements in future cycles

### PATTERN_KIRO_007: Code Review Cycles with Pattern Learning (Kiro)
- **Reason:** Pattern learning across repos requires persistent storage and model fine-tuning. Too complex for current cycle. Would be valuable when TaskPilot has enough historical data

## 3. Bugs Discovered During Research

### BUG-004: Git remote URL mismatch
- **Description:** SKILL.md task references `https://github.com/cortexark/AgentDojo.git` but actual remote is `https://github.com/mission-agi/AgentDojo.git`
- **Triage:** Filed to TASKPILOT-KNOWN-BUGS-AND-IMPROVEMENTS.md (cosmetic, no functional impact)

### BUG-005: No .gitignore for simulation artifacts
- **Description:** kpi_results.json and simulation_results/ should potentially be in .gitignore to avoid committing large test outputs
- **Triage:** Fixed inline — simulation results ARE committed per task spec (they serve as evidence for promote/reject decisions)

## 4. Top 10 Papers

| # | Title | URL | Year | Relevance | Module |
|---|-------|-----|------|-----------|--------|
| 1 | Why Do Multi-Agent LLM Systems Fail? | https://arxiv.org/abs/2503.13657 | 2025 | First failure taxonomy for MAS (14 failure modes, 1600+ traces) | Failure handling, quality evaluation |
| 2 | Agent Skills for LLMs: Architecture, Acquisition, Security | https://arxiv.org/abs/2602.12430 | 2026 | Comprehensive skill-based architecture survey | Skill definition, security |
| 3 | Evaluation and Benchmarking of LLM Agents: A Survey | https://arxiv.org/abs/2507.21504 | 2025 | Two-dimensional evaluation taxonomy | Quality evaluation |
| 4 | Multi-Agent LLM Orchestration for Incident Response | https://arxiv.org/abs/2511.15755 | 2025 | 100% actionable rate vs 1.7% single-agent (348 trials) | Inter-agent coordination |
| 5 | The Orchestration of Multi-Agent Systems | https://arxiv.org/abs/2601.13671 | 2026 | Unified architecture for planning, policy, state management | Orchestration architecture |
| 6 | SafePred: Predictive Guardrail via World Models | https://arxiv.org/abs/2602.01725 | 2026 | 97.6% safety with 21.4% task utility improvement | Security, failure handling |
| 7 | AgentOrchestra: TEA Protocol | https://arxiv.org/abs/2506.12508 | 2025 | Tool-Environment-Agent protocol with lifecycle management | Skill definition, coordination |
| 8 | Survey of Agent Interoperability Protocols | https://arxiv.org/abs/2505.02279 | 2025 | MCP, ACP, A2A, ANP protocol analysis | Inter-agent coordination |
| 9 | Safety and Security Framework for Agentic Systems | https://arxiv.org/abs/2511.21990 | 2025 | Dynamic framework with 10K+ attack/defense traces | Security, quality evaluation |
| 10 | AgentBench: Evaluating LLMs as Agents | https://arxiv.org/abs/2308.03688 | 2024 | Multi-dimensional benchmark across 8 environments | Quality evaluation |

## 5. Next 10 Backlog

| # | Title | URL | Year | Module |
|---|-------|-----|------|--------|
| 1 | Building a Foundational Guardrail via Synthetic Data | https://arxiv.org/abs/2510.09781 | 2025 | Security |
| 2 | Multi-Agent Collaboration via Evolving Orchestration | https://arxiv.org/abs/2505.19591 | 2025 | Coordination |
| 3 | Towards a Science of AI Agent Reliability | https://arxiv.org/abs/2602.16666 | 2026 | Quality evaluation |
| 4 | Agentic AI Security: Threats, Defenses, Evaluation | https://arxiv.org/abs/2510.23883 | 2025 | Security |
| 5 | Large-Scale Study on Multi-Agent AI Systems | https://arxiv.org/abs/2601.07136 | 2026 | Failure handling |
| 6 | Formalizing Safety and Security Properties | https://arxiv.org/abs/2510.14133 | 2025 | Security |
| 7 | AGrail: Lifelong Agent Guardrail | https://arxiv.org/abs/2502.11448 | 2025 | Security |
| 8 | AgentCompass: Production Evaluation Framework | https://arxiv.org/abs/2509.14647 | 2025 | Quality evaluation |
| 9 | Multi-Agent Coordination Survey | https://arxiv.org/abs/2502.14743 | 2025 | Coordination |
| 10 | Survey of Agentic AI and Cybersecurity | https://arxiv.org/html/2601.05293v1 | 2026 | Security |
