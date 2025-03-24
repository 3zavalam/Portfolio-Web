import streamlit as st

# Cambiar el fondo de la página usando CSS
st.set_page_config(page_title="Project", layout="centered")

st.write("## Dashboard Overview")
st.write("""
This project features two dashboards created by scraping data from **SofaScore** and **Fotmob**:

- **Match Recap Dashboard**: Key stats, shot data, and team performance.
- **Shot Maps Dashboard**: Detailed shot maps and **Player of the Match**.
""")

col1, col2 = st.columns(2)
with col1:
    st.write("Check out the **full report** for a detailed explanation of the dashboards.")
with col2:
    with open("./resources/1dashboard/Match Report Analysis Project.pdf", "rb") as pdf_file:
        st.download_button(
            label="Download the full report (PDF)",
            data=pdf_file,
            file_name="Match Report Analysis Project.pdf",
            mime="application/pdf"
        )
    st.write("""[Source code on GitHub](https://github.com/3zavalam/Match-Report-Analysis)""")
st.write("### Post-Match Dashboard")
st.write("""
The aim of this dashboard is to present the most relevant match information in a concise and user-friendly way. 
It includes key statistics that provide insights into the match's dynamics, helping users easily interpret the game’s performance."""
)
st.image("./resources/1dashboard/dashboard.png")

st.write("""Key features of the dashboard:
- **Best Player Stats:** Displays detailed statistics of the top-performing player in the match.
- **Shot Maps:** Visual representation of shots taken by each team, showing their location and accuracy.
- **Match Momentum:** A graph illustrating the progression of the match, highlighting key moments and shifts in performance.
- **Other Stats:** Includes additional metrics such as possession, expected goals, and more, to give a comprehensive overview of the match.
""")

st.write("### Shot Maps")
st.write("""
This section provides a detailed view of the shots taken during the match. The maps highlight the shooting activity of both the **Most Valuable Player (MVP)** and their respective **team**.""")
col1, col2 = st.columns(2)
with col1:
    st.image("./resources/1dashboard/playerShotmap.png")
with col2:
    st.image("./resources/1dashboard/teamShotmap.png")

st.write("""Key features of the shot maps:
- **Player Shot Map:** Displays the shots taken by the MVP, showing their location on the pitch and the accuracy of each attempt.
- **Team Shot Map:** Illustrates the shot distribution for the entire team, highlighting key areas where the team focused their attack.
""")

