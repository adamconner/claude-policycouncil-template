# Gemini Deep Research Prompt Template

This template is used to generate optimized prompts for Gemini Deep Research API.

## Template Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{topic}` | Research topic | "AI governance frameworks" |
| `{angle_name}` | Research angle name | "Academic Research" |
| `{angle_focus}` | Angle focus area | "Scholarly literature, peer-reviewed studies" |
| `{questions}` | Research questions | Bulleted list |
| `{date_range}` | Date constraints | "January 2020 - December 2025" |
| `{geo_focus}` | Geographic focus | "United States and European Union" |
| `{source_types}` | Priority source types | "peer-reviewed journals, government reports" |
| `{key_entities}` | Entities to investigate | "Stanford HAI, MIT CSAIL, EU AI Office" |
| `{sections}` | Required output sections | Formatted section list |
| `{tables}` | Required tables | Table specifications |
| `{citation_format}` | Citation instructions | Academic format details |
| `{word_targets}` | Section word counts | "Executive Summary: 300 words" |
| `{unknown_handling}` | Missing data instructions | "State 'Not available' rather than estimate" |

---

## Base Prompt Template

```
PERSONA:
You are a specialized {angle_name} analyst conducting comprehensive research
for a multi-stakeholder policy council. Your expertise is in {angle_focus}.

TASK:
Conduct deep research on the following topic from your specialized perspective:

TOPIC: {topic}

RESEARCH QUESTIONS:
{questions}

SCOPE CONSTRAINTS:
- Date Range: {date_range}
- Geographic Focus: {geo_focus}
- Source Types to Prioritize: {source_types}
- Key Entities/Organizations to Investigate: {key_entities}

OUTPUT STRUCTURE:
Organize your findings into these sections:

{sections}

TABLE REQUIREMENTS:
{tables}

CITATION REQUIREMENTS:
{citation_format}

For each finding, rate your confidence level:
- HIGH: Multiple corroborating authoritative sources
- MEDIUM: Single authoritative source or multiple secondary sources
- LOW: Limited sources, emerging research, or conflicting information

HANDLING UNKNOWNS:
{unknown_handling}

ADDITIONAL INSTRUCTIONS:
- Compare and contrast findings across different sources
- Identify patterns and trends in the data
- Note any conflicting information between sources
- Highlight emerging developments vs established findings
- Provide specific data points with their sources
- Include publication dates for all cited sources

DELIVERABLES:
1. Structured report following the sections above
2. All required tables with complete data
3. Full source bibliography with URLs
4. "Research Gaps" section noting what could not be found
5. "Recommended Follow-up" section with specific questions for further research
```

---

## Section Templates

### Executive Summary Section
```
## Executive Summary

Provide a {word_count}-word overview that includes:
- The most significant finding from this research angle
- 2-3 key data points with sources
- Primary recommendation or insight
- Confidence level for main conclusions
```

### Key Findings Section
```
## Key Findings

Organize findings by theme. For each theme:

### [Theme Name]

**Finding:** [Clear statement of finding]

**Evidence:**
- [Data point 1] (Source: [citation])
- [Data point 2] (Source: [citation])

**Confidence:** [HIGH/MEDIUM/LOW]

**Implications:** [1-2 sentences on significance]
```

### Data Table Section
```
## Data & Statistics

{table_name}:

| {col1} | {col2} | {col3} | {col4} | {col5} |
|--------|--------|--------|--------|--------|
| [data] | [data] | [data] | [data] | [data] |

Notes:
- All values sourced and dated
- Confidence ratings included where applicable
- Missing data explicitly noted
```

### Research Gaps Section
```
## Research Gaps

### Data Unavailable
- [Specific data point that could not be found]
- [Another gap]

### Conflicting Sources
- [Topic where sources disagreed]
- Resolution attempted: [Yes/No]
- Recommended: [Follow-up action]

### Areas Requiring Further Research
- [Topic needing deeper investigation]
- Suggested query: "[Specific follow-up question]"
```

---

## Angle-Specific Prompt Additions

### RA-01: Academic Research
```
ADDITIONAL CONTEXT FOR ACADEMIC RESEARCH:
- Prioritize peer-reviewed sources over preprints
- Note journal impact factors where relevant
- Identify seminal papers vs recent developments
- Track citation patterns for key findings
- Note methodological approaches used in studies
```

### RA-02: Industry Analysis
```
ADDITIONAL CONTEXT FOR INDUSTRY ANALYSIS:
- Include market size data with CAGR where available
- Identify market leaders by revenue/market share
- Note recent M&A activity and funding rounds
- Track regulatory impacts on business models
- Include analyst projections with source attribution
```

### RA-03: Policy & Regulatory
```
ADDITIONAL CONTEXT FOR POLICY RESEARCH:
- Include specific bill numbers and legislative status
- Note regulatory agency jurisdiction and enforcement history
- Track policy evolution and key amendments
- Identify stakeholder positions (industry, advocacy, government)
- Compare federal vs state approaches
```

### RA-04: Technical Deep-Dive
```
ADDITIONAL CONTEXT FOR TECHNICAL RESEARCH:
- Include specific version numbers and release dates
- Note technical standards and certifications
- Document architecture patterns and implementations
- Identify security considerations and CVEs
- Track benchmark performance data
```

### RA-05: International Comparative
```
ADDITIONAL CONTEXT FOR INTERNATIONAL RESEARCH:
- Compare approaches across at least 5 jurisdictions
- Note cultural/political context affecting policy
- Identify transferability to US context
- Track international coordination efforts
- Include non-English sources where significant
```

### RA-06: Public Discourse
```
ADDITIONAL CONTEXT FOR PUBLIC DISCOURSE:
- Include polling data with methodology notes
- Track media coverage volume and sentiment
- Identify key opinion leaders and influencers
- Note narrative frames used in public debate
- Document stakeholder coalition positions
```

---

## Example Generated Prompt

```
PERSONA:
You are a specialized Policy & Regulatory analyst conducting comprehensive
research for a multi-stakeholder policy council. Your expertise is in
government policy, regulatory frameworks, and legislative history.

TASK:
Conduct deep research on the following topic from your specialized perspective:

TOPIC: AI governance frameworks for autonomous systems

RESEARCH QUESTIONS:
- What federal legislation has been proposed or enacted for AI governance?
- Which regulatory agencies have jurisdiction over autonomous systems?
- What enforcement actions have been taken related to AI systems?
- How do state-level approaches differ from federal frameworks?
- What industry self-regulatory initiatives exist?

SCOPE CONSTRAINTS:
- Date Range: January 2022 - December 2025
- Geographic Focus: United States (federal and state), with EU comparison
- Source Types to Prioritize: Government websites (.gov), legislative databases,
  regulatory agency publications, legal journals
- Key Entities/Organizations to Investigate: FTC, NIST, OSTP, state AI task forces,
  EU AI Office

OUTPUT STRUCTURE:
Organize your findings into these sections:

1. Executive Summary (300 words)
   - Key legislative developments
   - Regulatory landscape overview
   - Primary recommendation

2. Federal Regulatory Framework
   - Current laws and regulations
   - Pending legislation (with bill numbers)
   - Agency guidance and enforcement

3. State-Level Approaches
   - Leading states and their frameworks
   - Comparison matrix of approaches
   - Preemption issues

4. EU Comparison
   - EU AI Act implementation status
   - Key differences from US approach
   - Lessons for US policy

5. Data & Statistics Table
6. Research Gaps
7. Source Bibliography

TABLE REQUIREMENTS:

Legislative Tracker:
| Bill | Status | Sponsor | Key Provisions | Last Action |
|------|--------|---------|----------------|-------------|

State Comparison:
| State | Framework | Focus Areas | Enforcement | Effective Date |
|-------|-----------|-------------|-------------|----------------|

CITATION REQUIREMENTS:
Use academic citation format:
- Inline: [Agency/Author, Year]
- Bibliography: Author/Agency (Year). "Title." Publication/Document Type. URL

For each finding, rate your confidence level:
- HIGH: Multiple corroborating authoritative sources
- MEDIUM: Single authoritative source or multiple secondary sources
- LOW: Limited sources, emerging research, or conflicting information

HANDLING UNKNOWNS:
If specific data is not available, explicitly state 'Data not available for
[item]' rather than estimating or inferring. Note all gaps in the Research
Gaps section.

ADDITIONAL CONTEXT FOR POLICY RESEARCH:
- Include specific bill numbers and legislative status
- Note regulatory agency jurisdiction and enforcement history
- Track policy evolution and key amendments
- Identify stakeholder positions (industry, advocacy, government)
- Compare federal vs state approaches

DELIVERABLES:
1. Structured report following the sections above
2. All required tables with complete data
3. Full source bibliography with URLs
4. "Research Gaps" section noting what could not be found
5. "Recommended Follow-up" section with specific questions for further research
```
