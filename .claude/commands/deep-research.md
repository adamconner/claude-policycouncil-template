# Deep Research (Iterative Claude ↔ Gemini Loop)

Comprehensive research using the iterative Claude-Gemini research loop with format confirmation.

## Arguments
- `$ARGUMENTS` - Research topic (required)

## Overview

This command runs the full deep research workflow:
1. **Research Mode Selection** → Claude Only / Hybrid / Gemini Deep Research
2. **Claude analyzes topic** → generates research spec
3. **User confirms format** → preset, format, length, scope
4. **Optional: Gemini Pro optimization** → refines search queries
5. **Research execution** → parallel agents or Gemini Deep Research
6. **Claude analyzes gaps** → identifies missing data
7. **Optional: Follow-up research** → fills gaps
8. **Writer Agent synthesizes** → final consolidated report

---

## CRITICAL: Parallel Execution Requirements

**This workflow is optimized for maximum parallelization. Follow these rules:**

### Rule 1: 6-Agent Research is ALWAYS Parallel
```
CORRECT: Single message with 6 Task tool calls
┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
│ RA-01   │ │ RA-02   │ │ RA-03   │ │ RA-04   │ │ RA-05   │ │ RA-06   │
└─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘
     ↓           ↓           ↓           ↓           ↓           ↓
[All 6 spawn simultaneously in ONE message]

WRONG: Sequential agent calls
RA-01 → wait → RA-02 → wait → RA-03 → wait → ...
```

### Rule 2: Post-Confirmation Parallel Block
After user confirms format, run these 3 tasks IN PARALLEL (single message, 3 Task calls):
1. **Task 1:** URL validation for context documents
2. **Task 2:** Directory structure + spec generation
3. **Task 3:** Gemini Pro optimization (if enabled)

### Rule 3: URL Validation is Batched
All URL checks run in parallel batches of 10 using multiple WebFetch calls in single message.

### Rule 4: Follow-Up Queries are Parallel
If gap analysis identifies multiple gaps, run up to 5 follow-up queries simultaneously.

### Rule 5: Writer + Full Validation Parallel
If full validation mode, run Writer synthesis and URL validation in parallel, merge results.

### Time Savings
| Mode | Sequential | Parallel | Savings |
|------|------------|----------|---------|
| Claude Only | 20-30 min | 7-11 min | **63%** |
| Hybrid | 30-50 min | 12-21 min | **58%** |
| Gemini Deep | 41-79 min | 17-31 min | **59%** |

---

## Research Agents

| Agent | Focus Area |
|-------|------------|
| RA-01 | Academic/Scholarly - Peer-reviewed studies, academic discourse |
| RA-02 | Legal/Regulatory - Laws, regulations, court cases, compliance |
| RA-03 | Technical/Engineering - Technical specs, standards, implementations |
| RA-04 | Market/Industry - Market trends, business applications, competition |
| RA-05 | Policy/Government - Government policy, think tanks, international |
| RA-06 | Media/Public Opinion - News coverage, polling, public discourse |
| WA-01 | Writer - Synthesis, formatting, source validation |

---

## PHASE 0: Research Mode Selection

Present the research mode selection first:

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                     🔬 DEEP RESEARCH: MODE SELECTION                          ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  TOPIC: {topic}                                                               ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  Select research mode:                                                        ║
║                                                                               ║
║  [1] Claude Only                                                              ║
║      └─ Fast research using Claude agents with web search                     ║
║      └─ Time: 3-5 minutes | Cost: No additional cost                          ║
║      └─ Best for: Quick exploration, iterative research, tight deadlines      ║
║                                                                               ║
║  [2] Hybrid                                                                   ║
║      └─ Claude quick scan, then Gemini Deep Research on key angles            ║
║      └─ Time: 10-15 minutes | Cost: ~$0.02                                    ║
║      └─ Best for: Balanced depth and speed, focused deep dives                ║
║                                                                               ║
║  [3] Gemini Deep Research                                                     ║
║      └─ Full Gemini Deep Research on all angles (100+ sources each)           ║
║      └─ Time: 15-25 minutes | Cost: ~$0.04                                    ║
║      └─ Best for: Comprehensive research, policy documents, market analysis   ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

Store selection in `research_mode` variable for use throughout workflow.

---

## PHASE 1: Topic Analysis

Parse the research topic from: `$ARGUMENTS`

Use a Task agent to analyze the topic:

```
You are a research planning analyst. Analyze this topic and identify:

TOPIC: {topic}
RESEARCH MODE: {research_mode}

1. **Topic Classification**
   - Domain(s): [e.g., policy, technology, economics, legal]
   - Complexity: [LOW/MEDIUM/HIGH]
   - Technical depth required: [YES/NO]
   - International scope needed: [YES/NO]

2. **Research Angles** (select relevant agents from RA-01 to RA-06)
   - RA-01 Academic: [YES/NO] - Why?
   - RA-02 Legal: [YES/NO] - Why?
   - RA-03 Technical: [YES/NO] - Why?
   - RA-04 Market: [YES/NO] - Why?
   - RA-05 Policy: [YES/NO] - Why?
   - RA-06 Media: [YES/NO] - Why?

3. **Key Questions** (5-7 per selected angle)
   Specific, answerable research questions.

4. **Key Entities**
   Organizations, institutions, people to investigate.

5. **Suggested Scope**
   - Date range recommendation
   - Geographic focus
   - Source type priorities

6. **Gemini Pro Optimization** (for Hybrid/Gemini modes)
   Recommend YES/NO based on:
   - Technical domain requiring specialized terms
   - International sources needed
   - Ambiguous topic interpretation

Output as structured JSON matching research_spec_schema.json
```

---

## PHASE 2: Format Confirmation

Present the format confirmation dialog with three layers:

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                     📋 DEEP RESEARCH: FORMAT CONFIRMATION                     ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  TOPIC: {topic}                                                               ║
║  MODE: {research_mode}                                                        ║
║  ANGLES: {count} ({angle_list})                                               ║
║  COMPLEXITY: {complexity}                                                     ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  1️⃣  OUTPUT FORMAT PRESET                                                     ║
║  ────────────────────────────────────────────────────────────────────────────  ║
║                                                                               ║
║  [A] Policy Brief        - Comprehensive policy research document             ║
║      └─ Full narrative, executive summary, recommendations                    ║
║      └─ Sections: Exec Summary, Background, Key Findings, Data Tables,        ║
║                   Source Comparison, Policy Implications, Recommendations     ║
║                                                                               ║
║  [B] Market Analysis     - Industry and market research with comparisons      ║
║      └─ Data-heavy with tables and comparisons                                ║
║      └─ Sections: Market Overview, Competitive Landscape, Trends,             ║
║                   Key Players, Opportunities & Risks                          ║
║                                                                               ║
║  [C] Literature Review   - Academic-focused research synthesis                ║
║      └─ Full academic citations, theoretical depth                            ║
║      └─ Sections: Research Landscape, Key Themes, Methodology,                ║
║                   Debates & Controversies, Research Gaps                      ║
║                                                                               ║
║  [D] Quick Scan          - Fast turnaround executive brief                    ║
║      └─ Bullet points, top statistics only                                    ║
║      └─ Sections: Key Findings, Top Stats, Source Summary                     ║
║                                                                               ║
║  [E] Data Extraction     - Structured JSON for pipeline integration           ║
║      └─ Machine-readable output                                               ║
║      └─ Schema: findings, statistics, sources, metadata                       ║
║                                                                               ║
║  [F] Custom              - Configure all options manually                     ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  2️⃣  FORMAT STYLE (if preset allows customization)                            ║
║  ────────────────────────────────────────────────────────────────────────────  ║
║                                                                               ║
║  [1] Narrative Report    - Flowing prose with structured sections             ║
║  [2] Structured Brief    - Bullets, tables, concise text                      ║
║  [3] Data-Heavy          - Tables, charts, minimal prose                      ║
║  [4] JSON/Structured     - Machine-readable structured output                 ║
║                                                                               ║
║  Default for {preset}: {default_format}                                       ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  3️⃣  LENGTH TARGET                                                            ║
║  ────────────────────────────────────────────────────────────────────────────  ║
║                                                                               ║
║  [S] Executive Summary   - 2-5 pages (1,000-2,500 words)                      ║
║  [M] Standard Report     - 10-20 pages (5,000-10,000 words)                   ║
║  [L] Comprehensive       - 30-50 pages (15,000-25,000 words)                  ║
║  [C] Custom              - Specify word count or page target                  ║
║                                                                               ║
║  Default for {preset}: {default_length}                                       ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  4️⃣  SCOPE SETTINGS                                                           ║
║  ────────────────────────────────────────────────────────────────────────────  ║
║                                                                               ║
║  Date Range:        [2020-01-01] to [2025-12-31]                              ║
║  Geographic Focus:  [Global] / [US] / [EU] / [Custom: ___]                    ║
║                                                                               ║
║  Source Types:                                                                ║
║    [Y] Academic/Peer-reviewed    [Y] Government/Official                      ║
║    [Y] Industry reports          [Y] News/Media                               ║
║    [N] Social media/Forums       [Y] Legal sources                            ║
║                                                                               ║
║  Unknown Data Handling:                                                       ║
║    State "Data not available for [item]" rather than estimating               ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  5️⃣  GEMINI PRO OPTIMIZATION (if using Gemini Deep Research)                  ║
║  ────────────────────────────────────────────────────────────────────────────  ║
║                                                                               ║
║  Use Gemini Pro to optimize search queries before Deep Research?              ║
║                                                                               ║
║  System recommendation: {gemini_pro_recommendation}                           ║
║  Reason: {recommendation_reason}                                              ║
║                                                                               ║
║  [Y] Yes - Optimize queries (+$0.002, +10s)                                   ║
║  [N] No - Use Claude-generated queries directly                               ║
║  [A] Auto - Let system decide                                                 ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  6️⃣  CONTEXT DOCUMENTS (Optional)                                             ║
║  ────────────────────────────────────────────────────────────────────────────  ║
║                                                                               ║
║  Provide files/URLs to ground the research:                                   ║
║                                                                               ║
║  [ ] No context files                                                         ║
║  [ ] Use project docs from: projects/{project}/human_documents/               ║
║  [ ] Specify files: _______________                                           ║
║  [ ] Specify URLs: _______________                                            ║
║                                                                               ║
║  ⚠️  URLs will be validated before research begins                            ║
║      Accessible URLs will be summarized for context                           ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  7️⃣  SOURCE VALIDATION                                                        ║
║  ────────────────────────────────────────────────────────────────────────────  ║
║                                                                               ║
║  [S] Spot Check (Default) - Validate 20% of URLs randomly                     ║
║  [F] Full Validation      - Validate all URLs before final output             ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  📊 RESEARCH ESTIMATE                                                         ║
║  ────────────────────────────────────────────────────────────────────────────  ║
║  Angles: {angle_count}                                                        ║
║  Est. Time: {time_estimate}                                                   ║
║  Est. Cost: {cost_estimate}                                                   ║
║  Expected Sources: {source_estimate}                                          ║
║  Output Size: {output_estimate}                                               ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  [CONFIRM] Proceed with these settings                                        ║
║  [EDIT]    Modify specific settings                                           ║
║  [PREVIEW] Show generated Gemini prompts first                                ║
║  [CANCEL]  Cancel research                                                    ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### Citation Format (Applied Automatically)

All outputs use hyperlink + footnote format:
- **Inline:** `[Source Title](URL)^[N]`
- **Example:** `According to [Stanford HAI](https://aiindex.stanford.edu)^[1], adoption increased 34%.`
- **Bibliography:** Organized by source type (Academic, Legal, Market, Policy, Media)

---

## PHASE 3: Context Document Validation (If Provided)

If user provides context documents or URLs:

1. **For Files:**
   - Verify file exists and is readable
   - Check file type is supported (.pdf, .md, .txt, .docx, .csv)
   - Check file size < 50MB (max 100MB total)

2. **For URLs:**
   - Validate URL accessibility
   - Categorize: Accessible | Redirect | Paywall | Broken | Timeout
   - For accessible URLs, generate brief summary:

```
📄 Context Document Validation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Files:
✅ policy_draft_v2.pdf (2.3MB) - Ready
✅ market_data.csv (156KB) - Ready

URLs:
✅ https://www.whitehouse.gov/ai-eo - Accessible
   Summary: Executive Order on AI safety, October 2023...
✅ https://arxiv.org/abs/2303.08774 - Accessible
   Summary: GPT-4 Technical Report from OpenAI...
⚠️  https://example.com/broken - Broken (404)
🔒 https://wsj.com/article - Paywall detected

Continue with 4/5 accessible sources? [Y/N]
```

---

## PHASE 4: Research Spec Generation

After user confirms format, generate the full research specification.

Create output directory structure:
```
projects/research/outputs/{timestamp}_{topic_slug}/
├── work/                           # Working files
│   ├── phase0_research_spec.json   # Original specification
│   ├── phase1_format_config.json   # Format configuration
│   ├── ra01_academic.md            # Individual agent outputs
│   ├── ra02_legal.md
│   ├── ra03_technical.md
│   ├── ra04_market.md
│   ├── ra05_policy.md
│   ├── ra06_media.md
│   ├── gemini_prompts/             # Generated prompts (for audit)
│   │   ├── ra01_prompt.md
│   │   └── ...
│   ├── gemini_responses/           # Raw API responses
│   ├── gap_analysis.json           # Gap analysis results
│   ├── writer_draft_v1.md          # Writer's first draft
│   └── validation_report.json      # Source validation results
├── final/                          # Clean deliverables
│   ├── RESEARCH_MASTER.md          # Final consolidated report
│   └── BIBLIOGRAPHY.md             # Optional separate bibliography
├── RESEARCH_LOG.md                 # Session log for resumability
└── metadata.json                   # Execution metadata
```

Save `phase0_research_spec.json` with:
- All angles and questions from Phase 1
- Format configuration from Phase 2
- Scope settings
- Context document summaries
- Metadata (timestamps, estimates)

Initialize `RESEARCH_LOG.md`:
```markdown
# Research Session Log

**Topic:** {topic}
**Mode:** {research_mode}
**Started:** {timestamp}
**Session ID:** {session_id}

## Progress

| Phase | Status | Started | Completed | Notes |
|-------|--------|---------|-----------|-------|
| 0 - Mode Selection | ✅ Complete | {time} | {time} | Mode: {mode} |
| 1 - Topic Analysis | ✅ Complete | {time} | {time} | {n} angles selected |
| 2 - Format Confirmation | ✅ Complete | {time} | {time} | Preset: {preset} |
| 3 - Context Validation | ⏳ Pending | | | |
| 4 - Research Execution | ⏳ Pending | | | |
| 5 - Gap Analysis | ⏳ Pending | | | |
| 6 - Follow-Up | ⏳ Pending | | | |
| 7 - Writer Synthesis | ⏳ Pending | | | |
| 8 - Final Output | ⏳ Pending | | | |

## Session Events

- {timestamp}: Session started
- {timestamp}: Mode selected: {mode}
- {timestamp}: {n} research angles identified
...

---
**To resume:** `/deep-research --resume {session_id}`
```

---

## PHASE 5: Gemini Pro Optimization (If Enabled)

If user selected Gemini Pro optimization:

```
You are a search query optimization specialist. Given this research specification,
optimize the search queries for maximum effectiveness with Gemini Deep Research.

RESEARCH SPEC:
{research_spec_json}

For each research angle, provide:
1. **Optimized Search Queries** - Better phrasing for web search
2. **Additional Search Terms** - Domain-specific terminology to add
3. **Source-Specific Queries** - Queries targeting specific source types
4. **Entity-Specific Queries** - Queries for specific organizations

Output format:
{
  "angle_id": "RA-01",
  "original_questions": [...],
  "optimized_queries": [...],
  "additional_terms": [...],
  "source_specific": {...}
}
```

---

## PHASE 6: Research Execution

**⚡ PARALLEL EXECUTION REQUIRED - See rules above**

Execution depends on research mode:

### Claude Only Mode

**MUST spawn ALL 6 agents in a SINGLE message with 6 Task tool calls:**

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  PARALLEL EXECUTION BLOCK - Send as SINGLE message with 6 Task calls          ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  Task 1 (RA-01):                                                              ║
║  ───────────────                                                              ║
║  subagent_type: "general-purpose"                                             ║
║  description: "RA-01 Academic research"                                       ║
║  prompt: "You are RA-01, Academic Research Specialist.                        ║
║          Read: shared/agents/research/ra01_academic.md                        ║
║          Topic: {topic}                                                       ║
║          Output research with citations [Title](URL)^[N] format.              ║
║          Save to: work/ra01_academic.md"                                      ║
║                                                                               ║
║  Task 2 (RA-02):                                                              ║
║  ───────────────                                                              ║
║  subagent_type: "general-purpose"                                             ║
║  description: "RA-02 Legal research"                                          ║
║  prompt: "You are RA-02, Legal Research Specialist.                           ║
║          Read: shared/agents/research/ra02_legal.md                           ║
║          Topic: {topic}                                                       ║
║          Output research with citations [Title](URL)^[N] format.              ║
║          Save to: work/ra02_legal.md"                                         ║
║                                                                               ║
║  Task 3 (RA-03):                                                              ║
║  ───────────────                                                              ║
║  subagent_type: "general-purpose"                                             ║
║  description: "RA-03 Technical research"                                      ║
║  prompt: "You are RA-03, Technical Research Specialist.                       ║
║          Read: shared/agents/research/ra03_technical.md                       ║
║          Topic: {topic}                                                       ║
║          Output research with citations [Title](URL)^[N] format.              ║
║          Save to: work/ra03_technical.md"                                     ║
║                                                                               ║
║  Task 4 (RA-04):                                                              ║
║  ───────────────                                                              ║
║  subagent_type: "general-purpose"                                             ║
║  description: "RA-04 Market research"                                         ║
║  prompt: "You are RA-04, Market Research Specialist.                          ║
║          Read: shared/agents/research/ra04_market.md                          ║
║          Topic: {topic}                                                       ║
║          Output research with citations [Title](URL)^[N] format.              ║
║          Save to: work/ra04_market.md"                                        ║
║                                                                               ║
║  Task 5 (RA-05):                                                              ║
║  ───────────────                                                              ║
║  subagent_type: "general-purpose"                                             ║
║  description: "RA-05 Policy research"                                         ║
║  prompt: "You are RA-05, Policy Research Specialist.                          ║
║          Read: shared/agents/research/ra05_policy.md                          ║
║          Topic: {topic}                                                       ║
║          Output research with citations [Title](URL)^[N] format.              ║
║          Save to: work/ra05_policy.md"                                        ║
║                                                                               ║
║  Task 6 (RA-06):                                                              ║
║  ───────────────                                                              ║
║  subagent_type: "general-purpose"                                             ║
║  description: "RA-06 Media research"                                          ║
║  prompt: "You are RA-06, Media Research Specialist.                           ║
║          Read: shared/agents/research/ra06_media.md                           ║
║          Topic: {topic}                                                       ║
║          Output research with citations [Title](URL)^[N] format.              ║
║          Save to: work/ra06_media.md"                                         ║
║                                                                               ║
║  [ALL 6 TASKS EXECUTE SIMULTANEOUSLY - ~2-3 min total vs 12-18 min serial]    ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### Hybrid Mode

**Step 1: Quick Claude Scan (PARALLEL - 6 agents in single message)**
- Run all 6 agents with web search simultaneously
- Each produces quick findings (~500-1000 words)
- Identify top 2-3 angles needing deeper research
- User confirms which angles to deep dive

**Step 2: Gemini Deep Research on Key Angles (PARALLEL - up to 3)**
- Run Gemini Deep Research on selected angles in parallel
- Continue with Claude results for other angles

### Gemini Deep Research Mode

**Execute in 2 parallel batches (API limit: 3 concurrent):**

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  GEMINI BATCH 1 - Send as SINGLE message with 3 Task calls                    ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  Task 1: Gemini Deep Research for RA-01 (Academic angle)                      ║
║  Task 2: Gemini Deep Research for RA-02 (Legal angle)                         ║
║  Task 3: Gemini Deep Research for RA-03 (Technical angle)                     ║
║  [Wait for all 3 to complete]                                                 ║
╚═══════════════════════════════════════════════════════════════════════════════╝
                                    ↓
╔═══════════════════════════════════════════════════════════════════════════════╗
║  GEMINI BATCH 2 - Send as SINGLE message with 3 Task calls                    ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  Task 4: Gemini Deep Research for RA-04 (Market angle)                        ║
║  Task 5: Gemini Deep Research for RA-05 (Policy angle)                        ║
║  Task 6: Gemini Deep Research for RA-06 (Media angle)                         ║
║  [Wait for all 3 to complete]                                                 ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

**Gemini API Integration:**

```python
from integrations.gemini_deep_research import GeminiDeepResearch

researcher = GeminiDeepResearch()

# Batch 1: First 3 angles in parallel
batch1_results = await asyncio.gather(
    researcher.research(topic, "RA-01", prompt_01),
    researcher.research(topic, "RA-02", prompt_02),
    researcher.research(topic, "RA-03", prompt_03)
)

# Batch 2: Next 3 angles in parallel
batch2_results = await asyncio.gather(
    researcher.research(topic, "RA-04", prompt_04),
    researcher.research(topic, "RA-05", prompt_05),
    researcher.research(topic, "RA-06", prompt_06)
)
```

### Progress Updates

Every 2 minutes during execution:

```
⏱️ Deep Research Progress - {timestamp}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Topic: {topic}
Mode: {research_mode}

Status by Agent:
✅ RA-01 Academic     - Complete (127s, ~3200 tokens, 18 sources)
✅ RA-02 Legal        - Complete (98s, ~2800 tokens, 15 sources)
🔄 RA-03 Technical    - In progress (45s elapsed...)
🔄 RA-04 Market       - In progress (42s elapsed...)
⏳ RA-05 Policy       - Queued
⏳ RA-06 Media        - Queued

Progress: 2/6 complete | Est. remaining: ~8 min
Cost so far: ~$0.012

Next update at {next_timestamp}
```

Update `RESEARCH_LOG.md` with each progress event.

---

## PHASE 7: Gap Analysis

After all research completes, run Claude gap analysis:

```
You are a research quality analyst. Review these research results and identify gaps.

ORIGINAL RESEARCH SPEC:
{research_spec}

RESEARCH RESULTS:
{all_angle_results}

For each angle, evaluate:

1. **Completeness Score** (0.0-1.0)
   - Were all questions answered?
   - Are required metrics present?
   - Are sources properly cited with URLs?

2. **Quality Assessment**
   - Source credibility
   - Data recency
   - Confidence levels appropriate?

3. **Gaps Identified**
   - Missing data points
   - Unanswered questions
   - Conflicting information unresolved

4. **Cross-Angle Analysis**
   - Do findings align across angles?
   - Contradictions to investigate?

5. **Follow-Up Required?**
   - YES if completeness < 0.75
   - Include specific follow-up queries

Output as JSON to work/gap_analysis.json
```

---

## PHASE 8: Follow-Up Research (If Needed)

**⚡ PARALLEL EXECUTION - Run up to 5 follow-up queries simultaneously**

If gap analysis returns `follow_up_required: true`:

1. **Present to user**:
```
📊 Gap Analysis Complete

Overall Completeness: 82%

Gaps Found:
• RA-02 Legal: Missing FTC enforcement statistics
• RA-03 Technical: Conflicting performance benchmarks
• RA-05 Policy: No international comparison data

Recommended Follow-Up:
1. "FTC AI enforcement actions 2023-2025 with penalties"
2. "AI model benchmark comparison methodology differences"
3. "EU AI Act vs US AI governance comparison"

[PROCEED] Run follow-up research (~2 min parallel, ~$0.01)
[SKIP] Proceed to synthesis without follow-up
[CUSTOM] Modify follow-up queries
```

2. **Execute ALL follow-ups in PARALLEL (single message, up to 5 Task calls):**

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  PARALLEL FOLLOW-UP BLOCK - Send as SINGLE message with N Task calls          ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  Task 1: Follow-up for RA-02 gap                                              ║
║  ───────────────────────────────                                              ║
║  subagent_type: "general-purpose"                                             ║
║  prompt: "Research: FTC AI enforcement actions 2023-2025 with penalties.      ║
║          Focus on: {specific_gap_details}                                     ║
║          Use citation format: [Title](URL)^[N]                                ║
║          Save to: work/followup_ra02.md"                                      ║
║                                                                               ║
║  Task 2: Follow-up for RA-03 gap                                              ║
║  ───────────────────────────────                                              ║
║  subagent_type: "general-purpose"                                             ║
║  prompt: "Research: AI model benchmark comparison methodology differences.    ║
║          Focus on: {specific_gap_details}                                     ║
║          Use citation format: [Title](URL)^[N]                                ║
║          Save to: work/followup_ra03.md"                                      ║
║                                                                               ║
║  Task 3: Follow-up for RA-05 gap                                              ║
║  ───────────────────────────────                                              ║
║  subagent_type: "general-purpose"                                             ║
║  prompt: "Research: EU AI Act vs US AI governance comparison.                 ║
║          Focus on: {specific_gap_details}                                     ║
║          Use citation format: [Title](URL)^[N]                                ║
║          Save to: work/followup_ra05.md"                                      ║
║                                                                               ║
║  [ALL FOLLOW-UPS EXECUTE SIMULTANEOUSLY - ~1-2 min vs 5-10 min serial]        ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

3. **Re-run gap analysis** (max 2 iterations from config)

---

## PHASE 9: Writer Agent Synthesis

Run the Writer Agent (WA-01) to synthesize all research:

```
You are WA-01, the Research Writer. Your role is to synthesize research
from multiple specialist agents into a cohesive document.

Read your full agent definition from:
shared/agents/research/wa01_writer.md

INPUT RESEARCH:
{research_from_all_agents}

GAP ANALYSIS:
{gap_analysis_results}

FORMAT REQUIREMENTS:
- Preset: {preset_name}
- Format Style: {format_style}
- Length: {length_target} ({word_count} words)
- Citation Format: Hyperlink + footnote [Title](URL)^[N]
- Validation Mode: {spot_check | full_validation}

SYNTHESIS TASKS:

1. **Cross-Reference Analysis**
   - What findings appear across multiple agents?
   - Where do agents agree or disagree?
   - What themes emerge from combining perspectives?

2. **Conflict Resolution**
   - Identify conflicting claims between agents
   - Analyze which sources are more authoritative
   - Present balanced view with reasoning

3. **Structure & Organization**
   - Follow {preset_name} structure from wa01_writer.md
   - Organize findings by theme, not by agent
   - Ensure logical flow between sections

4. **Citation Management**
   - Preserve ALL inline citations from agents
   - Use format: [Title](URL)^[N]
   - Create unified bibliography organized by source type
   - Run {validation_mode} validation

5. **Gap Notation**
   - Note any remaining gaps from gap analysis
   - Flag areas with weak sourcing
   - Suggest future research directions

OUTPUT:
- First draft to: work/writer_draft_v1.md
- Validation report to: work/validation_report.json
```

### Source Validation

**⚡ For Full Validation mode, run Writer + Validation in PARALLEL:**

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  PARALLEL BLOCK (Full Validation Only) - 2 Task calls in SINGLE message       ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  Task 1: Writer Synthesis                                                     ║
║  ────────────────────────────                                                 ║
║  subagent_type: "general-purpose"                                             ║
║  prompt: "You are WA-01, Research Writer.                                     ║
║          Synthesize all research from work/*.md files.                        ║
║          Create draft to: work/writer_draft_v1.md"                            ║
║                                                                               ║
║  Task 2: URL Validation (parallel with Writer)                                ║
║  ────────────────────────────                                                 ║
║  subagent_type: "general-purpose"                                             ║
║  prompt: "Validate all URLs from research files in work/*.md.                 ║
║          Check each URL for accessibility.                                    ║
║          Categorize: Accessible | Redirect | Paywall | Broken                 ║
║          Save report to: work/validation_report.json"                         ║
║                                                                               ║
║  [BOTH EXECUTE SIMULTANEOUSLY - merge results after]                          ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

For **Spot Check** (default):
- Validate 20% of all URLs randomly (runs inside Writer task)
- Alert user if >10% broken
- Continue if validation passes

For **Full Validation**:
- Writer and URL validation run in PARALLEL (2 Task calls)
- All URLs checked simultaneously in batches of 10
- Categorize: Accessible | Redirect | Paywall | Broken
- Merge validation report with Writer output
- Present to user before finalizing
- Offer to remove broken sources or find alternatives

---

## PHASE 10: Final Output

After Writer Agent completes:

1. **Move final document to `final/` folder:**
   - `final/RESEARCH_MASTER.md`
   - `final/BIBLIOGRAPHY.md` (if separate)

2. **Create `metadata.json`:**
```json
{
  "topic": "{topic}",
  "timestamp": "{ISO timestamp}",
  "session_id": "{session_id}",
  "research_mode": "{claude_only|hybrid|gemini_deep}",
  "total_execution_time_seconds": 847,
  "phases_completed": ["mode", "spec", "format", "research", "gap_analysis", "synthesis"],
  "agents_used": ["RA-01", "RA-02", "RA-04", "RA-05"],
  "total_sources": 94,
  "validation_mode": "spot_check",
  "validation_result": {
    "urls_checked": 19,
    "accessible": 17,
    "broken": 2,
    "pass": true
  },
  "follow_up_iterations": 1,
  "total_cost_estimate": 0.043,
  "format": {
    "preset": "policy_brief",
    "style": "narrative",
    "length": "standard"
  },
  "gemini_pro_optimization": true,
  "output_files": [
    "final/RESEARCH_MASTER.md",
    "final/BIBLIOGRAPHY.md"
  ]
}
```

3. **Update `RESEARCH_LOG.md`** with completion status

4. **Present completion summary:**
```
✅ DEEP RESEARCH COMPLETE

📋 Topic: {topic}
🔬 Mode: {research_mode}
⏱️ Total Time: 14m 7s
💰 Est. Cost: $0.043
📚 Sources: 94 across {n} agents

Outputs:
• final/RESEARCH_MASTER.md - Consolidated report ({word_count} words)
• {n} individual agent reports in work/
• Full source bibliography (94 sources)
• Validation: {validation_result}

Key Findings:
1. {finding_1}
2. {finding_2}
3. {finding_3}

📁 Location: projects/research/outputs/{folder}/

[VIEW] Open RESEARCH_MASTER.md
[COUNCIL] Feed into Policy Council Phase 1
[NEW] Start new research
```

---

## Error Handling

### Gemini API Timeout
- Retry with exponential backoff (3 attempts)
- If persistent, mark angle as incomplete
- Continue with other angles
- Note in gap analysis

### Gemini API Key Missing
- Fall back to Claude-only research automatically
- Notify user of limitation
- Log in RESEARCH_LOG.md

### User Cancellation
- Save all partial results
- Update RESEARCH_LOG.md with cancellation
- Allow resume with `/deep-research --resume {session_id}`

### Network Errors
- Retry up to 4 times with exponential backoff (2s, 4s, 8s, 16s)
- Log each retry attempt
- Continue with available results if retries exhausted

---

## Resume Support

To resume an interrupted session:

```bash
/deep-research --resume {session_id}
```

The system will:
1. Read `RESEARCH_LOG.md` from the session folder
2. Identify last completed phase
3. Reload all saved outputs
4. Continue from the next pending phase
5. Present status to user before resuming
