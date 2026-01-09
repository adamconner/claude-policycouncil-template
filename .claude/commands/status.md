Provide a quick status overview of all Policy Council projects.

Read MASTER_DASHBOARD.md and provide a concise summary showing:
- Each project name
- Current phase
- Progress percentage
- Whether anything is waiting for human input

Format as a brief overview, e.g.:
```
Policy Council Status:
- Economic Prosperity: Phase 2 Complete | 67% | No pending decisions
- Jobs Guarantee: Not Started | 0% | Awaiting kickoff
```

If the user specifies a project (e.g., "/status economic prosperity"), read that project's STATE.json at `projects/[project-name]/STATE.json` and provide detailed status for that project only.
