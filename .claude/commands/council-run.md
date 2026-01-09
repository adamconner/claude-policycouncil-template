# Run Policy Council Analysis

Run a policy council analysis on the specified topic.

## Usage
/council-run <topic> [--phases 1-2|1-5] [--project <name>]

## Instructions for Claude

When this command is invoked:

1. **Parse arguments**: Extract topic, phases (default 1-2), and project name (derive from topic if not provided)

2. **Phase 1 - Ideation**: Spawn 10 parallel Task agents (batch 1: PA-01 to PA-10, batch 2: PA-11 to PA-16 + specialists as needed). Each agent should:
   - Read their agent definition from `shared/agents/analysts/`
   - Generate 5-10 policy ideas for the topic
   - Return ideas in structured format

3. **Aggregate Phase 1**: Compile all ideas into `projects/<project>/outputs/phase1/ideas_master.md`

4. **Phase 2 - Voting** (if phases include 2): For each top policy:
   - Spawn parallel voting agents
   - Record votes with reasoning
   - Use `shared/tools/vote_tally.py` to calculate results

5. **Save state**: Update memory files in `shared/memory/agents/`

6. **Report**: Summarize results and ask user for approval to continue

## Agent Prompt Template

For each analyst agent spawned via Task tool, use this prompt structure:

```
You are {agent_id} ({agent_name}), a policy analyst on the AI Policy Council.

Your perspective: {read from shared/agents/analysts/{agent_id}.md}

Topic: {topic}

Generate 5-10 specific, actionable policy ideas from your unique perspective.

For each idea, provide:
- Title
- One-paragraph description
- Why this matters from your perspective
- Potential challenges

Return as structured markdown.
```
