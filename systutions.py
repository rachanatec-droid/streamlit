import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Define the database file name
DB_FILE = "student_database.csv"

# Function to load existing data
def load_data():
    if os.path.exists(DB_FILE):
        return pd.read_csv(DB_FILE)
    else:
        # Create an empty DataFrame with required columns if file doesn't exist
        return pd.DataFrame(columns=[
            "Registration Date", "Student Name", "Age", 
            "Grade/Class", "Parent Name", "Contact Number", 
            "Email", "Subjects Interested", "Additional Notes"
        ])

# Function to save data
def save_data(df):
    df.to_csv(DB_FILE, index=False)

# App Configuration
st.set_page_config(page_title="Tuition Registration Portal", page_icon="📚", layout="centered")

# App Header
st.title("📚 Student Registration Portal")
st.write("Welcome! Please fill out the form below to register for the tuition classes.")

# Navigation Tabs (Admin vs Student view)
# Using query parameters or simple tabs to hide/show the admin dashboard
tab1, tab2 = st.tabs(["📝 Student Registration", "🔒 Admin Dashboard"])

# --- TAB 1: STUDENT REGISTRATION FORM ---
with tab1:
    st.header("Student Information Form")
    
    with st.form(key="registration_form", clear_on_submit=True):
        student_name = st.text_input("Student Full Name*", placeholder="John Doe")
        age = st.number_input("Student Age*", min_value=3, max_value=100, step=1, value=10)
        grade = st.text_input("Grade / Class*", placeholder="e.g., Grade 10, Year 11")
        
        st.divider()
        
        parent_name = st.text_input("Parent/Guardian Name*", placeholder="Jane Doe")
        contact_number = st.text_input("Contact Number*", placeholder="+1234567890")
        email = st.text_input("Email Address*", placeholder="parent@example.com")
        
        st.divider()
        
        # Example subjects - customize these for your business
        subjects = st.multiselect(
            "Select Subjects Needed*",
            ["Mathematics", "Science", "English", "History", "Physics", "Chemistry", "Biology"]
        )
        
        notes = st.text_area("Any specific learning goals or medical/allergy notes?", placeholder="Type here...")
        
        submit_button = st.form_submit_button(label="Submit Registration")
        
        if submit_button:
            # Basic validation
            if not student_name or not grade or not parent_name or not contact_number or not subjects:
                st.error("Please fill out all required fields (*).")
            else:
                # Load current data
                df = load_data()
                
                # Create a new record
                new_data = {
                    "Registration Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Student Name": student_name,
                    "Age": age,
                    "Grade/Class": grade,
                    "Parent Name": parent_name,
                    "Contact Number": contact_number,
                    "Email": email,
                    "Subjects Interested": ", ".join(subjects),
                    "Additional Notes": notes
                }
                
                # Append and save
                df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
                save_data(df)
                
                st.success(f"🎉 Thank you, {student_name}! Your registration has been submitted successfully.")

# --- TAB 2: ADMIN DASHBOARD ---
with tab2:
    st.header("🔒 Registered Students Data")
    st.write("This view is for the tutor/admin to manage registered students.")
    
    # Simple password protection for admin view
    password = st.text_input("Enter Admin Password to View Data", type="password")
    
    # Change "admin123" to your preferred security password
    if password == "admin123":
        df = load_data()
        
        if df.empty:
            st.info("No students registered yet.")
        else:
            st.metric(label="Total Registered Students", value=len(df))
            
            # Display interactive table
            st.dataframe(df)
            
            # Provide a CSV download button for Excel
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Data as Excel/CSV",
                data=csv,
                file_name=f"tuition_students_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
            )
    elif password:
        st.error("Incorrect password. Access denied.")
