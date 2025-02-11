# https://github.com/3zavalam/xG-Model
import streamlit as st
import pandas as pd

st.title("Predicting Expected Goals (xG)")

st.write(""" 
In this project, we developed a machine learning model to predict Expected Goals (xG) in football. 
The xG metric quantifies the likelihood of a goal being scored from a particular shot based on 
various factors such as shot location, angle, and body part. 
                
You can find the **source code** for this project on my [GitHub](https://github.com/3zavalam/xG-Model).
""")

st.subheader("Data Collection")
col1, col2 = st.columns(2)
with col1: 
    st.write("""
    The dataset used in this study was retrieved using the **mplsoccer** library, which provides access 
    to detailed match event data from the **2022 FIFA World Cup**, collected by **StatsBomb**.  
     
    Each shot includes key attributes such as **location, angle, body part used, and shot type**, 
    which help improve the accuracy of our model.
    """)
    with open("./resources/2xGmodel/xG model report.pdf", "rb") as pdf_file:
        st.download_button(
            label="Download the full report (PDF)",
            data=pdf_file,
            file_name="xG model report.pdf",
            mime="application/pdf"
        )
with col2:
    st.image("./resources/2xGmodel/allShots.png", caption='All 2022 WC shots')

st.markdown("**Key dataset statistics:**")
st.write("""
- Total Matches: **64**
- Total Shots: **1453**
- Avg Shots per Match: **22.7**
""")

st.subheader("Modeling")
st.write("""
Two models were tested: **Linear Regression** and **Logistic Regression**. 
The latter was chosen as the final model due to its ability to avoid negative xG values.
""")


st.markdown("**Model Performance:**")
match_results = pd.DataFrame({
    "home_team_name": ["Serbia", "Argentina"],
    "away_team_name": ["Switzerland", "Australia"],
    "home_goal": [2, 2],
    "home_xg": [1.50, 1.35],
    "home_xg_sb": [1.189, 1.48],
    "away_goal": [3, 0],
    "away_xg": [2.44, 0.582],
    "away_xg_sb": [3.10, 0.42]
})
st.dataframe(match_results)

st.write("Our final R2 score was **0.187**, meanwhile the R2 of the statsbomb model is **0.240**")
