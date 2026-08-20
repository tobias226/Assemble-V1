"""
Shared styling for the Assemble platform.
Import and call apply_style() at the top of every page for a
consistent green/black corporate look and a smooth fade-in transition.
"""

import streamlit as st

# ---- Brand palette -----------------------------------------------------
BLACK = "#0B0F0D"
PANEL = "#141B16"
PANEL_LIGHT = "#1B241E"
GREEN = "#2ECC71"
GREEN_DARK = "#1B7A43"
GREEN_MUTED = "#8FD9AE"
TEXT = "#F2F4F1"
TEXT_MUTED = "#C9D3CD"
DANGER = "#E85D5D"
GOLD = "#D9B24C"

# Central place to register every page so nav + "back to home" buttons
# always point somewhere real and stay easy to update.
HOME_PATH = "home.py"

NAV_ITEMS = [
    {"key": "engineering", "icon": "🔧", "title": "Engineering Exchange",
     "path": "pages/1_Engineering_Exchange.py",
     "desc": "Trade technical skills, find a mentor, and join peer-led learning sprints."},
    {"key": "culture", "icon": "🌍", "title": "Culture Connect",
     "path": "pages/2_Culture_Connect.py",
     "desc": "Find and join communities that reflect your background, language and interests."},
    {"key": "women", "icon": "🌸", "title": "Women in Motion",
     "path": "pages/3_Women_in_Motion.py",
     "desc": "Mentorship, events and resources for the women's network."},
    {"key": "speakup", "icon": "🗣️", "title": "Speak Up",
     "path": "pages/4_Speak_Up.py",
     "desc": "Raise a concern confidentially — you'll always be heard, never identified without consent."},
    {"key": "survey", "icon": "📋", "title": "Monthly Survey",
     "path": "pages/5_Monthly_Survey.py",
     "desc": "Two minutes a month to help shape how the organisation listens and responds."},
    {"key": "dashboard", "icon": "📊", "title": "Management Dashboard",
     "path": "pages/6_Management_Dashboard.py",
     "desc": "Live view of turnover, engagement and risk signals for leaders."},
]


def apply_style():
    """Inject global CSS + page fade-in animation. Call once per page."""
    st.markdown(
        f"""
        <style>
        /* ---------- Fade-in transition for smooth page loads ---------- */
        .main .block-container {{
            animation: assembleFadeIn 0.45s ease-out;
            padding-top: 3rem !important;
            max-width: 1200px;
        }}
        @keyframes assembleFadeIn {{
            0%   {{ opacity: 0; transform: translateY(8px); }}
            100% {{ opacity: 1; transform: translateY(0); }}
        }}

        /* ---------- Fix: opaque top header so it never overlaps titles ---------- */
        header[data-testid="stHeader"] {{
            background: {BLACK} !important;
            border-bottom: 1px solid #24312A;
            height: 3.2rem;
        }}
        div[data-testid="stDecoration"] {{
            background: linear-gradient(90deg, {GREEN_DARK}, {GREEN}, {GREEN_DARK});
        }}
        div[data-testid="stToolbar"] {{
            right: 1rem;
        }}

        /* ---------- Base palette ---------- */
        html, body, [class*="css"] {{
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
        }}
        .stApp {{
            background: radial-gradient(circle at top left, {PANEL} 0%, {BLACK} 55%);
            color: {TEXT};
        }}

        /* ---------- Sidebar ---------- */
        section[data-testid="stSidebar"] {{
            background: linear-gradient(180deg, {BLACK} 0%, {PANEL} 100%);
            border-right: 1px solid {GREEN_DARK};
        }}
        section[data-testid="stSidebar"] * {{
            color: {TEXT} !important;
        }}
        /* Sidebar nav links */
        section[data-testid="stSidebar"] [data-testid="stPageLink"] {{
            border-radius: 8px;
            transition: background 0.15s ease;
        }}
        section[data-testid="stSidebar"] [data-testid="stPageLink"]:hover {{
            background: rgba(46, 204, 113, 0.10);
        }}

        /* ---------- Headings & spacing rhythm ---------- */
        h1, h2, h3 {{
            color: {TEXT} !important;
            letter-spacing: 0.3px;
        }}
        h1 {{
            border-bottom: none;
            padding-bottom: 0.3rem;
            margin-bottom: 0.5rem !important;
            font-weight: 650;
        }}
        h2, h3 {{
            margin-top: 1.6rem !important;
        }}
        .block-container div[data-testid="stVerticalBlock"] > div {{
            margin-bottom: 0.15rem;
        }}

        /* ---------- Buttons ---------- */
        .stButton > button, .stDownloadButton > button, .stFormSubmitButton > button {{
            background: linear-gradient(135deg, {GREEN} 0%, {GREEN_DARK} 100%);
            color: #06110A;
            font-weight: 600;
            border: none;
            border-radius: 10px;
            padding: 0.55rem 1.3rem;
            transition: transform 0.15s ease, box-shadow 0.15s ease;
            box-shadow: 0 2px 10px rgba(46, 204, 113, 0.15);
        }}
        .stButton > button:hover, .stDownloadButton > button:hover, .stFormSubmitButton > button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 18px rgba(46, 204, 113, 0.35);
        }}

        /* ---------- "Back to home" ghost button ---------- */
        .back-home-wrap [data-testid="stPageLink"] {{
            background: {PANEL};
            border: 1px solid #24312A;
            border-radius: 10px;
            padding: 0.3rem 0.8rem;
            width: fit-content;
        }}
        .back-home-wrap [data-testid="stPageLink"]:hover {{
            border: 1px solid {GREEN};
        }}

        /* ---------- Cards ---------- */
        .assemble-card {{
            background: rgba(27, 36, 30, 0.72);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border: 1px solid rgba(46, 204, 113, 0.14);
            border-radius: 18px;
            padding: 1.5rem 1.5rem;
            transition: transform 0.25s cubic-bezier(0.2, 0.8, 0.2, 1), border 0.25s ease, box-shadow 0.25s ease;
            height: 100%;
            display: flex;
            flex-direction: column;
        }}
        .assemble-card:hover {{
            transform: translateY(-5px);
            border: 1px solid rgba(46, 204, 113, 0.55);
            box-shadow: 0 16px 40px rgba(46, 204, 113, 0.16);
        }}
        .assemble-card h3 {{
            margin-top: 0 !important;
            color: {GREEN_MUTED} !important;
        }}
        .assemble-card p {{
            color: {TEXT_MUTED};
            font-size: 0.92rem;
            flex-grow: 1;
        }}
        .assemble-tag {{
            display: inline-block;
            background: rgba(46, 204, 113, 0.12);
            color: {GREEN};
            border: 1px solid {GREEN_DARK};
            border-radius: 999px;
            padding: 0.15rem 0.7rem;
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            margin-bottom: 0.7rem;
        }}

        /* ---------- Metrics ---------- */
        div[data-testid="stMetric"] {{
            background: rgba(27, 36, 30, 0.6);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(46, 204, 113, 0.12);
            border-radius: 16px;
            padding: 1.2rem 1.2rem 0.8rem 1.2rem;
        }}
        div[data-testid="stMetricLabel"] {{
            color: {TEXT_MUTED} !important;
        }}
        div[data-testid="stMetricValue"] {{
            color: {GREEN} !important;
        }}

        /* ---------- Inputs ---------- */
        .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div,
        .stNumberInput input {{
            background-color: {PANEL_LIGHT} !important;
            color: {TEXT} !important;
            border: 1px solid #2A362E !important;
            border-radius: 8px !important;
        }}

        /* ---------- Divider ---------- */
        hr {{
            border: none !important;
            height: 1px;
            background: linear-gradient(90deg, transparent, #2A3830 50%, transparent);
            margin: 2.4rem 0 !important;
        }}

        /* ---------- Section shading (Home page) ---------- */
        .section-eyebrow {{
            color: {GREEN_MUTED};
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 0.3rem;
        }}
        div[class*="st-key-snapshot-section"] {{
            background: linear-gradient(180deg, #12180F, #0F1512);
            border: 1px solid #1E2921;
            border-radius: 22px;
            padding: 1.9rem 2.1rem 1.5rem 2.1rem;
            margin-bottom: 2.2rem;
        }}
        div[class*="st-key-explore-section"] {{
            background: linear-gradient(180deg, #0D1310, #0A0E0C);
            border: 1px solid #1E2921;
            border-radius: 22px;
            padding: 2rem 2.1rem 1.6rem 2.1rem;
            margin-bottom: 2.2rem;
        }}
        div[class*="st-key-about-section"] {{
            background: {PANEL};
            border: 1px solid #24312A;
            border-radius: 18px;
            padding: 1.6rem 1.8rem;
        }}

        /* ---------- Alert boxes ---------- */
        div[data-testid="stAlert"] {{
            border-radius: 12px;
        }}

        /* ---------- Confidential banner ---------- */
        .confidential-banner {{
            background: linear-gradient(135deg, rgba(216,90,90,0.12), rgba(20,27,22,0.4));
            border: 1px solid {DANGER};
            border-radius: 14px;
            padding: 1rem 1.2rem;
            color: {TEXT};
            margin-bottom: 1.2rem;
        }}

        /* ---------- Footer ---------- */
        .assemble-footer {{
            margin-top: 3.5rem;
            padding-top: 1.2rem;
            border-top: 1px solid #24312A;
            color: {TEXT_MUTED};
            font-size: 0.8rem;
            text-align: center;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def back_to_home():
    """Small, consistent 'return to Home' link — call near the top of every page."""
    st.markdown('<div class="back-home-wrap">', unsafe_allow_html=True)
    st.page_link(HOME_PATH, label="Back to Home", icon="🔙")
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("")


def page_header(title: str, subtitle: str = "", icon: str = ""):
    st.markdown(f"# {icon}  {title}" if icon else f"# {title}")
    if subtitle:
        st.markdown(f"<p style='color:{TEXT_MUTED}; font-size:1.05rem; margin-top:0.1rem;'>{subtitle}</p>",
                     unsafe_allow_html=True)
    st.write("")


def nav_card(icon: str, title: str, desc: str, path: str, key: str):
    """Renders one clickable module card, used on the Home page grid."""
    st.markdown(
        f"""
        <div class="assemble-card">
            <h3>{icon} {title}</h3>
            <p>{desc}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.page_link(path, label=f"Open {title}", icon="👉")


def footer():
    st.markdown(
        f"""
        <div class="assemble-footer">
            Assemble &mdash; Employee Voice · Community Engagement · Workforce Risk Monitoring<br>
            Prototype build · All data shown is simulated for demonstration purposes only.
        </div>
        """,
        unsafe_allow_html=True,
    )
