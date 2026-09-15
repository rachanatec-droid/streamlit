import streamlit as st
import pandas as pd
import datetime
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="September Meal Tracker", page_icon="📅", layout="centered")

# --- FILE PATH FOR DATA PERSISTENCE ---
DATA_FILE = "september_meals.csv"
YEAR = 2026  # Target Year
MONTH = 9    # September

# --- INITIALIZE OR LOAD DATA ---
def load_data():
    # Number of days in September is 30
    days_in_september = 30
    dates = [datetime.date(YEAR, MONTH, day) for day in range(1, days_in_september + 1)]
    
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        df['Date'] = pd.to_datetime(df['Date']).dt.date
    else:
        # Create an empty template if file doesn't exist
        df = pd.DataFrame({
            "Date": dates,
            "Breakfast": [""] * days_in_september,
            "Lunch": [""] * days_in_september,
            "Dinner": [""] * days_in_september
        })
        df.to_csv(DATA_FILE, index=False)
    return df

# Initialize session state with data
if 'meal_db' not in st.session_state:
    st.session_state.meal_db = load_data()

# --- APP UI ---
st.title("📅 September 2026 Meal Tracker")
st.write("Log and track what you eat for Breakfast, Lunch, and Dinner every day.")

# --- SIDEBAR: LOG/UPDATE MEAL ---
st.sidebar.header("📝 Log a Meal")

# Date Picker (Restricted to September 2026)
min_date = datetime.date(YEAR, MONTH, 1)
max_date = datetime.date(YEAR, MONTH, 30)
selected_date = st.sidebar.date_input(
    "Select Date", 
    value=min_date, 
    min_value=min_date, 
    max_value=max_date
)

# Fetch existing entry for the selected date to prepopulate fields
current_row = st.session_state.meal_db[st.session_state.meal_db['Date'] == selected_date]

if not current_row.empty:
    default_b = current_row.iloc[0]['Breakfast'] if pd.notna(current_row.iloc[0]['Breakfast']) else ""
    default_l = current_row.iloc[0]['Lunch'] if pd.notna(current_row.iloc[0]['Lunch']) else ""
    default_d = current_row.iloc[0]['Dinner'] if pd.notna(current_row.iloc[0]['Dinner']) else ""
else:
    default_b, default_l, default_d = "", "", ""

# Input text areas
breakfast_input = st.sidebar.text_area("🍳 Breakfast", value=default_b, placeholder="What did you eat?")
lunch_input = st.sidebar.text_area("🥪 Lunch", value=default_l, placeholder="What did you eat?")
dinner_input = st.sidebar.text_area("🍲 Dinner", value=default_d, placeholder="What did you eat?")

# Save button logic
if st.sidebar.button("Save Entry", type="primary"):
    # Update the data frame
    st.session_state.meal_db.loc[st.session_state.meal_db['Date'] == selected_date, ['Breakfast', 'Lunch', 'Dinner']] = [
        breakfast_input, lunch_input, dinner_input
    ]
    # Persist to local CSV file
    st.session_state.meal_db.to_csv(DATA_FILE, index=False)
    st.sidebar.success(f"Saved entry for {selected_date.strftime('%B %d, %Y')}!")
    st.rerun()

# --- MAIN DASHBOARD: VIEW ENTRIES ---
tab1, tab2 = st.tabs(["📋 View Full Month", "🔍 Day-by-Day Summary"])

with tab1:
    st.subheader("September Meal Log Summary")
    
    # Format the date column cleanly for presentation
    display_df = st.session_state.meal_db.copy()
    display_df['Date'] = display_df['Date'].apply(lambda x: x.strftime('%A, %b %d'))
    
    # Display an interactive, clean table
    st.dataframe(display_df.set_index('Date'), use_container_width=True)

with tab2:
    st.subheader("Detailed Day View")
    
    # Filter only days that have at least one meal logged
    logged_days = st.session_state.meal_db[
        (st.session_state.meal_db['Breakfast'].str.strip() != "") |
        (st.session_state.meal_db['Lunch'].str.strip() != "") |
        (st.session_state.meal_db['Dinner'].str.strip() != "")
    ]
    
    if logged_days.empty:
        st.info("No meals logged yet! Use the sidebar to add entries.")
    else:
        for idx, row in logged_days.iterrows():
            formatted_date = row['Date'].strftime('%A, %B %d, %Y')
            with st.expander(f"🍴 {formatted_date}"):
                st.write(f"**Breakfast:** {row['Breakfast'] if row['Breakfast'] else '*Not logged*'}")
                st.write(f"**Lunch:** {row['Lunch'] if row['Lunch'] else '*Not logged*'}")
                st.write(f"**Dinner:** {row['Dinner'] if row['Dinner'] else '*Not logged*'}")
