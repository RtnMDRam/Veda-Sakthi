import streamlit as st
import pandas as pd

st.markdown("""
    <style>
    .block-container { padding-bottom: 0 !important; padding-top: 0.2rem !important; }
    .main { padding-bottom: 0 !important; margin-bottom: 0 !important; }
    .stTextArea label { font-size: 0.86em !important; font-weight: 500 !important; margin-bottom: -0.2em !important; }
    .stTextArea { margin-bottom: -0.5em !important; }
    textarea[data-baseweb="textarea"] { min-height: 44px !important; font-size: 0.98em !important; }
    body, html { margin-bottom: 0 !important; padding-bottom: 0 !important;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload a bilingual Excel file (.xlsx)", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.success("File uploaded successfully!")
    row = df.iloc[0]
    vilakkam_val = row.get('விளக்கம்', '') or row.get('விளக்கம் ', '')

    # Editable Question (single line above options)
    st.markdown('<span style="font-size:0.86em;font-weight:500;">கேள்வி</span>', unsafe_allow_html=True)
    tamil_q = st.text_area("", value=row.get('கேள்வி', ''), height=52, key="edit_q")

    # Option editing: two rows of two side-by-side
    st.markdown('<span style="font-size:0.86em;font-weight:500;">விருப்பங்கள்</span>', unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="small")
    with col1:
        optA = st.text_area("", value="", key="optA", height=40, label_visibility='collapsed')
    with col2:
        optB = st.text_area("", value="", key="optB", height=40, label_visibility='collapsed')
    col3, col4 = st.columns(2, gap="small")
    with col3:
        optC = st.text_area("", value="", key="optC", height=40, label_visibility='collapsed')
    with col4:
        optD = st.text_area("", value="", key="optD", height=40, label_visibility='collapsed')

    # Glossary/Answer (even row, matching Explanation height)
    col5, col6 = st.columns(2, gap="small")
    with col5:
        st.markdown('<span style="font-size:0.86em;font-weight:500;">Glossary</span>', unsafe_allow_html=True)
        gloss = st.text_area("", value="", key="gloss", height=40, label_visibility='collapsed')
    with col6:
        st.markdown('<span style="font-size:0.86em;font-weight:500;">Answer</span>', unsafe_allow_html=True)
        ans = st.text_area("", value=row.get('பதில் ', ''), key="ans", height=40, label_visibility='collapsed')

    # Large Explanation area (full width)
    st.markdown('<span style="font-size:0.86em;font-weight:500;">விளக்கம்</span>', unsafe_allow_html=True)
    tamil_exp = st.text_area("", value=vilakkam_val, height=175, key="edit_exp")

    # Non-editable reference (unchanged)
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
