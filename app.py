import streamlit as st
import pandas as pd
from datetime import datetime

# 1. PAGE SETUP
st.set_page_config(page_title="Hirenec Solutions Limited | Executive Portal", page_icon="🏢", layout="wide")

# 2. THE SPOT-ON DESIGN ENGINE (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;800&family=Playfair+Display:wght@700&display=swap');

    .stApp { background-color: #FFFFFF; font-family: 'Outfit', sans-serif; }

    /* HEADER: LOGO ON THE RIGHT */
    .header-box {
        background: #002349;
        padding: 40px 80px;
        color: white;
        border-bottom: 6px solid #C5A059;
        display: flex;
        justify-content: space-between; /* Pushes Logo to Right */
        align-items: center;
    }
    .brand-group { display: flex; flex-direction: column; }
    .brand-main { font-size: 45px; font-weight: 800; margin: 0; line-height: 1; letter-spacing: -1px; }
    .brand-sub { font-size: 14px; letter-spacing: 5px; text-transform: uppercase; color: #C5A059; margin-top: 10px; font-weight: 600; }
    
    .logo-square {
        background: #C5A059;
        color: #002349;
        font-weight: 800;
        font-size: 32px;
        width: 80px;
        height: 80px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }

    /* CONTACT STRIP */
    .contact-bar {
        background: #F0F4F8;
        padding: 12px 80px;
        display: flex;
        justify-content: space-between;
        font-size: 13px;
        color: #002349;
        font-weight: 600;
        border-bottom: 1px solid #DDE4ED;
    }

    /* CARDS */
    .stat-card {
        background: #FFFFFF;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #EAEAEA;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. PERMANENT HEADER (Logo on Right)
st.markdown("""
    <div class="header-box">
        <div class="brand-group">
            <h1 class="brand-main">HIRENEC SOLUTIONS LIMITED</h1>
            <div class="brand-sub">Precision | People | Performance</div>
        </div>
        <div class="logo-square">HS</div>
    </div>
    <div class="contact-bar">
        <div>📍 The Estate, Dickenson Road, Bangalore</div>
        <div>📧 contact@hirenecsolutions.com | 📞 Director: Juliet Jackson</div>
    </div>
    """, unsafe_allow_html=True)

# 4. NAVIGATION
with st.sidebar:
    st.markdown("### 🖥️ PORTAL ACCESS")
    page = st.radio("Navigation", ["HOME", "JOB BOARD", "RECRUITER HUB", "ADMIN PANEL"], label_visibility="collapsed")
    st.divider()
    if st.button("Logout"):
        st.rerun()

# 5. PAGE LOGIC (FULLY FILLED TABS)

# --- HOME PAGE ---
if page == "HOME":
    st.write("##")
    col_l, col_r = st.columns([2, 1])
    with col_l:
        st.markdown("### Executive Search & Strategic Hiring")
        st.write("""
        Hirenec Solutions Limited is Bangalore's premier recruitment firm. We provide a full-cycle 
        Application Tracking System (ATS) and human capital management for global firms. 
        Our mission is to deliver 'Unfiltered Truth' in talent acquisition.
        """)
        
        st.markdown("#### 🔑 Portal Login")
        c_login, r_login = st.columns(2)
        with c_login:
            with st.expander("Candidate Login"):
                st.text_input("Candidate Email")
                st.text_input("Password", type="password")
                st.button("Login as Candidate")
        with r_login:
            with st.expander("Recruiter Login"):
                st.text_input("Client ID")
                st.text_input("Access Key", type="password")
                st.button("Login as Recruiter")

    with col_r:
        st.markdown('<div class="stat-card"><h3>10K+</h3><p>Verified Profiles</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="stat-card" style="margin-top:10px;"><h3>500+</h3><p>Partner Companies</p></div>', unsafe_allow_html=True)

    st.divider()
    st.markdown("### Leadership: Director Juliet Jackson")
    c1, c2 = st.columns([1, 3])
    with c1:
        st.image("https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400")
    with c2:
        st.write("""
        Under the direction of **Juliet Jackson**, Hirenec Solutions Limited has scaled to become 
        a key player in the US-India recruitment corridor. Her focus on responsive design and 
        robust security ensures that both candidate and company data are managed with the highest integrity.
        """)
        st.info("“Precision in selection is the foundation of corporate excellence.”")

# --- JOB BOARD ---
elif page == "JOB BOARD":
    st.title("🔍 Global Job Listing & Search")
    st.write("Current active openings across all sectors.")
    
    search, loc, exp = st.columns([2, 1, 1])
    search.text_input("Keywords (e.g. Python, HR)")
    loc.selectbox("Location", ["All", "Bangalore", "Remote (USA)", "Hyderabad"])
    exp.selectbox("Experience", ["Any", "0-2 Yrs", "3-5 Yrs", "5-10 Yrs", "10+ Yrs"])

    st.markdown("---")
    # Simulated Job Postings
    jobs = [
        {"Role": "Senior Java Architect", "Company": "FinTech Corp", "Status": "Immediate"},
        {"Role": "Operations Manager", "Company": "Hirenec Partner", "Status": "Open"},
        {"Role": "HR Director", "Company": "Global Logistics", "Status": "New"}
    ]
    for j in jobs:
        with st.container():
            col_a, col_b = st.columns([3, 1])
            col_a.markdown(f"#### {j['Role']}")
            col_a.write(f"**Company:** {j['Company']} | **Type:** Full Time")
            if col_b.button(f"Apply Now", key=j['Role']):
                st.success("Application Form Opened.")
            st.divider()

# --- RECRUITER HUB ---
elif page == "RECRUITER HUB":
    st.title("🤝 Recruiter/Company Hub")
    st.write("Manage your job postings and track applicants.")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Active Postings", "12")
    m2.metric("Pending Interviews", "45")
    m3.metric("Offers Extended", "8")

    st.markdown("### 📋 Application Tracking System (ATS)")
    # Data Table for Candidates
    data = {
        "Candidate Name": ["Arjun Mehta", "Sana Khan", "Robert Wilson", "Priya Das"],
        "Applied Role": ["Java Architect", "HR Lead", "Operations", "Java Architect"],
        "Application Date": ["2026-03-25", "2026-03-28", "2026-03-29", "2026-03-30"],
        "Status": ["Interview Scheduled", "Shortlisted", "Under Review", "New"]
    }
    st.table(pd.DataFrame(data))
    
    if st.button("➕ Post a New Job Listing"):
        st.write("Opening Job Creation Form...")

# --- ADMIN PANEL ---
elif page == "ADMIN PANEL":
    st.title("⚙️ Super Admin Control Center")
    st.write("Welcome, Director Juliet Jackson.")
    
    # Critical Admin Metrics
    st.markdown("#### 📊 System Overview")
    a1, a2, a3, a4 = st.columns(4)
    a1.metric("Total Candidates", "10,245")
    a2.metric("Total Companies", "512")
    a3.metric("Joining This Month", "84")
    a4.metric("System Uptime", "99.9%")

    st.markdown("### 🛠️ Candidate & User Management")
    # Detailed Admin View
    admin_data = {
        "User ID": ["C-901", "C-902", "C-903", "R-101", "R-102"],
        "User Name": ["John Doe", "Anita Rao", "Michael S.", "Tech Mahindra", "Amazon US"],
        "Type": ["Candidate", "Candidate", "Candidate", "Company", "Company"],
        "Last Login": ["2 Hours ago", "1 Day ago", "Just now", "Active", "Active"],
        "Subscription": ["Free", "Free", "Free", "Premium", "Premium"]
    }
    st.dataframe(pd.DataFrame(admin_data), use_container_width=True)

    with st.expander("Security & Logs"):
        st.code("LOG [2026-03-30 00:45]: New Candidate Registered (ID: C-904)")
        st.code("LOG [2026-03-30 01:10]: Admin Juliet Jackson Updated Theme Settings")

# 6. FOOTER
st.divider()
st.markdown("""
    <div style="text-align:center; color:#999; padding-bottom:50px;">
        © 2026 Hirenec Solutions Limited | The Estate, Bangalore | 
        <a href="#">Privacy Policy</a> | <a href="#">Terms of Service</a>
    </div>
    """, unsafe_allow_html=True)
