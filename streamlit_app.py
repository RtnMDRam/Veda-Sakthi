import streamlit as st
import pandas as pd

st.title("Veda-Sakthi Educational SME Panel")
st.write("Welcome! Upload a bilingual Excel or start with sample questions.")

uploaded_file = st.file_uploader("Upload .xlsx", type="xlsx")
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
else:
    df = pd.DataFrame({
        "question": ["Sample question in English"],
        "கேள்வி": ["தமிழில் சாட்டம் கேள்வி"]
    })
st.dataframe(df)
