import streamlit as st
import modal
import json
import os

def create_dict_from_json_files(folder_path):
    try:
        json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
    except Exception as e:
        st.write(f"Error accessing directory: {e}")
        return {}

    data_dict = {}

    for file_name in json_files:
        file_path = os.path.join(folder_path, file_name)
        try:
            with open(file_path, 'r') as file:
                podcast_info = json.load(file)
                podcast_name = podcast_info.get('podcast_details', {}).get('podcast_title', file_name)
                data_dict[podcast_name] = podcast_info
        except Exception as e:
            st.write(f"Error processing file {file_name}: {e}")

    return data_dict




