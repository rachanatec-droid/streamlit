import streamlit as st

# Page Configuration
st.set_page_config(page_title="My Portfolio", page_icon="🚀", layout="wide")

# Header / Bio
st.title("Hi, I'm [Rachana K J] 👋")
st.subheader("Data Scientist | Software Developer | Creator")
st.write(
    "Welcome to my portfolio! Here is a collection of my recent work and projects."
)

st.divider()

# Project Data (Add your project details here)
projects = [
    {
        "title": "Project One: Data Dashboard",
        "description": "An interactive dashboard built with Pandas and Plotly to analyze real-time market trends.",
        "link": "https://github.com",
        "tags": ["Python", "Streamlit", "Pandas"],
    },
    {
        "title": "Project Two: Machine Learning App",
        "description": "A predictive modeling tool that estimates housing prices based on user inputs.",
        "link": "https://github.com",
        "tags": ["Scikit-Learn", "Python"],
    },
]

# Display Projects
st.header("Featured Projects")

for proj in projects:
  with st.container():
    st.subheader(proj["title"])
    st.write(proj["description"])
    st.markdown(f"**Tech Stack:** {', '.join(proj['tags'])}")
    st.markdown(f"[View Source Code / Live App]({proj['link']})")
    st.write("")  # spacing

# Contact Section
st.divider()
st.header("Get in Touch")
st.write("📫 Email: your.email@example.com")
st.markdown(
    "💼 [LinkedIn](https://linkedin.com) | 🐙"
    " [GitHub](https://github.com)"
)
