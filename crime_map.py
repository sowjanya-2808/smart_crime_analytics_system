import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from db import get_connection

def crime_map():

    st.header("Crime Map")

    conn = get_connection()

    df = pd.read_sql(
        "SELECT crime_type, location FROM Crime",
        conn
    )

    # ✅ Updated Location → Coordinates mapping
    location_coords = {
        "Vijayawada": [16.5062, 80.6480],
        "Gudlavalleru": [16.3333, 81.0500],
        "Machilipatnam": [16.1875, 81.1389],
        "Gudivada": [16.4350, 80.9950],
        "Hanuman Junction": [16.5200, 80.8000],
        "Gannavaram": [16.5400, 80.8000],
        "Pedana": [16.2550, 81.1430],
        "Pamarru": [16.3330, 80.9600]
    }

    m = folium.Map(location=[16.5062, 80.6480], zoom_start=10)

    for i in range(len(df)):
        loc = df["location"][i]
        crime = df["crime_type"][i]

        if loc in location_coords:
            lat, lon = location_coords[loc]

            # 🎨 Color logic (same as before)
            if crime == "Murder":
                color = "red"
            elif crime == "Theft":
                color = "blue"
            elif crime == "Robbery":
                color = "orange"
            elif crime == "Cyber Crime":
                color = "purple"
            elif crime == "Assault":
                color = "black"
            else:
                color = "green"

            folium.Marker(
                [lat, lon],
                popup=f"{crime} - {loc}",
                icon=folium.Icon(color=color)
            ).add_to(m)

    st_folium(m)