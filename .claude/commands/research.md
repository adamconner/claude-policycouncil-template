# Multi-Agent Deep Research

Conduct comprehensive research on a topic using multiple specialized research agents in parallel, powered by Google Gemini Deep Research API.

## Arguments
- `$ARGUMENTS` - Research topic (required)

## Instructions

You are running a multi-agent deep research workflow. Your task is to spawn parallel research agents that each investigate the topic from a specialized perspective.

### Research Agents Available

| Agent | Focus Area |
|-------|------------|
| RA-01 | Academic Research - Scholarly literature, peer-reviewed studies |
| RA-02 | Industry Analysis - Market trends, business applications |
| RA-03 | Policy & Regulatory - Government policy, legislative history |
| RA-04 | Technical Deep-Dive - Technical specs, implementation details |
| RA-05 | International Comparative - Global perspectives, cross-border analysis |
| RA-06 | Public Discourse - Media coverage, public opinion |

### Execution Steps

1. **Parse Topic**: Extract the research topic from arguments: `$ARGUMENTS`

2. **Create Output Directory**:
   ```
   projects/research/outputs/{timestamp}_{topic_slug}/
   ```

3. **Spawn 6 Parallel Research Agents**:

   Use the Task tool to spawn ALL 6 agents in parallel (in a single message with 6 Task tool calls):

   For each agent (RA-01 through RA-06):
   ```
   Task: "You are {agent_id} ({agent_name}), a specialized research analyst.

   Read your full research methodology from: shared/agents/research/{agent_file}.md

   RESEARCH TOPIC: {topic}

   Conduct comprehensive research from your specialized perspective. Include:

   1. Executive Summary (200-300 words)
   2. Detailed Analysis with evidence
   3. Key Statistics & Data with sources
   4. Source Citations (minimum 10 sources)
   5. Implications & Recommendations

   Use web search extensively to gather current, accurate information.
   Format output as markdown."
   ```

4. **Save Individual Results**:
   Save each agent's output to:
   - `{output_dir}/RA-01_academic.md`
   - `{output_dir}/RA-02_industry.md`
   - `{output_dir}/RA-03_policy.md`
   - `{output_dir}/RA-04_technical.md`
   - `{output_dir}/RA-05_international.md`
   - `{output_dir}/RA-06_public.md`

5. **Generate Consolidated Report**:
   After all agents complete, create `RESEARCH_MASTER.md` that:
   - Synthesizes findings across all perspectives
   - Identifies cross-cutting themes
   - Highlights key statistics and data points
   - Lists all sources from all agents
   - Provides actionable recommendations

6. **Save Metadata**:
   Create `metadata.json` with:
   ```json
   {
     "topic": "{topic}",
     "timestamp": "{ISO timestamp}",
     "agents_used": ["RA-01", "RA-02", "RA-03", "RA-04", "RA-05", "RA-06"],
     "execution_time_seconds": {total},
     "total_sources": {count}
   }
   ```

7. **Report Results**:
   Provide summary to user with:
   - Link to RESEARCH_MASTER.md
   - Key findings from each perspective
   - Total sources gathered
   - Execution time

### Example Usage

```
/research AI governance frameworks for autonomous systems
```

Output:
```
📊 Multi-Agent Research Complete: AI Governance Frameworks

✅ 6 agents completed research in parallel
⏱️ Total execution time: 3m 42s
📚 Sources gathered: 87

Key Findings by Perspective:
- RA-01 (Academic): 15 peer-reviewed papers identified...
- RA-02 (Industry): Market projected to reach $X by 2030...
- RA-03 (Policy): 12 pending federal bills, EU AI Act analysis...
- RA-04 (Technical): Key standards from IEEE, NIST...
- RA-05 (International): EU, UK, China approaches compared...
- RA-06 (Public): 67% public support for regulation per Pew...

📁 Full report: projects/research/outputs/20240115_ai_governance/RESEARCH_MASTER.md
```

### Progress Updates

For research taking >5 minutes, provide updates every 2 minutes:
```
⏱️ [HH:MM] Research Progress
✅ Completed: RA-01, RA-02, RA-03
🔄 In Progress: RA-04, RA-05
⏳ Pending: RA-06
```
