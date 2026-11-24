import json
from pathlib import Path

# shortcut: one local file = one user on one machine, move to a database if the app is ever hosted for many users
PROGRESS_FILE = Path(__file__).with_name("progress.json")


def load():
    """Set of skill IDs the user has marked as completed."""
    try:
        return set(json.loads(PROGRESS_FILE.read_text()).get("done", []))
    except (FileNotFoundError, json.JSONDecodeError):
        return set()


def save(done):
    tmp = PROGRESS_FILE.with_suffix(".tmp")
    tmp.write_text(json.dumps({"done": sorted(done)}, indent=2))
    tmp.replace(PROGRESS_FILE)   # atomic, so a crash mid-write can't wipe saved progress
