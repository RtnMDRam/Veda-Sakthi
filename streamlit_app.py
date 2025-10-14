import streamlit as st
import pandas as pd
from datetime import datetime

PANEL_W = 1024

st.set_page_config(page_title="SME iPad Panel", layout="centered")

st.markdown(f"""
<style>
.block-container {{
    max-width: {PANEL_W}px;
    margin: auto;
    padding-top: 2px;
}}
hr.sme-divider {{
    border: none;
    border-top: 1.5px solid #B0B8C8;
    margin: 0px 0 7px 0;
}}
.sme-uploader {{
    display: flex; gap:16px; margin-bottom:0px;
}}
.sme-uploadbox {{
    flex:1; display:flex; flex-direction:column; justify-content:center;
}}
.sme-upload-input input, .sme-upload-input .uploadedFileName {{
    font-size:1.05rem; width:100%; margin-top:2px; margin-bottom:2px;
    padding:7px 9px; border-radius:6px; border:1.3px solid #BBC9E0;
    background:#fff;
}}
.sme-btnbar {{display:flex; gap:7px; margin:4px 0 2px 0;}}
.sme-btn {{
    height: 40px; border-radius: 7px; font-size: 0.98rem; font-weight: 600;
    background: #fafcff; color: #3c255b; border: 1.3px solid #A5AECD;
    flex: 1; min-width: 0; padding: 0 2px; margin: 0; transition: background 0.2s;
}}
.sme-btn-id {{
    flex: 1.5; min-width:70px;
}}
.sme-label {{
    font-size: 1.06rem; font-weight: 700; margin-bottom: 0; padding-bottom: 1px;
}}
.sme-fieldblock {{
    margin: 2px 0 4px 0 !important;
    width: 100%;
}}
.sme-optrow {{
    display: flex; gap:7px; margin:0;align-items: stretch;
}}
.sme-optblock {{
    flex:1; padding:7px 4px 7px 8px; font-size:1.04rem; background:#EFF8F2;
    border:1px solid #A5AECD; border-radius:6px; min-width:0;
}}
.sme-group-compact {{
    display:flex;gap:9px;width:100%;margin:2px 0 0 0;
}}
.sme-inline-label {{
    display:inline-block;font-size:0.95rem;font-weight:600;margin-right:6px;
}}
.sme-refpanel {{
    display: flex; gap:20px; margin-top:2px;
}}
.sme-refbox {{
    flex: 1; min-width:0; font-size: 1.04rem; padding:1px 0px;
}}
.sme-reflabel {{
    font-weight:700;font-size:1.01rem;display: inline-block;margin-right:8px;
}}
</style>
""", unsafe_allow_html=True)

now = datetime.now()

# Date/Top Title
st.markdown('<div class="sme-label">Veda-Sakthi SME Panel</div>', unsafe_allow_html=True)
st.write(f"{now.strftime('“%Y-%b-%d”')} | {now.strftime('“%H:%M”')}")
st.markdown('<hr class="sme-divider">', unsafe_allow_html=True)

# Upload row (side-by-side, equal width and style)
st.markdown('<div class="sme-uploader">', unsafe_allow_html=True)
with st.container():
    up1, up2 = st.columns([1,1], gap="small")
    with up1:
        drive_link = st.text_input("", key="drive_link", placeholder="Paste Drive/Excel Link")
    with up2:
        uploaded_file = st.file_uploader("", type=["xlsx","xls","csv"])
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<hr class="sme-divider">', unsafe_allow_html=True)

# Button row, _id Number wider
st.markdown('<div class="sme-btnbar">', unsafe_allow_html=True)
btn_labels = [
    ("Hi! Glossary", ""), ("Save & Cont.", ""), ("Row #A", ""), 
    ("_id Number", "sme-btn-id"), ("Row #Z", ""), 
    ("Save & Next", ""), ("Save File", "")
]
btn_cols = st.columns([1,1,1,1.5,1,1,1])
for idx, (label, style) in enumerate(btn_labels):
    btn_class = f"sme-btn {style}"
    btn_html = f'<button class="{btn_class}">{label}</button>'
    btn_cols[idx].markdown(btn_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Edit Tamil
st.markdown('<hr class="sme-divider">', unsafe_allow_html=True)
st.markdown('<div class="sme-label" style="margin-bottom:2px;margin-top:0;">Edit Tamil (editable)</div>', unsafe_allow_html=True)
smq_edit = st.text_area("", value="உதாரணம்: ஒரு செல் என்றால் என்ன?", height=46)
st.markdown('<div class="sme-fieldblock">', unsafe_allow_html=True)

# MCQ options row
st.markdown('<div class="sme-optrow">', unsafe_allow_html=True)
for opt_label in ["Auto A Option A", "Auto B Option B", "Auto C Option C", "Auto D Option D"]:
    st.markdown(f'<div class="sme-optblock">{opt_label}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Glossary/Answer row, plus Explanation
st.markdown('<div class="sme-group-compact">', unsafe_allow_html=True)
with st.container():
    col_left, col_right = st.columns([1,1])
    with col_left:
        gloss = st.text_input("சொல் அகராதி / Glossary", key="glossinp")
    with col_right:
        answ = st.selectbox("சரியான பதில் / Correct", ["A", "B", "C", "D"], key="answerinp")
st.markdown('</div>', unsafe_allow_html=True)
explan = st.text_area("விளக்கங்கள் :", height=38)
st.markdown('</div>', unsafe_allow_html=True)

# Reference Area: no line or space between
st.markdown('<hr class="sme-divider">', unsafe_allow_html=True)
st.markdown('<div class="sme-refpanel">', unsafe_allow_html=True)
st.markdown(f'<div class="sme-refbox"><span class="sme-reflabel">தமிழ் அசல்</span> {smq_edit}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="sme-refbox"><span class="sme-reflabel">English</span> Sample: What is a cell?</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
