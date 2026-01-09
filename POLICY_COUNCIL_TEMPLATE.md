# Policy Council Template: Setup Instructions for Claude Code

**Version:** 2.0
**Based on:** AI Policy Council for Economic Prosperity
**Purpose:** Template for creating multi-agent policy councils on any topic
**Jurisdiction:** All policy development is for the **United States of America** and operates within the framework of U.S. federal and state law.

---

## Quick Start

Copy and paste this prompt to Claude Code to create a new policy council:

```
Create a Policy Council on [YOUR TOPIC] using the template at POLICY_COUNCIL_TEMPLATE.md.

The council's mission is: [YOUR MISSION STATEMENT]

The core goals are:
1. [GOAL 1]
2. [GOAL 2]
3. [GOAL 3]

Please set up the full council with analysts, workflows, dashboard, and slash commands.
```

---

## Table of Contents

1. [Overview](#1-overview)
2. [Core Configuration](#2-core-configuration)
3. [Agent Definitions](#3-agent-definitions)
4. [Workflow Phases](#4-workflow-phases)
5. [Dashboard Setup](#5-dashboard-setup)
6. [Slash Commands](#6-slash-commands)
7. [Output Templates](#7-output-templates)
8. [Execution Instructions](#8-execution-instructions)
9. [Customization Guide](#9-customization-guide)

---

## 1. Overview

### What is a Policy Council?

A Policy Council is a multi-agent system that:
- Generates diverse policy ideas from multiple ideological perspectives
- Debates and votes on policies using structured processes
- Identifies consensus, compromise, and partisan priorities
- Produces actionable policy recommendations
- **Develops policies specifically for the United States federal and state governments**

### Jurisdiction Statement

> **IMPORTANT:** All policy analysis, legislative drafting, regulatory recommendations, and implementation plans produced by this Policy Council are designed for the **United States of America**. This includes:
> - Federal legislation (U.S. Congress)
> - Federal regulations (executive agencies)
> - State legislation (with California and Colorado as default model states)
> - Analysis of U.S. Constitutional issues and Supreme Court precedent

### Key Components

```
Policy Council
├── Agents (26 total)
│   ├── Policy Analysts (16) - Generate and vote on ideas
│   ├── Specialist Agents (8) - Deep expertise, also vote
│   ├── Council Director (1) - Coordinates workflow
│   └── Writer/Editor (1) - Creates documents
├── Workflows (5 phases)
│   ├── Phase 1: Idea Generation
│   ├── Phase 2: Debate & Voting
│   ├── Phase 3: Policy Refinement & Initial Deeper Proposals
│   ├── Phase 4: Full Policy Development
│   └── Phase 5: Supporting Rollout Materials
├── Outputs
│   ├── Master Documents (Markdown)
│   ├── Data Files (CSV)
│   ├── Policy Papers (2-page and 25-30 page)
│   ├── Legislative Drafts
│   └── Rollout Materials
└── Dashboard & Commands
    ├── Status Dashboard
    ├── State Tracking (JSON)
    └── Slash Commands
```

---

## 2. Core Configuration

### 2.1 Create Goals Configuration

**File:** `config/goals.md`

```markdown
# [COUNCIL NAME] Core Goals

## Jurisdiction
All policies developed by this council are for the **United States of America**.

## Mission
[ONE SENTENCE MISSION STATEMENT]

## Core Goals

All policies must be evaluated against these three goals:

### Goal 1: [NAME]
**Definition:** [2-3 sentences]
**Success Metrics:**
- [Metric 1]
- [Metric 2]
- [Metric 3]

### Goal 2: [NAME]
**Definition:** [2-3 sentences]
**Success Metrics:**
- [Metric 1]
- [Metric 2]
- [Metric 3]

### Goal 3: [NAME]
**Definition:** [2-3 sentences]
**Success Metrics:**
- [Metric 1]
- [Metric 2]
- [Metric 3]

## Evaluation Framework

When evaluating policies, analysts should consider:
1. **Primary Goal Impact** - Which goal does this primarily serve?
2. **Secondary Effects** - Does it help or harm other goals?
3. **Trade-offs** - What are the costs and who bears them?
4. **Feasibility** - Can this realistically be implemented in the U.S.?
5. **Evidence Base** - What precedents or research support this?
6. **Legal Viability** - Is this Constitutional and legally defensible?
```

### 2.2 Create Voting Rules

**File:** `config/voting_rules.md`

```markdown
# Voting Rules and Procedures

## Voting Participants

All **24 voting agents** participate in voting rounds:
- 16 Policy Analysts (PA-01 through PA-16)
- 8 Specialist Agents (SA-01 through SA-08)

Non-voting roles: Council Director, Writer/Editor

## Voting Rounds

### 1. Effectiveness Voting
- **Purpose:** Identify most effective policies regardless of ideology
- **Weight:** Equal (1x) for all 24 voting agents
- **Selection:** Each agent picks top [20-25] policies
- **Criteria:** Evidence, feasibility, impact on goals

### 2. Compromise Voting
- **Purpose:** Find policies with cross-ideological appeal
- **Weight:** Equal (1x) for all 24 voting agents
- **Selection:** Each agent picks top [15-20] policies they could accept
- **Criteria:** Political feasibility, coalition potential

### 3. Partisan Sorting
- **Purpose:** Identify priorities for different ideological coalitions
- **Creates:** 4 separate rankings with weighted voting

#### Progressive/Liberal Weighting:
| Agent | Weight |
|-------|--------|
| PA-01, PA-02 (Left) | 3x |
| PA-03 (Center-Left) | 2x |
| PA-04 (Centrist) | 1x |
| PA-12, PA-13, PA-15 (Aligned Stakeholders) | 2x |
| SA-06 (Polling - if progressive-leaning data) | 1.5x |
| All Others | 0.5x |

#### Conservative Weighting:
| Agent | Weight |
|-------|--------|
| PA-06, PA-07 (Right) | 3x |
| PA-05 (Center-Right) | 2x |
| PA-04 (Centrist) | 1x |
| PA-08, PA-11, PA-16 (Aligned Stakeholders) | 2x |
| SA-07 (Budget - if fiscal focus) | 1.5x |
| All Others | 0.5x |

#### [COALITION 3] Weighting:
[CUSTOMIZE BASED ON YOUR TOPIC]

#### [COALITION 4] Weighting:
[CUSTOMIZE BASED ON YOUR TOPIC]

## Vote Aggregation

- **Unanimous:** All 24 agents agree (strongest signal)
- **Strong Consensus:** 18+ of 24 agents (75%+)
- **Moderate Support:** 12-17 agents (50-75%)
- **Limited Support:** 6-11 agents (25-50%)
- **Minimal Support:** 1-5 agents (<25%)
```

---

## 3. Agent Definitions

### 3.1 Policy Analyst Template

**File:** `agents/analysts/pa[XX]_[name].md`

```markdown
# PA-[XX]: [ANALYST NAME]

## Identity
- **ID:** PA-[XX]
- **Role:** Policy Analyst
- **Perspective:** [IDEOLOGY/STAKEHOLDER GROUP]
- **Jurisdiction:** United States

## Ideological Framework

### Core Beliefs
- [Belief 1]
- [Belief 2]
- [Belief 3]

### Key Priorities
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]
4. [Priority 4]
5. [Priority 5]

### Intellectual Influences
- [Thinker/Movement 1]
- [Thinker/Movement 2]
- [Thinker/Movement 3]

## Policy Perspective on [TOPIC]

### Primary Concerns
- [Concern 1]
- [Concern 2]
- [Concern 3]

### Likely Policy Positions
- **Supportive of:** [Types of policies]
- **Skeptical of:** [Types of policies]
- **Red Lines:** [Will not support]

## Voting Guidance

When evaluating policies:
- Weight [PRIORITY AREA] heavily
- Consider [STAKEHOLDER GROUP] impacts
- Evaluate through lens of [CORE VALUE]
- Assess feasibility within U.S. political and legal system

## Idea Generation Guidelines

Generate ideas that:
- Authentically reflect this perspective
- Are specific and actionable within U.S. law
- Include implementation mechanisms
- Address the 3 core goals
- Consider Constitutional constraints

## Quality Standards
- No strawman versions of opposing views
- Genuine engagement with trade-offs
- Specific policy mechanisms, not vague aspirations
- All proposals must be legally viable in the United States
```

### 3.2 Recommended Analyst Roster

#### Political Spectrum Analysts (7)

- **PA-01:** Economic Populist (pro-worker left)
- **PA-02:** Liberal/Progressive
- **PA-03:** Center-Left
- **PA-04:** Centrist/Pragmatist
- **PA-05:** Center-Right
- **PA-06:** Economic Conservative
- **PA-07:** Nationalist Conservative

#### Domain-Specific Analysts (5)

- **PA-08:** Industry Representative
- **PA-09:** Safety/Risk Advocate
- **PA-10:** Innovation/Growth Advocate
- **PA-11:** Finance/Investment Sector
- **PA-12:** Civil Rights/Equity Advocate

#### Stakeholder Group Analysts (4)

- **PA-13:** Organized Labor
- **PA-14:** Consumer Advocacy
- **PA-15:** Environmental/Sustainability
- **PA-16:** Small Business

### 3.3 Specialist Agents (8) - Voting Members

These agents provide deep expertise AND participate in all voting rounds.

**File:** `agents/specialists/sa[XX]_[name].md`

#### SA-01: Legislative Counsel

- **Role:** Drafts legislation to implement policy ideas
- **Expertise:** U.S. federal and state legislative drafting, bill structure, amendment processes
- **Key Tasks:**
  - Draft federal bill language
  - Draft state bill language (California and Colorado as defaults)
  - Advise on legislative strategy and procedural requirements
- **Voting Lens:** Evaluates policies based on legislative feasibility and drafting clarity

#### SA-02: Legal Counsel

- **Role:** Analyzes detailed legal issues
- **Expertise:** Administrative law, regulatory authority, statutory interpretation, Constitutional law
- **Key Tasks:**
  - Assess legal viability of proposals
  - Identify regulatory pathways vs. legislative requirements
  - Flag potential legal challenges
- **Voting Lens:** Evaluates policies based on legal defensibility and regulatory fit

#### SA-03: Supreme Court Analyst

- **Role:** Analyzes broader Constitutional and SCOTUS implications
- **Expertise:** Supreme Court jurisprudence, Constitutional law, current court composition
- **Key Focus Areas:**
  - Impact of *Loper Bright* (Chevron deference overturned)
  - Independent agency questions (*Humphrey's Executor* and its future)
  - Commerce Clause, spending power, federalism issues
  - Current court's ideological tilt and likely rulings
- **Voting Lens:** Evaluates policies based on likelihood of surviving judicial review

#### SA-04: Fact Checker

- **Role:** Verifies every claim in policy papers
- **Expertise:** Research methodology, source verification, data validation
- **Key Tasks:**
  - Verify all factual claims
  - Check statistics and data citations
  - Flag unsupported assertions
  - Mark items as "VERIFICATION NEEDED" for human review
- **Voting Lens:** Evaluates policies based on evidentiary support

#### SA-05: Citations Agent

- **Role:** Confirms all links and sources are real and valid
- **Expertise:** Academic citation, legal citation (Bluebook), source verification
- **Key Tasks:**
  - Verify all URLs and links are functional
  - Confirm cited sources exist and say what is claimed
  - Format citations consistently
  - Flag "CITATION VERIFICATION NEEDED" for human review when unable to confirm
- **Voting Lens:** Evaluates policies based on quality of supporting sources

#### SA-06: Polling Expert

- **Role:** Analyzes public opinion and shapes messaging
- **Expertise:** Public opinion research, polling methodology, political messaging
- **Key Tasks:**
  - Analyze existing public opinion data on issues
  - Generate polling questions to test policy popularity
  - Recommend policy modifications based on public opinion
  - Work with communications to shape messaging
- **Voting Lens:** Evaluates policies based on public support potential

#### SA-07: Federal Budget Expert

- **Role:** Analyzes costs, revenue, and fiscal implications
- **Expertise:** Federal budget process, CBO scoring, tax policy, appropriations
- **Key Tasks:**
  - Estimate policy costs (10-year window)
  - Identify revenue generation potential
  - Assess budget scoring implications
  - Evaluate fiscal sustainability
- **Voting Lens:** Evaluates policies based on fiscal responsibility and budget feasibility

#### SA-08: Implementation Expert

- **Role:** Analyzes administration and service delivery
- **Expertise:** Public administration, program implementation, bureaucratic processes
- **Key Tasks:**
  - Assess implementation feasibility
  - Identify state capacity requirements
  - Minimize bureaucratic roadblocks
  - Design service delivery mechanisms
  - Evaluate agency capacity to administer
- **Voting Lens:** Evaluates policies based on practical implementability

### 3.4 Supporting Agents (Non-Voting)

**Council Director** (`agents/council_director.md`):
- Coordinates workflow across phases
- Makes final quality decisions
- Resolves conflicts
- Issues certifications
- Does NOT vote

**Writer/Editor** (`agents/writer_editor.md`):
- Creates master documents
- Ensures consistent formatting
- Compiles outputs
- Does NOT vote

---

## 4. Workflow Phases

### 4.1 Phase 1: Idea Generation

**File:** `workflows/phase1_idea_generation.md`

```markdown
# Phase 1: Policy Idea Generation

## Jurisdiction
All ideas must be designed for implementation in the **United States**.

## Steps

### Step 1: Kickoff
- Council Director issues assignments
- Each analyst receives generation instructions
- Remind all agents: policies are for U.S. implementation

### Step 2: Idea Generation
- Each of 24 voting agents generates [10-20] policy ideas
- Each idea includes: ID, Headline, Goal, Cost, Description
- Run agents in parallel for efficiency

### Step 3: Big Ideas Generation (Optional)
- Each agent generates [3] crisis-scale ideas
- One per goal
- High ambition, transformative scale

### Step 4: Compilation
- Writer/Editor compiles master document
- Creates CSV for data analysis
- Updates statistics

### Step 5: QA Review
- Verify all agents represented
- Check formatting consistency
- Validate counts and IDs
- Confirm all ideas are U.S.-focused

### Step 6: Director Certification
- Final quality review
- Formal approval for Phase 2

### Step 7: Human Presentation
- Present outputs to human principal
- Await approval to proceed

## Outputs
- `policy_ideas_master.md` - All ideas organized by agent
- `policy_ideas.csv` - Spreadsheet format
- `big_ideas_master.md` - Crisis-scale proposals
- `big_ideas.csv` - Big ideas spreadsheet
- `qa_report.md` - Quality verification
- `director_certification.md` - Formal approval
```

### 4.2 Phase 2: Policy Debate & Voting

**File:** `workflows/phase2_debate.md`

```markdown
# Phase 2: Policy Debate & Voting

## Voting Agents
All 24 voting agents participate (16 Policy Analysts + 8 Specialists)

## Steps

### Step 1: Merge Voting Pool
- Combine regular and big ideas
- Create unified CSV for voting

### Step 2: Effectiveness Voting
- All 24 agents vote for most effective policies
- Equal weights
- Generate ranking and top list

### Step 3: Compromise Voting
- All 24 agents vote for acceptable compromises
- Equal weights
- Identify bipartisan potential

### Step 4: Partisan Sorting
- Create 4 weighted rankings
- Progressive, Conservative, [Coalition 3], [Coalition 4]
- Show ideological priorities

### Step 5: Compilation
- Create master results document
- Compare across voting rounds
- Identify consensus and divisions

### Step 6: Human Presentation
- Present findings
- Recommend Phase 3 priorities

## Outputs
- `voting_pool.csv` - All ideas for voting
- `effectiveness_votes.md` - Full voting record
- `effectiveness_ranking.md` - Ranked results
- `effectiveness_top[N].md` - Summary of top policies
- `compromise_votes.md` - Compromise voting record
- `compromise_ranking.md` - Compromise rankings
- `compromise_top[N].md` - Best compromise policies
- `partisan_[coalition].md` - 4 partisan rankings
- `partisan_summary.md` - Cross-coalition comparison
- `PHASE2_MASTER_RESULTS.md` - Comprehensive report
```

### 4.3 Phase 3: Policy Refinement & Initial Deeper Proposals

**File:** `workflows/phase3_refinement.md`

```markdown
# Phase 3: Policy Refinement & Initial Deeper Proposals

## Purpose
Conduct deeper research and policy development on human-selected ideas to assess viability before full development.

## Key Principle
**ALL 24 voting agents** analyze each selected policy, providing their best input and analysis **even if they would not personally support the policy**. The goal is comprehensive analysis from all perspectives.

## Steps

### Step 1: Human Selection
- Human principal selects ideas from Phase 2 for deeper analysis
- Typically 5-15 ideas

### Step 2: Deep Research
For each selected idea:
- Research experts who have written on the topic
- Assess feasibility based on evidence
- Identify likely path to development
- Research precedents and similar proposals

### Step 3: All-Agent Analysis
- All 24 voting agents provide analysis
- Each agent contributes perspective even if opposed to policy
- Focus on constructive analysis, not just critique

### Step 4: Paper Development
Create standardized 2-page paper for each idea containing:

1. **Headline** - Clear, descriptive title
2. **Summary** - 2-3 sentence overview
3. **Key Details** - Core mechanisms and features
4. **Recommended Approach** - Specific legislative or regulatory pathway:
   - NEW bill creating LAW that does X, OR
   - NEW regulation under existing authority Y to do Z
5. **Top 3-5 Pros** - Strongest arguments for
6. **Top 3-5 Cons** - Strongest arguments against
7. **Cost & Revenue Estimates** - Projected fiscal impact
8. **Potential Impact** - Expected outcomes if implemented
9. **Political Considerations** - Coalition potential, opposition, timing
10. **Sources & Citations** - Links and endnotes (flag "VERIFICATION NEEDED" where applicable)

### Step 5: Individual Document Creation
- Create separate .md file for each policy idea
- Filename: `phase3/policy_[ID]_initial_paper.md`

### Step 6: Master Document Compilation
Create `PHASE3_MASTER_INITIAL_PAPERS.md` containing:

**Part 1: Executive Summary (2 pages max)**
- Policy goals overview
- Themes across recommendations
- General summary of recommendations

**Part 2: Table of Contents/Index**
- List of all individual policy recommendations
- (Does not count against 2-page executive summary limit)

**Part 3: Individual Policy Papers**
- All individual papers in sequence

### Step 7: Human Review
- Present outputs for assessment
- Await selection for Phase 4

## Outputs
- `phase3/policy_[ID]_initial_paper.md` - Individual 2-page papers
- `phase3/PHASE3_MASTER_INITIAL_PAPERS.md` - Combined master document
- `phase3/phase3_qa_report.md` - Quality verification
```

### 4.4 Phase 4: Full Policy Development

**File:** `workflows/phase4_full_development.md`

```markdown
# Phase 4: Full Policy Development

## Purpose
The most extensive phase. Conduct comprehensive analysis to fully map out viability, impact, legality, and implementation of selected policies.

## Jurisdiction
All analysis is for **United States** federal and state implementation.
Default state models: **California** and **Colorado**

## Writing Style Requirements

Phase 4 papers must be written in **professional policy briefing format**, modeled primarily on publications from the **Center for American Progress** (https://www.americanprogress.org/), with additional reference to other major think tanks (Brookings, AEI, Urban Institute, etc.).

**Reference CAP Publications:**
- "The Needed Executive Actions to Address the Challenges of Artificial Intelligence"
- "How to Regulate Tech: A Technology Policy Framework for Online Services"
- "4 Reasons the Senate's AI Pause Should Be Opposed"
- "The Senate's AI Pause May Take Billions in State Broadband Funds Hostage"
- "The House Is Close To Passing a Moratorium on State Efforts To Regulate AI"
- "Congress Must Take More Steps on Technology Regulation Before It Is Too Late"
- "White House Must Take More Action To Address AI Concerns"
- "Taking Further Agency Action on AI"
- "The Dangers of a Twitter Bankruptcy or Acquisition"

**Style Requirements:**

1. **Write in narrative prose.** Present analysis in flowing paragraphs with strong topic sentences, supporting evidence, and clear conclusions. Each paragraph should typically be 4-8 sentences. Arguments should read as coherent narratives, not outlines or notes.

2. **Integrate evidence into prose.** Statistics, research findings, and case studies should be woven into narrative paragraphs with inline citations. Do not present data as disconnected bullet points. Example: *"According to the World Economic Forum's 2025 Future of Jobs Report, 41% of employers worldwide intend to reduce their workforce due to AI automation, with estimates suggesting 92 million jobs could be eliminated globally by 2030."*

3. **Use authoritative, accessible voice.** Write clearly for policymakers and informed general audiences. Use active voice, direct language, and confident assertions backed by evidence. Include clear calls to action where appropriate.

4. **Reserve bullet points for specific purposes only:**
   - Enumerated lists of discrete items (e.g., program components, specific requirements)
   - Legislative or regulatory text quotations
   - Technical definitions or statutory language
   - Quick-reference summaries when truly needed for clarity

   **Do NOT use bullet points for:** arguments, analysis, explanations, context, background information, or any content that can be expressed in prose.

5. **Use structural elements strategically:**
   - **Bold text** for key phrases and emphasis
   - **Block quotes** for important quotations or statutory language
   - **Tables** for data comparisons, cost breakdowns, and timelines
   - **Clear section headers** that organize the argument logically

6. **Ensure section coherence.** Each section should tell a complete story with clear implications. End sections with explicit "so what" conclusions that tie back to the policy recommendation.

## Steps

### Step 1: Human Selection
- Human principal selects policies from Phase 3 for full development
- Typically 3-7 policies

### Step 2: Comprehensive Research & Analysis
For each selected policy, develop a **30-40 page paper** (legislative appendix does not count toward page limit) containing:

#### Required Sections:

**1. Table of Contents**
- Full listing of all sections

**2. Executive Summary**
- 1-page overview of the proposal and findings

**3. Background Research**
- Full research on the issue
- Key or recommended readings section
- Historical context

**4. Landscape Analysis**
- Similar ideas or proposals
- Competing approaches
- Current policy status

**5. Precedents & Examples**
- Examples from U.S. states
- Examples from other countries
- Lessons learned from prior implementations

**6. Public Opinion**
- Existing polling data on the issue
- Public opinion on similar proposals
- Demographic breakdowns if available

**7. Detailed Proposal**
- Specific policy laid out in detail
- Core mechanisms
- Key provisions

**8. Policy Tool Identification**
- New law (federal or state)
- New regulation under existing authority
- Executive action
- Other mechanisms

**9. Goals & Expected Impact**
- Primary objectives
- Secondary benefits
- Hoped-for outcomes with metrics

**10. Administration & Implementation**
- How the policy would be administered
- Which agencies responsible
- Operational structure

**11. State Capacity Assessment**
- Capacity increases needed
- New personnel or offices required
- Technology or infrastructure needs

**12. Impact Measurement**
- How to measure policy success
- Key performance indicators
- Evaluation timeline

**13. Cost Analysis**
- Monetary costs (10-year projection)
- Other costs (jobs displaced, etc.)
- Budget scoring considerations

**14. Benefits Analysis**
- Monetary benefits (10-year projection)
- Other benefits (jobs created, health outcomes, etc.)
- Distributional analysis

**15. Legal Analysis**
- General legality assessment
- Constitutional issues
- Likely legal challenges on appeal
- Supreme Court outlook (considering current court composition, Loper Bright, etc.)

**16. Implementation Timeline**
- Phased rollout plan
- Key milestones
- Dependencies

**17. Arguments For**
- Strongest supporting arguments
- Key talking points

**18. Arguments Against**
- Strongest counterarguments
- Likely opposition points

**19. Stakeholder Impact Matrix**
- Identify all affected stakeholders
- Quantify impacts (positive/negative) for each group
- Winners and losers analysis
- Distributional effects by income, geography, industry

**20. Alternative Approaches Considered**
- Other policy options evaluated
- Why this approach was selected
- Trade-offs between alternatives
- Hybrid options considered

**21. Equity Assessment**
- Distributional effects across demographics
- Impact on underserved communities
- Racial equity implications
- Geographic equity considerations
- Compliance with EO 13985 framework

**22. Regulatory Impact Analysis (RIA)**
- Cost-benefit analysis (OMB Circular A-4 framework)
- Quantified benefits and costs
- Unquantified benefits and costs
- Comparison to regulatory alternatives
- Small business impact (Regulatory Flexibility Act)

**23. Administrative Procedure Timeline**
- If regulation: Full APA rulemaking timeline
  - ANPRM, NPRM, comment period, final rule
- If legislation: Congressional timeline estimate
- Implementation milestones
- Effective date considerations

**24. Sources & Citations**
- Full bibliography
- All links verified or flagged "VERIFICATION NEEDED"

**APPENDIX A: Draft Federal Legislation**
- Full draft bill language for U.S. Congress
- (Does not count toward 25-30 page limit)

**APPENDIX B: Draft State Legislation - California**
- Full draft bill language for California Legislature
- (Does not count toward 25-30 page limit)

**APPENDIX C: Draft State Legislation - Colorado**
- Full draft bill language for Colorado General Assembly
- (Does not count toward 25-30 page limit)

### Step 3: Quality Assurance Testing
Each paper undergoes comprehensive review:

#### Standard Reviews:
- **Legal Review** (SA-02, SA-03): Verify legality analysis
- **Fact Check** (SA-04): Verify all claims
- **Citation Check** (SA-05): Confirm all sources real and valid
- **Budget Review** (SA-07): Verify cost/benefit estimates
- **Implementation Review** (SA-08): Verify feasibility assessment

#### Enhanced QA Tests:

**Red Team Review**
- Adversarial analysis by opposing-perspective agents
- Identify strongest attacks on the policy
- Stress-test assumptions and claims
- Document vulnerabilities and rebuttals

**Legal Stress Test**
- Identify strongest possible legal challenges
- Draft potential litigation scenarios
- Prepare legal defenses
- Assess litigation risk by venue

**Political Vulnerability Scan**
- Identify potential attack ad angles
- Anticipate opposition talking points
- Prepare counter-messaging
- Flag politically toxic elements

**Implementation War Game**
- Simulate rollout with edge cases
- Identify failure modes
- Test contingency plans
- Document lessons for implementation

Flag items requiring human verification.

### Step 4: Individual Document Creation
- Create separate .md file for each policy
- Filename: `phase4/policy_[ID]_full_development.md`

### Step 5: Master Document Compilation
Create `PHASE4_MASTER_FULL_PAPERS.md` containing:
- Table of Contents
- All individual papers in sequence
- (No executive summary required for master)

### Step 6: Human Review
- Present completed papers
- Await selection for Phase 5

## Outputs
- `phase4/policy_[ID]_full_development.md` - Individual 30-40 page papers
- `phase4/PHASE4_MASTER_FULL_PAPERS.md` - Combined master document
- `phase4/phase4_qa_report.md` - Quality verification including fact-check and citation results
- `phase4/phase4_red_team_report.md` - Red team review findings
- `phase4/phase4_legal_stress_test.md` - Legal challenge analysis
- `phase4/phase4_political_vulnerability.md` - Political vulnerability scan
- `phase4/phase4_implementation_war_game.md` - Implementation simulation results
```

### 4.5 Phase 5: Supporting Rollout Materials

**File:** `workflows/phase5_rollout.md`

```markdown
# Phase 5: Supporting Rollout Materials

## Purpose
Generate think tank-style rollout package for selected policies to support public launch and advocacy.

## Steps

### Step 1: Human Selection
- Human principal selects policies from Phase 4 for rollout materials
- Typically 1-3 policies

### Step 2: Generate Rollout Package
For each selected policy, create:

#### 2.1 Executive Summary Document (5 pages)
- Condensed version of full paper
- Key findings and recommendations
- Designed for policymaker consumption

#### 2.2 Press Release
- Draft announcement for policy release
- Key quotes and findings
- Contact information placeholder

#### 2.3 Op-Eds (3)
- Three distinct opinion pieces
- Different angles/audiences:
  - General audience
  - Industry/stakeholder focus
  - Political/ideological angle
- 750-1000 words each

#### 2.4 Video Scripts (3)
- Three video scripts for different formats:
  - 60-second social media explainer
  - 3-minute overview video
  - 10-minute deep dive
- Include visual/graphic suggestions

#### 2.5 Event Speaker Recommendations
- Suggested speakers for launch event
- Academic experts
- Practitioners
- Political figures
- Stakeholder representatives

#### 2.6 Rollout Plan
- Launch timeline
- Media strategy
- Stakeholder engagement plan
- Hill outreach (if applicable)

#### 2.7 AI Generation Instructions - PowerPoint
- Detailed prompt for Gemini/other AI to generate presentation slides
- Specify key slides, data visualizations, talking points

#### 2.8 AI Generation Instructions - Graphics
- Detailed prompt for Gemini/other AI to generate:
  - Infographics
  - Social media graphics
  - Data visualizations
- Specify dimensions, style, key data points

#### 2.9 Polling Questions
- Questions to test policy efficacy and popularity
- A/B message testing questions
- Demographic cross-tabs to request
- Suggested polling methodology

#### 2.10 Fact Sheet (1-pager)
- One-page summary for quick reference
- Key facts, stats, and talking points
- Designed for media and staff use
- Print-ready format

#### 2.11 FAQ Document
- Frequently asked questions and answers
- Address common objections
- Technical clarifications
- Political/messaging FAQs

#### 2.12 Social Media Toolkit
- Pre-written tweets/posts for various platforms
- Shareable graphics specifications
- Hashtag recommendations
- Influencer engagement suggestions

#### 2.13 Coalition Letter Template
- Pre-drafted support letter for organizations
- Customizable by sector/stakeholder type
- Sign-on instructions
- Target recipient list

#### 2.14 Hill Leave-Behind
- One-page document for Congressional meetings
- Key asks and policy summary
- District/state-specific impacts (customizable)
- Contact information and follow-up asks

#### 2.15 Opposition Research Brief
- Anticipated opposition arguments
- Counter-arguments and rebuttals
- Opposition stakeholder mapping
- Attack ad inoculation strategies

### Step 3: Document Creation
Create files:
- `phase5/policy_[ID]_executive_summary.md`
- `phase5/policy_[ID]_press_release.md`
- `phase5/policy_[ID]_opeds.md`
- `phase5/policy_[ID]_video_scripts.md`
- `phase5/policy_[ID]_speakers.md`
- `phase5/policy_[ID]_rollout_plan.md`
- `phase5/policy_[ID]_ai_powerpoint_prompt.md`
- `phase5/policy_[ID]_ai_graphics_prompt.md`
- `phase5/policy_[ID]_polling_questions.md`
- `phase5/policy_[ID]_fact_sheet.md`
- `phase5/policy_[ID]_faq.md`
- `phase5/policy_[ID]_social_media_toolkit.md`
- `phase5/policy_[ID]_coalition_letter.md`
- `phase5/policy_[ID]_hill_leave_behind.md`
- `phase5/policy_[ID]_opposition_research.md`

### Step 4: Master Compilation
Create `PHASE5_MASTER_ROLLOUT_MATERIALS.md` containing all materials organized by policy.

### Step 5: Human Review
- Present rollout package
- Gather feedback for refinement

## Outputs
- Individual rollout material files per policy
- `phase5/PHASE5_MASTER_ROLLOUT_MATERIALS.md` - Combined master document
```

### 4.6 Process Recommendations

These cross-phase process guidelines ensure quality and flexibility throughout the policy development lifecycle.

#### Iteration Loops
- **Phase 4 → Phase 3 Return:** If Phase 4 analysis reveals fatal flaws (legal, fiscal, implementation), policy may return to Phase 3 for redesign
- **Phase 5 → Phase 4 Return:** If rollout preparation reveals messaging/political issues, may return for policy refinement
- **Document iteration decisions** in DECISION_LOG.md with rationale

#### Human Checkpoints
- **Mandatory approval required** at end of each phase before proceeding
- **Present options clearly** when human input needed
- **Document all human decisions** with timestamp and rationale
- **No phase advancement** without explicit human approval

#### Version Control on Policy Papers
- **Track all drafts:** `policy_[ID]_v1.md`, `policy_[ID]_v2.md`, etc.
- **Changelog required:** Document what changed between versions
- **Preserve superseded versions:** Do not delete prior drafts
- **Final version clearly marked:** `policy_[ID]_FINAL.md`

#### Dissent Documentation
- **Record minority opinions:** When agents disagree with majority, document their view
- **Dissent format:** Agent ID, position, reasoning, suggested alternative
- **Include in outputs:** Add "Dissenting Views" section to master documents
- **No suppression:** All substantive disagreements must be preserved
- **Value dissent:** Minority views often identify overlooked risks or alternatives

#### Process Documentation Templates

**Iteration Decision Record:**
```markdown
## Iteration Decision: [Policy ID]

**Date:** [DATE]
**Decision:** Return to Phase [X] / Proceed to Phase [Y]
**Reason:** [Brief explanation]
**Key Issues Identified:**
1. [Issue 1]
2. [Issue 2]

**Required Revisions:**
- [Revision 1]
- [Revision 2]

**Approved by:** Human Principal
```

**Dissent Record:**
```markdown
## Dissenting View: [Policy ID]

**Agent:** [Agent ID and Name]
**Position:** [Support/Oppose/Modify]
**Reasoning:**
[Agent's explanation]

**Suggested Alternative:**
[If applicable]

**Response from Majority:**
[How majority addressed this concern, if at all]
```

---

## 5. Dashboard Setup

### 5.1 Main Dashboard

**File:** `DASHBOARD.md`

```markdown
# [COUNCIL NAME] Dashboard

> **Last Updated:** [DATE]
> **Session Status:** [STATUS]
> **Jurisdiction:** United States

---

## Current Status

\`\`\`
╔═══════════════════════════════════════════════════════════════════════════╗
║                        [COUNCIL NAME]                                      ║
║                         STATUS DASHBOARD                                   ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║   PHASE:    [X] - [PHASE NAME]                                             ║
║   STEP:     [X]/[X] - [STEP NAME]                                          ║
║   PROGRESS: [████████████░░░░░░░░] XX%                                     ║
║                                                                            ║
║   STATUS:   [STATUS MESSAGE]                                               ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
\`\`\`

---

## Phase Overview

| Phase | Name | Status | Progress |
|-------|------|--------|----------|
| **1** | Idea Generation | [STATUS] | XX% |
| **2** | Policy Debate & Voting | [STATUS] | XX% |
| **3** | Policy Refinement & Initial Proposals | [STATUS] | XX% |
| **4** | Full Policy Development | [STATUS] | XX% |
| **5** | Supporting Rollout Materials | [STATUS] | XX% |

---

## Voting Agents (24)

### Policy Analysts (16)
| ID | Name | Perspective |
|----|------|-------------|
| PA-01 | Economic Populist | Pro-worker left |
| PA-02 | Liberal/Progressive | Progressive |
| PA-03 | Center-Left | Center-left |
| PA-04 | Centrist/Pragmatist | Centrist |
| PA-05 | Center-Right | Center-right |
| PA-06 | Economic Conservative | Conservative |
| PA-07 | Nationalist Conservative | Right |
| PA-08 | Industry Representative | Industry |
| PA-09 | Safety/Risk Advocate | Safety |
| PA-10 | Innovation/Growth Advocate | Innovation |
| PA-11 | Finance/Investment Sector | Finance |
| PA-12 | Civil Rights/Equity Advocate | Civil rights |
| PA-13 | Organized Labor | Labor |
| PA-14 | Consumer Advocacy | Consumer |
| PA-15 | Environmental/Sustainability | Environment |
| PA-16 | Small Business | Small business |

### Specialist Agents (8)
| ID | Name | Expertise |
|----|------|-----------|
| SA-01 | Legislative Counsel | Bill drafting |
| SA-02 | Legal Counsel | Legal analysis |
| SA-03 | Supreme Court Analyst | SCOTUS/Constitutional |
| SA-04 | Fact Checker | Verification |
| SA-05 | Citations Agent | Source validation |
| SA-06 | Polling Expert | Public opinion |
| SA-07 | Federal Budget Expert | Fiscal analysis |
| SA-08 | Implementation Expert | Administration |

---

## Documents

### Phase 1 Outputs
| Document | Description | Link |
|----------|-------------|------|
| **[Doc 1]** | [Description] | [View](path) |
...

### Phase 2 Outputs
| Document | Description | Link |
|----------|-------------|------|
...

### Phase 3 Outputs
| Document | Description | Link |
|----------|-------------|------|
...

### Phase 4 Outputs
| Document | Description | Link |
|----------|-------------|------|
...

### Phase 5 Outputs
| Document | Description | Link |
|----------|-------------|------|
...

---

## Quick Links

### Agent Definitions
- [Council Director](agents/council_director.md)
- [Policy Analysts](agents/analysts/)
- [Specialist Agents](agents/specialists/)
- [All Agents](agents/)

### Workflows
- [Phase 1](workflows/phase1_idea_generation.md)
- [Phase 2](workflows/phase2_debate.md)
- [Phase 3](workflows/phase3_refinement.md)
- [Phase 4](workflows/phase4_full_development.md)
- [Phase 5](workflows/phase5_rollout.md)

### Configuration
- [Core Goals](config/goals.md)
- [Voting Rules](config/voting_rules.md)

---

## Commands Reference

| Command | Description |
|---------|-------------|
| `/dashboard` | Show this dashboard |
| `/status` | Quick one-line status |
| `/pending` | Items awaiting decision |
| `/documents` | List all documents |
| `/decide` | Walk through pending decisions |
```

### 5.2 State Tracking

**File:** `STATE.json`

```json
{
  "council_name": "[COUNCIL NAME]",
  "jurisdiction": "United States",
  "created": "[DATE]",
  "last_updated": "[DATE]",

  "current_phase": {
    "number": 1,
    "name": "Policy Idea Generation",
    "status": "in_progress",
    "started": "[DATE]"
  },

  "current_step": {
    "number": 1,
    "name": "Kickoff",
    "status": "in_progress"
  },

  "progress": {
    "phase1_percent": 0,
    "phase2_percent": 0,
    "phase3_percent": 0,
    "phase4_percent": 0,
    "phase5_percent": 0,
    "overall_percent": 0
  },

  "statistics": {
    "total_ideas_generated": 0,
    "total_votes_cast": 0,
    "documents_created": 0,
    "policies_in_phase3": 0,
    "policies_in_phase4": 0,
    "policies_in_phase5": 0
  },

  "agents": {
    "policy_analysts": 16,
    "specialist_agents": 8,
    "total_voting": 24,
    "support_agents": 2
  },

  "pending_human_decisions": [],

  "activity_log": []
}
```

---

## 6. Slash Commands

### 6.1 Dashboard Command

**File:** `.claude/commands/dashboard.md`

```markdown
Display the full [COUNCIL NAME] dashboard showing:

1. Current phase and step
2. Progress indicators
3. Recent activity
4. Pending decisions
5. Links to key documents
6. Agent roster (24 voting + 2 support)

Read and display the contents of DASHBOARD.md, formatted for terminal display.
```

### 6.2 Status Command

**File:** `.claude/commands/status.md`

```markdown
Provide a quick one-line status of the [COUNCIL NAME].

Read STATE.json and output a single line like:
"Phase [X] Step [Y]: [Status] - [Next action needed]"
```

### 6.3 Pending Command

**File:** `.claude/commands/pending.md`

```markdown
List all items awaiting human decision.

Read STATE.json and human_review/ folder.
Display pending items with brief descriptions and recommended actions.
```

### 6.4 Documents Command

**File:** `.claude/commands/documents.md`

```markdown
List all documents created by the [COUNCIL NAME].

Scan outputs/ folder (including phase1-5 subfolders) and display:
- Document name
- Phase
- Creation date
- Brief description
```

### 6.5 Decide Command

**File:** `.claude/commands/decide.md`

```markdown
Walk through pending decisions step by step.

For each pending decision:
1. Explain what needs to be decided
2. Present options
3. Show relevant context
4. Ask for user input
5. Record decision in DECISION_LOG.md
```

---

## 7. Output Templates

### 7.1 Policy Idea Template (Phase 1)

```markdown
### [ID]: [Headline]
**Primary Goal:** [Goal]
**Cost Estimate:** [Low/Medium/High/Very High]

[2-3 sentence description of the policy, including specific mechanisms and expected outcomes. Must be implementable within U.S. legal framework.]
```

### 7.2 Big Idea Template (Phase 1)

```markdown
### [ID]: [Headline]
**Primary Goal:** [Goal]
**Cost Estimate:** [Very High - $XXX over X years]

[3-4 sentence description of the crisis-scale policy proposal, explaining the transformative mechanism, scale of investment, and expected impact. These should be ambitious proposals that would seem impossible today but could become feasible in a crisis moment. Must be implementable within U.S. legal framework.]
```

### 7.3 Initial Paper Template (Phase 3)

```markdown
# [ID]: [Headline]

## Summary
[2-3 sentence overview]

## Key Details
[Core mechanisms and features - 3-5 bullet points]

## Recommended Legislative/Regulatory Approach
[Specific pathway: NEW bill creating LAW that does X, OR NEW regulation under existing authority Y]

## Pros
1. [Pro 1]
2. [Pro 2]
3. [Pro 3]
4. [Pro 4 - optional]
5. [Pro 5 - optional]

## Cons
1. [Con 1]
2. [Con 2]
3. [Con 3]
4. [Con 4 - optional]
5. [Con 5 - optional]

## Cost & Revenue Estimates
- **Estimated Cost:** $X over Y years
- **Potential Revenue:** $X over Y years
- **Net Fiscal Impact:** $X

## Potential Impact
[Expected outcomes if implemented]

## Political Considerations
[Coalition potential, opposition, timing factors]

## Sources & Citations
1. [Source 1] - [VERIFIED/VERIFICATION NEEDED]
2. [Source 2] - [VERIFIED/VERIFICATION NEEDED]
...
```

### 7.4 Full Development Paper Template (Phase 4)

See Section 4.4 for complete 25-30 page template with all required sections.

### 7.5 Voting Record Template

```markdown
## [Agent Name] (PA-XX or SA-XX)
**Perspective:** [Brief description]

### Top [N] Selections:
1. **[ID]**: [Headline] - [Brief rationale]
2. **[ID]**: [Headline] - [Brief rationale]
...
```

### 7.6 CSV Formats

**Policy Ideas:**
```
ID,Headline,Description,Agent,Agent_Type,Perspective,Goal_1,Goal_2,Goal_3,Cost_Estimate
```

**Big Ideas:**
```
ID,Headline,Agent,Agent_Type,Perspective,Goal,Cost_Estimate,Description
```

**Voting Results:**
```
ID,Headline,Effectiveness_Votes,Compromise_Votes,Progressive_Score,Conservative_Score
```

### 7.7 Document Style Guide

All policy papers must follow these formatting standards for consistency and usability.

#### Citation Format

Use **both** inline hyperlinks AND numbered footnote citations:

**In-text example:**
```markdown
[Goldman Sachs economists have estimated](https://www.goldmansachs.com/insights/pages/generative-ai-could-raise-global-gdp-by-7-percent.html) that generative AI alone could raise global GDP by seven percent over a ten-year period, representing approximately seven trillion dollars in additional economic output.[^1]
```

**Sources & Citations section:**
```markdown
[^1]: Goldman Sachs. "Generative AI Could Raise Global GDP by 7%." April 2023. [https://www.goldmansachs.com/insights/pages/generative-ai-could-raise-global-gdp-by-7-percent.html](https://www.goldmansachs.com/insights/pages/generative-ai-could-raise-global-gdp-by-7-percent.html)
```

**Requirements:**
- Hyperlink the relevant claim text directly to the source
- Include a numerical footnote citation `[^N]`
- In Sources section, provide: Author/Org. "Title." Date. Full URL as clickable hyperlink
- Full URL must be visible in the citation text AND hyperlinked

#### Complex Structure Formatting

Convert dense paragraphs describing governance, processes, or multi-part structures into **bullet lists**:

**❌ Avoid (dense paragraph):**
```markdown
The Council would be governed by a fifteen-member Board of Directors with balanced representation across key stakeholder groups. Five seats would be reserved for representatives of the public interest: two appointed by the President with Senate confirmation, one appointed by the Speaker of the House...
```

**✅ Preferred (bullet list):**
```markdown
The Council would be governed by a fifteen-member Board of Directors:

**Public Interest Representatives (5 seats):**
- 2 appointed by the President with Senate confirmation
- 1 appointed by the Speaker of the House
- 1 appointed by the Senate Majority Leader
- 1 appointed jointly by minority leaders of both chambers

**Constituency Representatives (5 seats):**
- Organized Labor (appointed by AFL-CIO)
- Industry (appointed by technology/business association consortium)
- Academia (appointed by Association of American Universities)
- Small Business (appointed by Small Business Administration)
- Civil Society (appointed by public interest technology consortium)

**Ex Officio Members (5 seats):**
- Secretary of Commerce
- Secretary of Labor
- Director, National Science Foundation
- Director, Office of Science and Technology Policy
- Administrator, Small Business Administration
```

#### General Formatting Rules

1. **Use bullet lists** for any enumeration of 3+ items
2. **Use tables** for comparative information
3. **Use headers** to break up sections longer than 3 paragraphs
4. **Bold key terms** on first use or for emphasis
5. **All URLs** must be both visible and hyperlinked

---

## 8. Execution Instructions

### 8.1 Initial Setup

```
1. Create folder structure:
   /[council-name]/
   ├── agents/
   │   ├── analysts/
   │   └── specialists/
   ├── config/
   ├── workflows/
   ├── templates/
   ├── outputs/
   │   ├── phase1/
   │   ├── phase2/
   │   ├── phase3/
   │   ├── phase4/
   │   └── phase5/
   ├── human_review/
   └── .claude/
       └── commands/

2. Create configuration files:
   - config/goals.md (include jurisdiction statement)
   - config/voting_rules.md (24 voting agents)

3. Create agent definitions:
   - agents/council_director.md
   - agents/writer_editor.md
   - agents/analysts/pa01_[name].md through pa16_[name].md
   - agents/specialists/sa01_legislative_counsel.md
   - agents/specialists/sa02_legal_counsel.md
   - agents/specialists/sa03_scotus_analyst.md
   - agents/specialists/sa04_fact_checker.md
   - agents/specialists/sa05_citations_agent.md
   - agents/specialists/sa06_polling_expert.md
   - agents/specialists/sa07_budget_expert.md
   - agents/specialists/sa08_implementation_expert.md

4. Create workflow documents:
   - workflows/phase1_idea_generation.md
   - workflows/phase2_debate.md
   - workflows/phase3_refinement.md
   - workflows/phase4_full_development.md
   - workflows/phase5_rollout.md

5. Create dashboard and state:
   - DASHBOARD.md (updated for 5 phases)
   - STATE.json (updated for 24 agents)
   - DECISION_LOG.md
   - human_review/README.md

6. Create slash commands:
   - .claude/commands/dashboard.md
   - .claude/commands/status.md
   - .claude/commands/pending.md
   - .claude/commands/documents.md
   - .claude/commands/decide.md
```

### 8.2 Running Phase 1

```
1. Spawn all 24 voting agents in parallel to generate ideas:
   - Use Task tool with subagent_type="general-purpose"
   - Each agent generates [10-20] ideas + [3] big ideas
   - Ideas written to outputs/phase1/[agent]_ideas.md
   - Remind agents: all policies for United States

2. Compile master documents:
   - Combine all ideas into policy_ideas_master.md
   - Create policy_ideas.csv
   - Compile big_ideas_master.md and big_ideas.csv

3. Run QA review:
   - Verify counts, formatting, completeness
   - Confirm all ideas are U.S.-focused
   - Write qa_report.md

4. Director certification:
   - Final quality check
   - Write director_certification.md

5. Update dashboard and state

6. Present to human for approval
```

### 8.3 Running Phase 2

```
1. Create voting pool:
   - Merge all ideas into voting_pool.csv
   - Write voting_pool_summary.md

2. Effectiveness voting:
   - All 24 voting agents vote for top [20-25] effective policies
   - Equal weights
   - Create effectiveness_votes.md, effectiveness_ranking.md, effectiveness_top[N].md

3. Compromise voting:
   - All 24 voting agents vote for compromise policies
   - Equal weights
   - Create compromise_votes.md, compromise_ranking.md, compromise_top[N].md

4. Partisan sorting:
   - Create 4 weighted rankings
   - Write partisan_[coalition].md for each
   - Write partisan_summary.md comparing all 4

5. Compile master results:
   - Create PHASE2_MASTER_RESULTS.md
   - Update dashboard

6. Present to human for Phase 3 decisions
```

### 8.4 Running Phase 3

```
1. Human selects ideas for deeper analysis (typically 5-15)

2. For each selected idea:
   - Conduct deep research
   - All 24 voting agents provide analysis (even if opposed)
   - Create 2-page standardized paper
   - Save as phase3/policy_[ID]_initial_paper.md

3. Compile master document:
   - Create PHASE3_MASTER_INITIAL_PAPERS.md
   - 2-page executive summary
   - Table of contents
   - All individual papers

4. QA review:
   - Verify formatting consistency
   - Check citations (flag VERIFICATION NEEDED)

5. Present to human for Phase 4 selection
```

### 8.5 Running Phase 4

```
1. Human selects policies for full development (typically 3-7)

2. For each selected policy:
   - Comprehensive research and analysis
   - Create 25-30 page paper with all required sections
   - Draft federal legislation (Congress)
   - Draft state legislation (California)
   - Draft state legislation (Colorado)
   - Save as phase4/policy_[ID]_full_development.md

3. Quality assurance:
   - SA-02/SA-03: Legal review
   - SA-04: Fact check all claims
   - SA-05: Verify all citations
   - SA-07: Review budget estimates
   - SA-08: Review implementation feasibility
   - Flag items for human verification

4. Compile master document:
   - Create PHASE4_MASTER_FULL_PAPERS.md
   - Table of contents
   - All papers in sequence

5. Present to human for Phase 5 selection
```

### 8.6 Running Phase 5

```
1. Human selects policies for rollout materials (typically 1-3)

2. For each selected policy, generate:
   - 5-page executive summary
   - Press release
   - 3 op-eds
   - 3 video scripts
   - Speaker recommendations
   - Rollout plan
   - AI PowerPoint generation prompt
   - AI graphics generation prompt
   - Polling questions

3. Save individual files to phase5/

4. Compile master document:
   - Create PHASE5_MASTER_ROLLOUT_MATERIALS.md

5. Present to human for review and refinement
```

---

## 9. Customization Guide

### 9.1 Adjusting Number of Analysts

**Fewer analysts (12-16):** Good for focused topics with less ideological diversity
**More analysts (20-24):** Better for broad policy areas with many stakeholders
**Note:** Always include the 8 specialist agents for quality assurance

### 9.2 Adjusting Ideas per Agent

**Fewer ideas (5-10):** Faster execution, focused output
**More ideas (15-25):** More comprehensive, but more to process

### 9.3 Customizing Voting Weights

Adjust partisan sorting weights based on:
- Relevance of ideology to your topic
- Stakeholder importance
- Desired coalition structure

### 9.4 Customizing State Legislation

Default states are **California** and **Colorado**. To change:
- Update Phase 4 workflow
- Modify legislative counsel instructions
- Consider states with different political compositions for broader applicability

### 9.5 Adding Specialized Analysts

For domain-specific councils, consider adding:
- Technical experts
- Regional representatives
- Demographic representatives
- Historical perspective analysts

### 9.6 Modifying Goals

The 3-goal framework works well for most topics. Choose goals that:
- Are distinct but related
- Create genuine trade-offs
- Can be measured or evaluated
- Cover the key dimensions of success

### 9.7 Citation Verification Workflow

The Citations Agent (SA-05) will:
1. Attempt to verify all sources
2. Mark verified sources as [VERIFIED]
3. Mark unverifiable sources as [VERIFICATION NEEDED]
4. Human reviews all [VERIFICATION NEEDED] items before publication

---

## Example: Creating a Healthcare Policy Council

```
Create a Policy Council on Healthcare Reform using the template at POLICY_COUNCIL_TEMPLATE.md.

The council's mission is: Develop policy recommendations for reforming the US healthcare system.

The core goals are:
1. Universal Access - Everyone can obtain necessary healthcare
2. Cost Control - Total healthcare spending is sustainable
3. Quality Improvement - Health outcomes improve across all populations

Please set up the full council with all 24 voting agents, 5-phase workflow, dashboard, and slash commands.
```

---

## Example: Creating an Education Policy Council

```
Create a Policy Council on Education Reform using the template at POLICY_COUNCIL_TEMPLATE.md.

The council's mission is: Develop policy recommendations for improving K-12 education outcomes in the United States.

The core goals are:
1. Academic Achievement - Students meet or exceed learning standards
2. Equity - Outcomes are not predicted by demographics
3. Affordability - Education is accessible without financial burden

Please set up the full council with all 24 voting agents, 5-phase workflow, dashboard, and slash commands.
```

---

## Example: Creating a Climate Policy Council

```
Create a Policy Council on Climate Action using the template at POLICY_COUNCIL_TEMPLATE.md.

The council's mission is: Develop policy recommendations for addressing climate change while maintaining economic prosperity in the United States.

The core goals are:
1. Emissions Reduction - Significant decrease in greenhouse gas emissions
2. Economic Resilience - Economy thrives during and after transition
3. Just Transition - Costs and benefits distributed fairly

Please set up the full council with all 24 voting agents, 5-phase workflow, dashboard, and slash commands.
```

---

*Template created from AI Policy Council for Economic Prosperity*
*Version 2.0 - December 2024*
*Jurisdiction: United States of America*
