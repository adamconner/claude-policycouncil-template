# Research Status

Check the status of research projects and outputs.

## Arguments
- `$ARGUMENTS` - Optional: specific project folder or "latest"

## Instructions

You are checking the status of research outputs. This command shows available research results and their completion status.

### Execution Steps

1. **List Research Outputs**:
   Check `projects/research/outputs/` for completed research:
   ```bash
   ls -la projects/research/outputs/
   ```

2. **For Each Research Project**, show:
   - Topic researched
   - Date/time completed
   - Agents used
   - Number of sources gathered
   - File sizes

3. **If "latest" specified**:
   - Find most recent research folder
   - Display summary from RESEARCH_MASTER.md or RESEARCH_SUMMARY.md
   - List all output files with links

4. **If specific folder specified**:
   - Navigate to that folder
   - Read and display metadata.json
   - Provide links to all outputs

### Output Format

```
📊 Research Projects Status

Recent Research:
┌──────────────────────────────────────────────────────────────┐
│ 20240115_142330_ai_governance                                │
│ Topic: AI Governance Frameworks                              │
│ Completed: 2024-01-15 14:27:45                              │
│ Agents: RA-01, RA-02, RA-03, RA-04, RA-05, RA-06 (6/6)     │
│ Sources: 87 | Files: 8                                       │
├──────────────────────────────────────────────────────────────┤
│ 20240114_093012_healthcare_ai                                │
│ Topic: Healthcare AI Regulation                              │
│ Completed: 2024-01-14 09:35:22                              │
│ Agents: RA-01, RA-03, RA-04 (3/6)                           │
│ Sources: 42 | Files: 5                                       │
└──────────────────────────────────────────────────────────────┘

Commands:
- /research-status latest      - View most recent research
- /research-status [folder]    - View specific project
- /research [topic]            - Start new research
```

### Example: Latest Research

```
/research-status latest
```

Output:
```
📊 Latest Research: AI Governance Frameworks

📅 Completed: 2024-01-15 14:27:45
⏱️ Duration: 4m 15s
💰 Est. Cost: $0.018

Agents Completed:
✅ RA-01 Academic - 15 sources
✅ RA-02 Industry - 12 sources
✅ RA-03 Policy - 18 sources
✅ RA-04 Technical - 14 sources
✅ RA-05 International - 16 sources
✅ RA-06 Public - 12 sources

Output Files:
- RESEARCH_MASTER.md (consolidated report)
- RA-01_academic.md
- RA-02_industry.md
- RA-03_policy.md
- RA-04_technical.md
- RA-05_international.md
- RA-06_public.md
- metadata.json

📁 Location: projects/research/outputs/20240115_142330_ai_governance/
```
