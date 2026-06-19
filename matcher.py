
from email.mime import text
from encodings.aliases import aliases

from skills import SKILLS

def detect_skills(text):
    text = text.lower()
    found = set()


    for skill_name, data in SKILLS.items():
        for alias in data["aliases"]:
            if alias in text:
                found.add(skill_name)
                break

    return found
