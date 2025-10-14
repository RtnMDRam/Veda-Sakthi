import streamlit as st
import pandas as pd
from datetime import datetime

PANEL_W = 1024

st.set_page_config(page_title="SME Panel", layout="centered")

st.markdown(f"""
<style>
.block-container {{
    max-width: {PANEL_W}px;
    margin: auto;
    padding-top: 6px;
}}
.section-title {{
    font-size: 1.11rem;
    font-weight: 700;
    padding-bottom: 3px;
}}
hr.sme-divider {{
    border: none;
    border-top: 1.5px solid #A0A8B8;
    margin: 0 0 7px 0;
}}
.ref-row {{
    display: flex; gap: 18px
}}
.ref-tam, .ref-eng {{
    font-size: 1.07rem; font-weight: 600; margin: 0; padding: 2px 0 1px 0;
}}
</style>
""", unsafe_allow_html=True)

now = datetime.now()
# Top 15%: Title, date/time, upload
st.markdown('<div class="section-title">Veda-Sakthi SME Panel</div>', unsafe_allow_html=True)
st.write(f"{now.strftime('“%Y-%b-%d”')} | {now.strftime('“%H:%M”')}")
st.markdown('<hr class="sme-divider">', unsafe_allow_html=True)

col_link, col_file = st.columns([1, 1])
with col_link:
    drive_link = st.text_input("Paste Drive/Excel Link:", key="drive_link", placeholder="https://...")
with col_file:
    uploaded_file = st.file_uploader("Browse file from device", type=["xlsx","xls","csv"])
st.markdown('<hr class="sme-divider">', unsafe_allow_html=True)

btns = st.columns(7)
btn_labels = ["Hi! Glossary", "Save & Cont.", "Row #A", "_id Number", "Row #Z", "Save & Next", "Save File"]
for idx, label in enumerate(btn_labels):
    with btns[idx]:
        st.button(label)
st.markdown('<hr class="sme-divider">', unsafe_allow_html=True)

# Middle 45%: SME Edit Zone
st.markdown('<div class="section-title">Edit Tamil (editable)</div>', unsafe_allow_html=True)
smq_edit = st.text_area("", value="உதாரணம்: ஒரு செல் என்றால் என்ன?", height=48)
st.markdown('<hr class="sme-divider">', unsafe_allow_html=True)

optrow = st.columns(4)
for idx, l in enumerate(["Auto A\nOption A", "Auto B\nOption B", "Auto C\nOption C", "Auto D\nOption D"]):
    with optrow[idx]:
        st.markdown(l)
st.markdown('<hr class="sme-divider">', unsafe_allow_html=True)

gcol, acol = st.columns(2)
with gcol:
    gloss = st.text_input("சொல் அகராதி / Glossary")
with acol:
    answ = st.selectbox("சரியான பதில் / Correct", ["A", "B", "C", "D"])
st.markdown('<hr class="sme-divider">', unsafe_allow_html=True)
explan = st.text_area("விளக்கங்கள் :", height=44)
st.markdown('<hr class="sme-divider">', unsafe_allow_html=True)

# Bottom 40%, split 20/20, no spacing, lines only
st.markdown('<div class="ref-row">', unsafe_allow_html=True)
col_tam, col_eng = st.columns(2)
with col_tam:
    st.markdown('<div class="ref-tam">தமிழ் அசல்</div>', unsafe_allow_html=True)
    st.markdown(smq_edit)
with col_eng:
    st.markdown('<div class="ref-eng">English</div>', unsafe_allow_html=True)
    st.markdown("Sample: What is a cell?")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<hr class="sme-divider">', unsafe_allow_html=True)
