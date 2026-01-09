# Deep Research Parallel Execution Guide

## Parallelization Strategy

This document defines how to maximize parallel execution in the deep research workflow.

## Execution Timeline (Optimized)

```
TIME    PHASE 0        PHASE 1-2       PHASE 3-5           PHASE 6            PHASE 7-9
0:00    ┌─────────┐
        │ Mode    │
        │ Select  │
0:30    └────┬────┘
             │
             ▼
        ┌─────────┐
        │ Topic   │
        │ Analysis│
1:00    └────┬────┘
             │
             ▼
        ┌─────────┐
        │ Format  │
        │ Confirm │
1:30    └────┬────┘
             │
             ├──────────────────┬──────────────────┐
             ▼                  ▼                  ▼
        ┌─────────┐       ┌─────────┐       ┌─────────┐
        │ Validate│       │ Gen Spec│       │ Gemini  │
        │ URLs    │       │ + Folder│       │ Pro Opt │
        │ (||)    │       │         │       │ (if on) │
2:00    └────┬────┘       └────┬────┘       └────┬────┘
             └─────────────────┴─────────────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
        ┌─────────┐       ┌─────────┐       ┌─────────┐
        │ RA-01   │       │ RA-02   │       │ RA-03   │
        │ Academic│       │ Legal   │       │ Technical
        └────┬────┘       └────┬────┘       └────┬────┘
             │                 │                 │
             ▼                 ▼                 ▼
        ┌─────────┐       ┌─────────┐       ┌─────────┐
        │ RA-04   │       │ RA-05   │       │ RA-06   │
        │ Market  │       │ Policy  │       │ Media   │
5:00    └────┬────┘       └────┬────┘       └────┬────┘
             └─────────────────┴─────────────────┘
                               │
                               ▼
                         ┌─────────┐
                         │ Gap     │
                         │ Analysis│
6:00                     └────┬────┘
                              │
                    (if follow-up needed)
                              │
             ┌────────────────┼────────────────┐
             ▼                ▼                ▼
        ┌─────────┐      ┌─────────┐     ┌─────────┐
        │ Follow  │      │ Follow  │     │ Follow  │
        │ Up #1   │      │ Up #2   │     │ Up #3   │
7:00    └────┬────┘      └────┬────┘     └────┬────┘
             └────────────────┴────────────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
              ┌─────────┐         ┌─────────┐
              │ Writer  │         │ Validate│
              │ Synth   │         │ URLs    │
              │         │         │ (||)    │
8:00          └────┬────┘         └────┬────┘
                   └─────────┬─────────┘
                             ▼
                       ┌─────────┐
                       │ Final   │
                       │ Output  │
9:00                   └─────────┘
```

**Time Savings:**
- Sequential: ~25-35 minutes
- Parallel: ~8-12 minutes
- **Savings: 60-70%**

---

## Phase-by-Phase Parallel Instructions

### Phase 3-5: Post-Confirmation Parallel Block

**Execute these three tasks IN PARALLEL immediately after user confirms format:**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ PARALLEL BLOCK 1: Post-Confirmation Setup                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Task 1: URL Validation (if context docs provided)                          │
│  ─────────────────────────────────────────────────────────────────────────  │
│  For ALL URLs simultaneously:                                               │
│  - Validate accessibility                                                   │
│  - Generate summaries for accessible URLs                                   │
│  - Categorize: Accessible | Redirect | Paywall | Broken                     │
│                                                                             │
│  Task 2: Research Spec Generation                                           │
│  ─────────────────────────────────────────────────────────────────────────  │
│  - Create output directory structure                                        │
│  - Save phase0_research_spec.json                                           │
│  - Save phase1_format_config.json                                           │
│  - Initialize RESEARCH_LOG.md                                               │
│                                                                             │
│  Task 3: Gemini Pro Optimization (if enabled)                               │
│  ─────────────────────────────────────────────────────────────────────────  │
│  - Optimize search queries for all angles                                   │
│  - Save optimized prompts to work/gemini_prompts/                           │
│                                                                             │
│  WAIT FOR ALL THREE before proceeding to Phase 6                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Phase 6: Research Execution (MAXIMUM PARALLELIZATION)

**This is the highest-value parallelization opportunity.**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ PARALLEL BLOCK 2: Research Agent Execution                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CLAUDE ONLY MODE: Run all 6 agents simultaneously                          │
│  ───────────────────────────────────────────────────────────────────────    │
│                                                                             │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌───────┐│
│  │ RA-01   │  │ RA-02   │  │ RA-03   │  │ RA-04   │  │ RA-05   │  │ RA-06 ││
│  │Academic │  │ Legal   │  │Technical│  │ Market  │  │ Policy  │  │ Media ││
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘  └─────────┘  └───────┘│
│       ↓            ↓            ↓            ↓            ↓           ↓     │
│  [All 6 Task agents spawned in SINGLE message with 6 tool calls]           │
│                                                                             │
│  GEMINI MODE: Run up to 3 parallel (API limit), then next 3                 │
│  ───────────────────────────────────────────────────────────────────────    │
│                                                                             │
│  Batch 1:  ┌─────────┐  ┌─────────┐  ┌─────────┐                            │
│            │ RA-01   │  │ RA-02   │  │ RA-03   │                            │
│            └─────────┘  └─────────┘  └─────────┘                            │
│                              ↓                                              │
│  Batch 2:  ┌─────────┐  ┌─────────┐  ┌─────────┐                            │
│            │ RA-04   │  │ RA-05   │  │ RA-06   │                            │
│            └─────────┘  └─────────┘  └─────────┘                            │
│                                                                             │
│  HYBRID MODE: All Claude in parallel, then Gemini batch on selected         │
│  ───────────────────────────────────────────────────────────────────────    │
│                                                                             │
│  Step 1: All 6 Claude agents in parallel (quick scan)                       │
│  Step 2: User selects 2-3 angles for deep dive                              │
│  Step 3: Selected angles run Gemini in parallel (up to 3)                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Phase 8: Follow-Up Research (Parallel)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ PARALLEL BLOCK 3: Follow-Up Queries                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  If gap analysis identifies multiple gaps, run follow-ups in parallel:      │
│                                                                             │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐              │
│  │ Follow-Up #1    │  │ Follow-Up #2    │  │ Follow-Up #3    │              │
│  │ (Gap from RA-02)│  │ (Gap from RA-03)│  │ (Gap from RA-05)│              │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘              │
│                                                                             │
│  Maximum parallel follow-ups: 5                                             │
│  If more than 5 gaps, batch into groups of 5                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Phase 9: Writer + Validation (Parallel)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ PARALLEL BLOCK 4: Writer Synthesis + Source Validation                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  For FULL VALIDATION mode, run validation parallel to writer:               │
│                                                                             │
│  ┌─────────────────────────┐    ┌─────────────────────────┐                 │
│  │ Writer Agent (WA-01)    │    │ URL Validation          │                 │
│  │ - Synthesize research   │    │ - Check all URLs        │                 │
│  │ - Create draft          │    │ - Categorize status     │                 │
│  │ - Format output         │    │ - Flag broken links     │                 │
│  └───────────┬─────────────┘    └───────────┬─────────────┘                 │
│              │                              │                               │
│              └──────────────┬───────────────┘                               │
│                             ▼                                               │
│                    ┌─────────────────┐                                      │
│                    │ Merge Results   │                                      │
│                    │ - Add validation│                                      │
│                    │   report        │                                      │
│                    │ - Flag issues   │                                      │
│                    └─────────────────┘                                      │
│                                                                             │
│  For SPOT CHECK mode, validation runs inside Writer (no parallel gain)      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Implementation: Parallel Task Patterns

### Pattern 1: 6-Agent Research Execution

**CRITICAL: Spawn all 6 agents in a SINGLE message with 6 Task tool calls.**

```markdown
When executing Phase 6 research, you MUST use a single message containing
6 parallel Task tool invocations:

<example>
[Single message with 6 tool calls]

Task 1: RA-01 Academic Research
Task 2: RA-02 Legal Research
Task 3: RA-03 Technical Research
Task 4: RA-04 Market Research
Task 5: RA-05 Policy Research
Task 6: RA-06 Media Research

[All 6 execute simultaneously]
</example>

DO NOT:
- Send agents one at a time
- Wait for one agent before starting another
- Batch into groups smaller than 6 (unless Gemini API limits apply)
```

### Pattern 2: URL Validation Batch

```markdown
When validating context URLs or source URLs:

1. Collect ALL URLs into a single list
2. Spawn parallel WebFetch calls (max 10 per batch)
3. Process results together

<example>
[Single message with N WebFetch calls]

WebFetch 1: https://example.com/doc1
WebFetch 2: https://example.com/doc2
WebFetch 3: https://example.com/doc3
...

[All validate simultaneously]
</example>
```

### Pattern 3: Post-Confirmation Parallel Setup

```markdown
Immediately after user confirms format, spawn 3 parallel tasks:

Task 1: "Validate all context URLs: {url_list}. For each accessible URL,
         provide a 2-sentence summary. Return JSON with status and summaries."

Task 2: "Create research output directory structure at
         projects/research/outputs/{timestamp}_{topic}/
         Initialize RESEARCH_LOG.md with session metadata.
         Save research_spec.json and format_config.json."

Task 3: "Optimize search queries for Gemini Deep Research.
         Input: {research_spec}
         Output: Optimized queries per angle to work/gemini_prompts/"

[All 3 execute simultaneously]
```

---

## Timing Estimates

### Claude Only Mode (Parallel)

| Phase | Sequential | Parallel | Savings |
|-------|------------|----------|---------|
| 0-2: User Input | 1-2 min | 1-2 min | - |
| 3-5: Setup | 1-2 min | 30s | 50-75% |
| 6: Research (6 agents) | 12-18 min | 2-3 min | **83%** |
| 7: Gap Analysis | 1 min | 1 min | - |
| 8: Follow-Up | 3-5 min | 1-2 min | 60% |
| 9: Writer | 2-3 min | 2-3 min | - |
| **TOTAL** | **20-30 min** | **7-11 min** | **63%** |

### Gemini Deep Research Mode (Parallel)

| Phase | Sequential | Parallel | Savings |
|-------|------------|----------|---------|
| 0-2: User Input | 1-2 min | 1-2 min | - |
| 3-5: Setup | 2-3 min | 1 min | 67% |
| 6: Research (6 angles) | 30-60 min | 10-20 min | **67%** |
| 7: Gap Analysis | 1 min | 1 min | - |
| 8: Follow-Up | 5-10 min | 2-4 min | 60% |
| 9: Writer | 2-3 min | 2-3 min | - |
| **TOTAL** | **41-79 min** | **17-31 min** | **59%** |

### Hybrid Mode (Parallel)

| Phase | Sequential | Parallel | Savings |
|-------|------------|----------|---------|
| 0-2: User Input | 1-2 min | 1-2 min | - |
| 3-5: Setup | 1-2 min | 30s | 50-75% |
| 6a: Claude Quick Scan | 12-18 min | 2-3 min | **83%** |
| 6b: Gemini Deep (2-3) | 10-20 min | 5-10 min | 50% |
| 7: Gap Analysis | 1 min | 1 min | - |
| 8: Follow-Up | 3-5 min | 1-2 min | 60% |
| 9: Writer | 2-3 min | 2-3 min | - |
| **TOTAL** | **30-50 min** | **12-21 min** | **58%** |

---

## System Instructions for Maximum Parallelization

Add these instructions to ensure parallel execution:

```markdown
## Parallel Execution Rules for Deep Research

### RULE 1: Never Sequential When Parallel is Possible
Before executing any phase, check if multiple independent tasks exist.
If yes, spawn them in a SINGLE message with multiple Task tool calls.

### RULE 2: 6-Agent Research is ALWAYS Parallel
Phase 6 research execution MUST use 6 simultaneous Task agents (Claude mode)
or 2 batches of 3 (Gemini mode). Never run agents sequentially.

### RULE 3: Batch URL Validation
All URL validation (context docs, source validation) runs in parallel batches
of up to 10 URLs per batch.

### RULE 4: Post-Confirmation Parallel Block
After format confirmation, ALWAYS run these 3 tasks in parallel:
1. URL validation (if context docs)
2. Directory/spec generation
3. Gemini Pro optimization (if enabled)

### RULE 5: Follow-Up Queries are Parallel
If gap analysis identifies multiple gaps, run up to 5 follow-up queries
simultaneously.

### RULE 6: Writer + Full Validation Parallel
If full validation mode is selected, run Writer synthesis and URL validation
in parallel, then merge results.
```

---

## Parallel Execution Checklist

Before each phase, verify:

- [ ] Are there multiple independent tasks? → Parallelize
- [ ] Am I spawning Task agents one at a time? → STOP, batch them
- [ ] Am I waiting for URL validation before other setup? → Run in parallel
- [ ] Am I running research agents sequentially? → STOP, run all 6 together
- [ ] Am I running follow-up queries one by one? → Batch up to 5
