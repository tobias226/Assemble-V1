import streamlit as st
import pandas as pd
from utils.styling import apply_style, page_header, footer

st.set_page_config(page_title="Culture Connect | Assemble", page_icon="🌍", layout="wide")
apply_style(active="culture")

page_header(
    "Culture Connect",
    "Find community, celebrate heritage, and connect with colleagues who share your background and interests.",
    icon="🌍",
)

tab_groups, tab_events, tab_spotlight = st.tabs(["👥 Community Groups", "📅 Upcoming Events", "✨ Member Spotlight"])

with tab_groups:
    st.markdown("#### Browse community groups")
    search = st.text_input("Search groups", placeholder="e.g. Diaspora, Language, Faith, Heritage...")

    groups = [
        ("African & Caribbean Network", "612 members", "Heritage & culture-sharing sessions, monthly socials."),
        ("Asian Professionals Circle", "784 members", "Lunar New Year events, mentoring, language exchange."),
        ("Latinx Connect", "398 members", "Community meetups, Spanish/Portuguese conversation clubs."),
        ("South Asian Collective", "530 members", "Festival celebrations, cultural cooking nights."),
        ("LGBTQ+ Allies & Community", "441 members", "Safe space discussions, Pride events, allyship training."),
        ("Faith & Belief Network", "276 members", "Interfaith dialogue, prayer room access, holiday calendars."),
        ("Global Languages Club", "509 members", "Weekly practice circles across 12 languages."),
        ("Neurodiversity Community", "233 members", "Peer support, workplace adjustments guidance."),
    ]
    filtered = [g for g in groups if search.lower() in g[0].lower()] if search else groups

    cols = st.columns(2)
    for i, (name, members, desc) in enumerate(filtered):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class="assemble-card">
                    <div class="assemble-tag">{members}</div>
                    <h3>{name}</h3>
                    <p>{desc}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.button("Join Group", key=f"join_{i}", use_container_width=True)
            st.write("")

with tab_events:
    st.markdown("#### Upcoming community events")
    events = pd.DataFrame([
        {"Date": "2026-08-28", "Event": "Lunar Heritage Cooking Night", "Group": "Asian Professionals Circle", "Location": "HQ Kitchen / Virtual"},
        {"Date": "2026-09-04", "Event": "Interfaith Dialogue Lunch", "Group": "Faith & Belief Network", "Location": "Level 3 Lounge"},
        {"Date": "2026-09-12", "Event": "Latin Rhythms Social", "Group": "Latinx Connect", "Location": "Rooftop Terrace"},
        {"Date": "2026-09-19", "Event": "Language Exchange Circle", "Group": "Global Languages Club", "Location": "Virtual"},
        {"Date": "2026-09-25", "Event": "Diaspora Stories Panel", "Group": "African & Caribbean Network", "Location": "Auditorium"},
    ])
    st.dataframe(events, use_container_width=True, hide_index=True)
    st.button("➕ Propose a New Event")

with tab_spotlight:
    st.markdown("#### This month's member spotlight")
    st.markdown(
        """
        <div class="assemble-card">
            <div class="assemble-tag">Community Story</div>
            <h3>"Assemble helped me find my people in a new country."</h3>
            <p>A member of the South Asian Collective shares how joining a cultural
            group in their first month made the office feel like home — from festival
            celebrations to finding a language-practice buddy.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.caption("Spotlight stories are illustrative examples for this prototype.")

footer()
