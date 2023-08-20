import streamlit as st
import modal
import json
import os


def main():
    st.title("Newsletter Dashboard")
    
    # Only render the RSS feed input
    st.sidebar.header("Test Sidebar")
    url = st.sidebar.text_input("Link to RSS Feed")

if __name__ == '__main__':
    main()
