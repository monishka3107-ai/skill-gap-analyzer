import re

from skills import SKILLS

# shortcut: negation is only checked in the 4 words before a match, upgrade to an NLP parser if users hit misses
NEGATION = re.compile(r"\b(no|not|never|without|lack|lacking|don't|dont|haven't|havent)\b")


def detect_skills(text):
    """Returns {skill_id: evidence snippet} for every skill mentioned positively in text."""
    lower = text.lower()
    found = {}

    for skill_id, data in SKILLS.items():
        for alias in data["aliases"]:
            # whole-word match: "py" must not hit "happy", "rag" must not hit "storage"
            pattern = r"(?<![a-z0-9])" + re.escape(alias) + r"(?![a-z0-9])"
            for m in re.finditer(pattern, lower):
                sentence_start = max(lower.rfind(c, 0, m.start()) for c in ".\n;!?") + 1
                before = lower[sentence_start:m.start()].split()[-4:]
                if NEGATION.search(" ".join(before)):
                    continue
                found[skill_id] = " ".join(text[max(0, m.start() - 40):m.end() + 40].split())
                break
            if skill_id in found:
                break

    return found
