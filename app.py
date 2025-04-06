import streamlit as st

# Set up the Streamlit sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ("Home", "Multi-Emotions"))

# Switch between pages based on sidebar choice
if page == "Home":
    import home  # This imports the home.py script
elif page == "Multi-Emotions":
    import multiemotions  # This imports the multiemotions.py script
