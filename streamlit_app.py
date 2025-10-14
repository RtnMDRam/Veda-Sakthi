import streamlit as st
import pandas as pd

st.markdown("""
    <style>
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        margin-top: 0 !important;
        margin-bottom: 0 !important;
    }
    header, footer { display: none !important; }
    .main { margin-top: 0 !important; margin-bottom: 0 !important; }
    .tight-label {
        font-size: 0.85em !important;
        font-weight: 500 !important;
        line-height: 1.08;
        margin-bottom: -0.34em !important;
        margin-top: -0.51em !important;
        padding-bottom:0 !important;
        padding-top:0 !important;
    }
    .stTextArea {
        margin-top: -0.44em !important;
        margin-bottom: -0.55em !important;
    }
    textarea[data-baseweb="textarea"] {
        min-height: 44px !important;
        font-size: 0.98em !important;
    }
    .stTextArea label { display:none !important; }
    .editable-vh45 {
        height: 45vh !important;
        min-height: 45vh !important;
        max-height: 45vh !important;
        overflow-y: auto;
        overflow-x: hidden;
        margin-bottom: 0 !important;
        padding-bottom: 0 !important;
        box-sizing: border-box;
        background: none;
    }
    .cw-40-fixed {
        height: 40vh !important;
        min-height: 40vh !important;
        max-height: 40vh !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
        font-size: 1.035em !important;
        line-height: 1.14 !important;
        margin: 0 !important;
        padding: 0 0.09em 0.28em 0.09em !important;  /* ZERO top padding! */
        overflow-y: auto;
        overflow-x: hidden;
        box-sizing: border-box;
        background: none;
    }
    .cw-40-fixed strong { font-weight: 600 !important; }
    </style>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload a bilingual Excel file (.xlsx)", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.success("File uploaded successfully!")
    row = df.iloc[0]
    vilakkam_val = row.get('விளக்கம்', '') or row.get('விளக்கம் ', '')

    # --- Editable block: exactly 45vh, scrollable, top ---
    st.markdown('<div class="editable-vh45">', unsafe_allow_html=True)
    st.markdown('<div class="tight-label">கேள்வி</div>', unsafe_allow_html=True)
    tamil_q = st.text_area("", value=row.get('கேள்வி', ''), height=52, key="edit_q", label_visibility='collapsed')

    st.markdown('<div class="tight-label">விருப்பங்கள்</div>', unsafe_allow_html=True)
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

    cols = st.columns(2, gap="small")
    with cols[0]:
        st.markdown('<div class="tight-label">Glossary</div>', unsafe_allow_html=True)
        gloss = st.text_area("", value="", key="gloss", height=40, label_visibility='collapsed')
    with cols[1]:
        st.markdown('<div class="tight-label">Answer</div>', unsafe_allow_html=True)
        ans = st.text_area("", value=row.get('பதில் ', ''), key="ans", height=40, label_visibility='collapsed')
    st.markdown('<div class="tight-label">விளக்கம்</div>', unsafe_allow_html=True)
    tamil_exp = st.text_area("", value=vilakkam_val, height=175, key="edit_exp", label_visibility='collapsed')
    st.markdown('</div>', unsafe_allow_html=True)

    # --- Horizontal divider line: zero margin, zero padding, thin ---
    st.markdown(
        '<hr style="height:1.3px;border:none;background:#666;margin:0 0 0 0;padding:0;">',
        unsafe_allow_html=True
    )

    # --- Non-editable block: exactly 40vh, centered if underfilled, scrolls if overflows ---
    st.markdown(f"""
    <div class="cw-40-fixed">
        <div><b>தமிழ்</b></div>
        <div><strong>கேள்வி:</strong> {row.get('கேள்வி', '')}</div>
        <div><strong>விருப்பங்கள்:</strong> {row.get('விருப்பங்கள் ', '')}</div>
        <div><strong>பதில்:</strong> {row.get('பதில் ', '')}</div>
        <div><strong>விளக்கம்:</strong> {vilakkam_val}</div>
        <div style="height:0.13em"></div>
        <div><b>English</b></div>
        <div><strong>Question:</strong> {row.get('question ', '')}</div>
        <div><strong>Options:</strong> {row.get('questionOptions', '')}</div>
        <div><strong>Answer:</strong> {row.get('answers ', '')}</div>
        <div><strong>Explanation:</strong> {row.get('explanation', '')}</div>
    </div>
    """, unsafe_allow_html=True)

else:
    st.info("Please upload your bilingual Excel file to begin.")
