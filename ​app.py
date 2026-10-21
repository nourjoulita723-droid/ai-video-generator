import streamlit as st
import fal_client
import os

# Set your API key here
os.environ["FAL_KEY"] = "YOUR_FAL_KEY_HERE"

st.set_page_config(page_title="AI Video Generator", page_icon="🎬")

st.title("🎬 AI Video Generator")
st.write("Enter a description to generate a video:")

prompt = st.text_area("Prompt:", "A cute pink Spider-Girl and Skye from PAW Patrol, 3d cartoon style")

if st.button("🚀 Generate Video"):
    if not prompt:
        st.warning("Please enter a prompt first!")
    else:
        with st.spinner("Generating video... Please wait"):
            try:
                result = fal_client.subscribe(
                    "fal-ai/kling-video/v1.5/pro/text-to-video",
                    arguments={
                        "prompt": prompt,
                        "aspect_ratio": "16:9"
                    }
                )
                
                video_url = result.get("video", {}).get("url")
                if video_url:
                    st.success("Video generated successfully!")
                    st.video(video_url)
                else:
                    st.error("Video URL not found in response.")
            except Exception as e:
                st.error(f"Error: {e}")

