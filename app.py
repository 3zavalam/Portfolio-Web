import streamlit as st

# Set page configuration
st.set_page_config(page_title="My Data Analyst Portfolio", layout="centered")

# Header
st.title("Welcome to My Data Analyst Portfolio")

col1, col2 = st.columns([3, 1]) 
with col1:
    st.write("Hi! I'm Emilio Zavala, a passionate and detail-oriented data analyst with skills in Python, SQL and Power BI. I love transforming raw data into actionable insights.")
with col2:
    st.image("./resources/_330192171801.png", caption="Hi, I'm Emilio!")

# Skills Section
st.write("### Skills:")
st.write("""
- 📊 Data Analysis (Python: Pandas, NumPy)
- 📈 Data Visualization (Matplotlib, Power BI)
- 🗂️ Database Management (SQL)
""")

# Portfolio Projects
st.write("### Portfolio Projects:")
st.write("Click on each project to learn more about them:")
st.markdown("""
1. [**Post-Match Dashboard**](/1dashboard.py)  
   - Tools: Matplotlib, Scraping (BeautifulSoup)  
   - Created an interactive sales dashboard for insights into regional performance.
         
---
2. [**xG Prediction Model**](/2xGmodel.py)  
   - Tools: Python (Scikit-learn, Pandas)  
   - Built a machine learning model to predict customer churn.
         
---
3. [**Streamlit Web**](/3streamlitWeb.py)  
   - Tools: Python (BeautifulSoup, NLTK)  
   - Analyzed customer reviews for product sentiment trends.
""")

# Contact Section
st.write("### Contact Me:")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/emilio-zavala-miceli-86595927b/)")
with col2:
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/3zavalam)")
with col3:
    st.markdown("[![Email](https://img.shields.io/badge/Email-Contact-red)](mailto:your_email@example.com)")


# Footer
st.markdown("---")
st.write("© 2025 Emilio Zavala. All rights reserved.")