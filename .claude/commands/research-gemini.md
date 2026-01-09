# Gemini Deep Research API

Run deep research using Google's Gemini Deep Research API for comprehensive web-sourced analysis.

## Arguments
- `$ARGUMENTS` - Research topic and optional flags

## Syntax
```
/research-gemini <topic> [--agents RA-01,RA-02,...] [--output json|markdown]
```

## Instructions

You are running research using the Gemini Deep Research API. This provides more comprehensive web research than standard search.

### Prerequisites

1. **API Key Required**: Ensure `GEMINI_API_KEY` is set in environment
2. **Package Required**: `google-genai >= 1.55.0`

### Available Research Agents

| Agent | Focus | Source Priorities |
|-------|-------|-------------------|
| RA-01 | Academic | Journals, working papers, university research |
| RA-02 | Industry | Analyst reports, corporate filings, trade pubs |
| RA-03 | Policy | Government sites, legislative databases |
| RA-04 | Technical | Tech docs, engineering blogs, standards |
| RA-05 | International | International orgs, foreign government sources |
| RA-06 | Public | News outlets, polling orgs, advocacy groups |

### Execution Steps

1. **Parse Arguments**:
   - Extract topic
   - Parse optional `--agents` flag (default: all 6)
   - Parse optional `--output` flag (default: markdown)

2. **Verify API Access**:
   ```python
   # Check for API key
   import os
   api_key = os.getenv('GEMINI_API_KEY')
   if not api_key:
       print("⚠️ GEMINI_API_KEY not set. Configure in .env file.")
       return
   ```

3. **For Each Agent, Create Deep Research Request**:

   Using the Gemini Interactions API:
   ```python
   from google import genai

   client = genai.Client(api_key=api_key)

   interaction = client.interactions.create(
       input=research_prompt,
       agent='deep-research-pro-preview-12-2025',
       background=True
   )
   ```

4. **Poll for Completion**:
   - Deep Research typically takes 2-10 minutes
   - Poll every 10 seconds
   - Maximum wait: 10 minutes per agent

5. **Save Results**:
   ```
   projects/research/outputs/gemini_{timestamp}_{topic}/
   ├── RA-01_academic.md
   ├── RA-02_industry.md
   ├── ...
   ├── RESEARCH_MASTER.md
   └── metadata.json
   ```

6. **Cost Tracking**:
   - Gemini Deep Research: $2 per million input tokens
   - Log estimated costs in metadata.json

### Without API Key (Mock Mode)

If no API key is configured, the system runs in mock mode:
- Returns placeholder research structure
- Allows testing workflow without API costs
- Clearly marked as [MOCK] in output

### Example Usage

```bash
# Full 6-agent research
/research-gemini AI safety alignment techniques

# Specific agents only
/research-gemini healthcare AI --agents RA-01,RA-03,RA-04

# JSON output
/research-gemini autonomous vehicles --output json
```

### Progress Updates

```
⏱️ Gemini Deep Research Progress
📋 Topic: AI Safety Alignment Techniques
🤖 Agents: RA-01, RA-02, RA-03, RA-04, RA-05, RA-06

Status:
✅ RA-01 Academic - Complete (127s, ~3000 tokens)
✅ RA-02 Industry - Complete (98s, ~2800 tokens)
🔄 RA-03 Policy - In progress (45s elapsed)
🔄 RA-04 Technical - In progress (45s elapsed)
⏳ RA-05 International - Queued
⏳ RA-06 Public - Queued

Estimated cost so far: $0.012
```

### Output Format

Each agent produces:

```markdown
# [Agent Name] Research: [Topic]

## Executive Summary
[200-300 word overview]

## Detailed Findings

### [Theme 1]
[Findings with citations]

### [Theme 2]
[Findings with citations]

## Key Statistics
- [Stat 1 with source]
- [Stat 2 with source]

## Sources
1. [Title](URL) - [Brief description]
2. [Title](URL) - [Brief description]
...

## Research Metadata
- Agent: [ID]
- Focus: [Area]
- Execution Time: [Xs]
- Sources Found: [N]
```
