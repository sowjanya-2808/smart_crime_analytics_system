
import streamlit as st

from login import login
from dashboard import dashboard
from complaint import complaint_page
from investigation import investigation_page
from analytics import analytics_page
from prediction import prediction_page
from criminal_search import criminal_search
from crime_map import crime_map


st.title("Smart Crime Analytics and Predictive Policing System")

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# If not logged in → show login
if not st.session_state.logged_in:
    login()

else:
    role = st.session_state.role

    # Role-based menu
    if role == "Citizen":
        menu = ["Dashboard", "File Complaint"]

    elif role == "Officer":
        menu = ["Dashboard", "Investigation", "Criminal Search", "Crime Map"]

    else:  # Admin
        menu = ["Dashboard", "Crime Analytics", "Prediction"]

    choice = st.sidebar.selectbox("Menu", menu)

    # Logout button
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.role = None
        st.rerun()

    # Navigation
    if choice == "Dashboard":
        dashboard()

    elif choice == "File Complaint":
        complaint_page()

    elif choice == "Investigation":
        investigation_page()

    elif choice == "Crime Analytics":
        analytics_page()

    elif choice == "Prediction":
        prediction_page()

    elif choice == "Criminal Search":
        criminal_search()

    elif choice == "Crime Map":
        crime_map()
