
from roles import ROLES

def analyze_gap(role_id, user_skills):
    required = ROLES[role_id]["skills"]   # {skill_id: weight}

    have = set()
    missing = set()

    for skill_id in required:
        if skill_id in user_skills:
            have.add(skill_id)
        else:
            missing.add(skill_id)

    total_weight = sum(required.values())
    have_weight = sum(required[s] for s in have)
    readiness = round(have_weight / total_weight * 100)

    ranked_missing = sorted(missing, key=lambda s: required[s], reverse=True)

    return {
        "have": have,
        "missing": missing,
        "ranked_missing": ranked_missing,
        "readiness": readiness,
    }
