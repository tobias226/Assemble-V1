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
TEXT_MUTED = "#A9B4AD"
DANGER = "#E85D5D"
GOLD = "#D9B24C"

CARD_ICONS = {
    "engineering": "🔧",
    "culture": "🌍",
    "women": "🌸",
    "speakup": "🗣️",
    "survey": "📋",
    "dashboard": "📊",
}


def apply_style(active: str = ""):
    """Inject global CSS + page fade-in animation. Call once per page."""
    st.markdown(
        f"""
        <style>
        /* ---------- Fade-in transition for "seamless" page loads ---------- */
        .main .block-container {{
            animation: assembleFadeIn 0.55s ease-out;
        }}
        @keyframes assembleFadeIn {{
            0%   {{ opacity: 0; transform: translateY(10px); }}
            100% {{ opacity: 1; transform: translateY(0); }}
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

        /* ---------- Headings ---------- */
        h1, h2, h3 {{
            color: {TEXT} !important;
            letter-spacing: 0.3px;
        }}
        h1 {{
            border-bottom: 2px solid {GREEN};
            padding-bottom: 0.4rem;
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

        /* ---------- Cards ---------- */
        .assemble-card {{
            background: {PANEL};
            border: 1px solid #24312A;
            border-radius: 16px;
            padding: 1.4rem 1.4rem;
            transition: transform 0.2s ease, border 0.2s ease, box-shadow 0.2s ease;
            height: 100%;
        }}
        .assemble-card:hover {{
            transform: translateY(-4px);
            border: 1px solid {GREEN};
            box-shadow: 0 10px 30px rgba(46, 204, 113, 0.18);
        }}
        .assemble-card h3 {{
            margin-top: 0;
            color: {GREEN_MUTED} !important;
        }}
        .assemble-card p {{
            color: {TEXT_MUTED};
            font-size: 0.92rem;
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
            margin-bottom: 0.6rem;
        }}

        /* ---------- Metrics ---------- */
        div[data-testid="stMetric"] {{
            background: {PANEL};
            border: 1px solid #24312A;
            border-radius: 14px;
            padding: 1rem 1rem 0.6rem 1rem;
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
            border-color: #24312A !important;
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
            margin-bottom: 1rem;
        }}

        /* ---------- Footer ---------- */
        .assemble-footer {{
            margin-top: 3rem;
            padding-top: 1rem;
            border-top: 1px solid #24312A;
            color: {TEXT_MUTED};
            font-size: 0.8rem;
            text-align: center;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def page_header(title: str, subtitle: str = "", icon: str = ""):
    st.markdown(f"# {icon}  {title}" if icon else f"# {title}")
    if subtitle:
        st.markdown(f"<p style='color:{TEXT_MUTED}; font-size:1.05rem; margin-top:-0.6rem;'>{subtitle}</p>",
                     unsafe_allow_html=True)
    st.write("")


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
