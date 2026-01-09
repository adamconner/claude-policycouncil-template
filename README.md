# Claude Policy Council Framework

Give the Policy Council a topic, and 21 AI agents — each with a distinct ideological perspective — will debate it from every angle. They generate ideas in parallel, vote on proposals, then develop the winners into comprehensive policy papers complete with draft legislation, economic analysis, and rollout materials like press releases and social media toolkits.

You stay in control throughout: reviewing ideas before voting, approving what moves forward, and guiding refinement at each phase. The result is well-rounded policy development that stress-tests ideas across the political spectrum — from economic populists to fiscal conservatives, from labor advocates to national security experts — all in a few hours instead of months.

---

## Quick Start

### Requirements

- **Claude Pro subscription** ($20/month) from [claude.ai](https://claude.ai)
- **Claude Code** installed ([download](https://claude.ai/download) or `npm install -g @anthropic-ai/claude-code`)

### Setup

1. Clone this repository
2. Open Claude Code in the folder
3. Run `/council-test Should cities ban cars from downtown areas?` to verify setup

### Your First Council Session

```bash
# Create a project
cp -r projects/_example projects/my-policy

# Edit goals
# projects/my-policy/config/goals.md

# Run Phase 1 (ideation)
/council-phase1 Your policy topic here

# Review ideas, then run Phase 2 (voting)
/council-vote latest
```

---

## The 21 Agents

### Policy Analysts (14)
| Agent | Perspective |
|-------|-------------|
| Economic Populist | Working-class economic impact, anti-monopoly |
| Progressive | Social equity, civil rights |
| Centrist | Bipartisan solutions, stability |
| Conservative/Market | Market principles, limited government |
| MAGA Conservative | America First, traditional values |
| AI Safety | Risk mitigation, alignment |
| AI Accelerationist | Technology advancement |
| Capital & Industry | Investment climate, business growth |
| Rights & Consumer | Civil rights, consumer protection |
| Organized Labor | Worker protections, job security |
| Environmental/Climate | Sustainability, climate action |
| Small Business | Main Street, entrepreneurship |
| National Security | Defense, military, homeland security |
| International Relations | Diplomacy, global cooperation |

### Specialists (7)
| Agent | Expertise |
|-------|-----------|
| Legislative Counsel | Bill drafting, constitutional analysis |
| Legal Counsel | Regulatory law, legal challenges |
| SCOTUS Analyst | Supreme Court jurisprudence |
| Verification & Sources | Fact-checking, citations |
| Polling Expert | Public opinion analysis |
| Budget Expert | Fiscal analysis, CBO-style scoring |
| Implementation Expert | Operational feasibility |

---

## The 5 Phases

The Policy Council develops proposals through a five-phase workflow, with human checkpoints between each phase.

- **Phase 1: Idea Generation** — All 21 agents propose policies from their unique perspectives, generating 60-100+ ideas in parallel, each required to include transformational "Big Ideas."
- **Phase 2: Voting** — Agents vote on top proposals with reasoning, revealing where consensus exists and where ideological fault lines emerge.
- **Phase 3: Refinement** — Specialists produce research briefs, economic analysis, implementation plans, and political assessments for the winning policy.
- **Phase 4: Full Development** — The policy expands into a comprehensive 24-section paper with draft federal and state legislation.
- **Phase 5: Rollout** — Communication materials are created: press releases, op-eds, fact sheets, talking points, social media content, and FAQs.

---

## Example Output: Affordable Housing

See a **complete 5-phase example** in [`examples/affordable-housing/`](examples/affordable-housing/).

| Phase | Output |
|-------|--------|
| Phase 1 | [30 policy proposals](examples/affordable-housing/outputs/phase1/ideas_master.md) |
| Phase 2 | [Voting results](examples/affordable-housing/outputs/phase2/voting_results.md) |
| Phase 3 | [Policy recommendation](examples/affordable-housing/outputs/phase3/national_zoning_reform_recommendation.md) |
| Phase 4 | [24-section paper + legislation](examples/affordable-housing/outputs/phase4/national_zoning_reform_full_paper.md) |
| Phase 5 | [Press release, social media, FAQ](examples/affordable-housing/outputs/phase5/) |

---

## Available Commands

| Command | Description |
|---------|-------------|
| `/council-phase1 [topic]` | Full 21-agent ideation |
| `/council-vote latest` | Vote on Phase 1 proposals |
| `/run-council [topic]` | Phase 1 + 2 combined |
| `/council-test [topic]` | Quick 3-agent test |
| `/research [topic]` | 6-agent parallel research |
| `/status` | Project status overview |
| `/dashboard` | Full project dashboard |

---

## Project Structure

```
claude-policycouncil-template/
├── .claude/commands/        # Slash commands
├── shared/
│   ├── agents/              # 21 agent definitions
│   ├── config/              # Voting rules
│   ├── integrations/        # Optional Gemini/OpenAI
│   ├── templates/           # Document templates
│   └── workflows/           # Phase guides
├── projects/
│   └── _example/            # Project template
├── examples/
│   └── affordable-housing/  # Complete 5-phase example
└── CLAUDE.md                # Claude Code instructions
```

---

## Optional Integrations

The framework supports optional API integrations:

- **Gemini** — Deep research with 100+ sources
- **OpenAI** — Additional capabilities (future)

See `shared/integrations/README.md` for setup.

---

## License

MIT License — free to use, modify, and share.

---

*Built for deliberative AI policy development*
