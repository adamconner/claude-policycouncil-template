# AI Policy Council - Shared Architecture
**Version:** 2.0
**Jurisdiction:** United States of America
**Last Updated:** 2024

## Overview

This document defines the shared architecture for all AI Policy Council projects. Future projects inherit this architecture automatically, requiring only project-specific goals and configuration.

---

## 1. Architecture Philosophy

### 1.1 Minimal Project Configuration
New projects require only:
- `config/goals.md` - Project-specific policy goals
- `config/project.md` - Optional project-specific overrides (scope, timeline, constraints)

Everything else draws from shared resources:
- Agent definitions and voting rules
- Phase workflows and completion criteria
- Document templates and output formats
- Quality assurance processes

### 1.2 Shared Resource Locations
```
shared/
├── COUNCIL_ARCHITECTURE.md    # This document - master specification
├── agents/
│   ├── analysts/              # 16 Policy Analyst agents (PA-01 to PA-16)
│   ├── specialists/           # 8 Specialist agents (SA-01 to SA-08)
│   └── [support roles]        # Non-voting support agents
├── config/
│   └── voting_rules.md        # Voting procedures and agent roster
├── templates/
│   ├── phase3_initial_paper.md
│   ├── phase4_full_development.md
│   └── [document templates]
└── workflows/
    ├── phase1_idea_generation.md
    ├── phase2_debate.md
    ├── phase3_refinement.md
    ├── phase4_full_development.md
    └── phase5_rollout.md
```

---

## 2. Council Composition

### 2.1 Voting Agents (19 Total)

#### Policy Analysts (12 Total)
| ID | Perspective | Voting Focus |
|----|-------------|--------------|
| PA-01 | Economic Populist | Working-class economic impact |
| PA-02 | Progressive | Progressive reform (liberal to center-left) |
| PA-04 | Centrist | Bipartisan viability |
| PA-06 | Conservative/Market | Market principles (center-right to free market) |
| PA-07 | MAGA Conservative | Traditional values and sovereignty |
| PA-09 | AI Safety | Risk mitigation and safeguards |
| PA-10 | AI Accelerationist | Technology advancement |
| PA-11 | Capital & Industry | Investment climate and industry growth |
| PA-12 | Rights & Consumer Protection | Civil rights and consumer protections |
| PA-13 | Organized Labor | Worker protections |
| PA-15 | Environmental/Climate | Sustainability |
| PA-16 | Small Business | SMB impact |

#### Specialist Agents (7 Total)
| ID | Role | Expertise |
|----|------|-----------|
| SA-01 | Legislative Counsel | Bill drafting, amendment language, legislative strategy, constitutional analysis |
| SA-02 | Legal Counsel | Constitutional and regulatory law |
| SA-03 | SCOTUS Analyst | Supreme Court jurisprudence |
| SA-04 | Verification & Sources | Fact checking, verification, and citations |
| SA-06 | Polling Expert | Public opinion analysis |
| SA-07 | Budget Expert | Fiscal analysis and CBO scoring |
| SA-08 | Implementation Expert | Operational feasibility |

**Note:** SA-01 (Legislative Counsel) is the sole legislative drafting specialist, combining federal and state legislative drafting capabilities with constitutional analysis and legal translation of policy concepts.

### 2.2 Non-Voting Support Roles
- **Council Director** - Facilitation and process management
- **Research Librarian** - Source gathering and verification
- **Writer/Editor** - Document preparation and consistency
- **Communications Lead** - Public-facing materials
- **Designer** - Visual elements and formatting
- **Political Strategist** - Political landscape analysis

### 2.3 Voting Rules
- **Quorum:** 16 of 19 voting agents
- **Consensus:** 80% agreement (16+ votes)
- **Strong Majority:** 66% agreement (13+ votes)
- **Simple Majority:** 51% agreement (10+ votes)
- **Vote Types:** Effectiveness, Compromise, Progressive, Conservative, Innovation, Safety

See [voting_rules.md](./config/voting_rules.md) for complete procedures.

---

## 3. Five-Phase Workflow

### Phase 1: Idea Generation
**Duration:** Initial session
**Goal:** Generate diverse policy approaches
**Output:** 10-15 policy ideas across political spectrum

**Process:**
1. Council Director presents policy goals
2. Each analyst proposes 2-3 ideas from their perspective
3. Initial clustering of similar approaches
4. Preliminary viability assessment

**Workflow:** [phase1_idea_generation.md](./workflows/phase1_idea_generation.md)

---

### Phase 2: Debate & Ranking
**Duration:** Extended deliberation
**Goal:** Evaluate and rank policy ideas
**Output:** Top 5 ranked policies with detailed scores

**Process:**
1. Present top ideas from Phase 1
2. Structured debate (3 rounds per policy)
3. Six-dimensional voting (Effectiveness, Compromise, Progressive, Conservative, Innovation, Safety)
4. Calculate aggregate scores and rankings
5. Prepare detailed rationale for top 5

**Workflow:** [phase2_debate.md](./workflows/phase2_debate.md)

---

### Phase 3: Policy Refinement (Initial Paper)
**Duration:** Single session per policy
**Goal:** Develop refined 2-page policy papers
**Output:** 3-5 standardized initial policy papers

**Process:**
1. Take top 3-5 ranked ideas from Phase 2
2. Refine and expand each into 2-page format
3. Include all 10 required content elements
4. Initial legal and constitutional review
5. Human checkpoint for direction approval

**Template:** [phase3_initial_paper.md](./templates/phase3_initial_paper.md)

**Paper Structure (2 pages):**
1. Policy Title and One-Sentence Summary
2. Problem Statement (3-4 sentences)
3. Proposed Solution (3-5 bullet points)
4. Key Mechanisms (numbered list)
5. Expected Outcomes (bullet points with metrics)
6. Political Feasibility Assessment (brief paragraph)
7. Implementation Timeline (phases)
8. Estimated Costs/Savings
9. Potential Opposition and Responses
10. Next Steps for Full Development

**Workflow:** [phase3_refinement.md](./workflows/phase3_refinement.md)

---

### Phase 4: Full Policy Development
**Duration:** Extended development
**Goal:** Comprehensive policy documentation
**Output:** 30-40 page detailed policy paper

**Process:**
1. Human selects 1-2 policies for full development
2. Deep research and analysis phase
3. Draft all 23 required sections + appendices
4. Specialist review (Legal, Budget, Implementation)
5. Standard QA (Technical, Political, Stakeholder)
6. Enhanced QA (Red Team, Legal Stress Test, Political Vulnerability, Implementation War Game)

**Template:** [phase4_full_development.md](./templates/phase4_full_development.md)

**Required Sections (23):**
1. Executive Summary
2. Problem Statement
3. Policy Objectives
4. Current Legal/Regulatory Framework
5. Proposed Solution
6. Legislative Text (Draft)
7. Implementation Mechanisms
8. Budget Analysis
9. Economic Impact Assessment
10. Stakeholder Analysis
11. Political Feasibility
12. Timeline and Milestones
13. Risk Assessment
14. Metrics and Evaluation
15. Case Studies/Precedents
16. Expert Opinions
17. Public Opinion Data
18. Recommendations
19. Stakeholder Impact Matrix
20. Alternative Approaches Considered
21. Equity Assessment
22. Regulatory Impact Analysis (RIA)
23. Administrative Procedure Timeline

**Appendices:**
- A: Full Legislative Text
- B: Detailed Budget Projections
- C: Supporting Research

**Workflow:** [phase4_full_development.md](./workflows/phase4_full_development.md)

---

### Phase 5: Supporting Rollout Materials
**Duration:** Material production
**Goal:** Create comprehensive advocacy toolkit
**Output:** 15 deliverables for policy rollout

**Process:**
1. Human approves Phase 4 paper for rollout
2. Generate core deliverables (9 items)
3. Generate additional materials (6 items)
4. Communications review
5. Final human approval

**Core Deliverables (9):**
1. Press Release (1 page)
2. Op-Ed Draft (800-1000 words)
3. Social Media Thread (10-15 posts)
4. Policy Brief for Legislators (2 pages)
5. Talking Points (1 page)
6. Draft Legislation with Section-by-Section Analysis
7. Congressional Testimony Draft (5-7 pages)
8. Regulatory Comments Template
9. State-Level Adaptation Guide (CA/CO focus)

**Additional Deliverables (6):**
10. Fact Sheet (1 page, infographic-ready)
11. FAQ Document (15-20 questions)
12. Social Media Toolkit (graphics specs, hashtags, scheduling)
13. Coalition Letter Template
14. Hill Leave-Behind (2 pages)
15. Opposition Research Brief

**Workflow:** [phase5_rollout.md](./workflows/phase5_rollout.md)

---

## 4. Quality Assurance

### 4.1 Standard QA Tests (All Phases)
- **Technical Review:** Accuracy of data and citations
- **Political Review:** Feasibility and coalition potential
- **Stakeholder Review:** Impact assessment completeness

### 4.2 Enhanced QA Tests (Phase 4+)
- **Red Team Review:** Devil's advocate critique attempting to defeat the policy
- **Legal Stress Test:** Constitutional challenges, preemption issues, litigation risks
- **Political Vulnerability Scan:** Attack ad simulation, opposition research
- **Implementation War Game:** Agency simulation of rollout challenges

### 4.3 Citation Standards
All citations must be flagged:
- `[VERIFIED]` - Source confirmed accessible and accurate
- `[VERIFICATION NEEDED]` - Source requires human confirmation

---

## 5. Process Requirements

### 5.1 Human Checkpoints
Required human approval at:
- End of Phase 1 (idea selection)
- End of Phase 2 (ranking approval)
- End of Phase 3 (policies for full development)
- End of Phase 4 (rollout approval)
- End of Phase 5 (final release)

### 5.2 Iteration Loops
- Phase 4 may return to Phase 3 if fatal flaws discovered
- Phase 5 may return to Phase 4 for revisions
- Any phase may iterate internally before completion

### 5.3 Version Control
All policy papers maintain version history:
- Major versions (v1.0, v2.0) for significant changes
- Minor versions (v1.1, v1.2) for refinements
- Track changes through drafts

### 5.4 Dissent Documentation
- Record minority agent opinions in all phases
- Include dissent summaries in final papers
- Preserve full dissent arguments in appendices

---

## 6. Project Setup Guide

### 6.1 New Project Checklist
```
projects/[project-name]/
├── PROJECT_DASHBOARD.md      # Project status and navigation
├── config/
│   ├── goals.md              # REQUIRED: Policy goals and priorities
│   └── project.md            # OPTIONAL: Project-specific overrides
└── outputs/
    ├── phase1/
    ├── phase2/
    ├── phase3/
    ├── phase4/
    └── phase5/
```

### 6.2 Minimal goals.md Template
```markdown
# [Project Name] - Policy Goals

## Primary Objective
[One sentence describing the main policy goal]

## Specific Goals
1. [Goal 1]
2. [Goal 2]
3. [Goal 3]

## Scope
- Geographic: [National/State/Local]
- Sector: [Relevant sectors]
- Timeline: [Target timeframe]

## Constraints
- [Any specific limitations or requirements]

## Success Criteria
- [How success will be measured]
```

### 6.3 Optional project.md Overrides
Use only if deviating from shared architecture:
```markdown
# Project-Specific Configuration

## Agent Modifications
[Any changes to voting agents for this project]

## Phase Customization
[Any workflow modifications]

## Output Requirements
[Any special deliverable requirements]
```

---

## 7. Reference Links

### Shared Resources
- [Voting Rules](./config/voting_rules.md)
- [Phase 1 Workflow](./workflows/phase1_idea_generation.md)
- [Phase 2 Workflow](./workflows/phase2_debate.md)
- [Phase 3 Workflow](./workflows/phase3_refinement.md)
- [Phase 4 Workflow](./workflows/phase4_full_development.md)
- [Phase 5 Workflow](./workflows/phase5_rollout.md)

### Templates
- [Phase 3 Initial Paper](./templates/phase3_initial_paper.md)
- [Phase 4 Full Development](./templates/phase4_full_development.md)

### Agent Definitions
- [Analysts Directory](./agents/analysts/)
- [Specialists Directory](./agents/specialists/)

---

## Version History
| Version | Date | Changes |
|---------|------|---------|
| 3.0 | Dec 2024 | Option B agent consolidation: 24→19 voting agents (merged PA-02+PA-03, PA-05+PA-06, PA-08+PA-11, PA-12+PA-14, SA-04+SA-05) |
| 2.1 | Dec 2024 | Merged redundant Legislative Drafter into SA-01 Legislative Counsel |
| 2.0 | 2024 | Added 5-phase workflow, 8 specialist agents, enhanced QA, process requirements |
| 1.0 | 2024 | Initial 3-phase architecture with 16 analysts |
