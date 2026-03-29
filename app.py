import streamlit as st

# 1. PAGE SETUP
st.set_page_config(page_title="Hirenec Solutions | Official Portal", page_icon="💼", layout="wide")

# 2. THE PREMIUM DESIGN ENGINE (The "Wow" Factor)
st.markdown("""
    <style>
    /* Modern, High-End Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700;800&family=Playfair+Display:wght@700&display=swap');

    /* Global Body Styling */
    .stApp {
        background-color: #FFFFFF;
        font-family: 'Outfit', sans-serif;
        color: #1E1E1E;
    }

    /* THE COMPANY LOGO & HEADER SECTION */
    .header-banner {
        background: linear-gradient(90deg, #002349 0%, #004080 100%);
        padding: 50px 80px;
        color: white;
        border-bottom: 6px solid #C5A059; /* Elegant Gold Accent */
        display: flex;
        align-items: center;
        gap: 30px;
        margin-bottom: 40px;
    }
    
    .logo-square {
        background: #C5A059;
        color: #002349;
        font-family: 'Outfit', sans-serif;
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

    .brand-title {
        font-family: 'Outfit', sans-serif;
        font-size: 52px;
        font-weight: 800;
        margin: 0;
        letter-spacing: -1.5px;
        line-height: 1;
    }

    .brand-tagline {
        font-size: 14px;
        letter-spacing: 5px;
        text-transform: uppercase;
        color: #C5A059;
        font-weight: 600;
        margin-top: 10px;
    }

    /* THE STAT CARDS (Fixed Visibility) */
    .stat-container {
        display: flex;
        gap: 20px;
        margin: 20px 0;
    }
    .stat-card {
        background: #F8F9FA;
        flex: 1;
        padding: 40px 20px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #E0E0E0;
        transition: 0.3s;
    }
    .stat-card:hover { transform: translateY(-5px); border-color: #C5A059; }
    .stat-number { color: #002349; font-size: 42px; font-weight: 800; }
    .stat-label { color: #666; font-weight: 600; text-transform: uppercase; font-size: 12px; letter-spacing: 1px; }

    /* REVIEWS SECTION */
    .review-box {
        background: #002349;
        color: white;
        padding: 40px;
        border-radius: 20px;
        margin: 40px 0;
    }
    .testimonial {
        font-style: italic;
        font-size: 18px;
        margin-bottom: 15px;
        border-left: 4px solid #C5A059;
        padding-left: 20px;
    }

    /* DIRECTOR SECTION */
    .director-card {
        background: #FFFFFF;
        border-radius: 20px;
        padding: 30px;
        border: 1px solid #E0E0E0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    }

    /* SIDEBAR NAVIGATION */
    [data-testid="stSidebar"] { background-color: #F0F2F6 !important; }
    .stRadio p { font-size: 18px !important; font-weight: 700 !important; color: #002349 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. TOP BANNER & LOGO
st.markdown("""
    <div class="header-banner">
        <div class="logo-square">HS</div>
        <div>
            <h1 class="brand-title">HIRENEC SOLUTIONS</h1>
            <div class="brand-tagline">Precision | People | Performance</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR MENU
with st.sidebar:
    st.markdown("### 🏢 NAVIGATION")
    choice = st.radio("Menu", ["HOME", "JOB BOARD", "RECRUITER HUB", "ADMIN PANEL"], label_visibility="collapsed")
    st.divider()
    st.info("Directing professional growth since 2026.")

# 5. PAGE CONTENT
if choice == "HOME":
    # Introduction
    st.markdown("### Professional Executive Recruitment & Search")
    st.write("Welcome to the official portal of **Hirenec Solutions Pvt Ltd**. We bridge the gap between world-class talent and industry-leading organizations with an unfiltered, honest approach to recruitment.")

    # Stat Cards (Fixed "Blank" issue)
    st.write("##")
    st.markdown('<div class="stat-container">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="stat-card"><div class="stat-number">10K+</div><div class="stat-label">Verified Candidates</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="stat-card"><div class="stat-number">500+</div><div class="stat-label">Corporate Clients</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="stat-card"><div class="stat-number">98%</div><div class="stat-label">Retention Rate</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Director Section
    st.write("##")
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        # High-quality corporate image placeholder
        st.image("https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=500", caption="Director Juliet Jackson")
    with col_txt:
        st.markdown("""
            <div class="director-card">
                <h2 style="color:#002349; font-family:'Playfair Display';">Juliet Jackson</h2>
                <p style="color:#C5A059; font-weight:700; text-transform:uppercase; margin-top:-10px;">Director & Founder</p>
                <p>Based in the heart of <b>Bangalore</b>, Juliet Jackson has built Hirenec Solutions into a premier gateway for global recruitment. 
                Her vision focuses on precision-driven hiring that fuels both candidate performance and organizational growth.</p>
                <hr style="border:0.5px solid #eee;">
                <p><i>"We don't just fill seats; we provide the human capital that drives global industries."</i></p>
            </div>
        """, unsafe_allow_html=True)

    # Candidate Feedback Section
    st.write("##")
    st.markdown("### 💬 Candidate Feedback & Reviews")
    rev1, rev2 = st.columns(2)
    with rev1:
        st.markdown("""<div class="review-box">
            <p class="testimonial">"The most professional recruitment experience I've had. They understood my skills perfectly and placed me in a top firm within weeks."</p>
            <p><b>— Rajesh K.</b> | Senior Developer</p>
        </div>""", unsafe_allow_html=True)
    with rev2:
        st.markdown("""

