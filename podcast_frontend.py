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




