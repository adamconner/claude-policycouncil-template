# Policy Council Test Run

Quick test with 3 diverse agents to verify parallel execution works.

## Arguments
- `$ARGUMENTS` - Policy topic (default: "AI and workforce displacement")

## Execution

Run a quick 3-agent test to verify the system works.

### Test Agents (spawn all 3 in ONE parallel Task call)
1. **PA-01 Economic Populist** (Pro-worker left)
2. **PA-06 Conservative/Market** (Free market right)
3. **PA-04 Centrist** (Pragmatic center)

### For Each Agent
1. Read their definition from `shared/agents/analysts/[file].md`
2. Spawn a Task with subagent_type="general-purpose" including:
   - Full agent definition
   - Policy topic: $ARGUMENTS (or "AI and workforce displacement" if empty)
   - Request: Generate 1 policy proposal with title, description, pros, cons

### Expected Output
3 policy proposals from 3 different perspectives, demonstrating:
- Parallel execution worked
- Agents maintained their ideological perspectives
- Structured output was generated

### Success Criteria
- All 3 agents respond
- Proposals reflect different viewpoints
- Output is structured markdown
