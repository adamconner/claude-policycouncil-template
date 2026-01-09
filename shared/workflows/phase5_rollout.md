# Phase 5: Supporting Rollout Materials

**Version:** 2.0
**Jurisdiction:** United States of America

## Purpose

Generate think tank-style rollout package for selected policies to support public launch and advocacy.

## Prerequisites

- Phase 4 complete
- Human principal has selected 1-3 policies for rollout materials
- All relevant agents available

---

## Workflow Steps

### Step 1: Human Selection

**Input:** Phase 4 full development papers
**Output:** List of policies for rollout package

- Human principal reviews Phase 4 outputs
- Selects 1-3 policies for rollout materials
- Documents selection rationale in DECISION_LOG.md

---

### Step 2: Generate Rollout Package

**Input:** Selected policies from Step 1
**Output:** Complete rollout package per policy

For each selected policy, create:

#### Core Materials (9):

**2.1 Executive Summary Document (5 pages)**
- Condensed version of full paper
- Key findings and recommendations
- Designed for policymaker consumption
- Clear call to action
- Contact information

**2.2 Press Release**
- Draft announcement for policy release
- Headline and subhead
- Key quotes (placeholder for real quotes)
- Key findings (3-5 bullet points)
- Background paragraph
- Contact information placeholder
- Boilerplate organization description

**2.3 Op-Eds (3)**
Three distinct opinion pieces for different audiences:

| Op-Ed | Target | Angle | Length |
|-------|--------|-------|--------|
| 1 | General audience | Why this matters to everyone | 750-1000 words |
| 2 | Industry/stakeholder | Sector-specific implications | 750-1000 words |
| 3 | Political/ideological | Political case for policy | 750-1000 words |

**2.4 Video Scripts (3)**
Three video scripts for different formats:

| Script | Format | Length | Content |
|--------|--------|--------|---------|
| 1 | Social media explainer | 60 seconds | Hook, problem, solution, CTA |
| 2 | Overview video | 3 minutes | Context, details, impact, next steps |
| 3 | Deep dive | 10 minutes | Full explanation, Q&A anticipation |

Include visual/graphic suggestions for each.

**2.5 Event Speaker Recommendations**
- 5-10 suggested speakers for launch event
- Categories:
  - Academic experts
  - Practitioners/implementers
  - Political figures (bipartisan if possible)
  - Stakeholder representatives
  - Beneficiary voices
- For each: Name, affiliation, why relevant, contact approach

**2.6 Rollout Plan**
- Launch timeline (week-by-week for first month)
- Media strategy
  - Earned media targets
  - Paid media considerations
  - Social media plan
- Stakeholder engagement plan
  - Pre-brief list
  - Coalition building
  - Opposition outreach
- Hill outreach (if applicable)
  - Target members/committees
  - Briefing schedule
  - Leave-behind distribution

**2.7 AI Generation Instructions - PowerPoint**
Detailed prompt for Gemini/other AI to generate presentation slides:
- Slide-by-slide outline
- Key data visualizations needed
- Talking points per slide
- Design guidance (colors, style)
- Recommended slide count: 15-20

**2.7a Slide Deck Generation (Gemini NanoBanana Input)**
Comprehensive specification file for AI slide deck generation:
- Metadata (title, subtitle, target audience, slide count, style)
- Slide-by-slide content specifications (title, key message, content, visual suggestions, speaker notes)
- Visual assets needed (charts, infographics, maps, comparisons)
- Data and statistics to include on each slide
- Color scheme and branding guidelines
- Target audience and tone guidance
- Format as structured markdown ready for Gemini NanoBanana or similar AI presentation tools

**2.8 AI Generation Instructions - Graphics**
Detailed prompts for AI to generate:
- Infographics (2-3 concepts)
  - Dimensions
  - Key data points
  - Style guidance
- Social media graphics
  - Platform-specific sizes
  - Quote cards
  - Data visualizations
- Data visualizations
  - Chart types needed
  - Data to visualize

**2.9 Polling Questions**
- 5-10 questions to test policy efficacy and popularity
- A/B message testing questions (2-3 pairs)
- Demographic cross-tabs to request
- Suggested polling methodology
- Sample size recommendations

---

#### Additional Materials (6):

**2.10 Fact Sheet (1-pager)**
- One-page summary for quick reference
- Key facts, stats, and talking points
- Designed for media and staff use
- Print-ready format
- Sections:
  - The Problem
  - The Solution
  - Key Facts (5-7 bullets)
  - Expected Impact
  - How to Learn More

**2.11 FAQ Document**
- 15-20 frequently asked questions and answers
- Categories:
  - General/Overview questions
  - Technical/Implementation questions
  - Cost/Funding questions
  - Political/Opposition questions
  - Messaging questions
- Include source citations where relevant

**2.12 Social Media Toolkit**
- Pre-written posts for various platforms:
  - Twitter/X (5-10 tweets)
  - LinkedIn (3-5 posts)
  - Facebook (3-5 posts)
  - Instagram captions (3-5)
- Shareable graphics specifications
- Hashtag recommendations (5-10)
- Influencer engagement suggestions
- Posting schedule recommendations

**2.13 Coalition Letter Template**
- Pre-drafted support letter for organizations
- Customizable sections by sector/stakeholder type
- Sign-on instructions
- Target recipient list
- Deadline for signatures
- Collection mechanism

**2.14 Hill Leave-Behind**
- One-page document for Congressional meetings
- Sections:
  - Policy Overview
  - Key Ask
  - District/State Impact (customizable)
  - Talking Points
  - Contact Information
- Design for easy customization by district/state

**2.15 Opposition Research Brief**
- Anticipated opposition arguments (5-10)
- Counter-arguments and rebuttals for each
- Opposition stakeholder mapping
  - Who will oppose
  - Their likely arguments
  - Their funding/influence
- Attack ad inoculation strategies
- Rapid response recommendations

---

### Step 3: Document Creation

**Input:** Content from Step 2
**Output:** Individual files per policy

Create files for each policy:

```
phase5/
├── policy_[ID]_executive_summary.md
├── policy_[ID]_press_release.md
├── policy_[ID]_opeds.md
├── policy_[ID]_video_scripts.md
├── policy_[ID]_speakers.md
├── policy_[ID]_rollout_plan.md
├── policy_[ID]_ai_powerpoint_prompt.md
├── policy_[ID]_slide_deck_gemini_input.md
├── policy_[ID]_ai_graphics_prompt.md
├── policy_[ID]_polling_questions.md
├── policy_[ID]_fact_sheet.md
├── policy_[ID]_faq.md
├── policy_[ID]_social_media_toolkit.md
├── policy_[ID]_coalition_letter.md
├── policy_[ID]_hill_leave_behind.md
└── policy_[ID]_opposition_research.md
```

---

### Step 4: Master Compilation

**Input:** Individual files from Step 3
**Output:** Master rollout document

Create `PHASE5_MASTER_ROLLOUT_MATERIALS.md` containing:
- Table of Contents
- All materials organized by policy
- Cross-reference to Phase 4 papers

---

### Step 5: Human Review

**Input:** Complete rollout package
**Output:** Human approval or revision requests

- Present rollout package to Human Principal
- Highlight key materials
- Note any customization needed
- Gather feedback for refinement
- Document final approval

---

## Outputs

| Output | Description |
|--------|-------------|
| `phase5/policy_[ID]_executive_summary.md` | 5-page executive summary |
| `phase5/policy_[ID]_press_release.md` | Draft press release |
| `phase5/policy_[ID]_opeds.md` | 3 op-eds |
| `phase5/policy_[ID]_video_scripts.md` | 3 video scripts |
| `phase5/policy_[ID]_speakers.md` | Speaker recommendations |
| `phase5/policy_[ID]_rollout_plan.md` | Launch plan |
| `phase5/policy_[ID]_ai_powerpoint_prompt.md` | AI slide generation prompt |
| `phase5/policy_[ID]_slide_deck_gemini_input.md` | Comprehensive Gemini NanoBanana slide deck specification |
| `phase5/policy_[ID]_ai_graphics_prompt.md` | AI graphics generation prompts |
| `phase5/policy_[ID]_polling_questions.md` | Survey questions |
| `phase5/policy_[ID]_fact_sheet.md` | 1-page fact sheet |
| `phase5/policy_[ID]_faq.md` | FAQ document |
| `phase5/policy_[ID]_social_media_toolkit.md` | Social media content |
| `phase5/policy_[ID]_coalition_letter.md` | Support letter template |
| `phase5/policy_[ID]_hill_leave_behind.md` | Congressional leave-behind |
| `phase5/policy_[ID]_opposition_research.md` | Opposition research brief |
| `phase5/PHASE5_MASTER_ROLLOUT_MATERIALS.md` | Combined master document |

---

## Completion Criteria

- [ ] Core rollout materials complete:
  - [ ] 5-page Executive Summary
  - [ ] Press Release
  - [ ] 3 Op-Eds
  - [ ] 3 Video Scripts
  - [ ] Speaker Recommendations
  - [ ] Rollout Plan
  - [ ] AI PowerPoint Instructions
  - [ ] Gemini NanoBanana Slide Deck Specification
  - [ ] AI Graphics Instructions
  - [ ] Polling Questions
- [ ] Additional materials complete:
  - [ ] Fact Sheet (1-pager)
  - [ ] FAQ Document
  - [ ] Social Media Toolkit
  - [ ] Coalition Letter Template
  - [ ] Hill Leave-Behind
  - [ ] Opposition Research Brief
- [ ] Master document compiled
- [ ] All materials ready for human review
- [ ] Human Principal has approved outputs

---

## Process Notes

### Iteration Loops
If rollout preparation reveals messaging or political issues, policy may return to Phase 4 for refinement. Document iteration decisions in DECISION_LOG.md.

### Customization
Many materials (especially Hill Leave-Behind) are designed for customization. Note where customization is expected.

### External Dependencies
- AI graphics/slides require external tools (Gemini, etc.)
- Polling requires external vendor
- Note these dependencies in rollout plan

---

## Agent Assignments

### Primary Authors:
- Writer/Editor - All written materials
- Communications Lead - Messaging, press, social media

### Specialist Contributions:
- SA-06 (Polling Expert) - Polling questions, public opinion analysis
- SA-01 (Legislative Counsel) - Hill materials, legislative strategy
- SA-02 (Legal Counsel) - Legal review of public materials

### Coordination:
- Council Director - Overall quality and coordination

---

## Templates

### Press Release Template
```markdown
# [ORGANIZATION NAME]

**FOR IMMEDIATE RELEASE**
**[DATE]**

## [HEADLINE: Active Voice, Key Finding]

### [Subhead: Additional Context]

**[CITY, STATE]** — [Opening paragraph: Who, what, when, where, why]

[Quote from organization leader]

[Key findings paragraph with 3-5 bullet points]

[Background paragraph on the issue]

[Quote from expert/stakeholder]

[Call to action paragraph]

### About [Organization]
[Boilerplate]

### Media Contact
[Name]
[Email]
[Phone]
```

### Fact Sheet Template
```markdown
# [POLICY NAME]
## Fact Sheet

### The Problem
[2-3 sentences]

### The Solution
[2-3 sentences]

### Key Facts
- [Fact 1]
- [Fact 2]
- [Fact 3]
- [Fact 4]
- [Fact 5]

### Expected Impact
[2-3 sentences with key metrics]

### Learn More
[Website/Contact]
```

---

*Workflow Version: 2.0*
*Jurisdiction: United States of America*
