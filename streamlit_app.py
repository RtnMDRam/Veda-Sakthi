import streamlit as st
import pandas as pd

# All space at the top, Tamil and English display sit at the bottom, very compact
st.markdown("""
    <style>
    .block-container {
        display: flex;
        flex-direction: column;
        justify-content: flex-end !important;
        min-height: 90vh !important;
        padding-bottom: 0rem !important;
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
    }
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload a bilingual Excel file (.xlsx)", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.success("File uploaded successfully!")

    row = df.iloc[0]
    vilakkam_val = row.get('விளக்கம்', '') or row.get('விளக்கம் ', '')

    st.write("")  # creates empty space above for future editable area!

    with st.container():
        st.markdown("#### தமிழ்")
        st.markdown(f"**கேள்வி:** {row.get('கேள்வி', '')}")
        st.markdown(f"**விருப்பங்கள்:** {row.get('விருப்பங்கள் ', '')}")
        st.markdown(f"**பதில்:** {row.get('பதில் ', '')}")
        st.markdown(f"**விளக்கம்:** {vilakkam_val}")

        st.markdown("#### English")
        st.markdown(f"**Question:** {row.get('question ', '')}")
        st.markdown(f"**Options:** {row.get('questionOptions', '')}")
        st.markdown(f"**Answer:** {row.get('answers ', '')}")
        st.markdown(f"**Explanation:** {row.get('explanation', '')}")

else:
    st.info("Please upload your bilingual Excel file to begin.")
