# Claude Policy Council Framework

A multi-agent policy deliberation system that runs entirely within Claude Code. Spawn 19 specialized agent personas to generate, debate, and refine policy proposals from diverse ideological perspectives.

## Features

- **19 Voting Agents**: 12 policy analysts + 7 specialists covering the full ideological spectrum
- **5-Phase Workflow**: Ideation → Voting → Refinement → Development → Rollout
- **Parallel Execution**: Agents run concurrently using Claude Code's Task tool
- **No External APIs**: Works out of the box with just Claude Code
- **Optional Integrations**: Add Gemini, OpenAI, or other APIs for enhanced research

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/claude-policycouncil-template.git
cd claude-policycouncil-template
```

### 2. Open in Claude Code

```bash
claude
```

### 3. Create Your First Project

```bash
# Copy the example project
cp -r projects/_example projects/my-first-project

# Edit the goals file
# projects/my-first-project/config/goals.md
```

### 4. Run Phase 1 Ideation

```
/council-phase1 [Your policy topic]
```

Example: `/council-phase1 Universal basic income implementation strategies`

## Project Structure

```
claude-policycouncil-template/
├── .claude/commands/           # Slash commands for workflows
├── shared/
│   ├── agents/                 # 19 agent definitions
│   │   ├── analysts/           # PA-01 through PA-16
│   │   ├── specialists/        # SA-01 through SA-08
│   │   └── research/           # RA-01 through RA-06
│   ├── config/                 # Voting rules and weights
│   ├── integrations/           # Optional API integrations
│   ├── templates/              # Document templates
│   ├── workflows/              # Phase workflow guides
│   └── tools/                  # Vote tally utility
├── projects/
│   └── _example/               # Template project structure
├── MASTER_DASHBOARD.md         # Navigation hub
└── CLAUDE.md                   # Claude Code instructions
```

## Agent Roster

### Policy Analysts (12 voting members)
| ID | Name | Perspective |
|----|------|-------------|
| PA-01 | Economic Populist | Worker-focused economics |
| PA-02 | Progressive | Social justice, equity |
| PA-04 | Centrist | Pragmatic bipartisanship |
| PA-06 | Conservative/Market | Free market principles |
| PA-07 | Nationalist Conservative | National interest focus |
| PA-09 | Safety/Risk | Risk mitigation |
| PA-10 | Innovation | Technology advancement |
| PA-11 | Capital & Industry | Business perspective |
| PA-12 | Rights & Consumer | Consumer protection |
| PA-13 | Labor | Worker rights |
| PA-15 | Environmental | Sustainability |
| PA-16 | Small Business | SMB advocacy |

### Specialists (7 voting members)
| ID | Name | Expertise |
|----|------|-----------|
| SA-01 | Legislative Counsel | Bill drafting |
| SA-02 | Legal Analyst | Constitutional law |
| SA-03 | SCOTUS Watcher | Court precedent |
| SA-04 | Verification | Fact-checking |
| SA-06 | Polling Analyst | Public opinion |
| SA-07 | Budget Analyst | Fiscal impact |
| SA-08 | Implementation | Practical execution |

## Workflow Phases

### Phase 1: Ideation
Generate 5-10 policy proposals from each agent's unique perspective.

```
/council-phase1 [topic]
```

### Phase 2: Voting
Agents vote on the generated proposals with reasoning.

```
/council-vote latest
```

### Phase 3: Refinement
Develop top-ranked proposals into initial policy papers.

### Phase 4: Full Development
Complete 20+ section policy papers with legal analysis.

### Phase 5: Rollout
Create communication materials and implementation guides.

## Optional Integrations

The framework supports optional API integrations for enhanced capabilities:

```
shared/integrations/
├── claude/      # Default (always available)
├── gemini/      # Optional: Deep research with 100+ sources
└── openai/      # Future: Additional capabilities
```

See `shared/integrations/README.md` for setup instructions.

## Available Commands

| Command | Description |
|---------|-------------|
| `/council-phase1 [topic]` | Run Phase 1 ideation with all 19 agents |
| `/council-vote [file]` | Run Phase 2 voting |
| `/run-council [topic]` | Full Phase 1 + Phase 2 workflow |
| `/council-test [topic]` | Quick 3-agent test run |
| `/research [topic]` | 6-agent parallel research |
| `/research-quick [topic]` | Quick 3-agent research |
| `/status` | Project status overview |
| `/dashboard` | Full project dashboard |
| `/council-agents` | List all agents |

## Creating a New Project

1. Copy the example project:
   ```bash
   cp -r projects/_example projects/your-project-name
   ```

2. Edit `projects/your-project-name/config/goals.md` with your policy objectives

3. Update the project dashboard

4. Run `/council-phase1` to begin ideation

## Requirements

- [Claude Code CLI](https://github.com/anthropics/claude-code)
- A Claude API key (for Claude Code)

## License

MIT License - See LICENSE file for details.

## Contributing

Contributions welcome! Please submit issues and pull requests.

---

*Built for deliberative AI policy development*
