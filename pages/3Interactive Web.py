import streamlit as st

st.title("Interactive Web")

st.write("""
This project is an **interactive** web application built using the **Streamlit** library to create a **dynamic** and **engaging** user experience.  
It allows users to generate radar charts, shot maps for players, and team statistics for specific matches.  
You can find the **source code** on my [GitHub](https://github.com/3zavalam/Interactive-Web).
""")

st.video("./resources/3web/prueba portfolio web.mp4", autoplay=False)

st.write("### How the data is gathered:")
st.write("""
The project includes three main sections: **Radar**, **Shotmaps**, and **Team Shotmaps**. Here's how the data is gathered and processed:

- **Radar:** Every Sunday night, a script runs to update the data with the latest player and team stats. We scrape the main statistical tables for outfield players and goalkeepers from **FBref**, then merge them to generate the radar charts.

- **Shotmaps:** For individual player shot maps, we use **FotMob**. We identify the top scorers, extract their names and IDs, and organize them into a dictionary with the team name as the key and the player ID and name as values.

- **Team Shotmaps:** These are generated for specific matches. By using the match ID (found in the FotMob URL), we fetch a `.csv` file containing all the shots taken by each team in that match.
""")

st.write('---')
st.write("**Disclaimer:** This project is currently not functional due to recent changes in the structure of the websites used for data scraping.")
