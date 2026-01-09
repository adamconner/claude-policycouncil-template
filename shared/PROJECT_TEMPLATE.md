# New Project Setup Guide
**Version:** 2.0

This guide provides the minimal setup required to launch a new AI Policy Council project. All projects inherit the shared architecture automatically.

---

## Quick Start

### 1. Create Project Directory
```
projects/[project-name]/
├── PROJECT_DASHBOARD.md
├── config/
│   └── goals.md          # REQUIRED
└── outputs/              # Created as phases complete
```

### 2. Copy This goals.md Template

Create `projects/[project-name]/config/goals.md`:

```markdown
# [Project Name] - Policy Goals

## Primary Objective
[One clear sentence describing the main policy goal]

## Specific Goals
1. [Goal 1 - specific, measurable outcome]
2. [Goal 2 - specific, measurable outcome]
3. [Goal 3 - specific, measurable outcome]

## Scope
- **Geographic:** United States [+ specific states if applicable]
- **Sector:** [e.g., Technology, Healthcare, Finance, Labor]
- **Timeline:** [Target timeframe for policy implementation]

## Key Constraints
- [Budget constraints, if any]
- [Political constraints, if any]
- [Legal constraints, if any]

## Success Criteria
- [Metric 1 for measuring success]
- [Metric 2 for measuring success]

## Priority Focus Areas
- [Area 1]
- [Area 2]
- [Area 3]
```

### 3. Copy This Dashboard Template

Create `projects/[project-name]/PROJECT_DASHBOARD.md`:

```markdown
# [Project Name] - Project Dashboard

## Quick Links
- [Goals](./config/goals.md)
- [Shared Architecture](../shared/COUNCIL_ARCHITECTURE.md)

## Current Status
- **Phase:** 1 - Idea Generation
- **Status:** Not Started
- **Last Updated:** [Date]

## Phase Progress
| Phase | Status | Output |
|-------|--------|--------|
| Phase 1: Idea Generation | Not Started | — |
| Phase 2: Debate & Ranking | Not Started | — |
| Phase 3: Policy Refinement | Not Started | — |
| Phase 4: Full Development | Not Started | — |
| Phase 5: Rollout Materials | Not Started | — |

## Output Directory
```
outputs/
├── phase1/
├── phase2/
├── phase3/
├── phase4/
└── phase5/
```

## Notes
[Any project-specific notes]
```

---

## That's It!

Your project will automatically use:
- **24 Voting Agents** (16 analysts + 8 specialists) from [shared/agents/](./agents/)
- **5-Phase Workflow** from [shared/workflows/](./workflows/)
- **Voting Rules** from [shared/config/voting_rules.md](./config/voting_rules.md)
- **Document Templates** from [shared/templates/](./templates/)

See [COUNCIL_ARCHITECTURE.md](./COUNCIL_ARCHITECTURE.md) for full system documentation.

---

## Optional: Project-Specific Overrides

Only create `config/project.md` if you need to deviate from the shared architecture:

```markdown
# Project-Specific Configuration

## Agent Modifications
[Only if specific agents should be excluded or weighted differently]

## Phase Customization
[Only if workflow needs modification]

## Output Requirements
[Only if deliverables differ from standard]
```

---

## Starting Phase 1

To begin, prompt the council:

> "Initialize Phase 1: Idea Generation for [Project Name].
> Goals are defined in config/goals.md.
> Generate 10-15 policy ideas across the political spectrum,
> with each analyst contributing 2-3 ideas from their perspective."

The council will use the shared Phase 1 workflow automatically.

---

## Reference

- [Full Architecture Documentation](./COUNCIL_ARCHITECTURE.md)
- [Phase 1 Workflow](./workflows/phase1_idea_generation.md)
- [Phase 2 Workflow](./workflows/phase2_debate.md)
- [Phase 3 Workflow](./workflows/phase3_refinement.md)
- [Phase 4 Workflow](./workflows/phase4_full_development.md)
- [Phase 5 Workflow](./workflows/phase5_rollout.md)
