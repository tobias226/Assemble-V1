"""
Full-screen entry splash for Assemble.
Shown once per session before the person enters the platform.
"""

import streamlit as st

DOTS = [
    (164.3, 160.6, 2.9, 0.36), (141.6, 152.4, 2.6, 3.96), (144.7, 151.0, 2.7, 3.12),
    (206.1, 138.6, 3.5, 0.10), (191.3, 138.5, 2.6, 0.66), (163.2, 167.6, 3.5, 3.39),
    (169.8, 166.5, 2.7, 1.55), (159.9, 137.9, 2.6, 3.78), (205.4, 313.8, 3.2, 1.25),
    (243.3, 310.9, 2.8, 1.15), (227.6, 312.0, 2.6, 3.19), (209.1, 318.9, 3.6, 2.08),
    (237.4, 326.0, 2.4, 2.70), (208.3, 332.4, 3.1, 1.76), (214.2, 318.1, 3.0, 2.54),
    (214.9, 314.7, 3.4, 2.83), (218.9, 322.5, 3.4, 0.49), (415.4, 110.1, 2.7, 0.33),
    (462.5, 121.0, 3.1, 1.31), (417.6, 122.5, 2.4, 2.61), (455.3, 145.5, 3.2, 0.31),
    (438.2, 146.6, 2.6, 1.00), (436.9, 115.7, 3.0, 1.45), (426.8, 124.3, 3.3, 3.99),
    (435.0, 127.5, 2.5, 3.67), (430.3, 236.0, 2.4, 2.71), (438.5, 235.2, 2.9, 1.00),
    (514.8, 239.6, 2.9, 3.10), (461.8, 286.3, 2.9, 0.97), (462.0, 235.0, 2.8, 0.99),
    (505.0, 277.9, 2.9, 0.13), (447.9, 246.1, 2.5, 0.93), (580.6, 120.4, 3.5, 2.26),
    (674.0, 143.6, 3.5, 2.62), (652.0, 166.2, 2.9, 0.37), (588.2, 174.7, 3.5, 3.70),
    (602.0, 160.4, 3.3, 2.57), (654.6, 151.8, 3.1, 2.74), (594.5, 177.9, 3.5, 0.30),
    (671.8, 180.5, 3.1, 0.18), (663.9, 125.4, 3.6, 2.67), (722.2, 346.8, 2.9, 1.89),
    (694.2, 336.1, 3.3, 0.84), (679.4, 344.0, 2.6, 1.58), (716.2, 335.7, 2.5, 0.21),
    (727.1, 327.8, 3.1, 3.27), (703.7, 350.2, 3.5, 1.76), (674.7, 347.0, 2.4, 2.24),
]

# A handful of long arcs linking continents, to suggest global connection.
ARCS = [
    ("M 190,150 Q 320,40 440,125", 0.0),
    ("M 220,320 Q 330,420 440,240", 1.4),
    ("M 460,130 Q 540,60 630,140", 2.1),
    ("M 460,250 Q 560,300 650,160", 0.7),
    ("M 640,160 Q 700,250 700,340", 3.0),
    ("M 200,150 Q 120,250 215,320", 1.9),
]

SPLASH_CSS = """<style>
header[data-testid="stHeader"] { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }
div[data-testid="stDecoration"] { display: none !important; }
.main .block-container {
    padding: 0 !important;
    max-width: 100% !important;
}
.stApp {
    background: radial-gradient(ellipse at center, #0F1712 0%, #060A08 70%);
}
.splash-wrap {
    position: relative;
    height: 86vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    overflow: hidden;
    animation: splashIn 0.9s ease-out;
}
@keyframes splashIn {
    0%   { opacity: 0; transform: scale(0.98); }
    100% { opacity: 1; transform: scale(1); }
}
.globe-svg {
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    width: min(1100px, 96vw);
    opacity: 0.85;
    pointer-events: none;
}
.globe-outline {
    fill: none;
    stroke: rgba(46, 204, 113, 0.16);
    stroke-width: 1;
}
.globe-outline.spin {
    transform-origin: 450px 250px;
    animation: spin 60s linear infinite;
}
@keyframes spin {
    from { transform: rotate(0deg); }
    to   { transform: rotate(360deg); }
}
.node {
    fill: #2ECC71;
    filter: drop-shadow(0 0 4px rgba(46, 204, 113, 0.9));
    animation: pulse 3.6s ease-in-out infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 0.35; }
    50%      { opacity: 1; }
}
.arc {
    fill: none;
    stroke: #2ECC71;
    stroke-width: 1.1;
    stroke-linecap: round;
    stroke-dasharray: 6 10;
    opacity: 0.55;
    animation: dash 6s linear infinite;
}
@keyframes dash {
    to { stroke-dashoffset: -160; }
}
.splash-content {
    position: relative;
    z-index: 2;
}
.splash-tag {
    display: inline-block;
    color: #8FD9AE;
    font-size: 0.78rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    font-weight: 600;
    margin-bottom: 1.6rem;
    border: 1px solid #1B7A43;
    border-radius: 999px;
    padding: 0.35rem 1.1rem;
    background: rgba(46, 204, 113, 0.06);
}
.splash-title {
    font-family: -apple-system, 'Segoe UI', sans-serif;
    font-weight: 700;
    font-size: clamp(3.2rem, 9vw, 6.2rem);
    letter-spacing: -2px;
    margin: 0;
    color: #FFFFFF;
    text-shadow: 0 0 40px rgba(46, 204, 113, 0.35);
}
.splash-subtitle {
    font-size: clamp(1rem, 2vw, 1.3rem);
    color: #D9E2DC;
    font-weight: 300;
    max-width: 620px;
    margin: 1.1rem auto 2.6rem auto;
    line-height: 1.6;
}
div[data-testid="column"] .stButton > button {
    background: linear-gradient(135deg, #2ECC71 0%, #1B7A43 100%);
    color: #06110A;
    font-weight: 600;
    font-size: 1rem;
    border: none;
    border-radius: 999px;
    padding: 0.85rem 2.4rem;
    box-shadow: 0 8px 30px rgba(46, 204, 113, 0.28);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
div[data-testid="column"] .stButton > button:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 14px 40px rgba(46, 204, 113, 0.45);
}
.splash-hint {
    margin-top: 1.4rem;
    color: #93A69B;
    font-size: 0.78rem;
    letter-spacing: 0.5px;
}
</style>"""


def _dots_svg() -> str:
    circles = []
    for x, y, r, delay in DOTS:
        circles.append(
            f'<circle cx="{x}" cy="{y}" r="{r}" class="node" '
            f'style="animation-delay:{delay}s"></circle>'
        )
    return "".join(circles)


def _arcs_svg() -> str:
    paths = []
    for d, delay in ARCS:
        paths.append(
            f'<path d="{d}" class="arc" style="animation-delay:{delay}s"></path>'
        )
    return "".join(paths)


def render_splash():
    st.markdown(SPLASH_CSS, unsafe_allow_html=True)

    body = (
        '<div class="splash-wrap">'
        '<svg class="globe-svg" viewBox="0 0 900 500" xmlns="http://www.w3.org/2000/svg">'
        '<ellipse class="globe-outline spin" cx="450" cy="250" rx="380" ry="180"/>'
        '<ellipse class="globe-outline spin" cx="450" cy="250" rx="380" ry="90"/>'
        '<ellipse class="globe-outline" cx="450" cy="250" rx="380" ry="230"/>'
        + _arcs_svg() + _dots_svg() +
        '</svg>'
        '<div class="splash-content">'
        '<div class="splash-tag">ESG · Employee Voice Platform</div>'
        '<h1 class="splash-title">Assemble</h1>'
        '<p class="splash-subtitle">A platform to strengthen employee voice and improve '
        'outcomes &mdash; connecting people, culture and leadership in one place.</p>'
        '</div>'
        '</div>'
    )
    st.markdown(body, unsafe_allow_html=True)

    _, mid, _ = st.columns([1, 0.6, 1])
    with mid:
        if st.button("Enter Assemble", use_container_width=True, key="enter_assemble"):
            st.session_state.entered_app = True
            st.rerun()

    st.markdown(
        '<p class="splash-hint" style="text-align:center;">'
        'Simulated prototype · No real employee data is used</p>',
        unsafe_allow_html=True,
    )
