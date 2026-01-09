# Phase 2: Policy Debate - Workflow

## Overview

Phase 2 brings all 16 policy analysts together to debate the policy ideas generated in Phase 1. Through structured voting rounds, the council identifies the most effective policies, potential bipartisan compromises, and policies aligned with specific political coalitions.

**Note:** This is a shared workflow used by all projects. File paths refer to the current project's folder. Voting rules are in `shared/config/voting_rules.md`.

---

## Phase Objectives

1. Debate all 120 policy ideas from Phase 1
2. Identify Top 20 most effective policies (regardless of ideology)
3. Identify Top 10 bipartisan compromise policies
4. Identify Top 10 Progressive/Liberal policies
5. Identify Top 10 MAGA/Conservative policies
6. Document all votes, reasoning, and key debates

---

## Voting Rules Summary

| Vote Type | Weight Scheme | Output |
|-----------|---------------|--------|
| Effectiveness | Equal (all 1.0) | Top 20 policies |
| Compromise | Equal (all 1.0) | Top 10 bipartisan |
| Progressive Sort | Weighted (see config) | Top 10 progressive |
| Conservative Sort | Weighted (see config) | Top 10 conservative |

Reference `shared/config/voting_rules.md` for complete weighting details.

---

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                         PHASE 2 WORKFLOW                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ROUND 1: EFFECTIVENESS VOTING                                       │
│  ┌─────────────────────────────────────────────────────────────────┐ │
│  │ All 16 analysts vote on each policy                             │ │
│  │ Question: "Will this effectively achieve the stated goals?"     │ │
│  │ Weight: Equal (1.0 each)                                        │ │
│  │ Output: Top effective policies                                  │ │
│  └───────────────────────────┬─────────────────────────────────────┘ │
│                              │                                       │
│                              ▼                                       │
│  ROUND 2: COMPROMISE VOTING                                          │
│  ┌─────────────────────────────────────────────────────────────────┐ │
│  │ All 16 analysts vote on each policy                             │ │
│  │ Question: "Could you support this as a compromise?"             │ │
│  │ Weight: Equal (1.0 each)                                        │ │
│  │ Focus: LARGE policy ideas, not small non-controversial items    │ │
│  │ Output: Top 10 bipartisan-viable policies                       │ │
│  └───────────────────────────┬─────────────────────────────────────┘ │
│                              │                                       │
│                              ▼                                       │
│  ROUND 3: PARTISAN SORTING                                           │
│  ┌─────────────────────────────────────────────────────────────────┐ │
│  │ 3A: Progressive/Liberal Sort                                    │ │
│  │     Weight: PA-02, PA-12 (2.5x), PA-01, PA-03 (2.0x), etc.     │ │
│  │     Output: Top 10 progressive policies                         │ │
│  │                                                                  │ │
│  │ 3B: MAGA/Conservative Sort                                      │ │
│  │     Weight: PA-06, PA-07 (2.5x), PA-05, PA-11 (2.0x), etc.     │ │
│  │     Output: Top 10 conservative policies                        │ │
│  └───────────────────────────┬─────────────────────────────────────┘ │
│                              │                                       │
│                              ▼                                       │
│  COMPILATION AND DOCUMENTATION                                       │
│  ┌─────────────────────────────────────────────────────────────────┐ │
│  │ Writer/Editor compiles all vote records                         │ │
│  │ QA verifies accuracy                                            │ │
│  │ Council Director approves                                       │ │
│  └───────────────────────────┬─────────────────────────────────────┘ │
│                              │                                       │
│                              ▼                                       │
│  HUMAN PRINCIPAL PRESENTATION                                        │
│  ┌─────────────────────────────────────────────────────────────────┐ │
│  │ Present sorted lists with vote analysis                         │ │
│  │ Provide debate summary and key insights                         │ │
│  └─────────────────────────────────────────────────────────────────┘ │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Detailed Voting Procedures

### Round 1: Effectiveness Vote

**Purpose:** Identify policies most likely to achieve the three goals, regardless of ideological preference.

**Pre-Voting Preparation:**
> **ALL ANALYSTS:** Before voting begins, review your Phase 1 memory file:
> - Recall the ideas YOU proposed in Phase 1
> - Review your research findings and rationale
> - Note your ideological themes and core positions
> - Prepare to maintain consistency with Phase 1 work

**Instructions to Analysts:**
> "Vote based on what you believe will be MOST EFFECTIVE at achieving the policy goals (Broad Growth, Mobility, Affordability), NOT based on what your ideological perspective would prefer. Be objective."

**Process:**
1. Council Director presents each policy with brief summary
2. Original proposing analyst may provide 2-3 sentence context (referencing Phase 1 rationale)
3. Open discussion (time-boxed to 5 minutes per policy)
4. Each analyst votes: YES / NO / ABSTAIN
5. Each analyst provides 1-2 sentence reasoning (may reference Phase 1 work)
6. **Record in memory:** Add vote to `phases.phase2.votes_cast.effectiveness`
7. Votes tallied with equal weight (12 points max)

**Ranking:**
- Rank all 120 policies by total YES votes
- Select Top 20
- Ensure minimum 7 policies per goal in Top 20
- If goal minimum not met, add highest-scoring unselected policies for that goal

**Output Format:**
```markdown
## TOP 20 MOST EFFECTIVE POLICIES
### Voting Scheme: EQUAL WEIGHT (all analysts = 1.0)

| Rank | Policy | Score | Goal(s) | Proposing Analyst |
|------|--------|-------|---------|-------------------|
| 1 | [Name] | 11/12 | Growth, Mobility | PA-03 |
| 2 | [Name] | 10/12 | Affordability | PA-07 |
...

### Goal Distribution
- Broad Growth: X policies
- Economic Mobility: X policies
- Affordability: X policies

### Notable Patterns
- [Pattern observed in voting]
```

---

### Round 2: Compromise Vote

**Purpose:** Identify policies that could achieve cross-ideological support.

**Special Focus:**
> This vote is for identifying LARGER, more substantial policy ideas that could bridge ideological divides. Small, non-controversial policies are NOT the target - focus on meaningful policies where real compromise is possible.

**Memory Guidance:**
> Review your Phase 1 core positions and red lines. Compromise means accepting policies that aren't perfect from your perspective, but should NOT violate your fundamental principles. Note in memory when you compromise and WHY.

**Instructions to Analysts:**
> "Vote for policies you could genuinely support or accept as a reasonable compromise, even if they aren't your first choice. Focus on larger policies where agreement represents real compromise."

**Process:**
1. Council Director presents each policy
2. Discussion focuses on potential modifications for broader appeal
3. Each analyst votes: YES (could support) / NO (cannot support) / ABSTAIN
4. Reasoning emphasizes what makes compromise possible/impossible
5. **Record in memory:** Add vote to `phases.phase2.votes_cast.compromise`
6. **If compromising:** Note in `cross_phase_context.compromises_made`
7. **If dissenting:** Note in `cross_phase_context.dissents_recorded`
8. Votes tallied with equal weight

**Ranking:**
- Rank policies by total YES votes
- Filter to policies with > 6/12 support (majority)
- Focus on substantive policies
- Select Top 10

**Output Format:**
```markdown
## TOP 10 BIPARTISAN COMPROMISE POLICIES
### Voting Scheme: EQUAL WEIGHT (all analysts = 1.0)
### Unanimity: NOT REQUIRED

| Rank | Policy | Yes | No | Abstain | Coalition |
|------|--------|-----|----|---------|-----------|
| 1 | [Name] | 10 | 1 | 1 | [Who voted yes] |
...

### Coalition Analysis
Each policy shows which ideological perspectives supported it:
- Policy 1: Supported by Left, Center, and moderate Right
- Policy 2: Supported by Populists and Civil Rights across spectrum
...
```

---

### Round 3A: Progressive/Liberal Sort

**Purpose:** Identify policies that best represent progressive/liberal values.

**Weighting Scheme:**
| Analyst | Weight |
|---------|--------|
| PA-02 (Liberal) | 2.5 |
| PA-12 (Civil Rights) | 2.5 |
| PA-01 (Economic Populist) | 2.0 |
| PA-03 (Center-Left) | 2.0 |
| PA-09 (AI Safety) | 1.5 |
| PA-04 (Centrist) | 1.0 |
| PA-08 (AI Company) | 1.0 |
| All others | 0.5 |

**Max Score:** 15.0 points

**Instructions to Analysts:**
> "Vote based on how well this policy represents strong progressive/liberal values and priorities."

**Output Format:**
```markdown
## TOP 10 PROGRESSIVE/LIBERAL POLICIES
### Voting Scheme: WEIGHTED BY PROGRESSIVE ALIGNMENT

| Rank | Policy | Weighted Score | % of Max | Key Support |
|------|--------|----------------|----------|-------------|
| 1 | [Name] | 13.5/15.0 | 90% | PA-02, PA-12, PA-01 |
...

### Weighting Applied
[Table showing weight scheme]

### Progressive Values Represented
- [Theme 1]
- [Theme 2]
```

---

### Round 3B: MAGA/Conservative Sort

**Purpose:** Identify policies that best represent MAGA/conservative values.

**Weighting Scheme:**
| Analyst | Weight |
|---------|--------|
| PA-06 (Economic Conservative) | 2.5 |
| PA-07 (MAGA) | 2.5 |
| PA-05 (Center-Right) | 2.0 |
| PA-11 (Finance) | 2.0 |
| PA-01 (Economic Populist) | 1.5 |
| PA-08 (AI Company) | 1.5 |
| PA-10 (AI Accelerationist) | 1.5 |
| PA-04 (Centrist) | 1.0 |
| All others | 0.5 |

**Max Score:** 16.5 points

**Instructions to Analysts:**
> "Vote based on how well this policy represents strong MAGA/conservative values and priorities."

**Output Format:**
```markdown
## TOP 10 MAGA/CONSERVATIVE POLICIES
### Voting Scheme: WEIGHTED BY CONSERVATIVE ALIGNMENT

| Rank | Policy | Weighted Score | % of Max | Key Support |
|------|--------|----------------|----------|-------------|
| 1 | [Name] | 14.0/16.5 | 85% | PA-07, PA-06, PA-11 |
...

### Weighting Applied
[Table showing weight scheme]

### Conservative Values Represented
- [Theme 1]
- [Theme 2]
```

---

## Debate Documentation

### Analyst Memory Recording During Debates

**Each analyst should document:**
- Arguments they make: Add to `phases.phase2.arguments_made`
- Amendments they propose: Add to `phases.phase2.amendments_proposed`
- Alliances they form: Note in `phases.phase2.key_alliances`
- Conflicts that emerge: Note in `phases.phase2.key_conflicts`

**Reference Phase 1 work:**
- "As I proposed in Phase 1..." (cite your idea_id)
- "My Phase 1 research showed..." (cite research_conducted)
- "Consistent with my ideological theme of..." (cite ideological_themes)

### Individual Policy Debate Record
```markdown
## DEBATE RECORD: [Policy Name]

**Policy ID:** [ID]
**Proposing Analyst:** [ID]
**Goals Addressed:** [Goals]

### Summary
[1-2 sentence policy summary]

### Phase 1 Context (if applicable)
[If this was proposed in Phase 1, cite the analyst's original rationale]

### Discussion Summary
[Key points from debate - 3-5 bullets]

### Key Arguments For
1. [Argument from debate - note if referencing Phase 1 work]
2. [Argument from debate]

### Key Arguments Against
1. [Argument from debate]
2. [Argument from debate]

### Proposed Amendments
1. [Amendment suggested during debate]

### Vote Records

#### Effectiveness Vote (Equal Weight)
| Analyst | Vote | Weight | Score | Reasoning |
|---------|------|--------|-------|-----------|
| PA-01 | Y | 1.0 | 1.0 | [Reason] |
...
**Total: X/12**

#### Compromise Vote (Equal Weight)
| Analyst | Vote | Weight | Score | Reasoning |
|---------|------|--------|-------|-----------|
...
**Total: X/12**

#### Progressive Sort (Weighted)
| Analyst | Vote | Weight | Score | Reasoning |
|---------|------|--------|-------|-----------|
...
**Total: X/15.0**

#### Conservative Sort (Weighted)
| Analyst | Vote | Weight | Score | Reasoning |
|---------|------|--------|-------|-----------|
...
**Total: X/16.5**
```

---

## Compilation (Writer/Editor)

### Required Outputs

1. **Top 20 Effective Policies Document**
   - Ranked list with vote tallies
   - Goal distribution analysis
   - Key debate highlights

2. **Top 10 Compromise Policies Document**
   - Ranked list with coalition analysis
   - What made compromise possible
   - Potential modifications for broader support

3. **Top 10 Progressive Policies Document**
   - Ranked list with weighted scores
   - Progressive values represented
   - Weighting scheme clearly shown

4. **Top 10 Conservative Policies Document**
   - Ranked list with weighted scores
   - Conservative values represented
   - Weighting scheme clearly shown

5. **Debate Summary Document**
   - Major themes and patterns
   - Areas of broad agreement
   - Persistent disagreements
   - Unexpected alliances
   - Key insights for Human Principal

---

## Quality Assurance

### QA/Fact Checker Responsibilities
- Verify vote tallies are accurate
- Confirm weighting applied correctly
- Check that all policies were voted on
- Verify reasoning summaries are fair
- **Check memory files:** Ensure all analysts have updated Phase 2 memory
- **Verify consistency:** Spot-check that votes align with Phase 1 positions (or note evolution)

---

## Human Principal Presentation

**Deliverables:**
1. Top 20 Effective Policies (phase2_top20_effective.md)
2. Top 10 Compromise Policies (phase2_top10_compromise.md)
3. Top 10 Progressive Policies (phase2_top10_progressive.md)
4. Top 10 Conservative Policies (phase2_top10_conservative.md)
5. Debate Summary (phase2_debate_summary.md)
6. Full Vote Records (phase2_vote_records.md)

**Presentation Format:**
```markdown
## PHASE 2 DELIVERABLE: Policy Debate Complete

### Summary
- Policies debated: 120
- Voting rounds completed: 4

### Key Findings
1. [Major finding]
2. [Major finding]

### Recommendations for Phase 3
Based on voting, recommend these policies for deep refinement:
1. [Policy - reason]
2. [Policy - reason]

### Awaiting Human Principal Direction
- Which policies to advance to Phase 3?
- Any policies to remove from consideration?
- Priorities for refinement?
```

---

## Timeline

| Step | Duration | Cumulative |
|------|----------|------------|
| Round 1 Setup | 0.5 hours | 0.5 hours |
| Round 1 Voting | 4-6 hours | 6.5 hours |
| Round 2 Voting | 2-3 hours | 9.5 hours |
| Round 3A Voting | 1-2 hours | 11.5 hours |
| Round 3B Voting | 1-2 hours | 13.5 hours |
| Compilation | 2 hours | 15.5 hours |
| QA Review | 1 hour | 16.5 hours |
| Director Review | 1 hour | 17.5 hours |
| Presentation | 0.5 hours | 18 hours |

**Total Estimated Time:** 18 hours

---

## Memory System Completion

**At end of Phase 2, each analyst must:**
1. Set Phase 2 status to "completed"
2. Add completion timestamp
3. Verify all votes recorded in memory
4. Document key alliances and conflicts
5. Note any evolution in thinking
6. Update metadata (total_votes_cast, collaboration_partners, etc.)

**Memory files will be used in Phase 3 for:**
- Maintaining consistency in refinement work
- Understanding each analyst's positions and reasoning
- Building on established alliances
- Addressing recorded concerns and dissents

---

*Workflow Version: 2.0 (Multi-project)*
*Last Updated: December 2025*
