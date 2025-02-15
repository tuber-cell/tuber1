# app.py
import streamlit as st
from pytube import YouTube

# Set page title and icon
st.set_page_config(page_title="YouTube Video Downloader", page_icon="🎥")

# Title and description
st.title("YouTube Video Downloader 🎥")
st.write("Enter the URL of the YouTube video you want to download.")

# Input for YouTube URL
url = st.text_input("Paste the YouTube video URL here:")

if url:
    try:
        yt = YouTube(url)
        st.image(yt.thumbnail_url, width=300)
        st.write(f"**Title:** {yt.title}")
        st.write(f"**Author:** {yt.author}")

        # Select video resolution
        resolutions = [stream.resolution for stream in yt.streams.filter(progressive=True, file_extension='mp4')]
        selected_resolution = st.selectbox("Select resolution:", resolutions)

        if selected_resolution:
            # Get the selected stream
            stream = yt.streams.filter(res=selected_resolution, file_extension='mp4').first()

            # Download button
            if st.button("Download Video"):
                st.write("Downloading...")
                stream.download()
                st.success("Download complete! Check your local folder for the video.")
    except Exception as e:
        st.error(f"An error occurred: {e}")