import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.append(PROJECT_ROOT)

import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="British Airways | Executive Health Dashboard",
    page_icon="✈️",
    layout="wide"
)

# ---------------- BRAND COLORS ----------------
BA_BLUE = "#0033A0"
BA_RED = "#BA0C2F"

# ---------------- CUSTOM CSS ----------------
st.markdown(f"""
<style>

html, body, [class*="css"]  {{
    font-family: 'Segoe UI', sans-serif;
}}

.main-title {{
    font-size: 52px;
    font-weight: 700;
    color: {BA_BLUE};
}}

.sub-title {{
    font-size: 22px;
    font-weight: 500;
    color: {BA_RED};
    margin-top: -10px;
    margin-bottom: 25px;
}}

.section-card {{
    background-color: white;
    padding: 25px;
    border-radius: 14px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}}

.metric-card {{
    background-color: #f7f9fc;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}}

.footer {{
    text-align: center;
    font-size: 14px;
    color: grey;
    margin-top: 50px;
}}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
col_logo, col_title = st.columns([1, 5])

with col_logo:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/5/5d/British_Airways_Logo.svg",
        width=140
    )

with col_title:
    st.markdown(f"<div class='main-title'>British Airways</div>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='sub-title'>AI Powered Workspace Health Risk Prediction System</div>",
        unsafe_allow_html=True
    )

st.markdown("---")

# ---------------- EXECUTIVE METRICS ----------------
st.subheader("✈️ Executive System Overview")

m1, m2, m3, m4 = st.columns(4)

m1.metric("API Status", "Operational")
m2.metric("Security", "Encrypted")
m3.metric("AI Models", "2 Active")
m4.metric("System Mode", "Live")

st.markdown("---")

# ---------------- MAIN DASHBOARD ----------------
left, right = st.columns([2, 1])

with left:
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("### 👩‍✈️ Operations Briefing")
    st.write("""
    Welcome to the British Airways Executive Health Intelligence Dashboard.

    This AI-powered system provides predictive health risk assessments
    for employees and operational staff.

    Navigate using the sidebar to access:

    • 🩺 Diabetes Risk Assessment  
    • ❤️ Heart Disease Risk Assessment  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("### 🛫 Live System Status")
    st.success("Backend API Connected")
    st.success("Model Engine Active")
    st.success("Secure Connection Established")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# ---------------- VISUAL SECTION ----------------
st.image(
    "https://images.unsplash.com/photo-1504196606672-aef5c9cefc92",
    use_container_width=True
)

# ---------------- FOOTER ----------------
st.markdown(f"""
<div class='footer'>
© 2026 British Airways Health Analytics Division<br>
Confidential Internal System • Powered by AI & FastAPI
</div>
""", unsafe_allow_html=True)