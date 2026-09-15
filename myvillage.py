import streamlit as st
import pandas as pd
import numpy as np

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Village Profile Dashboard",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🏡 Village Navigator")
st.sidebar.markdown("Use the menu below to explore different aspects of our village.")
page = st.sidebar.radio(
    "Go to:",
    ["Overview & History", "Demographics & Stats", "Map & Geography", "Gallery & Attractions", "Community Feedback"]
)

# --- TEMP DATA (Replace with your actual village details) ---
VILLAGE_NAME = "Greenwood Village"
ESTABLISHED_YEAR = "1845"
POPULATION = 1250
HOUSEHOLDS = 320
LITERACY_RATE = "88%"

# --- PAGE 1: OVERVIEW & HISTORY ---
if page == "Overview & History":
    st.title(f"Welcome to {VILLAGE_NAME} ✨")
    st.subheader("A glimpse into our heritage, culture, and community.")
    
    # Hero layout
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"""
        ### About Us
        **{VILLAGE_NAME}** is a vibrant, tight-knit community known for its lush landscapes, rich agricultural heritage, and welcoming people. Founded in **{ESTABLISHED_YEAR}**, the village has preserved its traditional roots while steadily adapting to modern sustainable living.
        
        ### Key Features
        - 🌾 **Primary Occupation:** Organic Farming & Handicrafts
        - 🏛️ **Heritage Sites:** 150-year-old Community Hall, Ancient Banyan Tree
        - 🌱 **Eco-Initiatives:** 100% solar-powered street lighting, rainwater harvesting
        """)
    with col2:
        # Placeholder metrics
        st.metric(label="Established", value=ESTABLISHED_YEAR)
        st.metric(label="Primary Climate", value="Temperate")

# --- PAGE 2: DEMOGRAPHICS & STATS ---
elif page == "Demographics & Stats":
    st.title("📊 Village Demographics & Statistics")
    st.write("Key metrics showing the growth and development of our population.")
    
    # Metric cards
    m1, m2, m3 = st.columns(3)
    m1.metric(label="Total Population", value=POPULATION, delta="+2% vs last year")
    m2.metric(label="Total Households", value=HOUSEHOLDS)
    m3.metric(label="Literacy Rate", value=LITERACY_RATE)
    
    st.markdown("---")
    st.subheader("Occupation Breakdown")
    
    # Sample Chart Data
    chart_data = pd.DataFrame({
        "Occupation": ["Agriculture", "Local Business", "Services", "Education", "Others"],
        "Percentage": [45, 20, 15, 12, 8]
    }).set_index("Occupation")
    
    st.bar_chart(chart_data)

# --- PAGE 3: MAP & GEOGRAPHY ---
elif page == "Map & Geography":
    st.title("📍 Geography & Location")
    st.write(f"Geographical boundaries and key landmarks of {VILLAGE_NAME}.")
    
    # Replace these coordinates with your village's actual Latitude and Longitude
    # Example coordinates for a central point (approx. Bengaluru area as placeholder)
    village_lat = 13.10
    village_lon = 77.59
    
    # Generate mock coordinates around the village center for landmarks
    map_data = pd.DataFrame({
        'lat': [village_lat, village_lat + 0.002, village_lat - 0.003, village_lat + 0.004],
        'lon': [village_lon, village_lon - 0.002, village_lon + 0.001, village_lon - 0.004],
        'Landmark': ['Village Panchayat', 'Primary Health Centre', 'Government School', 'Community Lake']
    })
    
    st.write("**Key Landmarks Map:**")
    st.map(map_data)
    
    st.dataframe(map_data)

# --- PAGE 4: GALLERY & ATTRACTIONS ---
elif page == "Gallery & Attractions":
    st.title("📸 Village Gallery & Local Attractions")
    st.write("Explore the scenic beauty and daily life captured by our residents.")
    
    # Using Unsplash placeholder images (Replace URLs with your village photos)
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://unsplash.com", 
                 caption="Our beautiful community farms during harvest season.")
    with col2:
        st.image("https://unsplash.com", 
                 caption="The scenic hills protecting the north border of our village.")

# --- PAGE 5: COMMUNITY FEEDBACK ---
elif page == "Community Feedback":
    st.title("✍️ Grievance & Suggestion Box")
    st.write("Are you a resident or visitor? Let the village council know your thoughts or requirements.")
    
    with st.form("feedback_form", clear_on_submit=True):
        name = st.text_input("Full Name")
        resident_status = st.selectbox("Status", ["Resident", "Non-Resident Owner", "Visitor"])
        category = st.selectbox("Category", ["Suggestion", "Infrastructure Issue", "Water/Electricity", "Other"])
        details = st.text_area("Provide details here...")
        
        submitted = st.form_submit_submit_button("Submit Entry")
        if submitted:
            if name and details:
                st.success(f"Thank you, {name}! Your {category.lower()} has been recorded successfully.")
            else:
                st.error("Please fill out both your name and the details field.")

# --- FOOTER ---
st.markdown("---")
st.caption(f"© 2026 {VILLAGE_NAME} Digital Panchayat Initiative. Powered by Streamlit.")
