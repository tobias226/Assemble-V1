import streamlit as st
import pandas as pd
from datetime import datetime
from utils.styling import apply_style, page_header, footer, back_to_home
from utils.data_generator import get_survey_participation, get_enps_trend, init_session_stores

apply_style()
init_session_stores()
back_to_home()

page_header(
    "Monthly Survey",
    "Two minutes a month — your input directly shapes what leadership prioritises next.",
    icon="📋",
)

part = get_survey_participation()
enps = get_enps_trend()
c1, c2, c3 = st.columns(3)
c1.metric("This month's participation", f"{int(part['Participation Rate (%)'].iloc[-1])}%")
c2.metric("Current eNPS", int(enps["eNPS"].iloc[-1]))
c3.metric("Surveys completed (you)", len(st.session_state.survey_submissions))

st.write("")
tab_survey, tab_history = st.tabs(["🖊️ Take This Month's Survey", "📈 Your Participation History"])

with tab_survey:
    with st.form("monthly_survey_form", clear_on_submit=True):
        st.markdown("##### Engagement")
        q1 = st.slider("I feel motivated to do great work here", 1, 5, 3, help="1 = Strongly disagree, 5 = Strongly agree")
        q2 = st.slider("I would recommend this organisation as a great place to work", 1, 5, 3)

        st.markdown("##### Wellbeing")
        q3 = st.slider("My current workload feels manageable", 1, 5, 3)
        q4 = st.radio("How would you rate your work-life balance this month?",
                       ["Excellent", "Good", "Fair", "Poor"], horizontal=True)

        st.markdown("##### Voice & Inclusion")
        q5 = st.slider("I feel comfortable raising concerns at work", 1, 5, 3)
        q6 = st.multiselect(
            "Which support would help you most right now?",
            ["Flexible hours", "Mental health support", "Career development", "Manager support",
             "Better tools/resources", "Recognition", "None right now"],
        )

        st.markdown("##### In your own words")
        q7 = st.text_area("Anything you'd like leadership to know this month? (optional)", height=120)

        submitted = st.form_submit_button("Submit Survey")

    if submitted:
        st.session_state.survey_submissions.append({
            "Submitted": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Motivation": q1, "Recommend": q2, "Workload": q3,
            "Work-Life Balance": q4, "Voice Comfort": q5,
            "Support Needed": ", ".join(q6) if q6 else "None selected",
            "Comment Provided": "Yes" if q7.strip() else "No",
        })
        st.success("Thank you — your response has been recorded confidentially and rolled into this month's aggregate results.")
        st.balloons()

with tab_history:
    if st.session_state.survey_submissions:
        st.dataframe(pd.DataFrame(st.session_state.survey_submissions), use_container_width=True, hide_index=True)
    else:
        st.caption("You haven't submitted a survey this session yet. Your responses will appear here once submitted.")

    st.markdown("---")
    st.markdown("#### Organisation-wide participation trend")
    st.line_chart(part.set_index("Month"))

footer()
