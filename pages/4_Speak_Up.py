import streamlit as st
import uuid
import pandas as pd
from datetime import datetime
from utils.styling import apply_style, page_header, footer
from utils.data_generator import REPORT_CATEGORIES, init_session_stores

st.set_page_config(page_title="Speak Up | Assemble", page_icon="🗣️", layout="wide")
apply_style(active="speakup")
init_session_stores()

page_header(
    "Speak Up",
    "A confidential channel to raise concerns, ask questions, or report something that doesn't feel right.",
    icon="🗣️",
)

st.markdown(
    """
    <div class="confidential-banner">
        🔒 <b>Your confidentiality matters.</b> Reports can be submitted anonymously.
        If you choose to share contact details, they are only visible to the
        designated case handling team and are never shared with your line manager
        without your consent. Retaliation of any kind against someone who speaks up
        in good faith is a breach of policy.
    </div>
    """,
    unsafe_allow_html=True,
)

tab_report, tab_process, tab_history = st.tabs(["📝 Submit a Report", "ℹ️ How it works", "📁 My Submissions (this session)"])

with tab_report:
    with st.form("speakup_form", clear_on_submit=True):
        anonymous = st.toggle("Submit anonymously", value=True)

        c1, c2 = st.columns(2)
        with c1:
            category = st.selectbox("What is this concern about?", REPORT_CATEGORIES)
            date_occurred = st.date_input("When did this happen? (approximate is fine)")
        with c2:
            severity = st.select_slider("How urgent does this feel?", options=["Low", "Medium", "High", "Immediate risk"])
            location = st.text_input("Location / department (optional)")

        description = st.text_area(
            "Tell us what happened",
            placeholder="Share as much detail as you're comfortable with — dates, people involved (roles rather than names is fine), and what you've observed.",
            height=180,
        )

        contact_email = None
        if not anonymous:
            contact_email = st.text_input("Contact email (only used for case follow-up)")

        consent = st.checkbox("I understand this report will be reviewed by the confidential case handling team.")
        submitted = st.form_submit_button("Submit Report Confidentially")

    if submitted:
        if not description.strip():
            st.error("Please add a short description before submitting so the case team has something to act on.")
        elif not consent:
            st.error("Please confirm the consent checkbox to submit.")
        else:
            ref = str(uuid.uuid4())[:8].upper()
            st.session_state.speakup_reports.append({
                "Reference": ref,
                "Submitted": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "Category": category,
                "Severity": severity,
                "Anonymous": "Yes" if anonymous else "No",
            })
            st.success(
                f"Your report has been submitted confidentially. "
                f"**Reference number: {ref}** — save this to check on your case status later."
            )
            if severity == "Immediate risk":
                st.warning(
                    "You flagged this as an immediate risk. If anyone is in danger right now, "
                    "please also contact site security or emergency services directly."
                )

with tab_process:
    st.markdown("#### What happens after you submit")
    steps = [
        ("1. Acknowledged", "You'll receive a reference number immediately, whether or not you shared contact details."),
        ("2. Reviewed", "A trained, independent case handler reviews the report within 3 working days."),
        ("3. Investigated", "If needed, a fair and confidential investigation is opened. You'll be updated where possible."),
        ("4. Resolved", "Findings and any actions are recorded. Anonymised trends inform the risk dashboard."),
    ]
    cols = st.columns(4)
    for col, (title, desc) in zip(cols, steps):
        with col:
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
    st.info("Prefer to speak to someone directly? A confidential phone line and external ombudsperson option are also available through People & Culture.")

with tab_history:
    if st.session_state.speakup_reports:
        st.dataframe(pd.DataFrame(st.session_state.speakup_reports), use_container_width=True, hide_index=True)
    else:
        st.caption("No submissions yet this session. Anything you submit above will appear here with its reference number.")

footer()
