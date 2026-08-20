import streamlit as st
from utils.styling import apply_style, footer, GREEN, TEXT_MUTED, NAV_ITEMS, nav_card
from utils.data_generator import (
    get_turnover_trend, get_engagement_heatmap, init_session_stores
)

apply_style()
init_session_stores()

# ---------------------------------------------------------------- Hero ----
st.markdown('<div class="assemble-tag">ESG · People &amp; Culture Prototype</div>', unsafe_allow_html=True)
st.markdown(
    f"""
    <h1 style="font-size:2.7rem; margin-bottom:0.5rem;">Assemble</h1>
    <p style="color:{TEXT_MUTED}; font-size:1.15rem; max-width:720px; line-height:1.65; font-weight:300;">
        Welcome. This is your home for employee voice, community connection
        and workforce wellbeing &mdash; everything below is one click away.
    </p>
    """,
    unsafe_allow_html=True,
)

st.write("")
st.write("")

# --------------------------------------------------------- Quick stats ----
with st.container(key="snapshot-section"):
    st.markdown('<div class="section-eyebrow">Overview</div>', unsafe_allow_html=True)
    st.markdown("#### Platform snapshot")
    st.write("")
    col1, col2, col3 = st.columns(3, gap="medium")
    with col1:
        st.metric("Active Employees on Platform", "1,842", "+3.1% MoM")
    with col2:
        turnover = get_turnover_trend()
        st.metric("Current Turnover Rate", f"{turnover['Turnover Rate (%)'].iloc[-1]}%",
                  f"{round(turnover['Turnover Rate (%)'].iloc[-1] - turnover['Turnover Rate (%)'].iloc[-2], 1)} pts")
    with col3:
        heat = get_engagement_heatmap()
        st.metric("Avg. Engagement Score", f"{heat.values.mean():.0f}/100", "+1.4 pts")

# ---------------------------------------------------------- Nav cards -----
with st.container(key="explore-section"):
    st.markdown('<div class="section-eyebrow">Modules</div>', unsafe_allow_html=True)
    st.markdown("#### Explore Assemble")
    st.markdown(
        f"<p style='color:{TEXT_MUTED}; margin-top:-0.4rem; margin-bottom:1.4rem; font-size:0.92rem;'>"
        "Jump into any module below, or use the sidebar to navigate anytime.</p>",
        unsafe_allow_html=True,
    )

    for row_start in range(0, len(NAV_ITEMS), 3):
        row = NAV_ITEMS[row_start:row_start + 3]
        cols = st.columns(3, gap="medium")
        for col, item in zip(cols, row):
            with col:
                nav_card(item["icon"], item["title"], item["desc"], item["path"], item["key"])
        st.write("")

# ---------------------------------------------------------------- About ---
with st.container(key="about-section"):
    st.markdown(
        f"""<b style="color:{GREEN}; font-size:1.0rem;">About this prototype</b><br><br>
        <span style="color:{TEXT_MUTED}; font-size:0.92rem; line-height:1.7;">
        Assemble is a concept platform demonstrating how ESG-aligned employee
        listening tools &mdash; skills exchange, cultural communities, a women's
        network, confidential reporting, pulse surveys and a management
        dashboard &mdash; can live under one roof. All figures shown are
        simulated for demonstration purposes and no real personal data is
        collected or stored.</span>""",
        unsafe_allow_html=True,
    )

footer()
