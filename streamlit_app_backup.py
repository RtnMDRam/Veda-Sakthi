import streamlit as st
import pandas as pd

st.markdown("""
    <style>
    /* Editable area */
    .block-container { padding-bottom: 0 !important; padding-top: 0.2rem !important; }
    .main { padding-bottom: 0 !important; margin-bottom: 0 !important; }
    .tight-label { 
        font-size: 0.85em !important; 
        font-weight: 500 !important; 
        line-height: 1.08; 
        margin-bottom: -0.34em !important; 
        margin-top: -0.51em !important;
        padding-bottom:0 !important; 
        padding-top:0 !important; 
    }
    .stTextArea { margin-top: -0.44em !important; margin-bottom: -0.55em !important; }
    textarea[data-baseweb="textarea"] { min-height: 44px !important; font-size: 0.98em !important; }
    .stTextArea label { display:none !important; }
    body, html { margin-bottom: 0 !important; padding-bottom: 0 !important;}
    footer {visibility: hidden;}
    /* Reference block (absolute minimum margin) */
    .cw-min {
        line-height: 1.06 !important;
        margin: 0 !important;
        padding: 0 !important;
        font-size: 1.01em !important;
    }
    .cw-min strong { font-weight: 600 !important; }
    </style>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload a bilingual Excel file (.xlsx)", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.success("File uploaded successfully!")
    row = df.iloc[0]
    vilakkam_val = row.get('விளக்கம்', '') or row.get('விளக்கம் ', '')

    # --- Editable block: ultra-compact ---
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

    # --- Non-editable reference block: ultra-compact (custom HTML for minimal vertical space) ---
    st.markdown(f"""
    <div class="cw-min">
      <b>தமிழ்</b><br>
      <strong>கேள்வி:</strong> {row.get('கேள்வி', '')}<br>
      <strong>விருப்பங்கள்:</strong> {row.get('விருப்பங்கள் ', '')}<br>
      <strong>பதில்:</strong> {row.get('பதில் ', '')}<br>
      <strong>விளக்கம்:</strong> {vilakkam_val}
    </div>
    <div style="height: 0.3em;"></div>
    <div class="cw-min">
      <b>English</b><br>
      <strong>Question:</strong> {row.get('question ', '')}<br>
      <strong>Options:</strong> {row.get('questionOptions', '')}<br>
      <strong>Answer:</strong> {row.get('answers ', '')}<br>
      <strong>Explanation:</strong> {row.get('explanation', '')}
    </div>
    """, unsafe_allow_html=True)

else:
    st.info("Please upload your bilingual Excel file to begin.")
