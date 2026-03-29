import streamlit as st

# 1. PAGE CONFIG
st.set_page_config(page_title="Hirenec Solutions | Executive Portal", page_icon="🏢", layout="wide")

# 2. THE SPOT-ON DESIGN ENGINE
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

    /* STATS & CARDS */
    .stat-card {
        background: #FFFFFF;
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #EAEAEA;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }
    .stat-val { color: #002349; font-size: 40px; font-weight: 800; }
    .stat-lab { color: #888; font-size: 12px; text-transform: uppercase; letter-spacing: 1px; }

    /* REVIEW SECTION */
    .review-card {
        background: #002349;
        color: white;
        padding: 30px;
        border-radius: 15px;
        border-left: 5px solid #C5A059;
        margin-bottom: 20px;
    }

    /* DIRECTOR AREA */
    .director-profile {
        background: #FDFDFD;
        padding: 40px;
        border-radius: 20px;
        border: 1px solid #EEE;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. TOP BANNER & CONTACT INFO
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
        <span>📞 +91 [Your Number]</span>
    </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("### 🖥️ PORTAL MENU")
    page = st.radio("Navigate", ["HOME", "JOB BOARD", "RECRUITER HUB", "ADMIN"], label_visibility="collapsed")
    st.divider()
    st.markdown("**Director: Juliet Jackson**")

# 5. PAGE CONTENT
if page == "HOME":
    st.write("##")
    # Intro Paragraph
    st.markdown("### Welcome to the Premier Gateway for Global Talent")
    st.write("""
    Hirenec Solutions Pvt Ltd is a leading executive recruitment firm based in Bangalore. 
    We specialize in connecting high-performance professionals with world-class organizations 
    through a strategy of 'Unfiltered Truth' and data-driven precision.
    """)

    # Statistics
    st.write("##")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="stat-card"><div class="stat-val">10K+</div><div class="stat-lab">Candidates</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="stat-card"><div class="stat-val">500+</div><div class="stat-lab">Global Partners</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="stat-card"><div class="stat-val">98%</div><div class="stat-lab">Success Rate</div></div>', unsafe_allow_html=True)

    # Director Section
    st.write("##")
    st.markdown("### Leadership")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=500")
    with col2:
        st.markdown("""
            <div class="director-profile">
                <h2 style="font-family:'Playfair Display'; color:#002349; margin-top:0;">Director Juliet Jackson</h2>
                <p style="color:#C5A059; font-weight:700; text-transform:uppercase; font-size:13px; margin-top:-10px;">Founder & Strategic Lead</p>
                <p>Based in Bangalore, Juliet Jackson leads Hirenec Solutions with a vision for transparency 
                in the recruitment landscape. Her expertise ensures that every placement is built on 
                long-term performance and organizational fit.</p>
                <p><i>"We don't just fill positions; we build the future of leadership."</i></p>
            </div>
        """, unsafe_allow_html=True)

    # Reviews Section
    st.write("##")
    st.markdown("### 💬 Candidate Feedback")
    r1, r2 = st.columns(2)
    with r1:
        st.markdown("""<div class="review-card">
            <p style="font-style:italic;">"The transition to my new role at a US-based firm was seamless. Hirenec is professional and incredibly honest."</p>
            <p><b>— Arjun M.</b> | Senior Engineer</p>
        </div>""", unsafe_allow_html=True)
    with r2:
        st.markdown("""<div class="review-card">
            <p style="font-style:italic;">"Juliet's team understands the Bangalore market better than anyone. They matched my profile perfectly."</p>
            <p><b>— Sarah D.</b> | Project Manager</p>
        </div>""", unsafe_allow_html=True)

elif page == "JOB BOARD":
    st.title("🔍 Active Opportunities")
    st.markdown("---")
    # Example Jobs
    st.subheader("Senior Python Developer")
    st.caption("Location: Bangalore (Hybrid) | Experience: 5+ Years")
    st.button("Apply Now", key="job1")
    
    st.subheader("Operations Manager")
    st.caption("Location: Remote (US Firm) | Experience: 8+ Years")
    st.button("Apply Now", key="job2")

else:
    st.title(page)
    st.info(f"The {page} dashboard is currently active and secure.")

# 6. FOOTER
st.divider()
st.markdown("<p style='text-align:center; color:#999;'>© 2026 Hirenec Solutions Pvt Ltd | Authorized Executive Portal</p>", unsafe_allow_html=True)

