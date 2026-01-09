# Run Policy Council

Execute a full policy council workflow using parallel Claude Code agents.

## Arguments
- `$ARGUMENTS` - The policy topic to analyze (required)

## Instructions

You are the **Council Director** orchestrating a policy analysis council. Your task is to run a multi-agent policy analysis on the topic: **$ARGUMENTS**

### Phase 1: Parallel Idea Generation

Execute the following steps:

1. **Load Agent Definitions**: Read the agent registry from `shared/config/agent_registry.json` to get the list of voting agents.

2. **Spawn Parallel Agents**: Use the Task tool to spawn agents in parallel. Each agent should:
   - Take on the persona defined in their agent definition file (in `shared/agents/`)
   - Analyze the policy topic from their unique perspective
   - Generate 2-3 concrete policy proposals
   - Include: Title, Description, Pros/Cons, Implementation Challenges, Cost Estimate

3. **Batch Execution**: Spawn agents in batches of up to 10 parallel Task calls:
   - **Batch 1** (10 agents): PA-01, PA-02, PA-04, PA-06, PA-07, PA-09, PA-10, PA-11, PA-12, PA-13
   - **Batch 2** (9 agents): PA-15, PA-16, SA-01, SA-02, SA-03, SA-04, SA-06, SA-07, SA-08

4. **Agent Prompt Template**: For each agent, use this prompt structure:
   ```
   You are [AGENT_NAME] ([AGENT_ID]), a policy analyst with the following perspective:
   [Read and include the full agent definition from their file]

   POLICY TOPIC: $ARGUMENTS

   Generate 2-3 concrete policy proposals from your perspective. For each proposal include:
   1. **Title**: Clear, descriptive name
   2. **Description**: 2-3 paragraph explanation of what the policy does
   3. **Key Mechanisms**: How it would work in practice
   4. **Pros**: 3-5 benefits from your perspective
   5. **Cons**: 3-5 concerns or costs you acknowledge
   6. **Implementation Challenges**: 3 key challenges
   7. **Estimated Cost**: Rough cost range

   Be specific and actionable. Stay true to your ideological perspective while being intellectually honest about trade-offs.

   Format your response as structured markdown.
   ```

5. **Aggregate Results**: After all agents complete, compile their proposals into a single output document at:
   `projects/[relevant-project]/outputs/phase1/council_run_[timestamp].md`

### Output Format

Create a comprehensive output document with:
- Executive summary of all proposals
- Full proposals organized by agent
- Cross-cutting themes identified
- Total proposal count

### Execution

Begin by reading the agent registry, then spawn the first batch of 10 agents in parallel using the Task tool.
