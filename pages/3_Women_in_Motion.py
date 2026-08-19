import streamlit as st
import pandas as pd
from utils.styling import apply_style, page_header, footer
from utils.data_generator import get_diversity_snapshot

st.set_page_config(page_title="Women in Motion | Assemble", page_icon="🌸", layout="wide")
apply_style(active="women")

page_header(
    "Women in Motion",
    "A network for connection, mentorship and advancement — supporting women at every career stage.",
    icon="🌸",
)

snap = get_diversity_snapshot()
c1, c2, c3, c4 = st.columns(4)
c1.metric("Women in Workforce", f"{snap['Women in Workforce (%)']}%")
c2.metric("Women in Leadership", f"{snap['Women in Leadership (%)']}%")
c3.metric("Network Members", f"{snap['Employee Resource Group Members']}")
c4.metric("Avg. Tenure", f"{snap['Avg. Tenure (yrs)']} yrs")

st.write("")
tab_mentorship, tab_events, tab_resources = st.tabs(["🤝 Mentorship Program", "📅 Events", "📚 Resources"])

with tab_mentorship:
    st.markdown("#### Join the mentorship program")
    st.markdown(
        """
        <div class="assemble-card">
            <h3>How it works</h3>
            <p>Get matched with a mentor or become one yourself. Programs run in
            12-week cohorts with structured check-ins, goal-setting and a closing
            showcase session.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    role = st.radio("I would like to join as a:", ["Mentee", "Mentor", "Both"], horizontal=True)
    focus = st.multiselect(
        "Areas of interest",
        ["Career progression", "Technical leadership", "Returning from leave", "Negotiation & pay equity",
         "Executive presence", "Work-life integration", "Starting in management"],
    )
    if st.button("Submit Interest"):
        st.success(f"Thanks! You've registered interest as a {role.lower()}. The Women in Motion team will follow up within 2 weeks.")

with tab_events:
    st.markdown("#### Upcoming events")
    events = pd.DataFrame([
        {"Date": "2026-08-26", "Event": "Executive Presence Workshop", "Format": "In-person"},
        {"Date": "2026-09-03", "Event": "Returning from Leave Circle", "Format": "Virtual"},
        {"Date": "2026-09-10", "Event": "Negotiation & Pay Equity Talk", "Format": "Hybrid"},
        {"Date": "2026-09-18", "Event": "Women in Engineering Panel", "Format": "In-person"},
        {"Date": "2026-09-30", "Event": "Quarterly Networking Mixer", "Format": "In-person"},
    ])
    st.dataframe(events, use_container_width=True, hide_index=True)

with tab_resources:
    st.markdown("#### Resource library")
    resources = [
        ("Career Progression Playbook", "Guide to promotion readiness and sponsorship."),
        ("Returning from Parental Leave Toolkit", "Practical guidance for a smooth transition back."),
        ("Pay Equity & Negotiation Guide", "Know your worth — preparation and scripts."),
        ("Confidence & Executive Presence Series", "Short video series with senior leaders."),
    ]
    cols = st.columns(2)
    for i, (title, desc) in enumerate(resources):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class="assemble-card">
                    <h3>{title}</h3>
                    <p>{desc}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.write("")

footer()
