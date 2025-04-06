import streamlit as st
st.set_page_config(page_title="Emotion Analyzer AI", page_icon="😃")
# Set up the Streamlit sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ("Home", "Multi-Emotions"))

# Switch between pages based on sidebar choice
if page == "Home":
    import main  # This imports the main.py script
elif page == "Multi-Emotions":
    import multiemotions  # This imports the multiemotions.py script
