# Run: python3 test_core.py   (also works with pytest)
from matcher import detect_skills
from analyzer import analyze_gap
from roadmap import build_roadmap
from parser import extract_text
from report import build_report
from roles import ROLES


def test_no_substring_false_positives():
    text = "Happy, excellent person; interest in rapid input, storage, average html. CV attached."
    assert detect_skills(text) == {}


def test_detects_and_negation():
    found = detect_skills("Built REST APIs with FastAPI and PostgreSQL. I have never used Docker. Know Python.")
    assert {"apis", "sql", "python"} <= found.keys()
    assert "docker" not in found
    assert "python" in detect_skills("No Java. Python daily.")
    assert "PostgreSQL" in found["sql"]


def test_scoring_and_partial():
    weights = ROLES["data_analyst"]["skills"]
    assert analyze_gap("data_analyst", set(weights))["readiness"] == 100
    assert analyze_gap("data_analyst", set())["readiness"] == 0
    r = analyze_gap("data_analyst", {"tableau"})
    assert r["partial"]["power_bi"] == "tableau"          # Tableau gives half credit for Power BI
    assert "power_bi" not in r["missing"]
    assert r["readiness"] == round((4 + 5 / 2 + 2 / 2 + 4 / 2) / sum(weights.values()) * 100)


def test_roadmap_prereqs_first_and_adds_missing_prereqs():
    road = build_roadmap(["mlops", "python"], set(), {"mlops": 2, "python": 5})
    assert "machine_learning" in road and "statistics" in road and "probability" in road
    for skill, pre in [("mlops", "machine_learning"), ("machine_learning", "statistics"),
                       ("statistics", "probability"), ("mlops", "python")]:
        assert road.index(pre) < road.index(skill)
    # among ready skills, heavier first
    assert build_roadmap(["sql", "excel", "git"], set(), {"sql": 5, "excel": 5, "git": 3})[-1] == "git"


def test_parser_and_report():
    assert "Python" in extract_text("cv.TXT", b"Python")
    r = analyze_gap("data_analyst", {"sql"})
    md = build_report("Data Analyst", r, ["excel"], {"sql"}, {"excel"}, {"sql": "SQL daily"})
    assert "Overall readiness" in md and "Excel" in md and "✅" in md


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
