# Agent Memory System - Schema Documentation

## Overview

The Agent Memory System enables policy analysts to maintain context across multiple phases of policy development. This solves the critical problem of agents "forgetting" their previous contributions, positions, and reasoning when moving from one phase to the next.

**Problem Solved:** PA-01 can now remember their Phase 1 ideas when voting in Phase 2, recall their Phase 2 votes when refining in Phase 3, and maintain ideological consistency throughout the entire policy development lifecycle.

---

## Architecture

### Two-Tier Memory Structure

```
Memory System
├── Shared Memory (cross-project)
│   └── shared/memory/agents/
│       └── [agent-id].json (e.g., pa01.json)
│
└── Project Memory (project-specific)
    └── projects/[project-name]/memory/
        └── [agent-id]_[project].json (e.g., pa01_economic_prosperity.json)
```

### When to Use Each Tier

**Shared Memory (`shared/memory/agents/`):**
- Core agent identity and consistent patterns
- Cross-project learnings and meta-insights
- Permanent ideological positions and red lines
- Skills and expertise developed over time

**Project Memory (`projects/[project]/memory/`):**
- All phase-specific contributions for THIS project
- Policy ideas generated
- Votes cast with reasoning
- Arguments made in debates
- Positions taken on specific policies
- Dissents and compromises

---

## Memory File Structure

### File Format
- **Format:** JSON (human-readable, programmatically accessible)
- **Naming:** `[agent-id].json` (shared) or `[agent-id]_[project].json` (project)
- **Encoding:** UTF-8
- **Indentation:** 2 spaces

### Schema Version
Current version: **1.0**

Each memory file includes a schema version for future compatibility.

---

## Memory Schema

### Top-Level Structure

```json
{
  "schema_version": "1.0",
  "agent_id": "PA-XX",
  "agent_perspective": "Brief description",
  "project_id": "project-name",
  "last_updated": "ISO 8601 timestamp",
  "phases": {
    "phase1": { ... },
    "phase2": { ... },
    "phase3": { ... },
    "phase4": { ... },
    "phase5": { ... }
  },
  "cross_phase_context": { ... },
  "metadata": { ... }
}
```

---

## Phase-Specific Schemas

### Phase 1: Idea Generation

```json
"phase1": {
  "status": "completed|in_progress|not_started",
  "completed_date": "ISO 8601 timestamp",
  "ideas_generated": [
    {
      "idea_id": "unique-id",
      "headline": "Policy headline",
      "description": "Brief description",
      "goals_addressed": ["growth", "mobility", "affordability"],
      "cost_estimate": "$X - $Y over Z years",
      "key_rationale": "Why this idea from my perspective",
      "research_sources": ["url1", "url2"],
      "generated_date": "ISO 8601 timestamp"
    }
  ],
  "research_conducted": [
    {
      "topic": "Research area",
      "key_findings": "Summary of findings",
      "sources": ["url1", "url2"]
    }
  ],
  "ideological_themes": [
    "Theme 1 across my ideas",
    "Theme 2 across my ideas"
  ]
}
```

### Phase 2: Debate & Voting

```json
"phase2": {
  "status": "completed|in_progress|not_started",
  "completed_date": "ISO 8601 timestamp",
  "votes_cast": {
    "effectiveness": [
      {
        "policy_id": "unique-id",
        "policy_headline": "Policy name",
        "vote": "yes|no|abstain",
        "reasoning": "1-2 sentence explanation",
        "vote_date": "ISO 8601 timestamp"
      }
    ],
    "compromise": [
      {
        "policy_id": "unique-id",
        "policy_headline": "Policy name",
        "vote": "yes|no|abstain",
        "reasoning": "Why I could/couldn't support this as compromise",
        "vote_date": "ISO 8601 timestamp"
      }
    ],
    "progressive_sort": [
      {
        "policy_id": "unique-id",
        "policy_headline": "Policy name",
        "vote": "yes|no|abstain",
        "reasoning": "How this aligns with progressive values",
        "vote_date": "ISO 8601 timestamp"
      }
    ],
    "conservative_sort": [
      {
        "policy_id": "unique-id",
        "policy_headline": "Policy name",
        "vote": "yes|no|abstain",
        "reasoning": "How this aligns with conservative values",
        "vote_date": "ISO 8601 timestamp"
      }
    ]
  },
  "arguments_made": [
    {
      "policy_id": "unique-id",
      "argument_type": "support|oppose|amendment",
      "argument_text": "The argument I made",
      "debate_context": "What prompted this argument",
      "date": "ISO 8601 timestamp"
    }
  ],
  "amendments_proposed": [
    {
      "policy_id": "unique-id",
      "amendment_text": "Proposed change",
      "rationale": "Why this amendment",
      "outcome": "accepted|rejected|modified|pending",
      "date": "ISO 8601 timestamp"
    }
  ],
  "key_alliances": [
    {
      "analyst_ids": ["PA-XX", "PA-YY"],
      "policy_area": "Where we aligned",
      "common_ground": "What we agreed on"
    }
  ],
  "key_conflicts": [
    {
      "analyst_ids": ["PA-XX"],
      "policy_area": "Where we disagreed",
      "point_of_contention": "The disagreement"
    }
  ]
}
```

### Phase 3: Refinement

```json
"phase3": {
  "status": "completed|in_progress|not_started",
  "completed_date": "ISO 8601 timestamp",
  "policies_refined": [
    {
      "policy_id": "unique-id",
      "my_role": "lead|contributor|reviewer",
      "contributions": [
        "Specific contribution 1",
        "Specific contribution 2"
      ],
      "concerns_raised": [
        "Concern about implementation",
        "Concern about unintended consequences"
      ],
      "compromises_accepted": [
        "What I compromised on and why"
      ]
    }
  ],
  "detailed_analyses_provided": [
    {
      "policy_id": "unique-id",
      "analysis_type": "economic|legal|technical|political",
      "key_findings": "Summary of my analysis",
      "recommendations": ["Recommendation 1", "Recommendation 2"]
    }
  ]
}
```

### Phase 4: Full Development

```json
"phase4": {
  "status": "completed|in_progress|not_started",
  "completed_date": "ISO 8601 timestamp",
  "implementation_reviews": [
    {
      "policy_id": "unique-id",
      "review_focus": "What I reviewed",
      "feedback_provided": "My detailed feedback",
      "approval_status": "approved|conditional|opposed"
    }
  ],
  "cost_benefit_analyses": [
    {
      "policy_id": "unique-id",
      "my_assessment": "From my perspective",
      "key_concerns": ["Concern 1", "Concern 2"],
      "key_benefits": ["Benefit 1", "Benefit 2"]
    }
  ]
}
```

### Phase 5: Rollout Planning

```json
"phase5": {
  "status": "completed|in_progress|not_started",
  "completed_date": "ISO 8601 timestamp",
  "rollout_recommendations": [
    {
      "policy_id": "unique-id",
      "recommended_approach": "My rollout recommendation",
      "stakeholder_concerns": ["Who might oppose", "Who would support"],
      "messaging_suggestions": ["Key message 1", "Key message 2"]
    }
  ]
}
```

---

## Cross-Phase Context

This section captures patterns and positions that span multiple phases:

```json
"cross_phase_context": {
  "core_positions": [
    {
      "position": "My consistent stance on X",
      "first_stated": "phase1|phase2|...",
      "reinforced_in": ["phase2", "phase3"],
      "examples": [
        "When I voted against policy X",
        "When I proposed amendment Y"
      ]
    }
  ],
  "evolution_of_thinking": [
    {
      "topic": "My thinking on this evolved",
      "initial_position": "What I thought in Phase 1",
      "evolved_position": "What I think now",
      "reason_for_change": "Why I changed my mind",
      "influenced_by": ["PA-XX argument", "New research"]
    }
  ],
  "dissents_recorded": [
    {
      "policy_id": "unique-id",
      "phase": "phase2|phase3|...",
      "nature_of_dissent": "I opposed because...",
      "my_alternative": "What I proposed instead",
      "outcome": "Dissent noted|Policy modified|Overruled"
    }
  ],
  "compromises_made": [
    {
      "policy_id": "unique-id",
      "phase": "phase2|phase3|...",
      "what_i_gave_up": "What I compromised on",
      "what_i_gained": "What made compromise acceptable",
      "lessons_learned": "What I learned from this"
    }
  ],
  "key_insights": [
    {
      "insight": "Important realization",
      "emerged_in_phase": "phase2",
      "impact_on_later_phases": "How this affected my later work"
    }
  ]
}
```

---

## Metadata

```json
"metadata": {
  "total_ideas_generated": 10,
  "total_votes_cast": 120,
  "total_arguments_made": 25,
  "total_amendments_proposed": 5,
  "participation_phases": ["phase1", "phase2", "phase3"],
  "ideological_consistency_score": 0.85,
  "collaboration_partners": ["PA-03", "PA-12", "PA-13"],
  "frequent_opponents": ["PA-06", "PA-08"],
  "notes": "Any special notes about this agent's participation"
}
```

---

## Memory Operations

### Reading Memory

**Before each phase, agents should:**
1. Load their project memory file
2. Review contributions from previous phases
3. Note their positions, votes, and reasoning
4. Identify any commitments or positions to maintain consistency

**Example Read Operation:**
```python
import json

def load_agent_memory(agent_id, project_id):
    filepath = f"projects/{project_id}/memory/{agent_id}_{project_id}.json"
    with open(filepath, 'r') as f:
        return json.load(f)

memory = load_agent_memory("pa01", "economic_prosperity")
phase1_ideas = memory["phases"]["phase1"]["ideas_generated"]
phase2_votes = memory["phases"]["phase2"]["votes_cast"]
```

### Writing Memory

**After each phase, agents should:**
1. Load existing memory
2. Update the relevant phase section
3. Update cross_phase_context if applicable
4. Update metadata
5. Update last_updated timestamp
6. Write back to file

**Example Write Operation:**
```python
import json
from datetime import datetime

def update_agent_memory(agent_id, project_id, updates):
    filepath = f"projects/{project_id}/memory/{agent_id}_{project_id}.json"

    # Load existing
    with open(filepath, 'r') as f:
        memory = json.load(f)

    # Update
    memory.update(updates)
    memory["last_updated"] = datetime.now().isoformat()

    # Write back
    with open(filepath, 'w') as f:
        json.dump(memory, f, indent=2)
```

### Querying Memory

**Common queries agents might perform:**

```python
# What did I propose in Phase 1?
my_ideas = memory["phases"]["phase1"]["ideas_generated"]

# How did I vote on policy X?
effectiveness_votes = memory["phases"]["phase2"]["votes_cast"]["effectiveness"]
my_vote_on_x = [v for v in effectiveness_votes if v["policy_id"] == "x"][0]

# What are my consistent positions?
core_positions = memory["cross_phase_context"]["core_positions"]

# Who do I frequently align with?
partners = memory["metadata"]["collaboration_partners"]

# Have I changed my mind on anything?
evolutions = memory["cross_phase_context"]["evolution_of_thinking"]
```

---

## Usage Guidelines

### For Orchestrators (Council Directors)

**Phase Transitions:**
1. Before starting a new phase, ensure all agents have updated their memory from the previous phase
2. Provide agents time to review their memory before participating
3. Reference memory in task assignments: "Recall your Phase 1 ideas when voting..."

**Quality Checks:**
- Verify memory files are being updated
- Check for consistency between memory and phase outputs
- Note when agents cite their own previous work (good sign)

### For Agents (Policy Analysts)

**Best Practices:**
1. **Read before you act:** Always review memory before contributing to a new phase
2. **Be consistent:** Your positions should build on previous work unless you explicitly note evolution
3. **Document reasoning:** Future you needs to understand why you took positions
4. **Note influences:** Record when other agents change your thinking
5. **Update promptly:** Add to memory immediately after phase completion

**Memory Prompts for Agents:**
- "Based on my Phase 1 research on X, I believe..."
- "Consistent with my vote in Phase 2, I recommend..."
- "While I initially thought X (Phase 1), I now believe Y because..."
- "As I argued in the Phase 2 debate, this policy..."

### For Developers

**Integration Points:**
- Automated memory initialization when agent first joins project
- Memory validation before phase transitions
- Memory backup before updates
- Memory analysis tools for spotting inconsistencies

---

## Troubleshooting

### Common Issues

**Issue: Agent doesn't remember previous contributions**
- Check if memory file exists and is being loaded
- Verify last_updated timestamp
- Check if phase section was properly populated

**Issue: Inconsistent positions across phases**
- Review cross_phase_context for evolution_of_thinking entries
- If no evolution documented, this may indicate a memory failure
- Agent should explicitly note when changing positions

**Issue: Memory file too large**
- This is unlikely in practice (even full 5-phase participation ~100KB)
- If it occurs, consider archiving older projects

**Issue: Conflicting entries**
- Use last_updated timestamp to determine most recent
- Check schema_version for compatibility

---

## Future Enhancements

### Potential Features (Not in v1.0)

1. **Memory Consolidation:** Automatic summarization of older phases
2. **Cross-Project Learning:** Shared memory references between projects
3. **Memory Search:** Full-text search across all agent memories
4. **Memory Visualization:** Graph of positions, alliances, conflicts
5. **Memory Validation:** Automated consistency checking
6. **Memory Analytics:** Pattern detection across agents and phases

---

## Example Usage in Phase Workflows

### Phase 2 Voting Example

```markdown
**Council Director to PA-01:**
"Please vote on the effectiveness of Policy X: AI Dividend for Workers.

Before voting, review your memory:
- Your Phase 1 research on worker ownership models
- Your stated priority on wealth distribution
- Your core positions on AI benefits sharing

Cast your vote with reasoning that builds on your previous work."

**PA-01 Response (with memory):**
"Vote: YES

Reasoning: This aligns with my Phase 1 proposal for 'AI Data Dividend'
and my consistent position that AI productivity gains must flow to workers,
not just capital owners. My Phase 1 research on Alaska's oil dividend
provides a precedent. I support this policy for effectiveness."
```

### Phase 3 Refinement Example

```markdown
**PA-01 Contribution (with memory):**
"During Phase 2, I voted YES on this policy and argued for strong
worker protections (see Phase 2 arguments_made). For refinement,
I recommend:

1. Add sunset clause - consistent with my cross_phase position on
   policy experiments
2. Increase dividend percentage - my Phase 2 dissent noted the
   original was too modest
3. Include worker board representation - builds on my Phase 1
   'Worker Ownership Stakes' idea

These refinements address my Phase 2 concerns while maintaining
my support for the core policy."
```

---

## Version History

**Version 1.0** (December 2025)
- Initial schema design
- Support for all 5 phases
- Cross-phase context tracking
- Metadata and analytics support

---

*Schema Version: 1.0*
*Last Updated: December 2025*
*Maintained by: Policy Council Development Team*
