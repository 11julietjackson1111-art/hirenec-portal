import streamlit as st
import pandas as pd

# 1. SYSTEM CONFIGURATION
st.set_page_config(page_title="Hirenec Solutions Limited", page_icon="🏢", layout="wide")

# 2. HIGH-VISIBILITY DESIGN ENGINE
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    /* Global Text: Charcoal Grey for perfect readability */
    .stApp { 
        background-color: #FFFFFF; 
        font-family: 'Inter', sans-serif;
        color: #1A1A1A !important; 
    }

    /* HEADER: Deep Executive Blue */
    .main-header {
        background-color: #002349; 
        padding: 40px 60px;
        color: #FFFFFF !important;
        border-bottom: 6px solid #C5A059;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .brand-text h1 { 
        font-size: 48px; 
        font-weight: 900; 
        margin: 0; 
        color: #FFFFFF !important;
        text-transform: uppercase;
    }
    
    .brand-text p { 
        font-size: 16px; 
        letter-spacing: 4px; 
        color: #C5A059 !important; 
        font-weight: 700; 
        margin-top: 5px;
    }

    /* BOLD TEXT FOR BODY CONTENT */
    h1, h2, h3, h4, p, label, .stMarkdown {
        color: #1A1A1A !important;
    }

    /* SIDEBAR NAVIGATION */
    [data-testid="stSidebar"] { 
        background-color: #F1F3F5 !important; 
        border-right: 2px solid #002349; 
    }
    
    .stRadio > label { 
        font-size: 18px !important; 
        font-weight: 800 !important; 
        color: #002349 !important; 
    }

    /* METRIC CARDS */
    .metric-card {
        background-color: #002349;
        color: #FFFFFF !important;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        border-bottom: 4px solid #C5A059;
    }
    .metric-card h2 { color: #C5A059 !important; font-size: 40px; margin: 0; }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER (REPLACE THE IMAGE URL BELOW)
st.markdown("""
    <div class="main-header">
        <div class="brand-text">
            <h1>Hirenec Solutions Limited</h1>
            <p>Precision | People | Performance</p>
        </div>
        <div style="background: white; padding: 10px; border-radius: 8px;">
            <img src="https://via.placeholder.com/150x80?text=HIRENEC+LOGO" width="150">
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. NAVIGATION CONTROL
with st.sidebar:
    st.markdown("### 🏢 HIRENEC MENU")
    page = st.radio("Navigation", ["HOME", "JOB BOARD", "RECRUITER HUB", "ADMIN"], label_visibility="collapsed")
    st.divider()
    st.info("System Status: Online & Secure")

# 5. PANELS
if page == "HOME":
    st.write("##")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### 🏛️ Executive Portal")
        st.write("Managing 10,000+ candidates for 500+ global firms.")
        st.write("#### 🔐 Secure Authorization")
        t1, t2 = st.tabs(["Candidate Login", "Admin Login"])
        with t1:
            st.text_input("Username")
            st.text_input("Password", type="password")
            st.button("Login as Candidate")
        with t2:
            st.text_input("Admin ID")
            st.text_input("Master Key", type="password")
            st.button("Authorized Login")
    with col2:
        st.markdown('<div class="metric-card"><h2>10,245</h2><p>VERIFIED CANDIDATES</p></div>', unsafe_allow_html=True)

elif page == "ADMIN":
    st.title("⚙️ Super Admin Control")
    st.write("Authorized Access: **Director Juliet Jackson**")
    st.metric("Total Companies", "512", "+5")
    st.write("#### System Logs")
    st.code("2026-03-30: Platform verified and secure.")

# 6. FOOTER
st.markdown("<div style='text-align:center; padding:50px; color:#1A1A1A; font-weight:700;'>© 2026 Hirenec Solutions Limited</div>", unsafe_allow_html=True)

