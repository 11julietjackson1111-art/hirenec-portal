import streamlit as st
import pandas as pd
import os

# 1. Permanent Database Logic (CSV files)
def load_data(filename, columns):
    if os.path.exists(filename):
        return pd.read_csv(filename)
    return pd.DataFrame(columns=columns)

def save_data(df, filename):
    df.to_csv(filename, index=False)

# Initialize files
job_db = load_data("jobs.csv", ["ID", "Title", "Location", "Description"])
app_db = load_data("applications.csv", ["Name", "Email", "Job", "Status"])

# 2. Professional Branding
st.set_page_config(page_title="Hirenec Solutions | Live Portal", layout="wide")
st.markdown('''
    <style>
    .stApp { background: #0a192f; color: white; }
    .card { background: rgba(255,255,255,0.05); padding: 20px; border-radius: 15px; border-left: 5px solid #d4af37; margin-bottom: 15px; }
    .stButton>button { background-color: #d4af37 !important; color: #0a192f !important; font-weight: bold; width: 100%; }
    </style>
    ''', unsafe_allow_html=True)

# 3. Sidebar Navigation
if os.path.exists("116925.jpg"):
    st.sidebar.image("116925.jpg", use_container_width=True)
page = st.sidebar.radio("Hirenec Menu", ["🏠 Home", "🔍 Job Board", "🏢 Recruiter Hub", "⚙️ Admin"])

# 4. Page Logic
if page == "🏠 Home":
    st.markdown("<h1 style='text-align:center;'>HIRENEC SOLUTIONS</h1>", unsafe_allow_html=True)
    st.write("### Precision | People | Performance")
    st.write("Welcome to the official recruitment portal of Hirenec Solutions Pvt Ltd. Explore our current openings or manage your hiring needs.")
    st.info("📍 The Estate, Dickenson Road, Bangalore | Director: Juliet Jackson")

elif page == "🔍 Job Board":
    st.header("Search Live Jobs")
    if job_db.empty:
        st.warning("No jobs currently active.")
    else:
        for idx, row in job_db.iterrows():
            with st.container():
                st.markdown(f'<div class="card"><h4>{row["Title"]}</h4><p>{row["Location"]}</p></div>', unsafe_allow_html=True)
                with st.expander("View Details & Apply"):
                    st.write(row["Description"])
                    with st.form(f"apply_{idx}"):
                        name = st.text_input("Full Name")
                        email = st.text_input("Email Address")
                        if st.form_submit_button("Submit Application"):
                            new_app = pd.DataFrame([[name, email, row["Title"], "New"]], columns=app_db.columns)
                            app_db = pd.concat([app_db, new_app], ignore_index=True)
                            save_data(app_db, "applications.csv")
                            st.success("Application sent successfully!")

elif page == "🏢 Recruiter Hub":
    st.header("Post a Requirement")
    with st.form("new_job"):
        title = st.text_input("Job Title")
        loc = st.text_input("Location")
        desc = st.text_area("Full Job Description")
        if st.form_submit_button("Post Live"):
            new_job = pd.DataFrame([[len(job_db), title, loc, desc]], columns=job_db.columns)
            job_db = pd.concat([job_db, new_job], ignore_index=True)
            save_data(job_db, "jobs.csv")
            st.success("Job is now live!")

elif page == "⚙️ Admin":
    st.header("Candidate Tracking System")
    st.write("### Total Applications Received")
    st.dataframe(app_db, use_container_width=True)

