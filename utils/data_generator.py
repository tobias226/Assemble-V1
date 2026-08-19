"""
Generates consistent, seeded dummy data for the Assemble prototype.
No real employee data is used anywhere in this app.
"""

import numpy as np
import pandas as pd
import streamlit as st

DEPARTMENTS = [
    "Engineering", "Operations", "Sales", "Customer Success",
    "People & Culture", "Finance", "Product", "Legal & Compliance",
]

MONTHS = pd.date_range(end=pd.Timestamp.today(), periods=12, freq="MS").strftime("%b %Y")

REPORT_CATEGORIES = [
    "Harassment / Bullying", "Discrimination", "Health & Safety",
    "Ethics / Fraud", "Management Conduct", "Wellbeing Concern", "Other",
]


@st.cache_data
def get_turnover_trend(seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    base = 12.5
    values = base + np.cumsum(rng.normal(0, 0.6, len(MONTHS)))
    values = np.clip(values, 6, 20)
    return pd.DataFrame({"Month": MONTHS, "Turnover Rate (%)": values.round(1)})


@st.cache_data
def get_engagement_heatmap(seed: int = 7) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    data = rng.normal(loc=72, scale=8, size=(len(DEPARTMENTS), len(MONTHS)))
    data = np.clip(data, 40, 98)
    df = pd.DataFrame(data.round(0), index=DEPARTMENTS, columns=MONTHS)
    return df


@st.cache_data
def get_headcount_by_dept(seed: int = 11) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    counts = rng.integers(40, 260, size=len(DEPARTMENTS))
    return pd.DataFrame({"Department": DEPARTMENTS, "Headcount": counts})


@st.cache_data
def get_diversity_snapshot(seed: int = 3) -> dict:
    rng = np.random.default_rng(seed)
    return {
        "Women in Workforce (%)": round(float(rng.uniform(38, 47)), 1),
        "Women in Leadership (%)": round(float(rng.uniform(28, 38)), 1),
        "Employee Resource Group Members": int(rng.integers(180, 420)),
        "Avg. Tenure (yrs)": round(float(rng.uniform(2.8, 4.6)), 1),
    }


@st.cache_data
def get_speakup_breakdown(seed: int = 9) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    counts = rng.integers(2, 24, size=len(REPORT_CATEGORIES))
    return pd.DataFrame({"Category": REPORT_CATEGORIES, "Reports (last 12 months)": counts})


@st.cache_data
def get_survey_participation(seed: int = 15) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    rate = np.clip(rng.normal(68, 6, len(MONTHS)), 45, 92)
    return pd.DataFrame({"Month": MONTHS, "Participation Rate (%)": rate.round(0)})


@st.cache_data
def get_enps_trend(seed: int = 21) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    values = np.clip(np.cumsum(rng.normal(0.3, 2.2, len(MONTHS))) + 18, -10, 55)
    return pd.DataFrame({"Month": MONTHS, "eNPS": values.round(0)})


def init_session_stores():
    """Initialise in-memory (session-only) stores for user-submitted demo data."""
    if "survey_submissions" not in st.session_state:
        st.session_state.survey_submissions = []
    if "speakup_reports" not in st.session_state:
        st.session_state.speakup_reports = []
    if "skill_requests" not in st.session_state:
        st.session_state.skill_requests = []
