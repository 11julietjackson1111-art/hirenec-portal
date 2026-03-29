import streamlit as st

# 1. ELITE CONFIGURATION
st.set_page_config(page_title="Hirenec Solutions | Executive Search", page_icon="🏢", layout="wide")

# 2. THE "SPOT-ON" DESIGN ENGINE
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Playfair+Display:ital,wght@0,700;1,700&display=swap');

    /* Background & Global Reset */
    .stApp {
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
        font-family: 'Outfit', sans-serif;
    }

    /* PREMIUM TOP NAVIGATION LOGO */
    .top-nav {
        background: #001f3f;
        padding: 30px 80px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 4px solid #D4AF37; /* Royal Gold */
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    .logo-container { display: flex; align-items: center; gap: 15px; }
    .logo-symbol {
        background: #D4AF37;
        color: #001f3f;
        font-weight: 800;
        font-size: 28px;
        width: 60px;
        height: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(212,175,55,0.4);
    }
    .brand-name
