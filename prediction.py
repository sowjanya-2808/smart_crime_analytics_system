import streamlit as st

def prediction_page():

    st.header("Crime Prediction")

    location = st.text_input("Enter Location")

    if st.button("Predict"):
        st.success(f"High risk of Theft in {location}")