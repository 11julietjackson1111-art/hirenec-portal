import streamlit as st

# 1. ELITE CONFIGURATION
st.set_page_config(
    page_title="Hirenec Solutions | Executive Recruitment Portal",
    page_icon="🏢",
    layout="wide"
)

# 2. THE "WOW" DESIGN ENGINE (Custom CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');

    /* Global Foundation */
    .stApp {
        background-color: #FFFFFF;
        font-family: 'Inter', sans-serif;
    }

    /* THE TOP NAVIGATION BAR */
    .nav-bar {
        background-color: #002349;
        padding: 15px 50px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
        border-bottom: 4px solid #C5A059; /* Gold Accent */
        margin-bottom: 30px;
    }

    /* LOGO & BRANDING */
    .brand-logo {
        font-family: 'Playfair Display', serif;
        font-size: 32px;
        font-weight: 700;
        color: #C5A059;
        text-decoration: none;
    }

    .brand-tagline {
        font-size: 12px;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #FFFFFF;
        margin-top: -5px;
    }

    /* HERO SECTION */
    .hero-section {
        background: linear-gradient(rgba(0,35,73,0.9), rgba(0,35,73,0.9)), 
                    url('https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80&w=1200');
        background-size: cover;
        padding: 100px 50px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 50px;
    }

    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: 60px;
        margin-bottom: 10px;
    }

    .hero-sub {
        font-size: 20px;
        font-weight: 300;
        color: #C5A059;
        margin-bottom: 30px;
    }

    /* CARDS */
    .stat-card {
        background: #F8F9FA;
        padding: 30px;
        border-radius: 15px;
        border-top: 5px solid #002349;
        text-align: center;
        transition: 0.3s;
    }
    .stat-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }

    /* BUTTONS */
    .stButton>button {
        background-color: #C5A059 !important;
        color: #002349 !important;
        font-weight: 700 !important;
        border-radius: 5px !important;
        border: none !important;
        padding: 12px 30px !important;
        text-transform: uppercase;
    }

    /* FOOTER */
    .footer {
        background-color: #002349;
        color: #FFFFFF;
        padding: 40px;
        border-radius: 15px 15px 0 0;
        margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. TOP NAVIGATION (Visible on all pages)
st.markdown("""
    <div class="nav-bar">
        <div>
            <div class="brand-logo">HIRENEC</div>
            <div class="brand-tagline">Solutions Pvt Ltd</div>
        </div>
        <div style="font-size: 14px; font-weight: 600;">
            EXECUTIVE SEARCH & RECRUITMENT PORTAL
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR (Simplified for a professional feel)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100) # Professional Icon
    st.markdown("### PORTAL MENU")
    page = st.radio("Navigate", ["HOME", "JOB BOARD", "RECRUITER HUB", "ADMIN PANEL"], label_visibility="collapsed")
    st.divider()
    st.success("Log-in Status: Secure")

# 5. PAGE LOGIC
if page == "HOME":
    # Hero Header
    st.markdown("""
        <div class="hero-section">
            <h1 class="hero-title">Precision. People. Performance.</h1>
            <p class="hero-sub">The Premier Gateway for Global Talent and Industry Leaders</p>
        </div>
    """, unsafe_allow_html=True)

    # Core Value Columns
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="stat-card"><h3>10k+</h3><p>Verified Candidates</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="stat-card"><h3>500+</h3><p>Corporate Partners</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="stat-card"><h3>98%</h3><p>Placement Success</p></div>', unsafe_allow_html=True)

    st.write("##")
    
    # Director Section
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        st.image("https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&q=80&w=400", caption="Director: Juliet Jackson")
    with col_txt:
        st.markdown("### From the Desk of the Director")
        st.info("**Juliet Jackson**")
        st.write("""
            At **Hirenec Solutions**, we believe that the right person in the right role 
            changes the trajectory of a company. Our mission is to provide an 
            unfiltered, honest, and high-performance recruitment experience 
            for both the seeker and the employer. 
            
            Located in the heart of **Bangalore**, we bridge the gap between 
            ambition and opportunity.
        """)
        st.button("Contact Our Office")

elif page == "JOB BOARD":
    st.markdown("## 🔍 Live Career Opportunities")
    st.text_input("Search by Keyword (e.g. Python, HR, Sales)")
    
    # Mock Job List
    for i in range(3):
        with st.container():
            st.markdown(f"""
            <div style="background:#FFF; border:1px solid #DDD; padding:20px; border-radius:10px; margin-bottom:10px;">
                <h3 style="color:#002349; margin:0;">Senior Software Engineer - Phase {i+1}</h3>
                <p style="color:#C5A059; font-weight:bold;">Bangalore | Full-Time</p>
                <p>Responsibility: Developing scalable backend systems using Python and PHP.</p>
            </div>
            """, unsafe_allow_html=True)
            st.button(f"Apply Now", key=f"btn_{i}")

elif page == "ADMIN PANEL":
    st.markdown("## ⚙️ Super Admin Control")
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("Total Revenue", "₹5.5L", "+12%")
        st.metric("Active Recruiters", "42", "+5")
    with col_b:
        st.write("### Recent Activity")
        st.table({"User": ["User_102", "Rec_99"], "Action": ["New Profile", "Job Posted"], "Time": ["2m ago", "15m ago"]})

# 6. SHARED FOOTER
st.markdown("""
    <div class="footer">
        <div style="display: flex; justify-content: space-between;">
            <div>
                <h2 style="color: #C5A059; margin:0;">HIRENEC SOLUTIONS</h2>
                <p>The Estate, Dickenson Road, Bangalore, KA</p>
            </div>
            <div style="text-align: right;">
                <p>Email: contact@hirenecsolutions.com</p>
                <p>© 2026 Hirenec Solutions Pvt Ltd | All Rights Reserved</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

