# roadmap.py
from prerequisites import PREREQS

PHASES = ["Foundation", "Core", "Advanced"]


def build_roadmap(missing, have, weights=None):
    """
    missing: list/set of skill IDs the user needs to learn
    have: set of skill IDs the user already has
    weights: {skill_id: importance}; among skills that are ready to learn, heavier ones come first
    Returns skills ordered so prerequisites always come first. Unmet prerequisites
    outside the role (e.g. machine_learning for mlops) are added as their own steps.
    """
    weights = weights or {}
    have = set(have)

    remaining = set()
    todo = list(missing)
    while todo:
        skill = todo.pop()
        if skill not in remaining and skill not in have:
            remaining.add(skill)
            todo.extend(PREREQS.get(skill, []))

    ordered = []
    satisfied = set(have)        # already-known skills count as done
    while remaining:
        ready = [s for s in remaining if all(p in satisfied for p in PREREQS.get(s, []))]
        if not ready:
            # cycle in PREREQS — append the rest by weight rather than loop forever
            ordered.extend(sorted(remaining, key=lambda s: -weights.get(s, 0)))
            break
        skill = max(ready, key=lambda s: (weights.get(s, 0), s))
        ordered.append(skill)
        satisfied.add(skill)
        remaining.remove(skill)

    return ordered


def phase_of(skill, have):
    """Foundation = nothing left to learn first, Core = one level of unmet prerequisites, Advanced = deeper."""
    def depth(s):
        unmet = [p for p in PREREQS.get(s, []) if p not in have]
        return 0 if not unmet else 1 + max(depth(p) for p in unmet)
    return PHASES[min(depth(skill), 2)]
