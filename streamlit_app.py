import streamlit as st
import pandas as pd

# Minimal and bottom-docked non-editable display
st.markdown("""
    <style>
    .block-container { padding-bottom: 0 !important; padding-top: 0.2rem !important; }
    .main { padding-bottom: 0 !important; margin-bottom: 0 !important; }
    h4 { font-size: 1.05em !important; font-weight: 600 !important; margin-bottom: 0.07em !important; margin-top: 0.13em !important;}
    p, ul, ol { margin-bottom: 0.07em !important; margin-top: 0.07em !important; font-size: 1.01em !important;}
    body, html { margin-bottom: 0 !important; padding-bottom: 0 !important;}
    footer {visibility: hidden;}
    /* Make Streamlit text_area height respect vh units */
    textarea[data-baseweb="textarea"] { min-height: 40vh !important; }
    </style>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload a bilingual Excel file (.xlsx)", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.success("File uploaded successfully!")
    row = df.iloc[0]
    vilakkam_val = row.get('விளக்கம்', '') or row.get('விளக்கம் ', '')

    # DRAW THE EDITABLE TAMIL PANEL - just above reference
    editable_tamil = (
        f"கேள்வி: {row.get('கேள்வி', '')}\n"
        f"விருப்பங்கள்: {row.get('விருப்பங்கள் ', '')}\n"
        f"பதில்: {row.get('பதில் ', '')}\n"
        f"விளக்கம்: {vilakkam_val}"
    )
    st.text_area("தமிழ் (Editable)", value=editable_tamil, height=300, key="edit_tamil")  # will render at least 40vh due to css above

    # NON-EDITABLE REFERENCE, still bottom-aligned
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
