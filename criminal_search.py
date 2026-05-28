import streamlit as st
import pandas as pd
from db import get_connection

def criminal_search():

    st.header("Criminal Search")

    name = st.text_input("Enter Criminal Name")

    if st.button("Search"):

        conn = get_connection()

        df = pd.read_sql(
            "SELECT * FROM Criminal WHERE name=?",
            conn,
            params=[name]
        )

        if not df.empty:
            st.dataframe(df)
        else:
            st.warning("No record found")