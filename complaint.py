import streamlit as st
from db import get_connection

def complaint_page():

    st.header("File Complaint")

    name = st.text_input("Name")
    phone = st.text_input("Phone")
    address = st.text_area("Address")

    crime_type = st.selectbox("Crime Type", ["Theft","Robbery","Murder","Cyber Crime","Assault"])
    description = st.text_area("Description")
    location = st.text_input("Location")

    if st.button("Submit Complaint"):

        conn = get_connection()
        cursor = conn.cursor()

        # Insert Citizen
        cursor.execute(
            "INSERT INTO Citizen(name,phone,address) VALUES (?,?,?)",
            (name, phone, address)
        )

        cursor.execute("SELECT @@IDENTITY")
        citizen_id = cursor.fetchone()[0]

        # Insert Complaint
        cursor.execute(
            """INSERT INTO Complaint(citizen_id,crime_type,description,location)
               VALUES (?,?,?,?)""",
            (citizen_id, crime_type, description, location)
        )

        cursor.execute("SELECT @@IDENTITY")
        complaint_id = cursor.fetchone()[0]

        # Insert Crime
        cursor.execute(
            """INSERT INTO Crime(complaint_id,crime_type,description,location)
               VALUES (?,?,?,?)""",
            (complaint_id, crime_type, description, location)
        )

        conn.commit()
        st.success("Complaint Submitted Successfully!")