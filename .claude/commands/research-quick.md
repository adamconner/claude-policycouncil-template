# Quick Research (3 Agents)

Conduct focused research on a topic using 3 core research agents in parallel.

## Arguments
- `$ARGUMENTS` - Research topic (required)

## Instructions

You are running a quick 3-agent research workflow. This is faster than full research but covers the most essential perspectives.

### Quick Research Agents

| Agent | Focus Area |
|-------|------------|
| RA-01 | Academic Research - Scholarly literature, peer-reviewed studies |
| RA-02 | Industry Analysis - Market trends, business applications |
| RA-03 | Policy & Regulatory - Government policy, legislative history |

### Execution Steps

1. **Parse Topic**: Extract the research topic from arguments: `$ARGUMENTS`

2. **Create Output Directory**:
   ```
   projects/research/outputs/{timestamp}_{topic_slug}/
   ```

3. **Spawn 3 Parallel Research Agents**:

   Use the Task tool to spawn all 3 agents in a single message:

   **Task 1 (RA-01 Academic)**:
   ```
   You are RA-01 (Academic Research Analyst). Research "{topic}" focusing on:
   - Peer-reviewed studies and academic papers
   - University research and working papers
   - Theoretical frameworks and academic debates
   - Empirical evidence with citations

   Use web search to find current academic sources. Output as markdown with Executive Summary, Findings, and Sources.
   ```

   **Task 2 (RA-02 Industry)**:
   ```
   You are RA-02 (Industry Analysis Researcher). Research "{topic}" focusing on:
   - Market size, trends, and projections
   - Key industry players and competitive landscape
   - Business case studies and applications
   - Investment and funding patterns

   Use web search to find current industry data. Output as markdown with Executive Summary, Findings, and Sources.
   ```

   **Task 3 (RA-03 Policy)**:
   ```
   You are RA-03 (Policy & Regulatory Analyst). Research "{topic}" focusing on:
   - Current laws and regulations (federal and state)
   - Pending legislation and bills
   - Regulatory agency positions and enforcement
   - Policy proposals from think tanks

   Use web search to find current policy information. Output as markdown with Executive Summary, Findings, and Sources.
   ```

4. **Save Results**:
   - `{output_dir}/RA-01_academic.md`
   - `{output_dir}/RA-02_industry.md`
   - `{output_dir}/RA-03_policy.md`
   - `{output_dir}/RESEARCH_SUMMARY.md` (consolidated)

5. **Report to User**:
   Provide concise summary with key findings from each perspective.

### Example

```
/research-quick cryptocurrency regulation
```

Output:
```
📊 Quick Research Complete: Cryptocurrency Regulation

✅ 3 agents completed in ~2 minutes

Key Findings:
- Academic: SEC v. Ripple case analysis dominates recent literature...
- Industry: $2.3T market cap, major exchanges adapting to regulations...
- Policy: 6 pending bills in Congress, state-by-state patchwork...

📁 Results: projects/research/outputs/20240115_crypto_regulation/
```
