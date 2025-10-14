import streamlit as st
import pandas as pd

st.markdown("""
    <style>
    .block-container { padding-bottom: 0 !important; padding-top: 0.2rem !important; }
    .main { padding-bottom: 0 !important; margin-bottom: 0 !important; }
    textarea[data-baseweb="textarea"] { min-height: 12vh !important; margin-bottom: 0.1rem !important; }
    div[data-testid="stVerticalBlock"] > div { margin-bottom: -0.45rem; } /* Tight vertical spacing */
    h4 { font-size: 1.05em !important; font-weight: 600 !important; margin-bottom: 0.07em !important; margin-top: 0.13em !important;}
    p, ul, ol { margin-bottom: 0.07em !important; margin-top: 0.07em !important; font-size: 1.01em !important;}
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

    # Editable fields: only placeholder shows the context inside box, zero vertical gap
    tamil_q = st.text_area("", value=row.get('கேள்வி', ''), height=80, key="edit_q", placeholder="கேள்வி (Question)")
    tamil_opts = st.text_area("", value=row.get('விருப்பங்கள் ', ''), height=80, key="edit_opts", placeholder="விருப்பங்கள் (Options)")
    tamil_ans = st.text_area("", value=row.get('பதில் ', ''), height=60, key="edit_ans", placeholder="பதில் (Answer)")
    tamil_exp = st.text_area("", value=vilakkam_val, height=115, key="edit_exp", placeholder="விளக்கம் (Explanation)")

    # Non-editable reference display below
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
