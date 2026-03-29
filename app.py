import streamlit as st

# 1. PAGE SETUP
st.set_page_config(page_title="Hirenec Solutions | Executive Search", page_icon="🏢", layout="wide")

# 2. THE DESIGN ENGINE (Polished and Fixed)
st.markdown("""
    <style>
    /* Premium Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;800&family=Playfair+Display:wght@700&display=swap');

    .stApp {
        background-color: #FFFFFF;
        font-family: 'Outfit', sans-serif;
    }

    /* THE LOGO & HEADER AREA */
    .header-banner {
        background: #002349;
        padding: 40px 60px;
        color: white;
        border-bottom: 5px solid #C5A059;
        display: flex;
        align-items: center;
        gap: 25px;
    }
    
    .logo-box {
        background: #C5A059;
        color: #002349;
        font-weight: 800;
        font-size: 30px;
        width: 70px;
        height: 70px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 8px;
    }

    .brand-title {
        font-size: 48px;
        font-weight: 800;
        margin: 0;
        line-height: 1;
    }

    .brand-tag {
        font-size: 12px;
        letter-spacing: 4px;
        text-transform: uppercase;
        color: #C5A059;
        margin-top: 8px;
    }

    /* STAT CARDS */
    .stat-card {
        background: #F4F7F9;
        padding: 35px 20px;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #E0E0E0;
    }
    .stat-val { color: #002349; font-size: 38px; font-weight: 800; }
    .stat-lab { color: #666; font-size: 12px; text-transform: uppercase; letter-spacing: 1px; }

    /* REVIEWS SECTION */
    .review-card {
        background: #002349;
        color: white;
        padding: 30px;
        border-radius: 15px;
        margin-top: 20px;
    }
    .review-text { font-style: italic; font-size: 16px; border-left: 3px solid #C5A059; padding-left: 15px; }

    /* DIRECTOR BOX */
    .director-box {
        background: white;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #E0E0E0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. TOP BANNER
st.markdown("""
    <div class="header-banner">
        <div class="logo-box">HS</div>
        <div>
            <h1 class="brand-title">HIRENEC SOLUTIONS</h1>
            <div class="brand-tag">Precision | People | Performance</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR
with st.sidebar:
    st.markdown("### NAVIGATION")
    page = st.radio("Go to:", ["HOME", "JOB BOARD", "RECRUITER HUB", "ADMIN"], label_visibility="collapsed")
    st.divider()
    st.info("Director: Juliet Jackson")

# 5. CONTENT
if page == "HOME":
    st.write("##")
    st.markdown("### Executive Recruitment Excellence")
    st.write("Based in Bangalore, **Hirenec Solutions Pvt Ltd** is a premier gateway for high-performance talent and global industry leaders.")

    # Statistics (Visible and Clean)
    st.write("##")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="stat-card"><div class="stat-val">10K+</div><div class="stat-lab">Candidates</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="stat-card"><div class="stat-val">500+</div><div class="stat-lab">Corporate Clients</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="stat-card"><div class="stat-val">98%</div><div class="stat-lab">Success Rate</div></div>', unsafe_allow_html=True)

    # Director Section
    st.write("##")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=500", caption="Director: Juliet Jackson")
    with col2:
        st.markdown("""
            <div class="director-box">
                <h2 style="font-family:'Playfair Display'; color:#002349; margin-top:0;">Director Juliet Jackson</h2>
                <p>Leading with a vision of transparency and precision, Juliet Jackson has established 
                Hirenec as a trusted partner for US and Indian firms. Our focus remains on the 'unfiltered truth' 
                in talent acquisition.</p>
                <p><i>"The right hire doesn't just fill a role; they define the company's future."</i></p>
            </div>
        """, unsafe_allow_html=True)

    # Candidate Reviews
    st.write("##")
    st.markdown("### 💬 Candidate Reviews")
    r1, r2 = st.columns(2)
    with r1:
        st.markdown("""<div class="review-card">
            <p class="review-text">"The most professional team in Bangalore. They matched my skills to the perfect role within two weeks."</p>
            <p>— Arjun K., Senior Developer</p>
        </div>""", unsafe_allow_html=True)
    with r2:
        st.markdown("""<div class="review-card">
            <p class="review-text">"Juliet's guidance during the placement process was honest and incredibly helpful. Highly recommended."</p>
            <p>— Sarah M., Project Lead</p>
        </div>""", unsafe_allow_html=True)

else:
    st.title(page)
    st.info("Section currently under final polish.")

# 6. FOOTER
st.divider()
st.markdown("""
    <div style="text-align:center; padding:20px; color:#888;">
        <p>📍 The Estate, Dickenson Road, Bangalore | © 2026 Hirenec Solutions Pvt Ltd</p>
    </div>
    """, unsafe_allow_html=True)

