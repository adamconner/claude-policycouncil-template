# Claude Code Instructions for AI Policy Council

## Project Architecture

**This repository uses Claude Code as the primary execution environment.** The Policy Council runs entirely through Claude Code's native Task agents and slash commands - no external hosting, API keys, or Python SDK required.

### Core Components
- `projects/` — Individual policy council projects with outputs
- `shared/` — Shared agents, templates, workflows, and configuration
- `.claude/commands/` — Slash commands for running workflows
- `MASTER_DASHBOARD.md` — Navigation hub for all projects

---

## Policy Council Workflows (Claude Code Native)

The Policy Council runs entirely through Claude Code using the Task tool to spawn agent personas.

### Available Slash Commands

| Command | Description |
|---------|-------------|
| `/council-test [topic]` | Quick 3-agent test run to verify parallel execution |
| `/council-phase1 [topic]` | Full Phase 1 with all 19 voting agents (2 batches) |
| `/council-vote [file]` | Phase 2 voting on policies from Phase 1 output |
| `/run-council [topic]` | Full workflow (Phase 1 + Phase 2) |
| `/status` | Quick status of all projects |
| `/dashboard` | Full project dashboard |
| `/pending` | List pending human input |
| `/council-approve` | Approve pending gates |

### How It Works

1. **Agent Personas**: Each Task agent is given the full agent definition from `shared/agents/` as context
2. **Parallel Batches**: Agents run in batches of 10 (max concurrent) for efficiency
3. **Structured Output**: Results aggregated into project output folders
4. **No External APIs**: Uses Claude Code's native Task tool only

### Agent Roster (19 Voting Members)

**Policy Analysts (12):**
- PA-01 Economic Populist | PA-02 Progressive | PA-04 Centrist
- PA-06 Conservative/Market | PA-07 Nationalist Conservative
- PA-09 Safety/Risk | PA-10 Innovation | PA-11 Capital & Industry
- PA-12 Rights & Consumer | PA-13 Labor | PA-15 Environmental | PA-16 Small Business

**Specialists (7):**
- SA-01 Legislative | SA-02 Legal | SA-03 SCOTUS
- SA-04 Verification | SA-06 Polling | SA-07 Budget | SA-08 Implementation

---

## Multi-Agent Deep Research

Run comprehensive research using parallel specialized agents.

### Research Slash Commands

| Command | Description |
|---------|-------------|
| `/deep-research <topic>` | Full iterative research workflow with format confirmation |
| `/research <topic>` | Full 6-agent parallel research on a topic |
| `/research-quick <topic>` | Quick 3-agent research (Academic, Industry, Policy) |
| `/research-status [latest]` | Check status of research projects |

### Research Agents (6 Specialists + Writer)

| Agent | Focus Area |
|-------|------------|
| RA-01 | Academic/Scholarly - Peer-reviewed studies, academic discourse |
| RA-02 | Legal/Regulatory - Laws, regulations, court cases, compliance |
| RA-03 | Technical/Engineering - Technical specs, standards, implementations |
| RA-04 | Market/Industry - Market trends, business applications, competition |
| RA-05 | Policy/Government - Government policy, think tanks, international |
| RA-06 | Media/Public Opinion - News coverage, polling, public discourse |
| WA-01 | Writer - Synthesis, formatting, source validation |

---

## Repository Structure

```
claude-policycouncil-template/
├── projects/                    # Individual project folders
│   └── _example/                # Template project structure
│
├── shared/                      # Resources shared across all projects
│   ├── agents/                  # Agent definitions
│   │   ├── analysts/            # PA-01 through PA-16
│   │   ├── specialists/         # SA-01 through SA-08
│   │   └── research/            # RA-01 through RA-06
│   ├── config/                  # Shared config (voting rules, weights)
│   ├── integrations/            # Optional API integrations (Gemini, etc.)
│   ├── templates/               # Document templates
│   ├── workflows/               # Phase workflow guides
│   ├── tools/                   # Vote tally utility
│   └── memory/                  # Agent cross-phase memory (JSON)
│
├── .claude/commands/            # Claude Code slash commands
├── MASTER_DASHBOARD.md          # Navigation hub for all projects
├── POLICY_COUNCIL_TEMPLATE.md   # Guide for creating new projects
└── CLAUDE.md                    # Project instructions (this file)
```

---

## Running Phase 1 (Ideation)

1. **Batch agents into groups of 10** (max concurrent Task calls)
2. **For each agent batch**, spawn parallel Task agents:
   ```
   Task 1: "You are PA-01 Economic Populist. [Read shared/agents/analysts/pa01_economic_populist.md for full context]. Generate 5-10 policy ideas on {topic}..."
   Task 2: "You are PA-02 Progressive. [Read shared/agents/analysts/pa02_progressive.md]..."
   ... up to 10 parallel
   ```
3. **Aggregate results** into `projects/{project}/outputs/phase1/ideas_master.md`
4. **Update memory** for each agent in `shared/memory/agents/`

## Running Phase 2 (Voting)

1. **Load Phase 1 ideas** and select top candidates
2. **For each policy**, spawn parallel voting agents:
   ```
   Task: "You are PA-01. Vote on Policy X: [description].
   Your previous ideas on this topic: [from memory].
   Vote: FOR/AGAINST/ABSTAIN
   Reasoning: [2-3 sentences]
   Strength: [1-10]"
   ```
3. **Run vote tally**: `python shared/tools/vote_tally.py votes.json`
4. **Save votes to memory** and present results

## Memory Integration

Before each phase, load agent memory:
- Check `shared/memory/agents/{agent_id}_{project}.json`
- Include relevant prior contributions in prompts
- After phase, record new contributions to memory

---

## Agent Prompt Templates

**Ideation Agent:**
```
You are {agent_id} ({agent_name}), a member of the AI Policy Council.

Read your full perspective and values from: shared/agents/analysts/{agent_file}

TOPIC: {topic}

Generate 5-10 specific, actionable policy proposals from your unique ideological perspective.

For each proposal:
1. **Title**: Clear, descriptive name
2. **Summary**: One paragraph explaining the policy
3. **Rationale**: Why this matters from YOUR perspective
4. **Implementation**: Key steps to enact
5. **Challenges**: Potential obstacles

Format as markdown with clear headers.
```

**Voting Agent:**
```
You are {agent_id} ({agent_name}).

Your perspective: {brief summary from agent file}

Your Phase 1 contributions: {from memory}

POLICY TO EVALUATE:
Title: {policy_title}
Description: {policy_description}

Cast your vote:
- VOTE: [FOR / AGAINST / ABSTAIN]
- STRENGTH: [1-10, where 10 is strongest conviction]
- REASONING: [2-3 sentences explaining your position from your ideological perspective]
- KEY CONCERN: [If AGAINST, what would change your vote?]
```

---

## Parallel Execution Guidelines

When tasks can be parallelized, spawn multiple subagents using the Task tool simultaneously:

- **Always parallelize independent work**: If analyzing multiple policies, documents, or agents, spawn parallel Task calls
- **Maximum 10 concurrent subagents**: Batch larger workloads into groups of 10
- **Isolate by domain**: Each subagent should have a clear, non-overlapping scope
- **Aggregate results**: After parallel execution, synthesize findings into unified output

## Task Chunking for Large Documents

Always break Phase 4 papers and similar large documents into chunks:

| Chunk | Typical Content |
|-------|-----------------|
| 1 | Exec Summary, Background, Landscape (Sections 1-3) |
| 2 | Precedents, Public Opinion, Detailed Proposal (4-6) |
| 3 | Policy Tools, Goals, Administration (7-9) |
| 4 | State Capacity, Impact, Cost, Benefits, Legal (10-14) |
| 5 | Timeline, Arguments For/Against, Stakeholders (15-18) |
| 6 | Alternatives, Equity, RIA, Procedure, Dissents, Sources (19-24) |
| 7 | Appendices (Draft Federal + State Legislation) |

---

## Optional Integrations

This framework supports optional API integrations for enhanced capabilities. See `shared/integrations/README.md` for details.

**Available Integrations:**
- **Claude** (default) — Always available, no configuration needed
- **Gemini** (optional) — Deep research with 100+ sources
- **OpenAI** (future) — Placeholder for additional capabilities

---

*Policy Council Framework v3.0*
