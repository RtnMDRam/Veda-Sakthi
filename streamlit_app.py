import streamlit as st
import pandas as pd

# Maximize usable space, no bottom gap, small headings
st.markdown("""
    <style>
    .block-container {
        padding-bottom: 0rem !important;
        padding-top: 0.7rem !important;
    }
    .block-container h4 {
        font-size: 1.05em !important;
        font-weight: 600 !important;
        margin-bottom: 0.07em !important;
        margin-top: 0.13em !important;
    }
    .block-container p, .block-container ul, .block-container ol {
        margin-bottom: 0.07em !important;
        margin-top: 0.07em !important;
        font-size: 1.01em !important;
    }
    .main {
        padding-bottom: 0rem !important;
        margin-bottom: 0rem !important;
    }
    body, html {
        margin-bottom: 0rem !important;
        padding-bottom: 0rem !important;
        height: 100vh !important;
    }
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload a bilingual Excel file (.xlsx)", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.success("File uploaded successfully!")

    row = df.iloc[0]

    # Fetch explanation field in Tamil even if Excel has trailing spaces
    vilakkam_val = row.get('விளக்கம்', '') or row.get('விளக்கம் ', '')

    with st.container():
        st.markdown("#### தமிழ்")
        st.markdown(f"**கேள்வி:** {row.get('கேள்வி', '')}")
        st.markdown(f"**விருப்பங்கள்:** {row.get('விருப்பங்கள் ', '')}")
        st.markdown(f"**பதில்:** {row.get('பதில் ', '')}")
        st.markdown(f"**விளக்கம்:** {vilakkam_val}")

    with st.container():
        st.markdown("#### English")
        st.markdown(f"**Question:** {row.get('question ', '')}")
        st.markdown(f"**Options:** {row.get('questionOptions', '')}")
        st.markdown(f"**Answer:** {row.get('answers ', '')}")
        st.markdown(f"**Explanation:** {row.get('explanation', '')}")

else:
    st.info("Please upload your bilingual Excel file to begin.")
