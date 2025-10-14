import streamlit as st
import pandas as pd

st.markdown("""
    <style>
    .block-container { padding-bottom: 0 !important; padding-top: 0.2rem !important; }
    .main { padding-bottom: 0 !important; margin-bottom: 0 !important; }
    .option-row { display: flex; gap: 6px !important; margin-bottom: 0.15rem !important;}
    .option-cell { flex: 1; }
    .answer-row { display: flex; gap: 6px !important; margin-bottom: 0.18rem !important;}
    .glossary-cell { width: 30%; }
    .answer-cell { width: 70%; }
    label, .stTextArea label { font-size: 0.91em !important; font-weight: 500 !important; margin-bottom: 0.07em !important; }
    textarea[data-baseweb="textarea"] { min-height: 47px !important; font-size: 1em !important; }
    </style>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload a bilingual Excel file (.xlsx)", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.success("File uploaded successfully!")
    row = df.iloc[0]
    vilakkam_val = row.get('விளக்கம்', '') or row.get('விளக்கம் ', '')
    opts = str(row.get('விருப்பங்கள் ', '')).split('|')
    opts = [o.strip() for o in opts if o.strip()]
    # Default: split original options into 4 if possible, else fallback to blanks
    opts = (opts + [""]*4)[:4]

    # Editable Question (full width)
    st.markdown('<div style="font-size:0.99em; font-weight:500; margin-bottom: 0.09em;">கேள்வி</div>', unsafe_allow_html=True)
    tamil_q = st.text_area("", value=row.get('கேள்வி', ''), height=58, key="edit_q")

    # Editable Options A & B (row)
    st.markdown('<div style="font-size:0.98em; font-weight:500; margin-bottom: 0.04em;">விருப்பங்கள்</div>', unsafe_allow_html=True)
    colA, colB = st.columns([1, 1], gap="small")
    with colA:
        st.markdown('<div style="font-size:0.92em; margin-bottom:-6px;">A</div>', unsafe_allow_html=True)
        optA = st.text_area("", value=opts[0], key="optA", height=46)
    with colB:
        st.markdown('<div style="font-size:0.92em; margin-bottom:-6px;">B</div>', unsafe_allow_html=True)
        optB = st.text_area("", value=opts[1], key="optB", height=46)

    # Editable Options C & D (next row)
    colC, colD = st.columns([1, 1], gap="small")
    with colC:
        st.markdown('<div style="font-size:0.92em; margin-bottom:-6px;">C</div>', unsafe_allow_html=True)
        optC = st.text_area("", value=opts[2], key="optC", height=46)
    with colD:
        st.markdown('<div style="font-size:0.92em; margin-bottom:-6px;">D</div>', unsafe_allow_html=True)
        optD = st.text_area("", value=opts[3], key="optD", height=46)

    # Answer/Glossary row (side by side, matching your green/blue separation)
    colG, colAns = st.columns([1, 2], gap="small")
    with colG:
        st.markdown('<div style="font-size:0.92em; margin-bottom:-6px;">Glossary</div>', unsafe_allow_html=True)
        gloss = st.text_area("", value="", key="gloss", height=42)
    with colAns:
        st.markdown('<div style="font-size:0.92em; margin-bottom:-6px;">Answer</div>', unsafe_allow_html=True)
        ans = st.text_area("", value=row.get('பதில் ', ''), key="ans", height=42)

    # Editable Explanation
    st.markdown('<div style="font-size:0.99em; font-weight:500; margin-bottom: 0.09em;">விளக்கம்</div>', unsafe_allow_html=True)
    tamil_exp = st.text_area("", value=vilakkam_val, height=90, key="edit_exp")

    # Reference display for checking below (no changes)
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
