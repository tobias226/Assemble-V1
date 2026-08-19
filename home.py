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
    """
    <h1 style="border:none; font-size:2.6rem; margin-bottom:0.4rem;">Assemble</h1>
    <p style="color:#A9B4AD; font-size:1.15rem; max-width:720px; line-height:1.6;">
        Welcome. This is your home for employee voice, community connection
        and workforce wellbeing &mdash; everything below is one click away.
    </p>
    """,
    unsafe_allow_html=True,
)

st.write("")
st.write("")

# --------------------------------------------------------- Quick stats ----
st.markdown("### Platform snapshot")
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

st.divider()

# ---------------------------------------------------------- Nav cards -----
st.markdown("### Explore Assemble")
st.markdown(
    f"<p style='color:{TEXT_MUTED}; margin-top:-0.6rem; margin-bottom:1.4rem;'>"
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

st.divider()

# ---------------------------------------------------------------- About ---
st.markdown(
    f"""
    <div style="background:#141B16; border:1px solid #24312A; border-radius:14px; padding:1.4rem 1.6rem;">
        <b style="color:{GREEN}; font-size:1.02rem;">About this prototype</b><br><br>
        <span style="color:{TEXT_MUTED}; font-size:0.94rem; line-height:1.7;">
        Assemble is a concept platform demonstrating how ESG-aligned employee
        listening tools &mdash; skills exchange, cultural communities, a women's
        network, confidential reporting, pulse surveys and a management
        dashboard &mdash; can live under one roof. All figures shown are
        simulated for demonstration purposes and no real personal data is
        collected or stored.
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)

footer()
