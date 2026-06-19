# roadmap.py
from prerequisites import PREREQS

def build_roadmap(missing, have):
    """
    missing: list/set of skill IDs the user needs to learn
    have: set of skill IDs the user already has
    Returns missing skills ordered so prerequisites always come first.
    """
    remaining = list(missing)
    ordered = []
    satisfied = set(have)        # already-known skills count as done

    while remaining:
        progress = False
        for skill in remaining:
            prereqs = PREREQS.get(skill, [])   # [] if skill has no prereqs

          
            if all(prereq in satisfied for prereq in prereqs):
                ordered.append(skill)
                satisfied.add(skill)
                remaining.remove(skill)
                progress = True
                break

        if not progress:
            # leftover skills had unmet prereqs (or a cycle) — just append them
            ordered.extend(remaining)
            break

    return ordered