import streamlit as st

def login():

    st.subheader("Login")

    role = st.selectbox("Login As", ["Citizen","Officer","Admin"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if role == "Admin" and username == "admin" and password == "admin123":
            st.session_state.logged_in = True
            st.session_state.role = "Admin"

        elif role == "Officer" and username == "officer" and password == "officer123":
            st.session_state.logged_in = True
            st.session_state.role = "Officer"

        elif role == "Citizen":
            st.session_state.logged_in = True
            st.session_state.role = "Citizen"

        else:
            st.error("Invalid Login")