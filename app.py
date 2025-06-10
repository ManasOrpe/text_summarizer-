import streamlit as st
import base64
from transformers import pipeline


st.set_page_config(page_title="Text Summarization App", layout="centered")


@st.cache_resource
def load_summarization_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

@st.cache_data
def get_image_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img_base64 = get_image_as_base64("background.jpeg")
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpeg;base64,{img_base64}");
    background-size: cover;
    background-position: center;
}}
[data-testid="stHeader"]{{
    background-color: rgba(0, 0, 0, 0);
    
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


st.title("Text Summarization App using Hugging Face 🤗")
st.markdown("Summarize long articles using Transformer models")


text = st.text_area("📄 Enter text to summarize", height=300)
length = st.selectbox("📏 Summary Length", ["Short", "Medium", "Long"])
btn = st.button("Summarize")


length_map = {
    "Short": (30, 80),
    "Medium": (50, 120),
    "Long": (80, 200)
}

summarizer = load_summarization_model()


if btn and text.strip():
    min_len, max_len = length_map[length]
    with st.spinner("Generating summary..."):
        summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
        st.subheader("📌 Summary")
        st.success(summary[0]['summary_text'])
