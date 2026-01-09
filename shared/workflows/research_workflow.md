# Multi-Agent Deep Research Workflow

## Overview

The Multi-Agent Research Workflow enables comprehensive investigation of topics through parallel execution of specialized research agents. Each agent brings a unique perspective and source prioritization, resulting in well-rounded research coverage.

## Integration Points

- **Gemini Deep Research API**: Powers comprehensive web research with long-running background tasks
- **Claude Code Task Tool**: Orchestrates parallel agent execution
- **Policy Council**: Research outputs can feed into Phase 1 ideation as evidence base

## Research Agents

### Agent Roster

| ID | Name | Focus Area | Key Sources |
|----|------|------------|-------------|
| RA-01 | Academic Research | Scholarly literature | Journals, papers, university research |
| RA-02 | Industry Analysis | Market & business | Analyst reports, filings, trade pubs |
| RA-03 | Policy & Regulatory | Government policy | Gov sites, legislation, regulations |
| RA-04 | Technical Deep-Dive | Implementation details | Tech docs, standards, specs |
| RA-05 | International Comparative | Global perspectives | Int'l orgs, foreign sources |
| RA-06 | Public Discourse | Public opinion | News, polls, advocacy |

### Agent Definitions

Each agent is defined in `shared/agents/research/`:
- `ra01_academic.md`
- `ra02_industry.md`
- `ra03_policy.md`
- `ra04_technical.md`
- `ra05_international.md`
- `ra06_public.md`

## Workflow Execution

### Phase 1: Initialization

1. **Parse Research Topic**
   - Extract main topic from user input
   - Identify any specific angles or constraints
   - Generate topic slug for file naming

2. **Create Output Structure**
   ```
   projects/research/outputs/{timestamp}_{topic_slug}/
   ├── RA-01_academic.md
   ├── RA-02_industry.md
   ├── RA-03_policy.md
   ├── RA-04_technical.md
   ├── RA-05_international.md
   ├── RA-06_public.md
   ├── RESEARCH_MASTER.md
   └── metadata.json
   ```

### Phase 2: Parallel Research Execution

1. **Spawn Research Agents**
   - Use Claude Code Task tool to spawn agents in parallel
   - Maximum 6 concurrent agents (one per research perspective)
   - Each agent receives:
     - Full agent definition from `shared/agents/research/`
     - Research topic
     - Output format requirements

2. **Agent Execution Pattern**
   ```
   Task: "You are {agent_id} ({agent_name}).

   [Full agent definition from shared/agents/research/{agent_file}.md]

   RESEARCH TOPIC: {topic}

   Conduct comprehensive research using web search. Include:
   1. Executive Summary (200-300 words)
   2. Detailed Findings (organized by theme)
   3. Key Statistics with sources
   4. Source Citations (minimum 10)
   5. Implications & Recommendations

   Output as markdown."
   ```

3. **Progress Monitoring**
   - Track agent completion status
   - Provide updates every 2 minutes for long-running research
   - Handle agent failures gracefully

### Phase 3: Consolidation

1. **Aggregate Individual Reports**
   - Collect outputs from all completed agents
   - Note any failed agents and reasons

2. **Generate Master Report**
   - Synthesize cross-cutting themes
   - Identify points of consensus
   - Highlight contradictions or debates
   - Compile comprehensive source list

3. **Save Metadata**
   ```json
   {
     "topic": "Research topic",
     "timestamp": "ISO timestamp",
     "agents_requested": ["RA-01", "RA-02", ...],
     "agents_completed": ["RA-01", "RA-02", ...],
     "agents_failed": [],
     "total_sources": 87,
     "execution_time_seconds": 255,
     "output_files": [...]
   }
   ```

### Phase 4: Delivery

1. **Present Summary to User**
   - Key findings from each perspective
   - Total sources gathered
   - Execution time
   - Links to full reports

2. **Optional: Feed to Policy Council**
   - Research outputs can inform Phase 1 ideation
   - Provide evidence base for policy development
   - Update agent memory with research findings

## Slash Commands

| Command | Agents | Use Case |
|---------|--------|----------|
| `/research <topic>` | All 6 | Comprehensive research |
| `/research-quick <topic>` | RA-01, RA-02, RA-03 | Fast essential research |
| `/research-gemini <topic>` | Configurable | API-powered deep research |
| `/research-status [latest]` | N/A | Check research status |

## Gemini Deep Research API Integration

### When to Use

- For topics requiring comprehensive web research
- When current/recent information is critical
- For multi-source verification needs
- When standard search is insufficient

### API Configuration

```python
from integrations.gemini_deep_research import GeminiDeepResearch

researcher = GeminiDeepResearch(
    api_key="...",          # or GEMINI_API_KEY env var
    poll_interval=10,       # seconds between status checks
    max_wait_time=600       # max seconds to wait
)

# Single agent research
result = await researcher.research(
    topic="AI governance",
    agent_id="RA-03",
    approved_by_user=True
)

# Parallel multi-agent research
results = await researcher.parallel_research(
    topic="AI governance",
    agents=["RA-01", "RA-02", "RA-03"],
    approved_by_user=True
)
```

### Cost Estimation

- Gemini Deep Research: ~$2 per million tokens
- Typical research task: ~3,000 tokens per agent
- Full 6-agent research: ~$0.036 estimated

## Output Formats

### Individual Agent Report

```markdown
# [Agent Name] Research: [Topic]

## Executive Summary
[200-300 word overview of key findings]

## Detailed Findings

### [Theme 1]
[Findings with inline citations]

### [Theme 2]
[Findings with inline citations]

## Key Statistics
- [Statistic 1] — Source: [citation]
- [Statistic 2] — Source: [citation]

## Sources
1. [Title](URL) — [Brief description]
2. [Title](URL) — [Brief description]
...

## Research Metadata
- Agent: [ID]
- Focus: [Area]
- Sources: [Count]
- Generated: [Timestamp]
```

### Master Consolidated Report

```markdown
# Consolidated Research Report: [Topic]

**Generated:** [Timestamp]
**Agents:** [Count]
**Total Sources:** [Count]

---

## Executive Overview
[Synthesis of all agent findings]

## Cross-Cutting Themes
[Themes appearing across multiple perspectives]

## Points of Consensus
[Areas where agents agree]

## Areas of Debate
[Conflicting findings or perspectives]

## Key Statistics Summary
[Most important data points across all agents]

---

## Individual Agent Reports

### RA-01: Academic Research
[Summary + link to full report]

### RA-02: Industry Analysis
[Summary + link to full report]

[... remaining agents ...]

---

## Complete Source List
[Deduplicated sources from all agents]

## Recommendations
[Synthesized recommendations for next steps]
```

## Integration with Policy Council

### As Evidence Base for Phase 1

```
1. Run /research on policy topic
2. Research outputs become context for policy analysts
3. Analysts reference research in their proposals
4. Citations flow through to Phase 4 papers
```

### Updating Agent Memory

After research completion, relevant findings can be added to Policy Council agent memory:

```
shared/memory/agents/{agent_id}_{project}.json
```

This allows policy analysts to reference research findings in subsequent phases.

## Best Practices

1. **Start Broad, Then Narrow**
   - Use `/research` for initial topic exploration
   - Follow up with targeted `/research-quick` on specific angles

2. **Verify Critical Claims**
   - Cross-reference findings across agents
   - Note conflicting information
   - Use SA-04 (Verification) for fact-checking

3. **Track Sources**
   - Always include source URLs
   - Note publication dates for currency
   - Distinguish primary vs. secondary sources

4. **Manage Costs**
   - Use `/research-quick` for routine research
   - Reserve `/research-gemini` for comprehensive needs
   - Monitor costs in metadata.json

## Troubleshooting

### Agent Timeout
- Increase `max_wait_time` for complex topics
- Check network connectivity
- Try running agents individually

### Missing Sources
- Some sources may be paywalled
- Try different agent perspectives
- Use RA-04 Technical for specialized sources

### API Key Issues
- Verify `GEMINI_API_KEY` is set
- Check API quota limits
- System falls back to mock mode without key
