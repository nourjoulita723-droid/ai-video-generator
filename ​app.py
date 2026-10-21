import streamlit as st
import fal_client
import os

# ضعي مفتاحك الجديد المكون من fal_sk_... بين القوسين
os.environ["FAL_KEY"] = "مفتاحك_الجديد_هنا"

st.set_page_config(page_title="AI Video Generator", page_icon="🎬")

st.title("🎬 مولد الفيديوهات بالذكاء الاصطناعي")
st.write("أدخل الوصف لتوليد فيديو:")

prompt = st.text_area("الوصف (Prompt):", "A cute pink Spider-Girl and Skye from PAW Patrol, 3d cartoon style")

if st.button("🚀 توليد الفيديو"):
    if not prompt:
        st.warning("يرجى كتابة وصف أولاً!")
    else:
        with st.spinner("جاري التوليد..."):
            try:
                result = fal_client.subscribe(
                    "fal-ai/kling-video/v1.5/pro/text-to-video",
                    arguments={"prompt": prompt, "aspect_ratio": "16:9"}
                )
                video_url = result.get("video", {}).get("url")
                if video_url:
                    st.success("تم التوليد بنجاح!")
                    st.video(video_url)
                else:
                    st.error("لم يتم العثور على الفيديو.")
            except Exception as e:
                st.error(f"خطأ: {e}")
