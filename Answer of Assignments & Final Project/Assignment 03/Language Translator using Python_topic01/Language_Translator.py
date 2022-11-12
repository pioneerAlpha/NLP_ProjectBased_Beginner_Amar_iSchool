from google_trans_new import google_translator
import streamlit as st
translator = google_translator(url_suffix="hk",timeout=10,proxies={'http':'138.128.59.129:9058','https':'93.190.245.171:9197'})
st.title("Language Translator")
text = st.text_input("Enter a text")
translate = translator.translate(text, lang_tgt='fr')
st.write(translate)