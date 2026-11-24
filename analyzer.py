
from roles import ROLES
from skills import SKILLS, RELATED


def analyze_gap(role_id, user_skills):
    required = ROLES[role_id]["skills"]   # {skill_id: weight}

    have = set()
    partial = {}    # {skill_id: related skill the user has}
    missing = set()

    for skill_id in required:
        if skill_id in user_skills:
            have.add(skill_id)
        else:
            bridge = next((r for r in RELATED.get(skill_id, []) if r in user_skills), None)
            if bridge:
                partial[skill_id] = bridge
            else:
                missing.add(skill_id)

    def score(skills):
        total = sum(required[s] for s in skills)
        got = sum(required[s] for s in skills if s in have) + sum(required[s] / 2 for s in skills if s in partial)
        return round(got / total * 100) if total else 100

    by_category = {}
    for s in required:
        by_category.setdefault(SKILLS.get(s, {}).get("category", "Other"), []).append(s)

    ranked_missing = sorted(missing, key=lambda s: required[s], reverse=True)

    return {
        "have": have,
        "partial": partial,
        "missing": missing,
        "ranked_missing": ranked_missing,
        "readiness": score(required),
        "core": score([s for s in required if required[s] == 5]),
        "by_category": {cat: score(skills) for cat, skills in by_category.items()},
    }
