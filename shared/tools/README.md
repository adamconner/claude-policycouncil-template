# AI Policy Council - Vote Tallying Tools

Automated vote tallying system for processing votes from 24 agents across 6 different weighting schemes.

## Overview

The AI Policy Council uses **6 distinct voting schemes** to evaluate policies from different perspectives:

1. **Effectiveness Vote** - Equal weight (all agents: 1.0) - Total: 24.0 points
2. **Compromise Vote** - Equal weight (all agents: 1.0) - Total: 24.0 points
3. **Progressive/Liberal Sort** - Weighted by progressive alignment - Total: 32.0 points
4. **Conservative Sort** - Weighted by conservative alignment - Total: 31.0 points
5. **Pro-Innovation Sort** - Weighted by innovation alignment - Total: 26.5 points
6. **Pro-Safety Sort** - Weighted by safety alignment - Total: 27.5 points

This tool automates the complex mathematical calculations required to tally votes across all 6 schemes simultaneously.

## Files

- **`vote_tally.py`** - Main Python script for vote tallying
- **`vote_input_template.json`** - Template for vote input files
- **`README.md`** - This documentation file

## Installation

No external dependencies required! Uses Python 3 standard library only.

**Requirements:**
- Python 3.7 or higher

## Quick Start

### 1. Create a Vote Input File

Copy and customize the template:

```bash
cp vote_input_template.json my_vote.json
```

Edit `my_vote.json` with actual votes:

```json
{
  "policy_id": "P001",
  "policy_name": "Your Policy Name",
  "votes": {
    "PA-01": {
      "vote": "for",
      "reasoning": "Your reasoning here",
      "confidence": "high"
    },
    ...
  }
}
```

### 2. Run the Tally

**Output to console:**
```bash
python vote_tally.py my_vote.json
```

**Save to file:**
```bash
python vote_tally.py my_vote.json results/my_vote_results.md
```

### 3. Review Results

The script generates a comprehensive markdown report with:
- Quick summary table across all 6 schemes
- Detailed vote-by-vote breakdowns for each scheme
- Weighted scores and percentages
- Consensus level indicators

## Vote Input Format

### Required Fields

```json
{
  "policy_id": "P001",              // Policy identifier
  "policy_name": "Policy Name",     // Human-readable name
  "votes": {                        // Agent votes (see below)
    "PA-01": { ... },
    ...
  }
}
```

### Vote Object Format

Each agent vote should include:

```json
"PA-01": {
  "vote": "for",           // Required: "for", "against", or "abstain"
  "reasoning": "...",      // Required: 1-2 sentence explanation
  "confidence": "high"     // Optional: "high", "medium", or "low"
}
```

**Valid vote values:**
- `"for"`, `"yes"`, `"y"` → Counted as FOR
- `"against"`, `"no"`, `"n"` → Counted as AGAINST
- `"abstain"`, `"a"` → Counted as ABSTAIN
- Missing agents → Counted as ABSENT (not included in totals)

### All 24 Agent IDs

**Policy Analysts (PA-01 to PA-16):**
- PA-01, PA-02, PA-03, PA-04, PA-05, PA-06, PA-07, PA-08
- PA-09, PA-10, PA-11, PA-12, PA-13, PA-14, PA-15, PA-16

**Specialist Agents (SA-01 to SA-08):**
- SA-01, SA-02, SA-03, SA-04, SA-05, SA-06, SA-07, SA-08

## Output Format

### Quick Summary Table

The report begins with a summary table showing results across all 6 schemes:

```
| Scheme | Total Possible | For | % | Against | % | Abstain | % | Result |
|--------|----------------|-----|---|---------|---|---------|---|--------|
| Type 1: Effectiveness Vote | 24.0 | 18.5 | 77.1% | 4.5 | 18.8% | 1.0 | 4.2% | ✓ Strong |
```

### Detailed Results Per Scheme

For each voting scheme, the report includes:

1. **Vote record header** with scheme name and weighting type
2. **Individual votes table** with:
   - Agent ID and name
   - Weight for that scheme
   - Vote (FOR/AGAINST/ABSTAIN)
   - Weighted score
   - Confidence level
   - Reasoning
3. **Summary** with:
   - Total possible points
   - For/Against/Abstain totals and percentages
   - Consensus level indicator

### Consensus Levels

- **✓ UNANIMOUS SUPPORT** - 100% (all votes FOR)
- **✓ STRONG CONSENSUS** - 75%+ support
- **✓ MODERATE SUPPORT** - 50-75% support
- **~ LIMITED SUPPORT** - 25-50% support
- **✗ MINIMAL SUPPORT** - <25% support

## Examples

### Example 1: Basic Usage

```bash
# Create vote file
cat > my_vote.json << 'EOF'
{
  "policy_id": "P042",
  "policy_name": "AI Safety Board",
  "votes": {
    "PA-01": {"vote": "for", "reasoning": "Protects workers"},
    "PA-02": {"vote": "for", "reasoning": "Progressive priority"},
    ...
  }
}
EOF

# Run tally
python vote_tally.py my_vote.json output/p042_tally.md

# View results
cat output/p042_tally.md
```

### Example 2: Batch Processing

```bash
# Tally multiple votes
for file in votes/*.json; do
  basename=$(basename "$file" .json)
  python vote_tally.py "$file" "results/${basename}_tally.md"
done
```

### Example 3: Quick Console Check

```bash
# See results immediately without saving
python vote_tally.py votes/p001.json | less
```

## Weighting Schemes Detail

### Type 1 & 2: Equal Weight (Effectiveness & Compromise)

All 24 agents have weight = 1.0
- Total possible: 24.0 points
- Used for: Objective effectiveness and bipartisan compromise

### Type 3: Progressive/Liberal Sort

Highest weights:
- PA-01 (Economic Populist): 3.0
- PA-02 (Liberal/Progressive): 3.0
- PA-12 (Civil Rights): 2.5

Total possible: 32.0 points

### Type 4: Conservative Sort

Highest weights:
- PA-06 (Economic Conservative): 3.0
- PA-07 (Nationalist Conservative): 3.0
- PA-11 (Finance): 2.5

Total possible: 31.0 points

### Type 5: Pro-Innovation Sort

Highest weights:
- PA-08 (Industry): 3.0
- PA-10 (Innovation Advocate): 3.0
- PA-11 (Finance): 2.5

Total possible: 26.5 points

### Type 6: Pro-Safety Sort

Highest weights:
- PA-09 (Safety/Risk Advocate): 3.0
- PA-12 (Civil Rights): 2.5
- PA-13 (Labor), PA-14 (Consumer), PA-15 (Environment): 2.0 each

Total possible: 27.5 points

## Technical Details

### Script Capabilities

- ✅ Reads JSON vote input
- ✅ Validates agent IDs
- ✅ Applies all 6 weighting schemes automatically
- ✅ Calculates weighted scores per agent
- ✅ Computes totals and percentages
- ✅ Determines consensus levels
- ✅ Generates markdown output
- ✅ Handles missing votes (marked as ABSENT)
- ✅ Flexible vote syntax (for/yes/y, against/no/n, abstain/a)

### Error Handling

- Invalid JSON → Error message with line number
- Missing file → Clear file not found error
- Invalid agent IDs → Silently ignored (allows partial votes)
- Invalid vote values → Treated as ABSENT

### Performance

- Processes 24 agents × 6 schemes = 144 calculations instantly
- Suitable for batch processing hundreds of votes
- No external dependencies = zero setup time

## Integration with Council Workflow

### Recommended Directory Structure

```
project/
├── votes/               # Input vote files
│   ├── p001_vote.json
│   ├── p002_vote.json
│   └── ...
├── results/            # Output tally reports
│   ├── p001_tally.md
│   ├── p002_tally.md
│   └── ...
└── shared/
    └── tools/          # This directory
        ├── vote_tally.py
        ├── vote_input_template.json
        └── README.md
```

### Workflow Steps

1. **Phase 2: Voting** - Collect votes from all 24 agents
2. **Create JSON** - Format votes using template
3. **Run Tally** - Execute script to generate results
4. **Review** - Analyze results across all 6 schemes
5. **Document** - Include tally report in phase deliverables

## Troubleshooting

### "File not found" error
- Check file path is correct
- Use absolute paths or run from correct directory

### "Invalid JSON" error
- Validate JSON syntax at jsonlint.com
- Check for missing commas, quotes, or brackets
- Ensure proper UTF-8 encoding

### Incorrect totals
- Verify all agent IDs are correct (PA-01 to PA-16, SA-01 to SA-08)
- Check vote values are valid ("for", "against", "abstain")
- Confirm you're using the correct weighting scheme

### Missing agents in output
- Script includes all 24 agents in output
- Missing votes shown as ABSENT
- This is expected behavior

## Advanced Usage

### Custom Output Formatting

Modify `vote_tally.py` to customize:
- Table column order
- Summary statistics
- Consensus thresholds
- Output styling

### Programmatic Integration

```python
from vote_tally import load_vote_data, tally_votes, WEIGHT_SCHEMES

# Load votes
vote_data = load_vote_data('my_vote.json')

# Tally specific scheme
for_total, against_total, abstain_total, details = tally_votes(
    vote_data['votes'],
    'progressive'
)

# Use results programmatically
print(f"Progressive support: {for_total:.1f}/{WEIGHT_SCHEMES['progressive']['total_possible']:.1f}")
```

## Support

For questions or issues:
1. Review this README
2. Check `/home/user/claude-agents/shared/config/voting_rules.md` for voting rules
3. Examine `vote_input_template.json` for format examples
4. Contact AI Policy Council Director

## Version History

- **v1.0** (2024-12-23) - Initial release
  - All 6 voting schemes implemented
  - Comprehensive markdown output
  - Template and documentation

## License

This tool is part of the AI Policy Council project.
See repository LICENSE for details.

---

*AI Policy Council - Automated Vote Tallying System*
*Ensuring transparent, consistent, and accurate vote counting across all schemes*
