import streamlit as st

# Set up the page title and icon
st.set_page_config(page_title="Meet Our Family", page_icon="👨‍👩‍👧‍👦", layout="centered")

# Main Header
st.title("Welcome to Our Family Webpage! 🏡")
st.write("We are so excited to introduce you to the members of our family.")

# Sidebar for navigation or quick facts
st.sidebar.header("Family Quick Facts")
st.sidebar.text("Location: Our Happy Home")
st.sidebar.text("Total Members: 4")
family_motto = st.sidebar.selectbox(
    "Our Family Motto:",
    ["Love and Laughter", "Teamwork makes the dream work", "Always together"],
)
st.sidebar.write(f"🌟 *{family_motto}*")

# Tabs for each family member
tab1, tab2, tab3, tab4 = st.tabs(["Dad", "Mom", "Me", "Pet"])

with tab1:
  st.header("Meet Dad (John)")
  st.write(
      "Our dad is the grill master and the one who fixes everything around the"
      " house."
  )
  st.info("Favorite Hobby: Gardening & BBQ")

with tab2:
  st.header("Meet Mom (Sarah)")
  st.write(
      "Our mom is the heart of the family, an amazing cook, and keeps us all"
      " organized."
  )
  st.info("Favorite Hobby: Reading & Painting")

with tab3:
  st.header("Meet Me (Alex)")
  st.write(
      "I love coding, playing video games, and hanging out with friends and"
      " family."
  )
  st.info("Favorite Hobby: Coding in Python!")

with tab4:
  st.header("Meet Our Dog (Max)")
  st.write(
      "Max is a golden retriever who loves belly rubs and chasing tennis balls."
  )
  st.info("Favorite Hobby: Eating treats and sleeping")

# Interactive section: Leave a note
st.subheader("Leave a Note for Our Family 📝")
visitor_name = st.text_input("Your Name:")
visitor_message = st.text_area("Your Message:")

if st.button("Send Message"):
  if visitor_name and visitor_message:
    st.success(
        f"Thank you, {visitor_name}! Your message has been shared with the"
        " family."
    )
  else:
    st.warning("Please fill in both your name and message before sending.")
