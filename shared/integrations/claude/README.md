# Claude Integration (Default)

The Claude integration is the default and always-available option. It uses Claude Code's native Task tool for multi-agent orchestration.

## Features

- **Multi-agent parallel execution** via Task tool
- **6-agent research teams** for comprehensive analysis
- **Structured voting and deliberation** across 19 policy agents
- **Full 5-phase workflow** (Ideation → Voting → Refinement → Development → Rollout)

## Setup

No additional setup required. Claude Code handles everything automatically.

## Usage

All commands use Claude by default:

```bash
/council-phase1 Universal Basic Income
/research AI policy frameworks
/deep-research Machine learning safety
```

## Capabilities

| Feature | Supported |
|---------|-----------|
| Parallel agent execution | Yes (up to 10 concurrent) |
| Multi-phase workflows | Yes |
| Agent memory | Yes |
| Structured voting | Yes |
| Document generation | Yes |

## Limitations

- Research relies on Claude's training data and web search
- For comprehensive research (100+ sources), consider the Gemini integration
