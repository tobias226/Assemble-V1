import streamlit as st
import pandas as pd
from utils.styling import apply_style, page_header, footer, back_to_home
from utils.data_generator import init_session_stores

apply_style()
init_session_stores()
back_to_home()

page_header(
    "Engineering Exchange",
    "Trade technical skills, learn from peers, and grow through hands-on knowledge sharing.",
    icon="🔧",
)

tab_learn, tab_mentors, tab_request = st.tabs(["📚 Learning Tracks", "🧑‍🤝‍🧑 Skill Mentors", "✍️ Request a Skill Swap"])

# ---------------------------------------------------------------- Tracks --
with tab_learn:
    st.markdown("#### Popular learning tracks this month")
    tracks = [
        ("Cloud Infrastructure Fundamentals", "Beginner", "4 weeks", "312 enrolled"),
        ("Advanced Python for Data Pipelines", "Intermediate", "6 weeks", "198 enrolled"),
        ("Sustainable Systems Design (ESG Eng.)", "Intermediate", "3 weeks", "146 enrolled"),
        ("Cybersecurity Essentials", "Beginner", "5 weeks", "271 enrolled"),
        ("Leading Technical Projects", "Advanced", "4 weeks", "89 enrolled"),
        ("Intro to Machine Learning", "Beginner", "6 weeks", "204 enrolled"),
    ]
    cols = st.columns(3)
    for i, (name, level, duration, enrolled) in enumerate(tracks):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div class="assemble-card">
                    <div class="assemble-tag">{level}</div>
                    <h3>{name}</h3>
                    <p>⏱ {duration} &nbsp;·&nbsp; 👥 {enrolled}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.button("Enrol", key=f"enrol_{i}", use_container_width=True)
            st.write("")

# --------------------------------------------------------------- Mentors --
with tab_mentors:
    st.markdown("#### Find a mentor by expertise")
    expertise = st.multiselect(
        "Filter by skill area",
        ["Cloud & DevOps", "Data Engineering", "Security", "Frontend", "Product Engineering", "Sustainability Tech"],
    )

    mentors = pd.DataFrame([
        {"Name": "A. Novak", "Role": "Principal Cloud Engineer", "Skill Area": "Cloud & DevOps", "Availability": "2 slots/wk"},
        {"Name": "S. Iyer", "Role": "Staff Data Engineer", "Skill Area": "Data Engineering", "Availability": "1 slot/wk"},
        {"Name": "M. Foster", "Role": "Security Architect", "Skill Area": "Security", "Availability": "3 slots/wk"},
        {"Name": "R. Adeyemi", "Role": "Frontend Lead", "Skill Area": "Frontend", "Availability": "2 slots/wk"},
        {"Name": "T. Nakamura", "Role": "Sustainability Systems Lead", "Skill Area": "Sustainability Tech", "Availability": "1 slot/wk"},
        {"Name": "L. García", "Role": "Product Engineering Manager", "Skill Area": "Product Engineering", "Availability": "2 slots/wk"},
    ])

    filtered = mentors[mentors["Skill Area"].isin(expertise)] if expertise else mentors
    st.dataframe(filtered, use_container_width=True, hide_index=True)
    st.caption("Select a mentor above, then use the request form in the next tab to reach out.")

# --------------------------------------------------------------- Request --
with tab_request:
    st.markdown("#### Request a skill swap or mentoring session")
    with st.form("skill_request_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            skill_offered = st.text_input("A skill you can offer / teach")
            skill_wanted = st.text_input("A skill you'd like to learn")
        with c2:
            preferred_format = st.selectbox("Preferred format", ["1:1 mentoring", "Small group swap", "Async / async review", "Workshop"])
            time_commitment = st.select_slider("Time you can commit weekly", options=["30 min", "1 hr", "2 hrs", "3+ hrs"])
        notes = st.text_area("Anything else to add?", placeholder="Optional context for your match...")
        submitted = st.form_submit_button("Submit Request")

    if submitted:
        st.session_state.skill_requests.append({
            "offered": skill_offered, "wanted": skill_wanted,
            "format": preferred_format, "commitment": time_commitment, "notes": notes,
        })
        st.success("Your skill exchange request has been logged. The Engineering Exchange team will match you within 5 working days.")

    if st.session_state.skill_requests:
        with st.expander(f"Your submitted requests this session ({len(st.session_state.skill_requests)})"):
            st.table(pd.DataFrame(st.session_state.skill_requests))

footer()
