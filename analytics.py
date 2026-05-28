import streamlit as st
import pandas as pd
from db import get_connection

def analytics_page():

    st.header("Crime Analytics")

    conn = get_connection()

    df = pd.read_sql("SELECT crime_type FROM Crime", conn)

    st.bar_chart(df["crime_type"].value_counts())