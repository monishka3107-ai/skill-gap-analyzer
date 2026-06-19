# app.py
# Skill Gap Analyzer — run with:  python3 -m streamlit run app.py
import streamlit as st

from skills import SKILLS
from roles import ROLES
from matcher import detect_skills
from analyzer import analyze_gap
from roadmap import build_roadmap
from resources import RESOURCES


def nice(skill_id):
    return SKILLS.get(skill_id, {}).get("name", skill_id)


# Emoji icon per skill category — quick visual scanning
CATEGORY_ICON = {
    "Programming": "💻",
    "Data Handling": "🧹",
    "Statistics": "📊",
    "Visualization": "📈",
    "Machine Learning": "🤖",
    "AI / GenAI": "🧠",
    "Deployment & Infra": "☁️",
    "Soft Skills": "💬",
}

def icon_for(skill_id):
    cat = SKILLS.get(skill_id, {}).get("category", "")
    return CATEGORY_ICON.get(cat, "✦")


st.set_page_config(page_title="Skill Gap Analyzer", page_icon="🗺️", layout="centered")

# ---------------- Styling: hand-drawn notebook theme ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@500;700&family=Nunito:wght@400;600;700;800&display=swap');

/* Paper + graph-paper grid (the subtle background "features") */
.stApp {
    background-color: #FCFBF7;
    background-image:
        linear-gradient(rgba(40,48,61,0.045) 1px, transparent 1px),
        linear-gradient(90deg, rgba(40,48,61,0.045) 1px, transparent 1px);
    background-size: 26px 26px;
    font-family: 'Nunito', sans-serif;
    color: #28303D;
}
.block-container { max-width: 760px; }

/* Headings */
h1 { font-family: 'Caveat', cursive !important; font-weight: 700 !important;
     font-size: 3.4rem !important; color: #28303D !important; margin-bottom: 0 !important; }
h2, h3 { font-family: 'Nunito', sans-serif !important; font-weight: 800 !important;
     color: #28303D !important; letter-spacing: -0.01em; }
p, label, .stMarkdown { color: #3a4150; }

/* Hand-drawn squiggle under the title */
.squiggle { margin: 2px 0 6px 2px; }

/* Floating doodle sparkles */
.doodles { position: fixed; inset: 0; pointer-events: none; z-index: 0; }
.doodles .d { position: absolute; opacity: 0.5; animation: float 6s ease-in-out infinite; }
.doodles .d1 { top: 110px; right: 6%; animation-delay: 0s; }
.doodles .d2 { top: 240px; left: 4%; animation-delay: 1.2s; }
.doodles .d3 { bottom: 90px; right: 10%; animation-delay: 2.1s; }
@keyframes float { 0%,100% { transform: translateY(0) rotate(0); } 50% { transform: translateY(-10px) rotate(6deg); } }

/* Inputs: sketchy outlined look */
div[data-baseweb="select"] > div,
.stTextArea textarea {
    background: #FFFFFF !important;
    border: 2px solid #28303D !important;
    border-radius: 14px !important;
    color: #28303D !important;
    box-shadow: 3px 3px 0 rgba(40,48,61,0.12);
    transition: box-shadow 0.2s ease, transform 0.2s ease;
}
.stTextArea textarea:focus,
div[data-baseweb="select"] > div:focus-within {
    box-shadow: 4px 4px 0 #19B8A6 !important;
}

/* Analyze button: sticker / marker style */
.stButton > button {
    background: #FF7A66;
    color: #fff;
    border: 2px solid #28303D;
    border-radius: 14px;
    padding: 0.5rem 1.7rem;
    font-family: 'Nunito', sans-serif; font-weight: 800;
    box-shadow: 4px 4px 0 #28303D;
    transition: transform 0.12s ease, box-shadow 0.12s ease;
}
.stButton > button:hover { transform: translate(-2px,-2px); box-shadow: 6px 6px 0 #28303D; }
.stButton > button:active { transform: translate(2px,2px); box-shadow: 1px 1px 0 #28303D; }

/* Readiness meter — sketchy bar */
.ready-wrap { display:flex; align-items:center; gap:16px; margin: 4px 0 8px; }
.ready-num { font-family:'Caveat',cursive; font-weight:700; font-size:2.8rem; color:#19B8A6; line-height:1; }
.ready-track { flex:1; height:18px; background:#fff; border:2px solid #28303D;
    border-radius:999px; overflow:hidden; box-shadow:3px 3px 0 rgba(40,48,61,0.12); }
.ready-fill { height:100%; background:repeating-linear-gradient(45deg,#19B8A6,#19B8A6 8px,#2ec9b7 8px,#2ec9b7 16px);
    width:var(--w); animation: grow 0.9s ease-out both; }
@keyframes grow { from { width:0; } to { width:var(--w); } }

/* Roadmap as a path: dashed line + step bubbles */
.path { position:relative; margin-left: 6px; padding-left: 30px; }
.path::before { content:""; position:absolute; left:12px; top:6px; bottom:6px;
    border-left: 3px dashed #c9b8d8; }
.card { position:relative; background:#fff; border:2px solid #28303D; border-radius:16px;
    padding:14px 18px; margin-bottom:18px; box-shadow:4px 4px 0 rgba(40,48,61,0.14);
    animation: pop 0.45s ease both; transition: transform 0.2s ease, box-shadow 0.2s ease; }
.card:hover { transform: translate(-2px,-3px); box-shadow:7px 8px 0 rgba(25,184,166,0.35); }
.card .bub { position:absolute; left:-30px; top:14px; width:28px; height:28px; border-radius:50%;
    background:#FFE08A; border:2px solid #28303D; display:flex; align-items:center; justify-content:center;
    font-weight:800; font-size:0.85rem; color:#28303D; }
.card .step { font-weight:800; font-size:1.08rem; color:#28303D; }
.card .meta { color:#54606f; font-size:0.92rem; margin-top:6px; line-height:1.55; }
.card .meta b { color:#28303D; }
@keyframes pop { from { opacity:0; transform: translateY(14px) scale(0.98); } to { opacity:1; transform: translateY(0) scale(1); } }

/* "Have" chips: highlighter style */
.chip { display:inline-block; background:#FFE08A; border:2px solid #28303D;
    color:#28303D; font-weight:700; padding:3px 12px; border-radius:999px;
    font-size:0.85rem; margin:5px 6px 0 0; box-shadow:2px 2px 0 rgba(40,48,61,0.15); }

/* Respect reduced motion */
@media (prefers-reduced-motion: reduce) {
    .card, .ready-fill, .doodles .d, .block-container { animation: none !important; }
}
</style>

<!-- floating doodles -->
<div class="doodles">
  <svg class="d d1" width="46" height="46" viewBox="0 0 24 24" fill="none" stroke="#FF7A66" stroke-width="2" stroke-linecap="round"><path d="M12 2v6M12 16v6M2 12h6M16 12h6"/></svg>
  <svg class="d d2" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#6C5CE7" stroke-width="2" stroke-linecap="round"><path d="M12 2l2.4 7.4H22l-6 4.4 2.3 7.2L12 16.8 5.7 21l2.3-7.2-6-4.4h7.6z"/></svg>
  <svg class="d d3" width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#19B8A6" stroke-width="2" stroke-linecap="round"><path d="M3 12c4-6 14-6 18 0M6 12c2-3 10-3 12 0"/></svg>
</div>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.markdown("<h1>Skill Gap Analyzer</h1>", unsafe_allow_html=True)
st.markdown("""
<svg class="squiggle" width="320" height="14" viewBox="0 0 320 14" fill="none">
<path d="M2 8 Q 30 2, 60 8 T 120 8 T 180 8 T 240 8 T 318 8" stroke="#19B8A6" stroke-width="3" stroke-linecap="round"/>
</svg>
""", unsafe_allow_html=True)
st.write("Pick a target role, drop in your skills, and get a hand-drawn roadmap of what to learn next.")

# ---------------- Inputs ----------------
role_names = {ROLES[rid]["name"]: rid for rid in ROLES}
chosen_name = st.selectbox("Target role", list(role_names.keys()))
role_id = role_names[chosen_name]

user_text = st.text_area(
    "Your current skills (or paste resume text)",
    placeholder="e.g. I know Python, SQL and Excel...",
    height=140,
)

# ---------------- Run ----------------
if st.button("Analyze"):
    if not user_text.strip():
        st.warning("Add a few skills first so I have something to work with.")
    else:
        user_skills = detect_skills(user_text)
        result = analyze_gap(role_id, user_skills)

        st.subheader("How ready are you?")
        st.markdown(f"""
        <div class="ready-wrap">
          <div class="ready-num">{result['readiness']}%</div>
          <div class="ready-track"><div class="ready-fill" style="--w:{result['readiness']}%"></div></div>
        </div>
        """, unsafe_allow_html=True)

        st.subheader("Skills you already have")
        if result["have"]:
            chips = "".join(f"<span class='chip'>{icon_for(s)} {nice(s)}</span>" for s in result["have"])
            st.markdown(chips, unsafe_allow_html=True)
        else:
            st.markdown("<p>None detected yet — that's fine, everyone starts somewhere.</p>", unsafe_allow_html=True)

        st.subheader("Your learning roadmap")
        roadmap = build_roadmap(result["ranked_missing"], result["have"])

        if not roadmap:
            st.success("Nothing missing for this role — you're ready to apply. 🎉")
        else:
            st.markdown("<div class='path'>", unsafe_allow_html=True)
            for i, skill in enumerate(roadmap, 1):
                info = RESOURCES.get(skill, {})
                resource = info.get("resource", "No resource added yet.")
                project = info.get("project", "—")
                delay = (i - 1) * 0.06
                st.markdown(f"""
                <div class="card" style="animation-delay:{delay}s">
                    <div class="bub">{i}</div>
                    <div class="step">{icon_for(skill)} {nice(skill)}</div>
                    <div class="meta"><b>Learn with:</b> {resource}<br>
                    <b>Build this:</b> {project}</div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)