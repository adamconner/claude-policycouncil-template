# Policy Council Phase 1: Parallel Idea Generation

Run Phase 1 (idea generation) with all 19 voting agents in parallel batches.

## Arguments
- `$ARGUMENTS` - Policy topic to analyze

## Execution

You are the Council Director. Run Phase 1 idea generation on: **$ARGUMENTS**

### Step 1: Read Agent Registry
Read `shared/config/agent_registry.json` to get agent list.

### Step 2: Spawn Batch 1 (10 agents simultaneously)
Use a SINGLE message with 10 parallel Task tool calls for:
- PA-01 Economic Populist
- PA-02 Progressive
- PA-04 Centrist
- PA-06 Conservative/Market
- PA-07 Nationalist Conservative
- PA-09 Safety/Risk Advocate
- PA-10 Innovation Advocate
- PA-11 Capital & Industry
- PA-12 Rights & Consumer Protection
- PA-13 Organized Labor

For each Task, read the agent's definition file first, then include it in the prompt.

### Step 3: Spawn Batch 2 (9 agents simultaneously)
After Batch 1 completes, spawn 9 more parallel Tasks for:
- PA-15 Environmental
- PA-16 Small Business
- SA-01 Legislative Counsel
- SA-02 Legal Counsel
- SA-03 Supreme Court Analyst
- SA-04 Verification & Sources
- SA-06 Polling Expert
- SA-07 Budget Expert
- SA-08 Implementation Expert

### Step 4: Compile Results
Aggregate all 19 agent responses into `projects/economic-prosperity/outputs/phase1/parallel_run_[date].md`

### Agent Task Prompt Template
```
You are {agent_name} ({agent_id}).

{FULL AGENT DEFINITION FROM FILE}

---

TASK: Analyze this policy topic and generate 2-3 proposals:
TOPIC: $ARGUMENTS

For each proposal provide:
- Title
- Description (2-3 paragraphs)
- Pros (3-5)
- Cons (3-5)
- Implementation Challenges (3)
- Cost Estimate

Return structured markdown. Stay true to your perspective.
```
