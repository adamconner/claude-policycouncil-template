# Example: Affordable Housing Policy Council

**Topic:** Increasing affordable housing availability in major US cities

This folder contains a complete example of Policy Council output across all 5 phases — from initial idea generation through final rollout materials.

---

## Complete Workflow Example

This example demonstrates the full Policy Council workflow:

| Phase | Description | Output |
|-------|-------------|--------|
| **Phase 1** | 6 agents generate 30 policy proposals | [View Ideas](outputs/phase1/ideas_master.md) |
| **Phase 2** | Agents vote on proposals | [View Results](outputs/phase2/voting_results.md) |
| **Phase 3** | Top policy refined into recommendation | [View Documents](#phase-3-policy-refinement) |
| **Phase 4** | Comprehensive paper + legislation | [View Documents](#phase-4-full-development) |
| **Phase 5** | Rollout materials created | [View Documents](#phase-5-rollout-materials) |

**Policy Developed:** National Zoning Reform Act (highest consensus from Phase 2)

---

## Phase 1: Idea Generation

**6 agents** generated **30 policy proposals** (5 each):
- **12 Big Ideas** (sweeping, transformational proposals)
- **18 Standard proposals** (targeted, incremental reforms)

### Files

| File | Description |
|------|-------------|
| [ideas_master.md](outputs/phase1/ideas_master.md) | All 30 proposals summarized |
| [pa01_economic_populist.md](outputs/phase1/pa01_economic_populist.md) | Full proposals from PA-01 |

### Big Ideas Generated

| Idea | Agent | Scope |
|------|-------|-------|
| National Social Housing Authority | PA-01, PA-02 | $500B, 2-3M units |
| National Zoning Preemption | PA-06 | Deregulatory |
| Housing Production Tax Credit | SA-07 | $45B over 10 years |
| Defense Workforce Housing | PA-17 | Security-focused |
| Global Housing Innovation Partnership | PA-18 | International |

---

## Phase 2: Voting

Agents voted on top 5 proposals. **National Zoning Reform** achieved highest consensus (5-1).

### Files

| File | Description |
|------|-------------|
| [voting_results.md](outputs/phase2/voting_results.md) | Voting results and analysis |

### Key Finding: Cross-Partisan Agreement

National Zoning Reform succeeded across ideological lines:
- **Conservatives:** "Removing government barriers to housing"
- **Progressives:** "Housing justice with anti-displacement protections"

---

## Phase 3: Policy Refinement

The top policy (National Zoning Reform) was developed into a full recommendation with supporting analysis.

### Files

| File | Description |
|------|-------------|
| [national_zoning_reform_recommendation.md](outputs/phase3/national_zoning_reform_recommendation.md) | Main policy recommendation |
| [research_brief.md](outputs/phase3/research_brief.md) | Academic literature and evidence |
| [economic_analysis.md](outputs/phase3/economic_analysis.md) | Cost-benefit analysis |
| [implementation_plan.md](outputs/phase3/implementation_plan.md) | Phased implementation roadmap |
| [political_assessment.md](outputs/phase3/political_assessment.md) | Political viability analysis |
| [one_pager.md](outputs/phase3/one_pager.md) | Executive summary (1 page) |
| [talking_points.md](outputs/phase3/talking_points.md) | Key messages for advocates |

### Key Findings

- **Feasibility:** Medium (legal authority strong, implementation complex)
- **Political Viability:** Moderate (65-70% Dem support, 35-45% GOP support)
- **Economic Impact:** High ($20B+ annual savings, 600:1 benefit-cost)
- **Recommended Vehicle:** Infrastructure reauthorization bill (2026)

---

## Phase 4: Full Development

Comprehensive 24-section policy paper with draft federal and state legislation.

### Files

| File | Description |
|------|-------------|
| [national_zoning_reform_full_paper.md](outputs/phase4/national_zoning_reform_full_paper.md) | Comprehensive 24-section paper |
| [draft_federal_legislation.md](outputs/phase4/draft_federal_legislation.md) | Draft federal bill (12 sections) |
| [draft_state_legislation_ca.md](outputs/phase4/draft_state_legislation_ca.md) | California state adaptation |
| [qa_summary.md](outputs/phase4/qa_summary.md) | Quality assurance review |

### Paper Sections

1. Executive Summary
2. Background & Context
3. Policy Landscape
4. Historical Precedents
5. Public Opinion
6. Detailed Proposal
7. Policy Tools & Mechanisms
8. Goals & Metrics
9. Administration & Enforcement
10. State Capacity Requirements
11. Impact Analysis
12. Cost Estimates
13. Benefits Analysis
14. Legal Analysis
15. Implementation Timeline
16. Arguments For
17. Arguments Against
18. Key Stakeholders
19. Alternative Approaches
20. Equity Considerations
21. Regulatory Impact Assessment
22. Procedural Pathway
23. Minority/Dissenting Views
24. Sources & References

---

## Phase 5: Rollout Materials

Communication materials for different audiences and channels.

### Files

| File | Description |
|------|-------------|
| [executive_summary.md](outputs/phase5/executive_summary.md) | 5-page overview |
| [press_release.md](outputs/phase5/press_release.md) | Media announcement |
| [op_ed_general.md](outputs/phase5/op_ed_general.md) | Opinion piece (~800 words) |
| [fact_sheet.md](outputs/phase5/fact_sheet.md) | Quick reference (1 page) |
| [talking_points_refined.md](outputs/phase5/talking_points_refined.md) | Final messaging guide |
| [social_media_toolkit.md](outputs/phase5/social_media_toolkit.md) | Ready-to-post content |
| [faq.md](outputs/phase5/faq.md) | Frequently asked questions |

---

## Output File Structure

```
outputs/
├── phase1/
│   ├── ideas_master.md              # All proposals summarized
│   └── pa01_economic_populist.md    # Individual agent output
├── phase2/
│   └── voting_results.md            # Voting and analysis
├── phase3/
│   ├── national_zoning_reform_recommendation.md
│   ├── research_brief.md
│   ├── economic_analysis.md
│   ├── implementation_plan.md
│   ├── political_assessment.md
│   ├── one_pager.md
│   └── talking_points.md
├── phase4/
│   ├── national_zoning_reform_full_paper.md
│   ├── draft_federal_legislation.md
│   ├── draft_state_legislation_ca.md
│   └── qa_summary.md
└── phase5/
    ├── executive_summary.md
    ├── press_release.md
    ├── op_ed_general.md
    ├── fact_sheet.md
    ├── talking_points_refined.md
    ├── social_media_toolkit.md
    └── faq.md
```

---

## How to Reproduce

Run from the repo root:

```bash
# Phase 1: Generate ideas
/council-phase1 Increasing affordable housing availability in major US cities

# Review Phase 1 output, then run Phase 2:
/council-vote latest

# After Phase 2, work with Claude to develop Phases 3-5
```

---

## Note

This example used a subset of 6 agents for Phase 1-2 demonstration. A full council run uses all 21 voting agents, generating 60-100+ proposals.

The Phase 3-5 outputs were generated for the top-ranked policy (National Zoning Reform) to demonstrate the complete workflow from idea to rollout-ready materials.
