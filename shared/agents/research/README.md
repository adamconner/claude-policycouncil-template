# Research Agents

Specialized agents for multi-angle deep research using Google Gemini Deep Research API.

## Overview

Research agents are designed to investigate topics from multiple perspectives simultaneously, leveraging parallel execution and the Gemini Deep Research API for comprehensive web research.

## Agent Roster

| ID | Agent | Focus Area | Specialization |
|----|-------|------------|----------------|
| RA-01 | Academic Research | Scholarly literature, peer-reviewed studies, academic discourse |
| RA-02 | Industry Analysis | Market trends, business applications, industry reports |
| RA-03 | Policy & Regulatory | Government policy, regulatory frameworks, legislative history |
| RA-04 | Technical Deep-Dive | Technical specifications, implementation details, architecture |
| RA-05 | International Comparative | Global perspectives, international approaches, cross-border analysis |
| RA-06 | Public Discourse | Media coverage, public opinion, stakeholder perspectives |

## Usage

### Via Slash Commands

```bash
# Quick 3-agent research
/research-quick "AI governance frameworks"

# Full 6-agent deep research
/research "Universal Basic Income economic impacts"

# Check status of running research
/research-status

# Generate consolidated report
/research-report latest
```

### Via Python SDK

```python
from integrations.gemini_deep_research import GeminiDeepResearch

# Initialize
researcher = GeminiDeepResearch()

# Start parallel research with multiple agents
results = await researcher.parallel_research(
    topic="AI regulation in healthcare",
    agents=["RA-01", "RA-02", "RA-03"],
    approved_by_user=True
)
```

## Output Structure

Research outputs are saved to `projects/{project}/outputs/research/`:

```
research/
├── {timestamp}_{topic}/
│   ├── RA-01_academic.md
│   ├── RA-02_industry.md
│   ├── RA-03_policy.md
│   ├── RA-04_technical.md
│   ├── RA-05_international.md
│   ├── RA-06_public.md
│   ├── RESEARCH_MASTER.md    # Consolidated findings
│   └── metadata.json         # Research metadata
```

## Integration with Policy Council

Research agents can feed directly into Policy Council workflows:
- Use research outputs as input for Phase 1 ideation
- Inform agent perspectives with research findings
- Provide evidence base for policy development
