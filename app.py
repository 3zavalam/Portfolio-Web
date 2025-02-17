import streamlit as st

st.set_page_config(page_title="My Data Analyst Portfolio", layout="centered")

st.title("Welcome to My Portfolio")

st.write(
    "Hi! I'm Emilio Zavala, a Computer Systems Engineering student with a strong interest in data analytics. "
    "I enjoy working with data, creating visualizations, and uncovering insights that can drive better decisions. "
    "I'm especially interested in sports analytics, where data helps identify patterns, improve strategies, and "
    "enhance performance. I work with Python, SQL, and Power BI to process and present data in a clear and impactful way. "
    "As I continue learning and developing my skills, I aim to apply data-driven approaches to real-world problems."
)

col1, col2 = st.columns(2)
with col1:
    st.write("### Skills:")
    st.write("""
        - 📊 Data Analysis (Python: Pandas, NumPy)
        - 📈 Data Visualization (Matplotlib, Power BI)
        - 🗂️ Database Management (SQL)
    """)
with col2:
    with open("./resources/cv_2025.pdf", "rb") as file:
        st.download_button(
            label="Download My CV",
            data=file,
            file_name="Emilio_Zavala_CV.pdf",
            mime="application/pdf"
        )


st.write("### Portfolio Projects")
st.write("Click on each project to learn more about them:")
st.markdown("""
1. [**Post-Match Dashboard**](/dashboard)  
   - Tools: Matplotlib, Scraping (BeautifulSoup)  
   - Created an interactive sales dashboard for insights into regional performance.
         
---
2. [**xG Prediction Model**](/xGmodel)  
   - Tools: Python (Scikit-learn, Pandas)  
   - Built a machine learning model to predict customer churn.
         
---
3. [**Streamlit Web**](/interactiveWeb)  
   - Tools: Python (BeautifulSoup, NLTK)  
   - Analyzed customer reviews for product sentiment trends.
""")


st.write("### Contact Me:")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/emilio-zavala-miceli-86595927b/)")
with col2:
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/3zavalam)")
with col3:
    st.markdown("[![Email](https://img.shields.io/badge/Email-Contact-red)](mailto:your_email@example.com)")

st.markdown("---")
st.write("© 2025 Emilio Zavala. All rights reserved.")