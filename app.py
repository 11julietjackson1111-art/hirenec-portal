import streamlit as st
import pandas as pd

# 1. SYSTEM CONFIGURATION
st.set_page_config(page_title="Hirenec Solutions Limited", page_icon="🏢", layout="wide")

# 2. HIGH-VISIBILITY DESIGN ENGINE (Deep Blue & Dark Grey for maximum readability)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    /* Global Text: Charcoal Grey for perfect readability on white */
    .stApp { 
        background-color: #FFFFFF; 
        font-family: 'Inter', sans-serif;
        color: #1A1A1A !important; 
    }

    /* HEADER: Deep Executive Blue */
    .main-header {
        background-color: #002349; 
        padding: 50px;
        color: #FFFFFF !important;
        border-bottom: 8px solid #C5A059;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-radius: 0 0 15px 15px;
    }
    
    .brand-text h1 { 
        font-size: 50px; 
        font-weight: 900; 
        margin: 0; 
        color: #FFFFFF !important;
        text-transform: uppercase;
    }
    
    .brand-text p { 
        font-size: 18px; 
        letter-spacing: 5px; 
        color: #C5A059 !important; 
        font-weight: 700; 
        margin-top: 10px;
    }

    /* BOLD BLACK TEXT FOR BODY CONTENT */
    h2, h3, h4, p, label, .stMarkdown {
        color: #1A1A1A !important;
        font-weight: 500;
    }

    /* SIDEBAR NAVIGATION: Darker background for contrast */
    [data-testid="stSidebar"] { 
        background-color: #E9ECEF !important; 
        border-right: 3px solid #002349; 
    }
    
    .stRadio > label { 
        font-size: 20px !important; 
        font-weight: 800 !important; 
        color: #002349 !important; 
    }

    /* METRIC CARDS: Deep Blue with Gold Text */
    .metric-card {
        background-color: #002349;
        color: #FFFFFF !important;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        border-bottom: 5px solid #C5A059;
        margin-bottom: 20px;
    }
    .metric-card h2 { color: #C5A059 !important; font-size: 45px; margin: 0; }
    .metric-card p { color: #FFFFFF !important; font-size: 14px; font-weight: 700; }

    /* ERROR PREVENTION FOR INPUT FIELDS */
    input {
        color: #1A1A1A !important;
        background-color: #F8F9FA !important;
        border: 2px solid #002349 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER (Logo Placeholder on Right)
st.markdown("""
    <div class="main-header">
        <div class="brand-text">
            <h1>Hirenec Solutions Limited</h1>
            <p>Precision | People | Performance</p>
        </div>
        <div style="background: white; padding: 10px; border-radius: 8px;">
            <img src="https://via.placeholder.com/150x80?text=LOGO+HERE" width="150">
        </div>
    </div>
    <div style="background:#F1F3F5; padding:15px 50px; border-bottom:2px solid #002349; font-weight:800; color:#002349; font-size:16px;">
        📍 Bangalore HQ | 📧 contact@hirenecsolutions.com | 👤 Director: Juliet Jackson
    </div>
    """, unsafe_allow_html=True)

# 4. NAVIGATION CONTROL
with st.sidebar:
    st.markdown("## 🛡️ PORTAL ACCESS")
    page = st.radio("SELECT VIEW", ["HOME PANEL", "JOB BOARD", "RECRUITER HUB", "SUPER ADMIN"], label_visibility="collapsed")
    st.divider()
    if st.button("🔴 Logout System"): 
        st.rerun()

# 5. FUNCTIONAL PANELS (All using high-contrast black/blue text)
if page == "HOME PANEL":
    st.write("##")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🏛️ Executive Recruitment Gateway")
        st.write("Welcome, **Juliet Jackson**. Access the management portals below for your 10,000+ verified candidates.")
        
        # LOGIN TABS
        st.write("#### 🔐 Secure Authorization")
        tab_cand, tab_rec = st.tabs(["Candidate Login", "Admin/Recruiter Login"])
        with tab_cand:
            st.text_input("Candidate Username/Email", key="c_user")
            st.text_input("Password", type="password", key="c_pass")
            st.button("Login as Candidate", use_container_width=True)
        with tab_rec:
            st.text_input("Admin Security ID", key="a_user")
            st.text_input("Master Key", type="password", key="a_pass")
            st.button("Authorized Admin Login", use_container_width=True)

    with col2:
        st.markdown('<div class="metric-card"><h2>10,000+</h2><p>Verified Candidates</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="metric-card"><h2>500+</h2><p>Global Companies</p></div>', unsafe_allow_html=True)

elif page == "JOB BOARD":
    st.title("🔍 Live Vacancy Board")
    st.write("### Filter and Manage Job Listings")
    c1, c2 = st.columns(2)
    c1.selectbox("Filter by Region", ["All", "India", "USA", "Remote"])
    c2.text_input("Keyword Search")
    
    st.table(pd.DataFrame({
        "Job ID": ["HS-101", "HS-102", "HS-103"],
        "Title": ["Senior Operations Lead", "Technical Architect", "HR Director"],
        "Status": ["Active", "Interviewing", "Offer Phase"]
    }))

elif page == "RECRUITER HUB":
    st.title("🤝 Recruitment Command Center")
    st.write("### Active Talent Pipeline")
    st.dataframe(pd.DataFrame({
        "Candidate": ["Arjun Kumar", "Anita S.", "Mark T."],
        "Applied For": ["Ops Manager", "Architect", "HR Director"],
        "Joining Date": ["2026-04-15", "2026-05-01", "Pending"]
    }), use_container_width=True)

elif page == "SUPER ADMIN":
    st.title("⚙️ Super Admin Control Panel")
    st.write("Authorized Personnel Only: **Director Juliet Jackson**")
    
    a1, a2, a3 = st.columns(3)
    a1.metric("System Users", "10,757", "+120")
    a2.metric("Company Partners", "512", "+5")
    a3.metric("Platform Uptime", "100%")
    
    st.divider()
    st.write("#### 🛠️ Internal Management Logs")
    st.code("2026-03-30 10:00 - User Admin (Juliet) login successful.")
    st.code("2026-03-30 09:45 - 24 New Candidates Verified.")

# 6. FOOTER
st.markdown("<div style='text-align:center; padding:50px; color:#666; font-weight:700;'>© 2026 Hirenec Solutions Limited | Spick and Span Execution</div>", unsafe_allow_html=True)

