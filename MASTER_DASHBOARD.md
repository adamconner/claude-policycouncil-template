# Policy Council Master Dashboard

> Central navigation hub for all policy council projects

## Quick Start

```bash
# Create a new project
/new-project [project-name] [policy-topic]

# Run Phase 1 ideation on a project
/council-phase1 [topic]

# Check project status
/status
```

## Active Projects

| Project | Status | Phase | Ideas | Votes |
|---------|--------|-------|-------|-------|
| _example | Template | — | — | — |

> Create your first project by copying `projects/_example/` to a new folder

## Phase Overview

| Phase | Purpose | Output |
|-------|---------|--------|
| Phase 1: Ideation | Generate policy ideas from 19 agent perspectives | `outputs/phase1/ideas_master.md` |
| Phase 2: Voting | Vote and rank top ideas | `outputs/phase2/voting_results.md` |
| Phase 3: Refinement | Develop shortlisted policies | `outputs/phase3/` |
| Phase 4: Full Development | Complete policy papers | `outputs/phase4/` |
| Phase 5: Rollout Materials | Communication & implementation | `outputs/phase5/` |

## Available Commands

### Project Management
- `/status` — Quick status of all projects
- `/dashboard` — Full project dashboard
- `/pending` — List items awaiting human review
- `/council-approve` — Approve pending gates

### Policy Development
- `/council-phase1 [topic]` — Run Phase 1 ideation with all 19 agents
- `/council-vote [file]` — Run Phase 2 voting
- `/run-council [topic]` — Full Phase 1 + Phase 2 workflow
- `/council-test [topic]` — Quick 3-agent test run

### Research
- `/research [topic]` — Full 6-agent parallel research
- `/research-quick [topic]` — Quick 3-agent research
- `/deep-research [topic]` — Iterative deep research workflow

## Council Composition

**19 Voting Members:**
- 12 Policy Analysts (diverse ideological perspectives)
- 7 Specialists (legal, budget, implementation expertise)

See `shared/COUNCIL_ARCHITECTURE.md` for full details.

---

*Policy Council Framework v3.0*
