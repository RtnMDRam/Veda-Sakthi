import streamlit as st
import pandas as pd

# CSS: minimize all default spacing and ensure bottom alignment of content section
st.markdown("""
    <style>
    .block-container {
        display: flex;
        flex-direction: column;
        min-height: 98vh;    /* Ensures full height usage */
        justify-content: flex-end;
        padding-bottom: 0 !important;
        padding-top: 0.5rem !important;
    }
    .main {
        padding-bottom: 0 !important;
        margin-bottom: 0 !important;
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
    body, html {
        margin-bottom: 0 !important;
        padding-bottom: 0 !important;
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

    # This pushes all content to the very bottom!
    st.markdown("<div style='flex:1'></div>", unsafe_allow_html=True)

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
