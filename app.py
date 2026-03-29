import streamlit as st
import pandas as pd

# 1. SYSTEM CONFIGURATION
st.set_page_config(page_title="Hirenec Solutions Limited", page_icon="🏢", layout="wide")

# 2. THE VISIBILITY ENGINE (Deep Navy & High-Contrast Charcoal)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    /* Global Font Visibility: Bold black text on white background */
    .stApp { background-color: #FFFFFF; font-family: 'Inter', sans-serif; color: #1A1A1A !important; }
    
    /* EXECUTIVE HEADER BOX */
    .main-header {
        background-color: #002349; 
        padding: 45px 60px;
        border-bottom: 6px solid #C5A059;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .brand-text h1 { font-size: 48px; font-weight: 900; margin: 0; color: #FFFFFF !important; text-transform: uppercase; }
    .brand-text p { font-size: 16px; letter-spacing: 5px; color: #C5A059 !important; font-weight: 700; margin-top: 10px; }
    
    /* FORCING TEXT VISIBILITY FOR ALL LABELS & TITLES */
    h1, h2, h3, h4, p, label, .stMarkdown, .stSelectbox label { color: #1A1A1A !important; font-weight: 700 !important; }
    
    /* METRIC CARDS */
    .metric-card {
        background-color: #002349;
        color: #FFFFFF !important;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        border-bottom: 4px solid #C5A059;
        margin-bottom: 15px;
    }
    .metric-card h2 { color: #C5A059 !important; font-size: 38px; margin: 0; }
    .metric-card p { color: #FFFFFF !important; font-size: 12px; text-transform: uppercase; }

    /* SIDEBAR */
    [data-testid="stSidebar"] { background-color: #F8F9FA !important; border-right: 2px solid #002349; }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER (FORCED LOGO.PNG TO THE RIGHT)
st.markdown("""
    <div class="main-header">
        <div class="brand-text">
            <h1>HIRENEC SOLUTIONS LIMITED</h1>
            <p>Precision | People | Performance</p>
        </div>
        <div style="background: white; padding: 10px; border-radius: 8px; display: flex; align-items: center;">
            <img src="app/static/logo.png" width="160" onerror="this.src='https://via.placeholder.com/160x70?text=LOGO.PNG'">
        </div>
    </div>
    <div style="background:#F0F2F5; padding:12px 60px; border-bottom:2px solid #002349; color:#002349; font-weight:900;">
        📍 Bangalore HQ | 📧 contact@hirenecsolutions.com | 👤 Director: Juliet Jackson
    </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("## 🛡️ SYSTEM MENU")
    page = st.radio("GO TO:", ["HOME PANEL", "JOB BOARD", "RECRUITER HUB", "SUPER ADMIN"], label_visibility="collapsed")
    st.divider()
    if st.button("🔴 Secure Logout"): st.rerun()

# 5. FUNCTIONAL PANELS

if page == "HOME PANEL":
    st.write("##")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### 🏛️ Executive Gateway")
        st.write("Welcome to Hirenec Solutions Limited, managing executive search and strategic hiring.")
        st.write("---")
        st.markdown("#### 🔐 SECURE AUTHORIZATION")
        t_cand, t_admin = st.tabs(["Candidate Portal", "Staff & Admin Access"])
        with t_cand:
            st.text_input("Candidate Email", key="c_user")
            st.text_input("Password", type="password", key="c_pass")
            st.button("Candidate Login")
        with t_admin:
            st.text_input("Admin ID", key="a_user")
            st.text_input("Security Key", type="password", key="a_pass")
            st.button("Authorized Staff Login")
    with col2:
        st.markdown('<div class="metric-card"><h2>10,245</h2><p>Verified Candidates</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="metric-card"><h2>512</h2><p>Global Partners</p></div>', unsafe_allow_html=True)

elif page == "JOB BOARD":
    st.title("🔍 Live Recruitment Board")
    st.write("Current active vacancies managed by Hirenec.")
    job_data = pd.DataFrame({
        "Job ID": ["HS-101", "HS-102", "HS-103", "HS-104"],
        "Position": ["Operations Director", "Python Lead", "HR Strategy", "Lead Architect"],
        "Location": ["Bangalore", "Remote (US)", "London", "Bangalore"],
        "Status": ["Active", "Urgent", "Interviewing", "Open"]
    })
    st.table(job_data)

elif page == "RECRUITER HUB":
    st.title("🤝 Recruiter Command Center")
    st.write("Current Talent Pipeline:")
    pipeline = pd.DataFrame({
        "Candidate": ["Rajesh Kumar", "Sana Ahmed", "Mark Thompson", "Juliet J."],
        "Stage": ["Technical Interview", "Final Round", "Screening", "Offer Phase"],
        "Score": ["98%", "92%", "85%", "99%"]
    })
    st.dataframe(pipeline, use_container_width=True)
    st.button("➕ Register New Talent")

elif page == "SUPER ADMIN":
    st.title("⚙️ Super Admin Control")
    st.write("Access Authorized: **Director Juliet Jackson**")
    m1, m2, m3 = st.columns(3)
    m1.metric("System Users", "10,757", "+120")
    m2.metric("Revenue Growth", "22%", "On Track")
    m3.metric("Platform Status", "Online")
    st.divider()
    st.markdown("#### 🛠️ Internal Management Logs")
    st.code("[LOG] 2026-03-30 01:15:00 - Master Admin Login Successful")
    st.code("[LOG] 2026-03-30 01:20:00 - Data Sync Completed")

# 6. FOOTER
st.markdown("<div style='text-align:center; padding:60px 0; color:#888; font-weight:bold;'>© 2026 Hirenec Solutions Limited | Spick and Span Execution</div>", unsafe_allow_html=True)

