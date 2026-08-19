import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from utils.styling import apply_style, page_header, footer, back_to_home, GREEN, PANEL, TEXT, TEXT_MUTED
from utils.data_generator import (
    get_turnover_trend, get_engagement_heatmap, get_headcount_by_dept,
    get_diversity_snapshot, get_speakup_breakdown, get_survey_participation,
    get_enps_trend, DEPARTMENTS,
)

apply_style()
back_to_home()

page_header(
    "Management Dashboard",
    "Workforce risk and engagement signals for leadership. All figures are simulated demo data.",
    icon="📊",
)

# ------------------------------------------------------------- Filters ----
with st.sidebar:
    st.markdown("### Dashboard Filters")
    dept_filter = st.multiselect("Departments", DEPARTMENTS, default=DEPARTMENTS)
    st.caption("Filters apply to the engagement heatmap and headcount chart below.")

turnover = get_turnover_trend()
heatmap_df = get_engagement_heatmap()
headcount = get_headcount_by_dept()
diversity = get_diversity_snapshot()
speakup = get_speakup_breakdown()
participation = get_survey_participation()
enps = get_enps_trend()

if dept_filter:
    heatmap_df = heatmap_df.loc[dept_filter]
    headcount = headcount[headcount["Department"].isin(dept_filter)]

# ---------------------------------------------------------------- KPIs ----
k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Turnover Rate", f"{turnover['Turnover Rate (%)'].iloc[-1]}%",
          f"{round(turnover['Turnover Rate (%)'].iloc[-1] - turnover['Turnover Rate (%)'].iloc[-2], 1)} pts")
k2.metric("Avg. Engagement", f"{heatmap_df.values.mean():.0f}/100")
k3.metric("eNPS", int(enps["eNPS"].iloc[-1]))
k4.metric("Survey Participation", f"{int(participation['Participation Rate (%)'].iloc[-1])}%")
k5.metric("Speak Up Reports (12mo)", int(speakup["Reports (last 12 months)"].sum()))

st.write("")

# ---------------------------------------------------------- Row 1 charts --
col_left, col_right = st.columns([1.3, 1])

with col_left:
    st.markdown("#### Employee Turnover Trend")
    fig = px.line(
        turnover, x="Month", y="Turnover Rate (%)", markers=True,
    )
    fig.update_traces(line_color=GREEN, marker=dict(size=7, color=GREEN))
    fig.update_layout(
        plot_bgcolor=PANEL, paper_bgcolor=PANEL,
        font=dict(color=TEXT), margin=dict(l=10, r=10, t=10, b=10),
        xaxis=dict(gridcolor="#24312A"), yaxis=dict(gridcolor="#24312A"),
        height=340,
    )
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.markdown("#### Diversity Snapshot")
    for label, value in diversity.items():
        st.metric(label, value)

st.write("")

# ------------------------------------------------------- Engagement heat --
st.markdown("#### Engagement Heatmap — Department x Month")
st.caption("Simulated engagement score (0–100) by department and month.")

fig2, ax = plt.subplots(figsize=(11, max(3, 0.55 * len(heatmap_df))))
fig2.patch.set_facecolor(PANEL)
ax.set_facecolor(PANEL)

cmap = sns.light_palette("#2ECC71", as_cmap=True)
sns.heatmap(
    heatmap_df, annot=True, fmt=".0f", cmap=cmap, cbar=True,
    linewidths=0.6, linecolor="#0B0F0D",
    annot_kws={"color": "#06110A", "fontsize": 9},
    ax=ax,
)
ax.tick_params(colors=TEXT, labelsize=9)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", color=TEXT)
plt.setp(ax.get_yticklabels(), rotation=0, color=TEXT)
cbar = ax.collections[0].colorbar
cbar.ax.yaxis.set_tick_params(color=TEXT)
plt.setp(plt.getp(cbar.ax.axes, "yticklabels"), color=TEXT)
fig2.tight_layout()

st.pyplot(fig2, use_container_width=True)

st.write("")

# --------------------------------------------------------- Row 3 charts --
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("#### Headcount by Department")
    fig3 = px.bar(headcount.sort_values("Headcount"), x="Headcount", y="Department", orientation="h")
    fig3.update_traces(marker_color=GREEN)
    fig3.update_layout(
        plot_bgcolor=PANEL, paper_bgcolor=PANEL, font=dict(color=TEXT),
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis=dict(gridcolor="#24312A"), yaxis=dict(gridcolor="#24312A"),
        height=360,
    )
    st.plotly_chart(fig3, use_container_width=True)

with col_b:
    st.markdown("#### Speak Up Reports by Category")
    fig4 = px.pie(speakup, names="Category", values="Reports (last 12 months)", hole=0.45)
    fig4.update_traces(marker=dict(colors=px.colors.sequential.Greens_r), textfont=dict(color="#06110A"))
    fig4.update_layout(
        plot_bgcolor=PANEL, paper_bgcolor=PANEL, font=dict(color=TEXT),
        margin=dict(l=10, r=10, t=10, b=10), height=360,
        legend=dict(font=dict(color=TEXT)),
    )
    st.plotly_chart(fig4, use_container_width=True)

st.write("")
st.markdown("#### eNPS &amp; Survey Participation Trend")
merged = turnover[["Month"]].copy()
merged["eNPS"] = enps["eNPS"]
merged["Survey Participation (%)"] = participation["Participation Rate (%)"]
fig5 = px.line(merged, x="Month", y=["eNPS", "Survey Participation (%)"], markers=True)
fig5.update_layout(
    plot_bgcolor=PANEL, paper_bgcolor=PANEL, font=dict(color=TEXT),
    margin=dict(l=10, r=10, t=10, b=10),
    xaxis=dict(gridcolor="#24312A"), yaxis=dict(gridcolor="#24312A"),
    legend=dict(font=dict(color=TEXT), title=""),
    height=340,
)
st.plotly_chart(fig5, use_container_width=True)

st.info("This dashboard uses simulated demo data. Connect a real data source (HRIS, survey platform, case management system) to make it production-ready.")

footer()
