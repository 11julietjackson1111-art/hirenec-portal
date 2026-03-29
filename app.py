# 1. THE FOUNDATION
st.set_page_config(page_title="Hirenec Solutions | Elite Recruitment", layout="wide")

# 2. THE "WOW" STYLING (The Best Professional Look)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;800&family=Open+Sans:wght@300;400;600&display=swap');

    /* Background and Global Font */
    .stApp {
        background-color: #050A18; /* Elegant Deep Dark Blue */
        font-family: 'Open Sans', sans-serif;
    }

    /* Professional Sidebar */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 2px solid #002D62;
    }
    [data-testid="stSidebar"] .stRadio p {
        color: #002D62 !important;
        font-size: 18px !important;
        font-weight: 600 !important;
    }

    /* BIG BOLD COMPANY NAME */
    .company-name {
        font-family: 'Montserrat', sans-serif;
        font-size: 64px !important;
        font-weight: 800;
        color: #FFFFFF;
        margin-bottom: 0px;
        letter-spacing: -2px;
        line-height: 1;
    }

    /* TAGLINE STYLING */
    .tagline {
        font-family: 'Montserrat', sans-serif;
        font-size: 18px;
        font-weight: 400;
        color: #4CC9FE; /* Electric blue accent */
        letter-spacing: 5px;
        text-transform: uppercase;
        margin-top: 10px;
        margin-bottom: 30px;
    }

    /* THE HERO SECTION CARD */
    .hero-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 40px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }

    /* WELCOME TEXT */
    .welcome-text {
        color: #D1D1D1;
        font-size: 20px;
        line-height: 1.6;
        max-width: 700px;
    }

    /* FOOTER BAR */
    .footer-bar {
        background: linear-gradient(90deg, #002D62 0%, #0056b3 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        margin-top: 50px;
        display: flex;
        justify-content: space-between;
        font-weight: 600;
    }

    /* BUTTON OVERRIDE */
    .stButton>button {
        background: #4CC9FE !important;
        color: #050A18 !important;
        font-weight: 700 !important;
        border-radius: 50px !important;
        border: none !important;
        padding: 15px 40px !important;
        transition: 0.3s all ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 20px rgba(76, 201, 254, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("### 🏢 NAVIGATION")
    choice = st.radio("Go to:", ["HOME", "JOB BOARD", "RECRUITER HUB", "ADMIN"], label_visibility="collapsed")
    st.divider()
    st.markdown("#### Hirenec Solutions")
    st.info("Directing professional growth since 2026.")

# 4. MAIN PAGE CONTENT
if choice == "HOME":
    # Layout Header with Logo space
    head_col1, head_col2 = st.columns([1, 5])
    
    with head_col1:
        # A sleek logo placeholder
        st.markdown("""<div style="background:#4CC9FE; width:80px; height:80px; border-radius:15px; display:flex; align-items:center; justify-content:center; font-weight:bold; color:#050A18; font-size:24px;">HS</div>""", unsafe_allow_html=True)

    with head_col2:
        st.markdown('<p class="company-name">HIRENEC SOLUTIONS</p>', unsafe_allow_html=True)
        st.markdown('<p class="tagline">PRECISION | PEOPLE | PERFORMANCE</p>', unsafe_allow_html=True)

    # Hero Content
    st.markdown("""
        <div class="hero-card">
            <p class="welcome-text">
                Welcome to the digital gateway of <b>Hirenec Solutions Pvt Ltd</b>. 
                We are a premier recruitment firm committed to connecting industry-leading 
                enterprises with world-class professional talent. Our precision-driven 
                approach ensures that every match fuels performance and growth.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.write(" ") # Spacer
    if st.button("EXPLORE OPENINGS"):
        st.balloons() # Just for a little "wow" when testing

    # The Info Footer
    st.markdown(f"""
        <div class="footer-bar">
            <span>📍 The Estate, Dickenson Road, Bangalore</span>
            <span>Director: Juliet Jackson</span>
        </div>
    """, unsafe_allow_html=True)

elif choice == "JOB BOARD":
    st.markdown('<p class="company-name" style="font-size:48px !important;">JOB BOARD</p>', unsafe_allow_html=True)
    st.markdown('<p class="tagline">Your Next Career Move Starts Here</p>', unsafe_allow_html=True)
    
    # Modern Job Card
    st.markdown("""
        <div class="hero-card" style="margin-bottom:20px;">
            <h2 style="color:#4CC9FE; margin-bottom:5px;">Senior Technical Recruiter</h2>
            <p style="color:#FFF;"><b>Location:</b> Remote / Bangalore | <b>Salary:</b> Competitive</p>
            <p class="welcome-text">Leading the search for top-tier IT talent for global partners.</p>
        </div>
    """, unsafe_allow_html=True)
    st.button("APPLY NOW")

else:
    st.markdown(f'<p class="company-name">{choice}</p>', unsafe_allow_html=True)
    st.write("Section under construction.")

