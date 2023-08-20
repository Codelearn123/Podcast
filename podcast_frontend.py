import streamlit as st
import modal
import json
import os

def main():
    st.title("Newsletter Dashboard")

    available_podcast_info = create_dict_from_json_files('/mnt/data/podcast/')  # Adjusted the folder path for this environment

    # Left section - Input fields
    st.sidebar.header("Podcast RSS Feeds")

    # Dropdown box
    st.sidebar.subheader("Available Podcasts Feeds")
    selected_podcast = st.sidebar.selectbox("Select Podcast", options=list(available_podcast_info.keys()))

    if selected_podcast:
        podcast_info = available_podcast_info[selected_podcast]
        display_podcast_info(podcast_info)

    # User Input box
    st.sidebar.header("Test Sidebar")
    url = st.sidebar.text_input("Link to RSS Feed")
    process_button = st.sidebar.button("Process Podcast Feed")
    st.sidebar.markdown("**Note**: Podcast processing can take up to 5 mins, please be patient.")

    if process_button:
        # Call the function to process the URLs and retrieve podcast guest information
        podcast_info = process_podcast_info(url)
        display_podcast_info(podcast_info)


def display_podcast_info(podcast_info):
    # Display podcast details
    st.header("Newsletter Content")

    st.subheader("Episode Title")
    st.write(podcast_info['podcast_details']['episode_title'])

    col1, col2 = st.columns([7, 3])
    with col1:
        st.subheader("Podcast Episode Summary")
        st.write(podcast_info['podcast_summary'])
    with col2:
        st.image(podcast_info['podcast_details']['episode_image'], caption="Podcast Cover", width=300, use_column_width=True)

    # Display the podcast guest details only if 'podcast_guest' key exists
    if 'podcast_guest' in podcast_info:
        col3, col4 = st.columns([3, 7])
        with col3:
            st.subheader("Podcast Guest")
            st.write(podcast_info['podcast_guest'].get('name', 'N/A'))  # Display guest name
        with col4:
            st.subheader("Podcast Guest Details")
            st.write(podcast_info['podcast_guest'].get('details', 'N/A'))  # Display guest details

    if 'podcast_highlights' in podcast_info:
        st.subheader("Key Moments")
        key_moments = podcast_info['podcast_highlights']
        for moment in key_moments.split('\n'):
            st.markdown(f"<p style='margin-bottom: 5px;'>{moment}</p>", unsafe_allow_html=True)
