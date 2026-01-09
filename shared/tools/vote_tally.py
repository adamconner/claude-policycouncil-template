#!/usr/bin/env python3
"""
AI Policy Council - Automated Vote Tallying System

This script processes votes from 24 agents across 6 different weighting schemes
and generates markdown-formatted results matching the official vote documentation format.

Author: AI Policy Council
Version: 1.0
"""

import json
import sys
from typing import Dict, List, Tuple
from pathlib import Path


# Agent definitions
AGENTS = {
    "PA-01": {"name": "Economic Populist", "type": "Policy Analyst"},
    "PA-02": {"name": "Liberal/Progressive", "type": "Policy Analyst"},
    "PA-03": {"name": "Center-Left", "type": "Policy Analyst"},
    "PA-04": {"name": "Centrist/Pragmatist", "type": "Policy Analyst"},
    "PA-05": {"name": "Center-Right", "type": "Policy Analyst"},
    "PA-06": {"name": "Economic Conservative", "type": "Policy Analyst"},
    "PA-07": {"name": "Nationalist Conservative", "type": "Policy Analyst"},
    "PA-08": {"name": "Industry Representative", "type": "Policy Analyst"},
    "PA-09": {"name": "Safety/Risk Advocate", "type": "Policy Analyst"},
    "PA-10": {"name": "Innovation Advocate", "type": "Policy Analyst"},
    "PA-11": {"name": "Finance/Wall Street", "type": "Policy Analyst"},
    "PA-12": {"name": "Civil Rights/Equity", "type": "Policy Analyst"},
    "PA-13": {"name": "Organized Labor", "type": "Policy Analyst"},
    "PA-14": {"name": "Consumer Advocacy", "type": "Policy Analyst"},
    "PA-15": {"name": "Environmental/Sustainability", "type": "Policy Analyst"},
    "PA-16": {"name": "Small Business", "type": "Policy Analyst"},
    "SA-01": {"name": "Legislative Counsel", "type": "Specialist"},
    "SA-02": {"name": "Legal Counsel", "type": "Specialist"},
    "SA-03": {"name": "Supreme Court Analyst", "type": "Specialist"},
    "SA-04": {"name": "Fact Checker", "type": "Specialist"},
    "SA-05": {"name": "Citations Agent", "type": "Specialist"},
    "SA-06": {"name": "Polling Expert", "type": "Specialist"},
    "SA-07": {"name": "Federal Budget Expert", "type": "Specialist"},
    "SA-08": {"name": "Implementation Expert", "type": "Specialist"},
}


# Weight schemes for all 6 voting types
WEIGHT_SCHEMES = {
    "effectiveness": {
        "name": "Type 1: Effectiveness Vote",
        "description": "Equal Weight",
        "total_possible": 24.0,
        "weights": {agent_id: 1.0 for agent_id in AGENTS.keys()}
    },
    "compromise": {
        "name": "Type 2: Compromise Vote",
        "description": "Equal Weight",
        "total_possible": 24.0,
        "weights": {agent_id: 1.0 for agent_id in AGENTS.keys()}
    },
    "progressive": {
        "name": "Type 3: Progressive/Liberal Sort",
        "description": "Progressive-Weighted",
        "total_possible": 32.0,
        "weights": {
            "PA-01": 3.0, "PA-02": 3.0, "PA-03": 2.0, "PA-04": 1.0,
            "PA-05": 0.5, "PA-06": 0.5, "PA-07": 0.5, "PA-08": 1.0,
            "PA-09": 1.5, "PA-10": 0.5, "PA-11": 0.5, "PA-12": 2.5,
            "PA-13": 2.0, "PA-14": 1.5, "PA-15": 2.0, "PA-16": 1.0,
            "SA-01": 1.0, "SA-02": 1.0, "SA-03": 1.0, "SA-04": 1.0,
            "SA-05": 1.0, "SA-06": 1.0, "SA-07": 1.0, "SA-08": 1.0,
        }
    },
    "conservative": {
        "name": "Type 4: Conservative Sort",
        "description": "Conservative-Weighted",
        "total_possible": 31.0,
        "weights": {
            "PA-01": 1.5, "PA-02": 0.5, "PA-03": 0.5, "PA-04": 1.0,
            "PA-05": 2.0, "PA-06": 3.0, "PA-07": 3.0, "PA-08": 2.0,
            "PA-09": 0.5, "PA-10": 1.5, "PA-11": 2.5, "PA-12": 0.5,
            "PA-13": 0.5, "PA-14": 1.0, "PA-15": 0.5, "PA-16": 2.0,
            "SA-01": 1.0, "SA-02": 1.0, "SA-03": 1.0, "SA-04": 1.0,
            "SA-05": 1.0, "SA-06": 1.0, "SA-07": 1.0, "SA-08": 1.0,
        }
    },
    "innovation": {
        "name": "Type 5: Pro-Innovation Sort",
        "description": "Innovation-Weighted",
        "total_possible": 26.5,
        "weights": {
            "PA-01": 0.5, "PA-02": 0.5, "PA-03": 0.5, "PA-04": 1.0,
            "PA-05": 1.5, "PA-06": 1.5, "PA-07": 0.5, "PA-08": 3.0,
            "PA-09": 0.5, "PA-10": 3.0, "PA-11": 2.5, "PA-12": 0.5,
            "PA-13": 0.5, "PA-14": 0.5, "PA-15": 0.5, "PA-16": 1.5,
            "SA-01": 1.0, "SA-02": 1.0, "SA-03": 1.0, "SA-04": 1.0,
            "SA-05": 1.0, "SA-06": 1.0, "SA-07": 1.0, "SA-08": 1.0,
        }
    },
    "safety": {
        "name": "Type 6: Pro-Safety Sort",
        "description": "Safety-Weighted",
        "total_possible": 27.5,
        "weights": {
            "PA-01": 0.5, "PA-02": 1.5, "PA-03": 1.5, "PA-04": 1.0,
            "PA-05": 0.5, "PA-06": 0.5, "PA-07": 0.5, "PA-08": 0.5,
            "PA-09": 3.0, "PA-10": 0.5, "PA-11": 0.5, "PA-12": 2.5,
            "PA-13": 2.0, "PA-14": 2.0, "PA-15": 2.0, "PA-16": 0.5,
            "SA-01": 1.0, "SA-02": 1.0, "SA-03": 1.0, "SA-04": 1.0,
            "SA-05": 1.0, "SA-06": 1.0, "SA-07": 1.0, "SA-08": 1.0,
        }
    }
}


def load_vote_data(file_path: str) -> Dict:
    """Load vote data from JSON file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{file_path}': {e}", file=sys.stderr)
        sys.exit(1)


def calculate_weighted_score(vote: str, weight: float) -> float:
    """Calculate weighted score for a vote."""
    vote_lower = vote.lower()
    if vote_lower in ["for", "yes", "y"]:
        return weight
    elif vote_lower in ["against", "no", "n"]:
        return 0.0
    elif vote_lower in ["abstain", "a"]:
        return 0.0
    else:
        return 0.0


def tally_votes(votes: Dict, scheme_key: str) -> Tuple[float, float, float, List[Dict]]:
    """
    Tally votes for a specific weighting scheme.

    Returns:
        (for_total, against_count, abstain_count, detailed_results)
    """
    scheme = WEIGHT_SCHEMES[scheme_key]
    weights = scheme["weights"]

    for_total = 0.0
    against_total = 0.0
    abstain_total = 0.0
    detailed_results = []

    for agent_id in sorted(AGENTS.keys()):
        agent_info = AGENTS[agent_id]
        weight = weights[agent_id]

        # Get vote data
        vote_data = votes.get(agent_id, {})
        vote = vote_data.get("vote", "ABSENT").upper()
        reasoning = vote_data.get("reasoning", "No reasoning provided")
        confidence = vote_data.get("confidence", "").upper()

        # Normalize vote
        if vote in ["FOR", "YES", "Y"]:
            vote_normalized = "FOR"
            weighted_score = weight
            for_total += weight
        elif vote in ["AGAINST", "NO", "N"]:
            vote_normalized = "AGAINST"
            weighted_score = 0.0
            against_total += weight
        elif vote in ["ABSTAIN", "A"]:
            vote_normalized = "ABSTAIN"
            weighted_score = 0.0
            abstain_total += weight
        else:
            vote_normalized = "ABSENT"
            weighted_score = 0.0
            # Don't count absent in any total

        detailed_results.append({
            "agent_id": agent_id,
            "name": agent_info["name"],
            "weight": weight,
            "vote": vote_normalized,
            "weighted_score": weighted_score,
            "reasoning": reasoning,
            "confidence": confidence
        })

    return for_total, against_total, abstain_total, detailed_results


def format_markdown_table(detailed_results: List[Dict], scheme_key: str) -> str:
    """Format results as markdown table."""
    scheme = WEIGHT_SCHEMES[scheme_key]

    lines = []
    lines.append(f"## VOTE RECORD: {{policy_name}}")
    lines.append("")
    lines.append(f"### Vote Type: {scheme['name']}")
    lines.append(f"### Weighting Scheme: {scheme['description']}")
    lines.append("")
    lines.append("### Individual Votes")
    lines.append("")
    lines.append("| Agent | Perspective | Weight | Vote | Weighted Score | Confidence | Reasoning |")
    lines.append("|-------|-------------|--------|------|----------------|------------|-----------|")

    for result in detailed_results:
        confidence_str = result['confidence'] if result['confidence'] else "-"
        lines.append(
            f"| {result['agent_id']} | {result['name']} | "
            f"{result['weight']:.1f} | {result['vote']} | "
            f"{result['weighted_score']:.1f} | {confidence_str} | "
            f"{result['reasoning']} |"
        )

    return "\n".join(lines)


def format_summary(for_total: float, against_total: float, abstain_total: float,
                   scheme_key: str) -> str:
    """Format vote summary."""
    scheme = WEIGHT_SCHEMES[scheme_key]
    total_possible = scheme["total_possible"]

    for_pct = (for_total / total_possible) * 100
    against_pct = (against_total / total_possible) * 100
    abstain_pct = (abstain_total / total_possible) * 100

    lines = []
    lines.append("")
    lines.append("### Summary")
    lines.append(f"- **Total Possible:** {total_possible:.1f}")
    lines.append(f"- **For:** {for_total:.1f} ({for_pct:.1f}%)")
    lines.append(f"- **Against:** {against_total:.1f} ({against_pct:.1f}%)")
    lines.append(f"- **Abstain:** {abstain_total:.1f} ({abstain_pct:.1f}%)")
    lines.append("")

    # Consensus level
    if for_pct >= 100:
        lines.append("**Result:** ✓ UNANIMOUS SUPPORT")
    elif for_pct >= 75:
        lines.append("**Result:** ✓ STRONG CONSENSUS")
    elif for_pct >= 50:
        lines.append("**Result:** ✓ MODERATE SUPPORT")
    elif for_pct >= 25:
        lines.append("**Result:** ~ LIMITED SUPPORT")
    else:
        lines.append("**Result:** ✗ MINIMAL SUPPORT")

    return "\n".join(lines)


def generate_all_schemes_report(vote_data: Dict) -> str:
    """Generate a comprehensive report across all 6 voting schemes."""
    policy_id = vote_data.get("policy_id", "UNKNOWN")
    policy_name = vote_data.get("policy_name", "Unknown Policy")
    votes = vote_data.get("votes", {})

    lines = []
    lines.append("# COMPREHENSIVE VOTE TALLY")
    lines.append(f"## Policy: {policy_name} ({policy_id})")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Quick summary table across all schemes
    lines.append("## Quick Summary - All Voting Schemes")
    lines.append("")
    lines.append("| Scheme | Total Possible | For | % | Against | % | Abstain | % | Result |")
    lines.append("|--------|----------------|-----|---|---------|---|---------|---|--------|")

    summary_data = []
    for scheme_key in ["effectiveness", "compromise", "progressive", "conservative", "innovation", "safety"]:
        for_total, against_total, abstain_total, _ = tally_votes(votes, scheme_key)
        scheme = WEIGHT_SCHEMES[scheme_key]
        total = scheme["total_possible"]
        for_pct = (for_total / total) * 100
        against_pct = (against_total / total) * 100
        abstain_pct = (abstain_total / total) * 100

        if for_pct >= 75:
            result = "✓ Strong"
        elif for_pct >= 50:
            result = "✓ Moderate"
        elif for_pct >= 25:
            result = "~ Limited"
        else:
            result = "✗ Minimal"

        summary_data.append({
            "name": scheme["name"],
            "total": total,
            "for": for_total,
            "for_pct": for_pct,
            "against": against_total,
            "against_pct": against_pct,
            "abstain": abstain_total,
            "abstain_pct": abstain_pct,
            "result": result
        })

        lines.append(
            f"| {scheme['name']} | {total:.1f} | {for_total:.1f} | {for_pct:.1f}% | "
            f"{against_total:.1f} | {against_pct:.1f}% | {abstain_total:.1f} | {abstain_pct:.1f}% | {result} |"
        )

    lines.append("")
    lines.append("---")
    lines.append("")

    # Detailed results for each scheme
    for scheme_key in ["effectiveness", "compromise", "progressive", "conservative", "innovation", "safety"]:
        for_total, against_total, abstain_total, detailed_results = tally_votes(votes, scheme_key)

        lines.append("")
        lines.append("---")
        lines.append("")

        table = format_markdown_table(detailed_results, scheme_key)
        table = table.replace("{policy_name}", policy_name)
        lines.append(table)

        summary = format_summary(for_total, against_total, abstain_total, scheme_key)
        lines.append(summary)

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"*Generated by AI Policy Council Automated Vote Tallying System*")

    return "\n".join(lines)


def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python vote_tally.py <vote_input.json> [output.md]")
        print("")
        print("Example:")
        print("  python vote_tally.py votes/policy_p001.json")
        print("  python vote_tally.py votes/policy_p001.json results/p001_tally.md")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    # Load vote data
    vote_data = load_vote_data(input_file)

    # Generate report
    report = generate_all_schemes_report(vote_data)

    # Output results
    if output_file:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w') as f:
            f.write(report)
        print(f"✓ Vote tally complete! Results written to: {output_file}")
    else:
        print(report)

    # Also print quick summary to stderr for easy viewing
    policy_name = vote_data.get("policy_name", "Unknown Policy")
    print(f"\n✓ Tallied votes for: {policy_name}", file=sys.stderr)


if __name__ == "__main__":
    main()
