# Phase 1: Policy Idea Generation - Workflow

## Overview

Phase 1 is the foundation of the policy development process. Each of the 16 policy analysts generates policy ideas from their unique ideological/interest perspective, resulting in comprehensive coverage of the policy landscape.

**Note:** This is a shared workflow used by all projects. File paths like `outputs/phase1/` refer to the current project's folder (e.g., `projects/economic-prosperity/outputs/phase1/`). Agent definitions are in `shared/agents/analysts/`.

---

## Phase Objectives

1. Generate diverse policy ideas from all 16 analysts (10+ per analyst recommended)
2. Ensure each project goal is addressed by multiple ideas
3. Document ideas with full required detail
4. Compile ideas into master documents for review
5. Present to Human Principal for initial feedback

---

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                         PHASE 1 WORKFLOW                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  STEP 1: KICKOFF                                                     │
│  ┌──────────────────┐                                                │
│  │ Council Director │                                                │
│  │ issues task      │                                                │
│  │ assignments      │                                                │
│  └────────┬─────────┘                                                │
│           │                                                          │
│           ▼                                                          │
│  STEP 2: PARALLEL IDEA GENERATION                                    │
│  ┌─────────────────────────────────────────────────────────────────┐ │
│  │  PA-01  PA-02  PA-03  PA-04  PA-05  PA-06  PA-07  PA-08         │ │
│  │  PA-09  PA-10  PA-11  PA-12  PA-13  PA-14  PA-15  PA-16         │ │
│  │  (Each generates 10+ ideas using web search for research)       │ │
│  └───────────────────────────┬─────────────────────────────────────┘ │
│                              │                                       │
│                              ▼                                       │
│  STEP 3: COMPILATION                                                 │
│  ┌──────────────────┐    ┌────────────────────┐                      │
│  │ Writer/Editor    │───▶│ Master Document    │                      │
│  │ compiles         │    │ + Spreadsheet      │                      │
│  └──────────────────┘    └─────────┬──────────┘                      │
│                                    │                                 │
│                                    ▼                                 │
│  STEP 4: QUALITY REVIEW                                              │
│  ┌──────────────────┐    ┌────────────────────┐                      │
│  │ QA/Fact Checker  │───▶│ Verified Documents │                      │
│  │ validates claims │    │                    │                      │
│  └──────────────────┘    └─────────┬──────────┘                      │
│                                    │                                 │
│                                    ▼                                 │
│  STEP 5: DIRECTOR REVIEW                                             │
│  ┌──────────────────┐    ┌────────────────────┐                      │
│  │ Council Director │───▶│ Final Documents    │                      │
│  │ reviews & approves│   │                    │                      │
│  └──────────────────┘    └─────────┬──────────┘                      │
│                                    │                                 │
│                                    ▼                                 │
│  STEP 6: HUMAN PRINCIPAL PRESENTATION                                │
│  ┌──────────────────────────────────────────┐                        │
│  │ Present policy ideas for review          │                        │
│  │ Await selection for further development  │                        │
│  └──────────────────────────────────────────┘                        │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Step-by-Step Instructions

### Step 1: Kickoff (Council Director)

**Actions:**
1. Review project goals and constraints (from project's `config/goals.md`)
2. Issue formal task assignments to all 16 analysts
3. Provide deadline and quality expectations
4. Confirm research permissions (web search enabled)
5. Establish communication channels for questions

**Task Assignment Template:**
```
TASK ASSIGNMENT: Policy Idea Generation

TO: [Analyst ID]
FROM: Council Director
DATE: [Date]

ASSIGNMENT:
Generate 10 policy ideas for AI development and adoption that
address economic prosperity in the United States.

REQUIREMENTS:
- Minimum 10 ideas
- At least 3 ideas addressing each goal:
  1. Broad Economic Growth
  2. Economic Mobility
  3. Affordability
- Original ideas encouraged (existing ideas acceptable)
- Use web search for current research and data
- Follow policy idea template format

DEADLINE: [Date/Time]

RESOURCES: Review your agent definition and the goals.md file.
```

---

### Step 2: Idea Generation (All 16 Analysts - Parallel)

**Instructions for Each Analyst:**

1. **Initialize Memory (First Time)**
   - Copy template from `shared/memory/memory_template.json`
   - Create your memory file: `projects/[project]/memory/[your-id]_[project].json`
   - Fill in basic agent info (id, perspective, project)
   - Set Phase 1 status to "in_progress"

2. **Review Your Role**
   - Read your agent definition thoroughly
   - Understand your ideological/interest perspective
   - Review the three core policy goals

3. **Research Phase**
   - Use web search to research current AI policy landscape
   - Find existing policy proposals relevant to your perspective
   - Identify gaps where new ideas are needed
   - Research examples, precedents, and evidence
   - **Document research in memory:** Add to `phases.phase1.research_conducted`

4. **Idea Generation**
   - Generate 10 policy ideas minimum
   - Ensure at least 3 ideas per goal
   - Prioritize ORIGINAL ideas, not just rehashing existing proposals
   - Think creatively within your perspective

5. **Documentation**
   - Use the policy idea template for each idea
   - Include all required elements:
     - Headline
     - Description (100-200 words)
     - Goal(s) addressed
     - Pros (3-5)
     - Cons (3-5)
     - Implementation challenges (3)
     - Estimated cost range
   - **Record in memory:** Add each idea to `phases.phase1.ideas_generated`

6. **Complete Memory Update**
   - Set Phase 1 status to "completed"
   - Add completion timestamp
   - Identify ideological themes across your ideas
   - Update metadata (total_ideas_generated)

**Policy Idea Template:**
```markdown
## [POLICY HEADLINE]

**Analyst:** [Your ID and Perspective]
**Goal(s) Addressed:** [Broad Growth | Mobility | Affordability]
**Estimated Cost:** [$X - $Y over Z years]

### Description
[100-200 word description of the policy, what it does, and how it works]

### Pros
1. [Pro 1]
2. [Pro 2]
3. [Pro 3]
4. [Pro 4 - optional]
5. [Pro 5 - optional]

### Cons
1. [Con 1]
2. [Con 2]
3. [Con 3]
4. [Con 4 - optional]
5. [Con 5 - optional]

### Implementation Challenges
1. [Challenge 1]
2. [Challenge 2]
3. [Challenge 3]

---
```

---

### Step 3: Compilation (Writer/Editor)

**Actions:**
1. Collect all analyst submissions
2. **Verify memory files updated:** Check that all 16 analysts have Phase 1 completed in memory
3. Verify completeness (120 ideas, all fields)
4. Check goal distribution (≥36 per goal total)
5. Format consistently using templates
6. Create two output documents:

**Output 1: Master Policy Ideas Document**
- Organized by analyst
- Each analyst section clearly labeled
- Ideas within each section tagged by goal
- Consistent formatting throughout

**Output 2: Policy Ideas Spreadsheet (CSV)**
```csv
ID,Headline,Description,Analyst,Analyst_Perspective,Goal_Growth,Goal_Mobility,Goal_Affordability,Cost_Estimate
1,"[Headline]","[One sentence]","PA-01","Economic Populist",1,0,1,"$X-$Y"
...
```

---

### Step 4: Quality Review (QA/Fact Checker)

**Actions:**
1. Review all 120 policy ideas
2. Verify factual claims (statistics, precedents, costs)
3. Flag unsupported assertions
4. Check for internal consistency
5. Provide verification report to Writer/Editor
6. Writer/Editor incorporates corrections

**Priority Verification:**
- Cost estimates (methodology reasonable?)
- Historical precedents (accurately described?)
- Statistics (sourced and current?)
- Legal claims (accurate?)

---

### Step 5: Director Review (Council Director)

**Actions:**
1. Review compiled documents
2. Verify all requirements met:
   - [ ] Expected number of ideas generated
   - [ ] All 16 analysts contributed
   - [ ] All project goals addressed
   - [ ] All required fields complete
   - [ ] QA verification complete
3. Review for overall quality and coherence
4. Approve for Human Principal presentation

---

### Step 6: Human Principal Presentation

**Actions:**
1. Present final documents to Human Principal:
   - Master Policy Ideas Document (.md)
   - Policy Ideas Spreadsheet (.csv)
2. Provide executive summary of key themes
3. Note any cross-cutting patterns or innovations
4. Request feedback and selection guidance

**Presentation Format:**
```markdown
## PHASE 1 DELIVERABLE: Policy Idea Generation Complete

### Summary
- Total ideas generated: 120
- Ideas per goal:
  - Broad Growth: [X]
  - Economic Mobility: [X]
  - Affordability: [X]

### Key Themes Observed
1. [Theme across multiple analysts]
2. [Theme across multiple analysts]

### Notable Original Ideas
1. [Idea that stands out]
2. [Idea that stands out]

### Documents Attached
1. Policy_Ideas_Master_Document.md
2. Policy_Ideas_Spreadsheet.csv

### Requested Action
Please review and identify ideas for:
- Further refinement
- Inclusion in debate phase
- Removal from consideration
```

---

## Quality Checkpoints

### Checkpoint 1: Pre-Compilation
- [ ] All 16 analysts submitted
- [ ] Each submitted 10+ ideas
- [ ] Format compliance checked

### Checkpoint 2: Post-Compilation
- [ ] 120 ideas in master document
- [ ] Spreadsheet complete and accurate
- [ ] Goal distribution verified

### Checkpoint 3: Post-QA
- [ ] Fact-check complete
- [ ] Corrections incorporated
- [ ] No major accuracy issues

### Checkpoint 4: Final
- [ ] Council Director approved
- [ ] Documents formatted correctly
- [ ] Ready for Human Principal

---

## Outputs

### Required Deliverables
| Document | Format | Location (relative to project folder) |
|----------|--------|---------------------------------------|
| Policy Ideas Master Document | .md | `outputs/phase1/policy_ideas_master.md` |
| Policy Ideas Spreadsheet | .csv | `outputs/phase1/policy_ideas.csv` |
| QA Verification Report | .md | `outputs/phase1/qa_report.md` |
| Director Certification | .md | `outputs/phase1/director_certification.md` |

**Example full path:** `projects/economic-prosperity/outputs/phase1/policy_ideas_master.md`

---

## Timeline

| Step | Duration | Cumulative |
|------|----------|------------|
| Kickoff | 0.5 hours | 0.5 hours |
| Idea Generation (parallel) | 4-6 hours | 6.5 hours |
| Compilation | 2 hours | 8.5 hours |
| QA Review | 3 hours | 11.5 hours |
| Director Review | 1 hour | 12.5 hours |
| Presentation | 0.5 hours | 13 hours |

**Total Estimated Time:** 13 hours (can be compressed with parallel work)

---

## Transition to Phase 2

Upon Human Principal review, Phase 2 (Policy Debate) begins. Phase 2 can proceed with all 120 ideas while Human Principal is reviewing Phase 1 deliverables.

**Memory System Preparation:**
- All analysts should have Phase 1 memory completed
- Phase 1 memories will be referenced during Phase 2 voting
- Analysts will recall their own ideas when voting and debating
- See `shared/memory/memory_schema.md` for details

---

*Workflow Version: 2.0 (Multi-project)*
*Last Updated: December 2025*
