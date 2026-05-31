import streamlit as st
from deep_translator import GoogleTranslator as gt
from gtts import gTTS
st.title("Language Transition Tool")
txt = st.text_area("Enter text")
source_language = st.selectbox("choose source language",['en','hi','te','fr','es'])
dest_language = st.selectbox("choose destination language",['en','hi','te','fr','es'])
if st.button("submit"):
    translated_text = gt(source = source_language,target = dest_language).translate(txt)
    st.session_state["text"]= translated_text
if "text" in st.session_state:
    if st.button("play audio"):
        audio = gTTS(st.session_state["text"],lang = dest_language)
        audio.save("LTT.mp3")
        st.audio("LTT.mp3")