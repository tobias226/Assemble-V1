import streamlit as st
from utils.styling import apply_style, page_header, footer, GREEN
from utils.data_generator import (
    get_turnover_trend, get_engagement_heatmap, init_session_stores
)

st.set_page_config(
    page_title="Assemble | Employee Voice Platform",
    page_icon="🟢",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_style(active="home")
init_session_stores()

# ---------------------------------------------------------------- Hero ----
st.markdown(
    """
    <div class="assemble-tag">ESG · People &amp; Culture Prototype</div>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    f"""
    <h1 style="border:none; font-size:2.6rem; margin-bottom:0;">Assemble</h1>
    <p style="color:#A9B4AD; font-size:1.15rem; max-width:760px;">
        A single digital home for employee voice, community connection and
        workforce risk monitoring &mdash; built to help the organisation listen,
        act, and stay accountable.
    </p>
    """,
    unsafe_allow_html=True,
)
st.write("")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Active Employees on Platform", "1,842", "+3.1% MoM")
with col2:
    turnover = get_turnover_trend()
    st.metric("Current Turnover Rate", f"{turnover['Turnover Rate (%)'].iloc[-1]}%",
              f"{round(turnover['Turnover Rate (%)'].iloc[-1] - turnover['Turnover Rate (%)'].iloc[-2], 1)} pts")
with col3:
    heat = get_engagement_heatmap()
    st.metric("Avg. Engagement Score", f"{heat.values.mean():.0f}/100", "+1.4 pts")

st.write("")
st.write("")

# ---------------------------------------------------------- Nav cards -----
st.markdown("### Explore Assemble")
st.caption("Jump into any module below, or use the sidebar to navigate.")

cards = [
    ("🔧", "Engineering Exchange", "Trade technical skills, find a mentor, and join peer-led learning sprints.",
     "pages/1_Engineering_Exchange.py"),
    ("🌍", "Culture Connect", "Find and join communities that reflect your background, language and interests.",
     "pages/2_Culture_Connect.py"),
    ("🌸", "Women in Motion", "Mentorship, events and resources for the women's network.",
     "pages/3_Women_in_Motion.py"),
    ("🗣️", "Speak Up", "Raise a concern confidentially — you'll always be heard, never identified without consent.",
     "pages/4_Speak_Up.py"),
    ("📋", "Monthly Survey", "Two minutes a month to help shape how the organisation listens and responds.",
     "pages/5_Monthly_Survey.py"),
    ("📊", "Management Dashboard", "Live view of turnover, engagement and risk signals for leaders.",
     "pages/6_Management_Dashboard.py"),
]

for row_start in range(0, len(cards), 3):
    row = cards[row_start:row_start + 3]
    cols = st.columns(3)
    for col, (icon, title, desc, target) in zip(cols, row):
        with col:
            st.markdown(
                f"""
                <div class="assemble-card">
                    <h3>{icon} {title}</h3>
                    <p>{desc}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.page_link(target, label=f"Open {title}", icon="👉")
            st.write("")

st.write("")
st.markdown("---")

st.markdown(
    f"""
    <div style="background:#141B16; border:1px solid #24312A; border-radius:14px; padding:1.2rem 1.5rem;">
        <b style="color:{GREEN};">About this prototype</b><br>
        <span style="color:#A9B4AD; font-size:0.92rem;">
        Assemble is a concept platform demonstrating how ESG-aligned employee
        listening tools — skills exchange, cultural communities, women's
        network, confidential reporting, pulse surveys and a management
        dashboard — can live under one roof. All figures shown are
        simulated for demonstration purposes and no real personal data is
        collected or stored.
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)

footer()
