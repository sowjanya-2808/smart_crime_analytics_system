import streamlit as st
import pandas as pd
from db import get_connection

def investigation_page():

    st.header("Investigation Management")

    conn = get_connection()
    cursor = conn.cursor()

    # Show all crimes
    df = pd.read_sql("SELECT * FROM Crime", conn)
    st.dataframe(df)

    st.subheader("Update Investigation Status")

    crime_id = st.number_input("Enter Crime ID", min_value=1)
    
    status = st.selectbox("Status", [
        "Pending",
        "In Progress",
        "Closed",
        "Completed"   # ✅ Added
    ])

    remarks = st.text_area("Remarks")

    if st.button("Update Status"):
        cursor.execute(
            """INSERT INTO Investigation(crime_id, status, remarks)
               VALUES (?,?,?)""",
            (crime_id, status, remarks)
        )
        conn.commit()
        st.success("Investigation Updated Successfully")

    # DELETE OPTION
    st.subheader("Delete Crime Record")

    delete_id = st.number_input("Enter Crime ID to delete", min_value=1)

    if st.button("Delete Crime"):
        try:
            cursor.execute("DELETE FROM Crime WHERE crime_id=?", (delete_id,))
            conn.commit()
            st.warning("Crime Record Deleted")
        except:
            st.error("Cannot delete due to related records")