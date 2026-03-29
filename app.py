import streamlit as st

# 1. PAGE SETUP (Professional Browser Tab Title)
st.set_page_config(
    page_title="Hirenec Solutions | Official Portal",
    page_icon="💼",
    layout="wide"
)

# 2. THE DESIGN ENGINE (Professional CSS - No "Bubbly" Fonts)
st.markdown("""
    <style>
    /* Import Clean, Corporate Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    /* Global Styling */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #1E1E1E;
    }

    /* Professional Navbar Color */
    [data-testid="stHeader"] {
        background-color: #002D62;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #F8F9FA;
        border-right: 1px solid #E0E0E0;
    }

    /* Main Header - Sharp and Elegant */
    .main-title {
        font-size: 48px;
        font-weight: 700;
        color: #002D62;
        letter-spacing: -1.5px;
        margin-bottom: 0px;
        line-height: 1.2;
    }

    /* Subtitle with a nice underline */
    .sub-title {
        font-size: 16px;
        font-weight: 600;
        color: #555555;
        letter-spacing: 2px;
        text-transform: uppercase;
        border-bottom: 2px solid #002D62;
        width: fit-content;
        padding-bottom: 8px;
        margin-bottom: 25px;
    }

    /* Information Bar at the Bottom */
    .footer-bar {
        background-color: #002D62;
        color: white;
        padding: 15px;
        border-radius: 8px;
        font-size: 14px;
        margin-top: 40px;
        display: flex;
        justify-content: space-between;
    }

    /* Job Card Styling for the Job Board */
    .job-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #E0E0E0;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.02);
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("### Hirenec Menu")
    choice = st.radio(
        "Navigate to:",
        ["Home", "Job Board", "Recruiter Hub", "Admin"],
        index=0
    )
    st.divider()
    st.caption("v1.0.2 | © 2026 Hirenec Solutions")

# 4. PAGE CONTENT LOGIC
if choice == "Home":
    # Layout with an image and text
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # A professional office/recruitment image
        st.image("https://images.unsplash.com/photo-1497215728101-856f4ea42174?auto=format&fit=crop&q=80&w=500", use_container_width=True)
    
    with col2:
        st.markdown('<p class="main-title">HIRENEC SOLUTIONS</p>', unsafe_allow_html=True)
        st.markdown('<p class="sub-title">Precision | People | Performance</p>', unsafe_allow_html=True)
        
        st.write("""
        Welcome to the official recruitment portal of **Hirenec Solutions Pvt Ltd**. 
        We specialize in bridging the gap between top-tier talent and industry-leading organizations. 
        Explore our current openings or manage your hiring needs through our secure dashboard.
        """)
        
        # Professional Call to Action
        if st.button("View Current Openings"):
            st.info("Redirecting to Job Board...")

    # Info Bar
    st.markdown(f"""
        <div class="footer-bar">
            <span>📍 The Estate, Dickenson Road, Bangalore</span>
            <span>Director: Juliet Jackson</span>
        </div>
    """, unsafe_allow_html=True)

elif choice == "Job Board":
    st.markdown('<p class="main-title">JOB BOARD</p>', unsafe_allow_html=True)
    st.write("Browse our latest career opportunities.")
    
    # Example Job Card
    st.markdown("""
        <div class="job-card">
            <h3 style="margin:0; color:#002D62;">Senior Talent Acquisition Specialist</h3>
            <p style="color:#666; font-size:14px;">Bangalore | Full-Time | Remote Friendly</p>
            <p>Seeking an experienced recruiter to manage high-volume technical hiring for our US-based clients.</p>
        </div>
    """, unsafe_allow_html=True)
    st.button("Apply Now", key="apply_1")

else:
    st.title(choice)
    st.write(f"This is the {choice} section. Content coming soon.")
