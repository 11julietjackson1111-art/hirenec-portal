import streamlit as st
import pandas as pd

# 1. CORE SYSTEM SETUP
st.set_page_config(page_title="Hirenec Solutions Limited", page_icon="🏢", layout="wide")

# 2. THE VISIBILITY ENGINE (Deep Navy & Charcoal Black)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    /* Global Styles: Forcing high visibility on white background */
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
    .brand-text h1 { font-size: 48px; font-weight: 900; margin: 0; color: #FFFFFF !important; text-transform: uppercase; line-height: 1; }
    .brand-text p { font-size: 16px; letter-spacing: 5px; color: #C5A059 !important; font-weight: 700; margin-top: 10px; }
    
    /* NAVIGATION & TEXT FIXES */
    h2, h3, h4, p, label { color: #1A1A1A !important; font-weight: 700 !important; }
    .stTabs [data-baseweb="tab"] { font-size: 18px !important; font-weight: 800 !important; color: #002349 !important; }
    
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
    .metric-card p { color: #FFFFFF !important; font-size: 12px; text-transform: uppercase; margin-top: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER (LOGO.PNG IS FORCED TO THE RIGHT)
st.markdown("""
    <div class="main-header">
        <div class="brand-text">
            <h1>HIRENEC SOLUTIONS LIMITED</h1>
            <p>Precision | People | Performance</p>
        </div>
        <div style="background: white; padding: 8px; border-radius: 6px;">
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
    st.info("Status: Fully Operational")
    if st.button("🔴 Secure Logout"): st.rerun()

# 5. FUNCTIONAL PANELS (NOTHING IS BLANK)

if page == "HOME PANEL":
    st.write("##")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### 🏛️ Executive Gateway")
        st.write("Welcome to the mission-control center for Hirenec Solutions Limited. We bridge the gap between global elite talent and industry leaders.")
        st.write("---")
        st.markdown("#### 🔐 SECURE AUTHORIZATION")
        t_cand, t_admin = st.tabs(["Candidate Portal", "Staff & Admin Access"])
        with t_cand:
            st.text_input("Candidate Email Address", key="c_in")
            st.text_input("Access Password", type="password", key="c_p")
            st.button("Login to Candidate Profile", use_container_width=True)
        with t_admin:
            st.text_input("Admin ID (HS-XXXX)", key="a_in")
            st.text_input("Security Key", type="

