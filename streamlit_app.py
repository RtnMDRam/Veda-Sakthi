import streamlit as st
import pandas as pd

st.markdown("""
    <style>
    .compact-block h4, .compact-block h3, .compact-block h2 {
        font-size: 1.05em !important; 
        font-weight: 700 !important; 
        margin-top: 0.07em !important; 
        margin-bottom: 0em !important;
        line-height: 1.07 !important;
    }
    .compact-block p, .compact-block ul, .compact-block ol, .compact-block {
        margin-bottom: 0em !important; 
        margin-top: 0em !important; 
        line-height: 1.13 !important;
        font-size: 1.00em !important;
        padding-top:0 !important; 
        padding-bottom:0 !important;
    }
    .compact-block strong {
        font-weight: 600 !important;
    }
    .compact-block {
        margin-top:-0.1em !important;
        margin-bottom:-0.1em !important;
        padding-top:0 !important; 
        padding-bottom:0 !important;
    }
    </style>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload a bilingual Excel file (.xlsx)", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.success("File uploaded successfully!")
    row = df.iloc[0]
    vilakkam_val = row.get('விளக்கம்', '') or row.get('விளக்கம் ', '')

    # --- Compact Non-editable reference blocks ---
    st.markdown('<div class="compact-block">', unsafe_allow_html=True)
    st.markdown("<h4>தமிழ்</h4>", unsafe_allow_html=True)
    st.markdown(f"<strong>கேள்வி:</strong> {row.get('கேள்வி', '')}", unsafe_allow_html=True)
    st.markdown(f"<strong>விருப்பங்கள்:</strong> {row.get('விருப்பங்கள் ', '')}", unsafe_allow_html=True)
    st.markdown(f"<strong>பதில்:</strong> {row.get('பதில் ', '')}", unsafe_allow_html=True)
    st.markdown(f"<strong>விளக்கம்:</strong> {vilakkam_val}", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="compact-block">', unsafe_allow_html=True)
    st.markdown("<h4>English</h4>", unsafe_allow_html=True)
    st.markdown(f"<strong>Question:</strong> {row.get('question ', '')}", unsafe_allow_html=True)
    st.markdown(f"<strong>Options:</strong> {row.get('questionOptions', '')}", unsafe_allow_html=True)
    st.markdown(f"<strong>Answer:</strong> {row.get('answers ', '')}", unsafe_allow_html=True)
    st.markdown(f"<strong>Explanation:</strong> {row.get('explanation', '')}", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

else:
    st.info("Please upload your bilingual Excel file to begin.")
