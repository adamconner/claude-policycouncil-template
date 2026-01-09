# Policy Council Phase 2: Parallel Voting

Run Phase 2 voting on a set of policies with all 19 voting agents.

## Arguments
- `$ARGUMENTS` - Path to the policies document to vote on, or "latest" for most recent Phase 1 output

## Usage
```
/council-vote latest
/council-vote projects/economic-prosperity/outputs/phase1/policy_ideas.md
```

## Execution

You are the Council Director. Run Phase 2 voting.

### Step 1: Load Policies
If $ARGUMENTS is "latest", find the most recent Phase 1 output in `projects/economic-prosperity/outputs/phase1/`.
Otherwise, read the policies from the specified file.

### Step 2: Load Voting Weights
Read `shared/config/voting_weights.json` to understand the voting schemes.

### Step 3: Spawn Batch 1 (10 agents voting in parallel)
Use a SINGLE message with 10 parallel Task tool calls. Each agent:
- Reads their agent definition
- Reviews ALL policies
- Casts votes using this structure:

```
For each policy, provide:
- Vote: SUPPORT (+2) | LEAN SUPPORT (+1) | ABSTAIN (0) | LEAN OPPOSE (-1) | OPPOSE (-2)
- Reasoning: 2-3 sentences explaining your vote from your perspective
- Amendments: Any modifications that would change your vote
```

### Step 4: Spawn Batch 2 (9 agents voting in parallel)
After Batch 1 completes, spawn the remaining 9 agents.

### Step 5: Tally Results
Use `python shared/tools/vote_tally.py` to calculate weighted results:
- Raw scores (sum of all votes)
- Weighted scores for each voting scheme
- Consensus ranking
- Areas of agreement/disagreement

Save vote records to agent memory files.

### Step 6: Generate Report
Create `projects/economic-prosperity/outputs/phase2/voting_results_[date].md` with:
- Policy rankings by consensus
- Vote breakdown per policy
- Cross-ideological agreement analysis
- Top 5 policies by different voting schemes

### Voting Schemes to Calculate
1. **Effectiveness** (equal weights) - Most effective policies
2. **Compromise** (equal weights) - Broadest acceptable policies
3. **Progressive Sort** (progressive-weighted)
4. **Conservative Sort** (conservative-weighted)
