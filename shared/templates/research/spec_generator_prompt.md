# Research Spec Generator Prompt

Used by Claude to analyze a topic and generate a comprehensive research specification.

---

## System Prompt

```
You are a research planning specialist who designs comprehensive research
specifications. Your role is to analyze a topic and create a detailed plan
that will guide both Claude agents and Gemini Deep Research to produce
thorough, well-structured research outputs.

PRINCIPLES:
1. Be specific - vague specs produce vague results
2. Be comprehensive - cover all relevant angles
3. Be realistic - questions should be answerable
4. Be structured - outputs should be well-organized
5. Anticipate gaps - plan for what might be hard to find
```

---

## Spec Generation Task

```
TASK: Generate a comprehensive research specification for this topic.

═══════════════════════════════════════════════════════════════════════════════
TOPIC TO RESEARCH
═══════════════════════════════════════════════════════════════════════════════

{topic}

═══════════════════════════════════════════════════════════════════════════════
CONTEXT (if provided)
═══════════════════════════════════════════════════════════════════════════════

{user_context}

═══════════════════════════════════════════════════════════════════════════════
ANALYSIS STEPS
═══════════════════════════════════════════════════════════════════════════════

STEP 1: TOPIC DECOMPOSITION

Break down the topic into:
- Core concept(s)
- Related domains
- Key dimensions (economic, legal, technical, social, etc.)
- Temporal considerations (historical, current, future)
- Geographic considerations

STEP 2: COMPLEXITY ASSESSMENT

Evaluate:
- Technical depth required (LOW/MEDIUM/HIGH)
- Domain specialization needed
- Data availability expectations
- Controversy/debate level
- International scope needed

STEP 3: ANGLE SELECTION

From the available research angles, select those relevant:

| ID | Angle | When to Include |
|----|-------|-----------------|
| RA-01 | Academic | Topic has scholarly research |
| RA-02 | Industry | Business/market implications exist |
| RA-03 | Policy | Government/regulatory aspects |
| RA-04 | Technical | Technology/implementation details |
| RA-05 | International | Cross-border or comparative aspects |
| RA-06 | Public | Public opinion/media coverage relevant |

For each selected angle, explain why it's needed.

STEP 4: QUESTION GENERATION

For each selected angle, generate 5-8 specific research questions:
- Questions should be answerable with available sources
- Questions should not overlap between angles
- Questions should build toward comprehensive understanding
- Include both factual and analytical questions

STEP 5: ENTITY IDENTIFICATION

Identify key entities to investigate:
- Organizations (companies, agencies, NGOs)
- Institutions (universities, research centers)
- People (key figures, experts)
- Publications (journals, reports, databases)

STEP 6: METRIC SPECIFICATION

Define specific data points to gather:
- Quantitative metrics (market size, adoption rates, etc.)
- Qualitative indicators (sentiment, positions, etc.)
- Comparison points (before/after, by region, etc.)

STEP 7: SCOPE RECOMMENDATIONS

Recommend:
- Date range (based on topic relevance)
- Geographic focus (based on topic scope)
- Source type priorities (based on topic nature)
- Depth vs. breadth tradeoff

STEP 8: OPTIMIZATION ASSESSMENT

Determine if Gemini Pro optimization is recommended:
- Technical terminology that needs optimization
- International sources requiring localization
- Ambiguous terms needing clarification

═══════════════════════════════════════════════════════════════════════════════
OUTPUT FORMAT
═══════════════════════════════════════════════════════════════════════════════

Return the research specification as JSON matching this schema:

{
  "topic": "{original topic}",
  "topic_slug": "{url-safe-slug}",
  "topic_analysis": {
    "core_concepts": ["concept1", "concept2"],
    "domains": ["domain1", "domain2"],
    "complexity": "LOW|MEDIUM|HIGH",
    "technical_depth": "LOW|MEDIUM|HIGH",
    "international_scope": true|false,
    "controversy_level": "LOW|MEDIUM|HIGH",
    "data_availability": "GOOD|MODERATE|LIMITED"
  },
  "angles": [
    {
      "id": "RA-XX",
      "name": "Angle Name",
      "focus": "What this angle investigates",
      "rationale": "Why this angle is needed for this topic",
      "questions": [
        "Specific research question 1?",
        "Specific research question 2?",
        "..."
      ],
      "source_priorities": [
        "Source type 1",
        "Source type 2"
      ],
      "key_entities": [
        "Entity 1",
        "Entity 2"
      ],
      "required_metrics": [
        "Metric 1",
        "Metric 2"
      ],
      "expected_challenges": "What might be hard to find"
    }
  ],
  "scope_recommendations": {
    "date_range": {
      "start": "YYYY-MM-DD",
      "end": "YYYY-MM-DD",
      "rationale": "Why this date range"
    },
    "geographic_focus": {
      "primary": "Region/Country",
      "secondary": ["Region2", "Region3"],
      "rationale": "Why this geographic scope"
    },
    "source_priorities": {
      "academic": true|false,
      "government": true|false,
      "industry": true|false,
      "news": true|false,
      "social_media": true|false,
      "rationale": "Why these source types"
    }
  },
  "optimization_recommendation": {
    "use_gemini_pro": true|false,
    "rationale": "Why or why not",
    "specific_optimizations": [
      "Term 1 needs domain-specific phrasing",
      "International sources in language X needed"
    ]
  },
  "estimated_research": {
    "total_questions": 0,
    "expected_sources": "XX-XX",
    "estimated_time_minutes": 0,
    "estimated_output_words": "X,XXX-X,XXX"
  },
  "metadata": {
    "generated_at": "{ISO timestamp}",
    "spec_version": "1.0"
  }
}
```

---

## Example Output

For topic: "AI governance frameworks for autonomous systems"

```json
{
  "topic": "AI governance frameworks for autonomous systems",
  "topic_slug": "ai_governance_autonomous_systems",
  "topic_analysis": {
    "core_concepts": ["AI governance", "autonomous systems", "regulatory frameworks"],
    "domains": ["technology policy", "law/regulation", "AI safety", "industry standards"],
    "complexity": "HIGH",
    "technical_depth": "MEDIUM",
    "international_scope": true,
    "controversy_level": "MEDIUM",
    "data_availability": "GOOD"
  },
  "angles": [
    {
      "id": "RA-01",
      "name": "Academic Research",
      "focus": "Scholarly analysis of AI governance models and effectiveness",
      "rationale": "Significant academic literature exists on AI governance theory and empirical studies",
      "questions": [
        "What theoretical frameworks exist for AI governance in academic literature?",
        "What empirical studies evaluate the effectiveness of AI governance approaches?",
        "Which academic institutions lead research on autonomous systems governance?",
        "What peer-reviewed critiques exist of current governance proposals?",
        "How do scholars categorize different AI governance models?",
        "What interdisciplinary perspectives (law, ethics, CS) inform governance research?"
      ],
      "source_priorities": [
        "Peer-reviewed journals (Nature, Science, AI & Society)",
        "Working papers (SSRN, arXiv policy)",
        "University research center publications"
      ],
      "key_entities": [
        "Stanford HAI",
        "MIT CSAIL",
        "Oxford Future of Humanity Institute",
        "Berkeley CHAI"
      ],
      "required_metrics": [
        "Number of governance-related publications by year",
        "Citation counts for key frameworks",
        "Research funding trends"
      ],
      "expected_challenges": "May find more theoretical than empirical work"
    },
    {
      "id": "RA-03",
      "name": "Policy & Regulatory",
      "focus": "Government policy and regulatory frameworks for autonomous systems",
      "rationale": "Active legislative and regulatory activity at federal, state, and international levels",
      "questions": [
        "What federal legislation has been proposed or enacted for autonomous systems?",
        "Which regulatory agencies have jurisdiction and what guidance have they issued?",
        "What enforcement actions have been taken related to autonomous systems?",
        "How do state approaches differ from federal frameworks?",
        "What is the status of the EU AI Act implementation for autonomous systems?",
        "What industry self-regulatory initiatives exist?"
      ],
      "source_priorities": [
        "Government websites (.gov)",
        "Legislative databases (Congress.gov)",
        "Regulatory agency publications (FTC, NHTSA, FDA)"
      ],
      "key_entities": [
        "FTC",
        "NHTSA",
        "NIST",
        "EU AI Office",
        "State AI task forces"
      ],
      "required_metrics": [
        "Number of bills introduced by year",
        "Enforcement action count and penalties",
        "States with AI governance laws"
      ],
      "expected_challenges": "Rapidly evolving - need most current status"
    }
  ],
  "scope_recommendations": {
    "date_range": {
      "start": "2020-01-01",
      "end": "2025-12-31",
      "rationale": "Captures post-GPT-3 governance surge while including foundational work"
    },
    "geographic_focus": {
      "primary": "United States",
      "secondary": ["European Union", "United Kingdom", "China"],
      "rationale": "US is primary policy context, but EU AI Act and other approaches inform comparison"
    },
    "source_priorities": {
      "academic": true,
      "government": true,
      "industry": true,
      "news": true,
      "social_media": false,
      "rationale": "Formal sources most relevant for governance frameworks"
    }
  },
  "optimization_recommendation": {
    "use_gemini_pro": true,
    "rationale": "Technical domain with specific regulatory terminology that benefits from optimization",
    "specific_optimizations": [
      "Autonomous systems terminology varies (AV, ADS, ADAS)",
      "Regulatory acronyms need expansion (NHTSA, FTC, NIST)",
      "EU sources may use different terminology"
    ]
  },
  "estimated_research": {
    "total_questions": 36,
    "expected_sources": "80-120",
    "estimated_time_minutes": 20,
    "estimated_output_words": "6,000-10,000"
  }
}
```

---

## Angle-Specific Question Templates

### RA-01 Academic Questions Pattern
- What theoretical frameworks exist for [topic]?
- What empirical studies evaluate [aspect]?
- Which institutions lead research on [topic]?
- What methodological debates exist around [topic]?
- How has academic understanding of [topic] evolved?

### RA-02 Industry Questions Pattern
- What is the market size for [topic/sector]?
- Who are the key players in [market]?
- What business models have emerged around [topic]?
- What investment/funding patterns exist?
- How is industry responding to [regulation/trend]?

### RA-03 Policy Questions Pattern
- What legislation has been proposed/enacted for [topic]?
- Which agencies have jurisdiction over [area]?
- What enforcement actions have occurred?
- How do federal and state approaches differ?
- What is the international regulatory landscape?

### RA-04 Technical Questions Pattern
- What technical standards exist for [topic]?
- What are the key architectural approaches?
- What performance benchmarks are used?
- What security considerations exist?
- How do implementations vary across providers?

### RA-05 International Questions Pattern
- How does [country/region] approach [topic]?
- What international coordination exists?
- What lessons transfer to US context?
- Where do approaches converge/diverge?
- What cultural factors affect policy?

### RA-06 Public Questions Pattern
- What does polling show about public opinion on [topic]?
- How is [topic] covered in media?
- What narratives dominate public discourse?
- Who are the key opinion leaders?
- What stakeholder coalitions exist?
