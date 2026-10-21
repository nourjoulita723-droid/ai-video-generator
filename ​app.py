import streamlit as st
import requests
import io
from PIL import Image

st.set_page_config(page_title="Free AI Image Generator", page_icon="🎨")

st.title("🎨 Free AI Image Generator")
st.write("Generate high-quality 3D anime & cartoon images for free!")

prompt = st.text_area("Prompt:", "A cute pink Spider-Girl and Skye from PAW Patrol, 3d cartoon style, highly detailed")

# Public free API endpoint
API_URL = "https://api-inference.huggingface.co/models/stablediffusionapi/anything-v5"

if st.button("🚀 Generate Image"):
    if not prompt:
        st.warning("Please enter a prompt first!")
    else:
        with st.spinner("Generating your image... Please wait"):
            try:
                response = requests.post(API_URL, json={"inputs": prompt})
                if response.status_code == 200:
                    image_bytes = response.content
                    image = Image.open(io.BytesIO(image_bytes))
                    st.success("Image generated successfully!")
                    st.image(image, caption="Generated Image")
                else:
                    st.error("Server is busy, please try clicking the button again in a few seconds.")
            except Exception as e:
                st.error(f"Error: {e}")
