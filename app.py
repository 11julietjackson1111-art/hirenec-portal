import streamlit as st

# 1. ELITE CONFIGURATION
st.set_page_config(page_title="Hirenec Solutions | Executive Portal", page_icon="🏢", layout="wide")

# 2. THE DESIGN ENGINE (Polished & Professional)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;800&family=Playfair+Display:wght@700&display=swap');

    .stApp { background-color: #FFFFFF; font-family: 'Outfit', sans-serif; }

    /* HEADER & LOGO */
    .header-box {
        background: #002349;
        padding: 50px 80px;
        color: white;
        border-bottom: 6px solid #C5A059;
        display: flex;
        align-items: center;
        gap: 30px;
    }
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
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .brand-main { font-size: 52px; font-weight: 800; margin: 0; line-height: 1; }
    .brand-sub { font-size: 14px; letter-spacing: 5px; text-transform: uppercase; color: #C5A059; margin-top: 10px; font-weight: 600; }

    /* CONTACT STRIP */
    .contact-bar {
        background: #F0F4F8;
        padding: 15px 80px;
        display: flex;
        gap: 40px;
        font-size: 14px;
        color: #002349;
        font-weight: 600;
        border-bottom: 1px solid #DDE4ED;
    }

    /* CARDS & REVIEWS */
    .stat-card {
        background: #FFFFFF;
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #EAEAEA;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }
    .review-card {
        background: #002349;
        color: white;
        padding: 30px;
        border-radius: 15px;
        border-left: 5px solid #C5A059;
        margin-bottom: 20px;
    }

    /* SIDEBAR */
    [data-testid="stSidebar"] { background-color: #F8F9FA !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. PERMANENT HEADER (Logo + Brand + Contact)
st.markdown("""
    <div class="header-box">
        <div class="logo-square">HS</div>
        <div>
            <h1 class="brand-main">HIRENEC SOLUTIONS</h1>
            <div class="brand-sub">Precision | People | Performance</div>
        </div>
    </div>
    <div class="contact-bar">
        <span>📍 The Estate, Dickenson Road, Bangalore</span>
        <span>📧 contact@hirenecsolutions.com</span>
        <span>📞 Director: Juliet Jackson</span>
    </div>
    """, unsafe_allow_html=True)

# 4. NAVIGATION
with st.sidebar:
    st.markdown("### 🖥️ MAIN NAVIGATION")
    page = st.radio("Select View", ["HOME", "JOB BOARD", "RECRUITER HUB", "ADMIN"], label_visibility="collapsed")
    st.divider()
    st.success("Portal Secured")

# 5. CONTENT LOGIC (NOT EMPTY)
if page == "HOME":
    st.write("##")
    st.markdown("### About Hirenec Solutions")
    st.write("""
    Hirenec Solutions Pvt Ltd is a premier executive recruitment firm based in Bangalore. 
    We specialize in connecting high-performance professionals with world-class organizations 
    through a strategy of 'Unfiltered Truth' and data-driven precision.
    """)

    # Statistics
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="stat-card"><h2 style="color:#002349;">10K+</h2><p>Candidates</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="stat-card"><h2 style="color:#002349;">500+</h2><p>Clients</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="stat-card"><h2 style="color:#002349;">98%</h2><p>Success</p></div>', unsafe_allow_html=True)

    # Director Section
    st.write("##")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=500")
    with col2:
        st.markdown(f"""
            <div style="background:#FDFDFD; padding:30px; border-radius:15px; border:1px solid #EEE;">
                <h2 style="font-family:'Playfair Display'; color:#002349;">Director Juliet Jackson</h2>
                <p style="color:#C5A059; font-weight:700; text-transform:uppercase;">Founder & Strategic Lead</p>
                <p>Juliet Jackson leads Hirenec Solutions with a vision for transparency and precision. 
                Based in Bangalore, her firm serves as a bridge for talent to excel in global markets.</p>
                <p><i>"We build the future of leadership through honest connections."</i></p>
            </div>
        """, unsafe_allow_html=True)

    # Reviews
    st.write("##")
    st.markdown("### 💬 Candidate Feedback")
    r1, r2 = st.columns(2)
    with r1:
        st.markdown('<div class="review-card"><i>"The most professional team in Bangalore. Exceptional service."</i><br><b>— Arjun K.</b></div>', unsafe_allow_html=True)
    with r2:
        st.markdown('<div class="review-card"><i>"Honest and transparent recruitment. Juliet truly understands the market."</i><br><b>— Sarah M.</b></div>', unsafe_allow_html=True)

elif page == "JOB BOARD":
    st.title("🔍 Active Opportunities")
    st.write("Browse current openings across our US and Indian partner networks.")
    
    jobs = [
        {"title": "Senior Python Developer", "loc": "Bangalore (Hybrid)", "exp": "5+ Years"},
        {"title": "Operations Manager", "loc": "Remote (US Based)", "exp": "8+ Years"},
        {"title": "HR Specialist", "loc": "Bangalore", "exp": "3+ Years"}
    ]
    
    for job in jobs:
        with st.expander(f"{job['title']} - {job['loc']}"):
            st.write(f"**Experience Required:** {job['exp']}")
            st.button("Apply Now", key=job['title'])

elif page == "RECRUITER HUB":
    st.title("🤝 Recruiter Dashboard")
    st.write("Manage candidate pipelines and client requirements.")
    col_a, col_b = st.columns(2)
    col_a.metric("New Applications", "142", "+12%")
    col_b.metric("Interviews Scheduled", "28", "Active")
    st.write("### Recent Talent Submissions")
    st.table({"Candidate Name": ["Rajesh V.", "Ananya S."], "Role": ["Full Stack", "Sales Lead"], "Status": ["Interview", "Screening"]})

elif page == "ADMIN":
    st.title("⚙️ Admin Control Panel")
    st.write("Secure access for Juliet Jackson.")
    with st.form("Post New Job"):
        st.text_input("Job Title")
        st.text_area("Job Description")
        st.selectbox("Region", ["India", "USA", "UK"])
        st.form_submit_button("Publish Job")

# 6. FOOTER
st.divider()
st.markdown("<p style='text-align:center; color:#999;'>© 2026 Hirenec Solutions Pvt Ltd | Official Executive Portal</p>", unsafe_allow_html=True)

