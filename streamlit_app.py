import streamlit as st
import pandas as pd

# Minimal vertical space between content blocks, remove bottom padding too
st.markdown("""
    <style>
    .block-container h2, .block-container h3 {
        margin-bottom: 0.25rem !important;
        margin-top: 0.4rem !important;
    }
    .block-container p {
        margin-bottom: 0.1rem !important;
        margin-top: 0.1rem !important;
    }
    .block-container {
        padding-bottom: 0rem !important;
    }
    footer {visibility: hidden;} /* Optional: Hide Streamlit footer bar */
    </style>
""", unsafe_allow_html=True)

st.title("Bilingual Content Preview")

uploaded_file = st.file_uploader("Upload a bilingual Excel file (.xlsx)", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.success("File uploaded successfully!")

    row = df.iloc[0]

    with st.container():
        st.header("தமிழ்")
        st.markdown(f"**கேள்வி:** {row.get('கேள்வி', '')}")
        st.markdown(f"**விருப்பங்கள்:** {row.get('விருப்பங்கள் ', '')}")
        st.markdown(f"**பதில்:** {row.get('பதில் ', '')}")
        st.markdown(f"**விளக்கம்:** {row.get('விளக்கம்', '')}")

    with st.container():
        st.header("English")
        st.markdown(f"**Question:** {row.get('question ', '')}")
        st.markdown(f"**Options:** {row.get('questionOptions', '')}")
        st.markdown(f"**Answer:** {row.get('answers ', '')}")
        st.markdown(f"**Explanation:** {row.get('explanation', '')}")

else:
    st.info("Please upload your bilingual Excel file to begin.")
