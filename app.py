import streamlit as st
import pandas as pd

# 1. CRITICAL CONFIGURATION
st.set_page_config(page_title="Hirenec Solutions Limited", page_icon="🏢", layout="wide")

# 2. THE VISIBILITY ENGINE (High-Contrast & Sharp Fonts)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&family=Playfair+Display:wght@700&display=swap');

    /* Background & Global Font */
    .stApp { background-color: #FFFFFF; font-family: 'Inter', sans-serif; }

    /* SPOT ON HEADER - LOGO ON RIGHT */
    .main-header {
        background: #002349; 
        padding: 50px 80px;
        color: white;
        border-bottom: 8px solid #C5A059;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .brand-text h1 { 
        font-size: 55px; 
        font-weight: 900; 
        margin: 0; 
        letter-spacing: -2px; 
        text-transform: uppercase;
    }
    .brand-text p { 
        font-size: 16px; 
        letter-spacing: 6px; 
        color: #C5A059; 
        font-weight: 700; 
        margin-top: 5px;
    }
    .logo-container {
        border: 3px solid #C5A059;
        padding: 10px;
        background: white;
        border-radius: 10px;
    }

    /* HIGH VISIBILITY NAVIGATION */
    [data-testid="stSidebar"] { background-color: #F0F2F6 !important; border-right: 2px solid #DDE4ED; }
    .stRadio > label { font-size: 22px !important; font-weight: 800 !important; color: #002349 !important; }

    /* DASHBOARD CARDS */
    .metric-card {
        background: #002349;
        color: white;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        border-bottom: 5px solid #C5A059;
        margin-bottom: 20px;
    }
    .metric-card h2 { font-size: 48px; margin: 0; color: #C5A059; }
    .metric-card p { font-size: 14px; text-transform: uppercase; font-weight: 700; margin-top: 10px; }

    /* TABLE STYLING */
    .stDataFrame, .stTable { border: 1px solid #DDE4ED; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER (Logo on Right)
st.markdown("""
    <div class="main-header">
        <div class="brand-text">
            <h1>Hirenec Solutions Limited</h1>
            <p>Precision | People | Performance</p>
        </div>
        <div class="logo-container">
            <img src="https://via.placeholder.com/150x80?text=HIRENEC+LOGO" width="150">
        </div>
    </div>
    <div style="background:#F8F9FA; padding:15px 80px; border-bottom:1px solid #DDD; font-weight:700; color:#002349;">
        📍 The Estate, Bangalore | 📧 contact@hirenecsolutions.com | 👤 Director: Juliet Jackson
    </div>
    """, unsafe_allow_html=True)

# 4. NAVIGATION BAR
with st.sidebar:
    st.markdown("## 🛡️ PORTAL CONTROL")
    page = st.radio("SELECT VIEW", ["HOME PANEL", "JOB BOARD", "RECRUITER HUB", "SUPER ADMIN"], label_visibility="collapsed")
    st.divider()
    st.info("System Status: Online & Secure")
    if st.button("🔴 Logout System"): st.rerun()

# 5. FUNCTIONAL PANELS
if page == "HOME PANEL":
    st.write("##")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🏛️ Welcome to the Executive Gateway")
        st.write("Managing the bridge between top-tier talent and global industry leaders from our headquarters in Bangalore.")
        
        st.write("#### 🔑 Secure Access")
        tab_cand, tab_rec = st.tabs(["Candidate Gateway", "Recruiter Access"])
        with tab_cand:
            st.text_input("Candidate Username/Email", placeholder="Enter your registered email")
            st.text_input("Password", type="password")
            st.button("Login as Candidate", use_container_width=True)
        with tab_rec:
            st.text_input("Recruiter/Admin ID", placeholder="HS-ADMIN-XXXX")
            st.text_input("Security Key", type="password")
            st.button("Authorized Login", use_container_width=True)

    with col2:
        st.markdown('<div class="metric-card"><h2>10,000+</h2><p>Verified Candidates</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="metric-card"><h2>500+</h2><p>Corporate Partners</p></div>', unsafe_allow_html=True)

elif page == "JOB BOARD":
    st.title("🔍 Live Job Board")
    st.write("Filter and manage active recruitment vacancies.")
    c1, c2 = st.columns(2)
    c1.selectbox("Region", ["All Regions", "India (Bangalore)", "USA (Remote)", "UK"])
    c2.text_input("Search Skills (e.g., Python, HR, Management)")
    
    jobs_data = {
        "Job ID": ["HS-101", "HS-102", "HS-103"],
        "Title": ["Senior Operations Manager", "Technical Architect", "HR Director"],
        "Company": ["Global FinTech", "Hirenec Partner", "Retail Giant"],
        "Status": ["Active", "Interviewing", "Offer Phase"]
    }
    st.table(pd.DataFrame(jobs_data))

elif page == "RECRUITER HUB":
    st.title("🤝 Recruiter Command Hub")
    st.markdown("#### Candidate Pipelines & Interview Tracking")
    
    rec_data = {
        "Candidate": ["Rajesh Kumar", "Anita Singh", "Mark Thompson"],
        "Role": ["Ops Manager", "Architect", "HR Director"],
        "Joining Date": ["2026-04-15", "2026-05-01", "Pending"],
        "Match Score": ["98%", "92%", "85%"]
    }
    st.dataframe(pd.DataFrame(rec_data), use_container_width=True)
    st.button("➕ Schedule New Interview")

elif page == "SUPER ADMIN":
    st.title("⚙️ Super Admin Control Panel")
    st.write("Authorized Access Only: **Director Juliet Jackson**")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Candidates", "10,245", "+150")
    m2.metric("Active Companies", "512", "+12")
    m3.metric("Revenue Growth", "28%", "Target Met")
    m4.metric("Pending Approvals", "23", "Action Required")
    
    st.divider()
    st.write("### 🛠️ System Management")
    with st.expander("Manage Registered Companies"):
        st.write("Listing all 512 corporate partners...")
        st.button("Export Partner List (CSV)")
    with st.expander("Security & Access Logs"):
        st.code("LOG: 2026-03-30 10:15 - Successful Login by Juliet Jackson")
        st.code("LOG: 2026-03-30 09:42 - New Candidate Profile Verified: Rajesh K.")

# 6. FOOTER
st.markdown("""
    <div style="text-align:center; padding:100px 0 50px 0; color:#888; font-size:12px;">
        © 2026 Hirenec Solutions Limited | Bangalore HQ | Precision Recruitment Excellence
    </div>
    """, unsafe_allow_html=True)

