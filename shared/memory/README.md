# Agent Memory System

## Overview

The Agent Memory System provides persistent context for policy analysts across all phases of policy development. This ensures analysts can:
- Remember their previous contributions
- Maintain ideological consistency
- Build on prior work
- Reference earlier positions when voting or debating
- Track evolution in their thinking

## Problem Solved

**Before Memory System:**
- PA-01 generates ideas in Phase 1
- PA-01 votes in Phase 2 but has "forgotten" their Phase 1 ideas
- Votes may contradict earlier positions
- Arguments don't reference prior work
- No continuity across phases

**With Memory System:**
- PA-01 generates ideas in Phase 1 and records them in memory
- PA-01 reviews memory before Phase 2 voting
- Votes reference Phase 1 ideas: "As I proposed in Phase 1..."
- Arguments build on earlier positions
- Full continuity and consistency

## Quick Start

### For New Analysts

1. **Phase 1 Start:** Copy `memory_template.json` to create your memory file
   ```bash
   cp shared/memory/memory_template.json \
      projects/[project]/memory/[your-id]_[project].json
   ```

2. **Update Basic Info:** Fill in agent_id, perspective, project_id

3. **Record as You Work:** After each phase, update your memory file

4. **Review Before Each Phase:** Read your memory before starting new work

### For Council Directors

1. **Phase Transitions:** Verify all analysts have updated memory files
2. **Task Assignments:** Remind analysts to review their memory
3. **Quality Checks:** Ensure votes/positions align with earlier work (or note evolution)

## Directory Structure

```
shared/memory/
├── README.md                    # This file
├── memory_schema.md             # Complete documentation
├── memory_template.json         # Template for new memory files
└── agents/                      # Shared agent memories (cross-project)
    └── [agent-id].json          # e.g., pa01.json

projects/[project]/memory/
└── [agent-id]_[project].json    # Project-specific memories
                                 # e.g., pa01_economic_prosperity.json
```

## Key Files

- **`memory_schema.md`** - Complete technical documentation of the memory format
- **`memory_template.json`** - Empty template to copy when creating new memory files
- **`agents/pa01_economic_prosperity.json`** - Example memory file showing realistic usage

## Memory File Sections

Each memory file contains:

1. **Agent Info:** ID, perspective, project
2. **Phase Records:** All contributions in each phase (ideas, votes, arguments, etc.)
3. **Cross-Phase Context:** Patterns, evolutions, compromises, dissents
4. **Metadata:** Stats and collaboration patterns

## Integration with Workflows

Memory system is integrated into phase workflows:

- **Phase 1:** Initialize memory, record ideas and research
- **Phase 2:** Review Phase 1 memory, record votes and arguments, note alliances
- **Phase 3:** Review Phase 1-2 memory, record refinement contributions
- **Phase 4:** Review all prior memory, record implementation reviews
- **Phase 5:** Review full memory, record rollout recommendations

See individual workflow files for specific memory instructions.

## Example Usage

**Phase 2 Voting with Memory:**

```
Council Director: "PA-01, please vote on 'AI Data Dividend' policy."

PA-01 (reviews memory):
- "I proposed this in Phase 1 (idea pa01-001)
- My rationale was: data is labor deserving compensation
- Vote: YES
- Reasoning: This is my own proposal from Phase 1. My research on
  Alaska oil dividend provides precedent. Consistent with my theme
  of redistributing AI gains."
```

**Phase 3 Refinement with Memory:**

```
PA-01 (reviews memory):
- Phase 1: I proposed data dividend idea
- Phase 2: I voted YES and proposed progressive payment amendment
- Phase 2: Amendment was accepted
- Phase 3: I should ensure progressive payment structure is preserved
  in refinement and address implementation challenges I noted
```

## Best Practices

### For Analysts

1. **Update promptly** after each phase completion
2. **Be specific** in recording reasoning and positions
3. **Note evolution** if your thinking changes
4. **Reference memory** explicitly when contributing
5. **Maintain consistency** with earlier positions (or explain changes)

### For Orchestrators

1. **Verify updates** at phase transitions
2. **Remind analysts** to review memory before new phases
3. **Check consistency** between memory and phase outputs
4. **Use memory** to identify patterns and insights

## Technical Notes

- **Format:** JSON (human-readable, programmatically accessible)
- **Schema Version:** 1.0 (included in each file for future compatibility)
- **Size:** Typical memory file is 50-150KB (even after all 5 phases)
- **Encoding:** UTF-8
- **Indentation:** 2 spaces for readability

## Support

- **Full Documentation:** See `memory_schema.md`
- **Example:** See `agents/pa01_economic_prosperity.json`
- **Template:** Use `memory_template.json` for new files

---

*Agent Memory System v1.0*
*December 2025*
