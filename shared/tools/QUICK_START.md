# Vote Tally Quick Start

## 🚀 Run a Vote Tally in 30 Seconds

```bash
# 1. Copy template
cp vote_input_template.json my_vote.json

# 2. Edit votes (use your editor)
nano my_vote.json

# 3. Run tally
python vote_tally.py my_vote.json my_results.md

# Done! Check my_results.md for comprehensive results
```

## 📊 What You Get

- **All 6 voting schemes** automatically calculated
- **Quick summary table** showing results at-a-glance
- **Detailed breakdowns** for each scheme with:
  - Individual agent votes
  - Weighted scores
  - Percentages and totals
  - Consensus level indicators

## 💡 Example Vote

```json
{
  "policy_id": "P042",
  "policy_name": "AI Safety Oversight Board",
  "votes": {
    "PA-01": {"vote": "for", "reasoning": "Protects workers from AI displacement"},
    "PA-06": {"vote": "against", "reasoning": "Excessive regulatory burden"}
  }
}
```

## 🎯 All 6 Schemes

1. **Effectiveness** (24.0 pts) - Equal weight
2. **Compromise** (24.0 pts) - Equal weight
3. **Progressive** (32.0 pts) - Progressive-weighted
4. **Conservative** (31.0 pts) - Conservative-weighted
5. **Innovation** (26.5 pts) - Innovation-weighted
6. **Safety** (27.5 pts) - Safety-weighted

## 📖 Full Documentation

See `README.md` for complete documentation including:
- All 24 agent IDs
- Weight schemes detail
- Advanced usage
- Troubleshooting

---

**Need help?** Check [README.md](README.md) or [voting_rules.md](../config/voting_rules.md)
