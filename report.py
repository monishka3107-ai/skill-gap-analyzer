from datetime import date

from skills import SKILLS
from resources import RESOURCES
from roadmap import phase_of


def nice(skill_id):
    return SKILLS.get(skill_id, {}).get("name", skill_id)


def build_report(role_name, result, roadmap, have, done, evidence):
    """Markdown career analysis report."""
    lines = [
        f"# Career Analysis: {role_name}",
        f"_Generated {date.today().isoformat()}_",
        "",
        "## Readiness",
        f"- **Overall readiness:** {result['readiness']}%",
        f"- **Core skills (highest-weight):** {result['core']}%",
        f"- **Roadmap progress:** {len(done & set(roadmap))}/{len(roadmap)} steps done",
        "",
        "| Category | Score |",
        "|---|---|",
        *(f"| {cat} | {pct}% |" for cat, pct in result["by_category"].items()),
        "",
        "## Matched skills",
        *(f"- {nice(s)}" + (f" — _\"{evidence[s]}\"_" if s in evidence else "") for s in sorted(result["have"])),
        "",
        "## Partially matched skills",
        *(f"- {nice(s)} (related: {nice(b)})" for s, b in sorted(result["partial"].items())),
        "",
        "## Missing skills",
        *(f"- {nice(s)}" for s in result["ranked_missing"]),
        "",
        "## Learning roadmap",
    ]
    total = 0
    for i, s in enumerate(roadmap, 1):
        info = RESOURCES.get(s, {})
        total += info.get("hours", 0)
        lines += [
            f"### {i}. {nice(s)} {'✅' if s in done else ''}",
            f"- **Phase:** {phase_of(s, have)} · **Estimated:** ~{info.get('hours', '?')} h",
            f"- **Learn with:** {info.get('resource', 'No resource added yet.')}",
            f"- **Build this:** {info.get('project', '—')}",
            "",
        ]
    lines.append(f"**Total estimated time:** ~{total} hours")
    return "\n".join(lines)
