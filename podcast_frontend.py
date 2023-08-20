import streamlit as st
import modal
import json
import os

def main():
    st.title("Newsletter Dashboard")
    
    available_podcast_info = create_dict_from_json_files('.')
    st.sidebar.header("Podcast RSS Feeds")
    st.sidebar.subheader("Available Podcasts Feeds")
    selected_podcast = st.sidebar.selectbox("Select Podcast", options=available_podcast_info.keys())
    
    st.sidebar.header("Test Sidebar")
    url = st.sidebar.text_input("Link to RSS Feed")

if __name__ == '__main__':
    main()
Continue reintroducing sections of the original code, checking the app after each addition.
By following this approach, you'll be able to identify the section of code that's causing the issue. Once identified, you can delve deeper into that section to pinpoint and fix the exact problem.

Would you like to proceed with this diagnostic approach, or do you have another preference?





