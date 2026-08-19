import streamlit as st
from utils.styling import NAV_ITEMS, HOME_PATH

st.set_page_config(
    page_title="Assemble | Employee Voice Platform",
    page_icon="🟢",
    layout="wide",
    initial_sidebar_state="expanded",
)

home_page = st.Page(HOME_PATH, title="Home", icon="🏠", default=True)

pages_by_key = {item["key"]: st.Page(item["path"], title=item["title"], icon=item["icon"])
                for item in NAV_ITEMS}

pg = st.navigation(
    {
        "Overview": [home_page],
        "Community & Growth": [
            pages_by_key["engineering"],
            pages_by_key["culture"],
            pages_by_key["women"],
        ],
        "Voice & Insights": [
            pages_by_key["speakup"],
            pages_by_key["survey"],
            pages_by_key["dashboard"],
        ],
    }
)

pg.run()
