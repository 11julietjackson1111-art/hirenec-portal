import streamlit as st

# 1. PAGE SETUP
st.set_page_config(page_title="Hirenec Solutions | Executive Search", page_icon="🏢", layout="wide")

# 2. THE DESIGN ENGINE (Every detail polished)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Playfair+Display:wght@700&display=swap');

    /* Global Foundation */
    .stApp {
        background: #fcfcfc;
        font-family: 'Outfit', sans-serif;
    }

    /* THE LOGO & NAV HEADER */
    .nav-header {
        background: #001f3f;
        padding: 40px 80px;
        border-bottom: 5px solid #D4AF37;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }
    .logo-badge {
        background: #D4AF37;
        color: #001f3f;
        font-weight: 800;
        font-size: 32px;
        padding: 10px 25px;
        border-radius: 4px;
        display: inline-block;
        margin-bottom: 15px;
    }
    .main-brand {
        font-size: 50px;
        font-weight: 800;
        color: white;
        letter-spacing: -1.5px;
        margin: 0;
    }
    .tagline {
        color: #D4AF37;
        letter-spacing: 5px;
        font-weight: 600;
        text-transform: uppercase;
        font-size: 14px;
        margin-top: 10px;
    }

    /* HERO CONTENT */
    .hero-container {
        text-align: center;
        padding: 100px 10%;
        background: white;
    }
    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: 64px;
        color: #001f3f;
        line-height: 1.1;
        margin-bottom: 30px;
    }

    /* STAT CARDS - VISIBLE & SPOT ON */
    .stat-row {
        display: flex;
        justify-content: center;
        gap: 30px;
        margin-top: -50px;
        margin-bottom: 60px;
    }
    .stat-card {
        background: white;
        width: 250px;
        padding: 40px 20px;
        border-radius: 8px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.06);
        border: 1px solid #eee;
        text-align: center;
    }
    .stat-val { color: #001f3f; font-size: 44px; font-weight: 800; }
    .stat-lab { color: #D4AF37; font-weight: 600; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; }

    /* DIRECTOR BOX */
    .director-section {
        background: #001f3f;
        border-radius: 12px;
        padding: 60px;
        color: white;
        margin: 50px 10%;
        display: flex;
        align-items: center;
        gap: 50px;
    }
    .director-info h2 { font-family: 'Playfair Display', serif; color: #D4AF37; font-size: 42px; margin: 0; }
    .director-info p { font-size: 18px; opacity: 0.9; line-height: 1.8; }

    /* SIDEBAR NAV */
    [data-testid="stSidebar"] { background-color: #f8f9fa !important; border-right: 1px solid #ddd; }
    .stRadio p { font-size: 20px !important; font-weight: 600 !important; color: #001f3f !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER
st.markdown("""
    <div class="nav-header">
        <div class="logo-badge">HS</div>
        <h1 class="main-brand">HIRENEC SOLUTIONS</h1>
        <p class="tagline">Precision | People | Performance</p>
    </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR
with st.sidebar:
    st.markdown("<br><br>", unsafe_allow_html=True)
    page = st.radio("PORTAL MENU", ["HOME", "JOB BOARD", "RECRUITER HUB", "ADMIN PANEL"])
    st.divider()
    st.caption("Official Executive Portal | 2026")

# 5. PAGE LOGIC
if page == "HOME":
    # Hero
    st.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">Elite Recruitment for <br>Industry Leaders.</h1>
            <p style="font-size:20px; color:#666; max-width:700px; margin: 0 auto;">
                Hirenec Solutions is a premier executive search firm based in Bangalore. 
                We specialize in connecting high-performance professionals with world-class organizations.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Stats
    st.markdown("""
        <div class="stat-row">
            <div class="stat-card">
                <div class="stat-val">10K+</div>
                <div class="stat-lab">Candidates</div>
            </div>
            <div class="stat-card">
                <div class="stat-val">500+</div>
                <div class="stat-lab">Clients</div>
            </div>
            <div class="stat-card">
                <div class="stat-val">98%</div>
                <div class="stat-lab">Retention</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Director Section
    st.markdown("""
        <div class="director-section">
            <div class="director-info">
                <h2>Director Juliet Jackson</h2>
                <p style="color:#D4AF37; font-weight:700; text-transform:uppercase; letter-spacing:2px; font-size:14px;">Founder & Strategic Lead</p>
                <p>
                    With over a decade of expertise in international recruitment, Juliet Jackson 
                    has built Hirenec Solutions into a trusted name for honest, data-driven hiring. 
                    Based in Bangalore, the firm serves as a bridge for talent looking to excel in 
                    global markets.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Reviews
    st.write("##")
    st.markdown("<h2 style='text-align:center; color:#001f3f; font-family:Playfair Display;'>Candidate Experiences</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.info("**Arjun M.** | *Senior Software Engineer*\n\n'The most professional recruitment experience I've had in India. Juliet's team truly understands your career goals.'")
    with c2:
        st.info("**Sarah L.** | *Operations Manager*\n\n'Hirenec managed my transition into a US-based firm perfectly. Their precision is unmatched.'")

# 6. FOOTER
st.markdown("""
    <div style="background:#001f3f; padding:50px; color:white; text-align:center; margin-top:100px;">
        <p>📍 The Estate, Dickenson Road, Bangalore</p>
        <p>© 2026 Hirenec Solutions Pvt Ltd | Official Portal</p>
    </div>
    """, unsafe_allow_html=True)

