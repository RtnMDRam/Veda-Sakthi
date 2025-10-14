import streamlit as st
import pandas as pd
from datetime import datetime

PASTEL_GREEN = "#D2F0D4"
PASTEL_BLUE = "#D5E6FA"
PASTEL_PURPLE = "#E5D7F7"
BORDER_COLOR = "#A3B1C6"
OFF_WHITE = "#F9F9FB"
PANEL_W = 1024

st.set_page_config(page_title="SME iPad Panel", layout="centered")

st.markdown(f"""
    <style>
    html, body, [data-testid="stAppViewContainer"] {{
        background: {OFF_WHITE} !important;
    }}
    .block-container {{
        max-width: {PANEL_W}px !important;
        margin:auto !important;
        padding-top:6px !important;
        padding-bottom:0 !important;
    }}
    .sme-headrow {{
        display:flex;align-items:center;width:100%;padding:6px 0 0 0;
    }}
    .sme-title {{
        background:{PASTEL_GREEN};font-size:1.13rem;font-weight:700;
        padding:8px 14px 8px 18px;border-radius:12px 12px 0 0;width:65%;
        border:2px solid {BORDER_COLOR};border-bottom:0;
    }}
    .sme-date {{
        background:{PASTEL_GREEN};padding:8px 18px;font-size:1.02rem;
        border-radius:0 12px 0 0; border:2px solid {BORDER_COLOR};border-bottom:0;border-left:0;width:35%;text-align:right;
    }}
    .sme-uploadbar {{
        background:{PASTEL_BLUE};display:flex;gap:18px;
        padding:7px 13px 7px 13px;width:100%;
        border:2px solid {BORDER_COLOR};border-top:0;border-bottom:0;
    }}
    .sme-uploadbox, .sme-filebox {{
        flex:1;background:#f7fbfd;border-radius:6px;
        border:1.3px solid #abc2d1;padding:4px 8px;min-width:0;
    }}
    .sme-filebox label, .sme-uploadbox label {{
        font-size:0.95rem;font-weight:500;margin-bottom:2px;display:block;
    }}
    .sme-btnbar {{
        background:{PASTEL_PURPLE};display:flex;gap:8px;
        padding:8px 8px 4px 8px;width:100%;
        border:2px solid {BORDER_COLOR};border-top:0;border-radius:0 0 12px 12px;
    }}
    .sme-btnbar button {{
        width:calc(100%/7 - 6px);min-width:54px;font-size:1rem;height:38px;
        background:#fff;color:#623d90;border:1.4px solid {BORDER_COLOR};
        border-radius:7px;font-weight:600;padding:0 2px;
    }}
    .sme-q-edit {{width:100%;background:{OFF_WHITE};padding:0;margin:0;}}
    .sme-options-row {{
        display:flex;gap:8px;margin:2px 0 0 0;
        background:transparent;
    }}
    .sme-option {{
        flex:1;padding:7px 6px 7px 10px;font-size:1.05rem;border-radius:6px;
        min-width:0;text-align:left;
        border:1.3px solid {BORDER_COLOR};background:{PASTEL_GREEN};
    }}
    .sme-option.b {{background:{PASTEL_GREEN};}}
    .sme-option.c, .sme-option.d {{background:{PASTEL_BLUE};}}
    .sme-glossdiv {{
        display:flex;gap:10px;padding:4px 0;
    }}
    .sme-glossbox,.sme-ansbox {{
        flex:1;padding:5px 7px;background:{PASTEL_PURPLE};
        border-radius:7px;min-width:0;font-size:1.02rem;border:1.3px solid {BORDER_COLOR};
    }}
    .sme-exp {{background:#fff;margin:0;border-radius:7px;border:1.3px solid {BORDER_COLOR};padding:2px 7px 2px 5px;}}
    .sme-ref-tam, .sme-ref-eng {{
        margin-top:0;margin-bottom:0;padding:4px 9px 4px 12px;
        border:1.8px solid {BORDER_COLOR};background:{PASTEL_PURPLE};
        border-radius:8px 8px 0 0;font-size:1.05rem;
    }}
    .sme-ref-eng {{
        background:{PASTEL_BLUE};border-radius:0 0 8px 8px;border-top:0;
        margin-top:0;
    }}
    </style>
""", unsafe_allow_html=True)

now = datetime.now()
st.markdown(
    f"""<div class="sme-headrow">
        <div class="sme-title">Veda-Sakthi SME Panel</div>
        <div class="sme-date">{now.strftime("“%Y-%b-%d”")} &nbsp;|&nbsp; {now.strftime("“%H:%M”")}</div>
    </div>""", unsafe_allow_html=True
)

st.markdown('<div class="sme-uploadbar">', unsafe_allow_html=True)
col_upload, col_file = st.columns([1,1])
with col_upload:
    drive_link = st.text_input("Paste Drive/Excel Link:", key="drive_link",placeholder="https://drive.google.com/...")
with col_file:
    uploaded_file = st.file_uploader("Browse file from device", type=["xlsx","xls","csv"], key="file_up")
st.markdown('</div>', unsafe_allow_html=True)

# Button bar tightly below
st.markdown('<div class="sme-btnbar">', unsafe_allow_html=True)
btn1, btn2, btn3, btn4, btn5, btn6, btn7 = st.columns(7)
with btn1: st.button("Hi! Glossary")
with btn2: st.button("Save & Cont.")
with btn3: st.button("Row #A")
with btn4: st.button("_id Number")
with btn5: st.button("Row #Z")
with btn6: st.button("Save & Next")
with btn7: st.button("Save File")
st.markdown('</div>', unsafe_allow_html=True)

# SME main edit block, all fields close together
st.markdown('<div class="sme-q-edit">', unsafe_allow_html=True)
smq_edit = st.text_area("Edit Tamil (editable)", value="உதாரணம்: ஒரு செல் என்றால் என்ன?", height=48)
st.markdown('</div>', unsafe_allow_html=True)
# MCQ option block tight rows
st.markdown('<div class="sme-options-row">', unsafe_allow_html=True)
o1, o2, o3, o4 = st.columns(4)
with o1: st.markdown('<div class="sme-option">Auto A<br>Option A</div>',unsafe_allow_html=True)
with o2: st.markdown('<div class="sme-option b">Auto B<br>Option B</div>',unsafe_allow_html=True)
with o3: st.markdown('<div class="sme-option c">Auto C<br>Option C</div>',unsafe_allow_html=True)
with o4: st.markdown('<div class="sme-option d">Auto D<br>Option D</div>',unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
# Glossary + Answer
st.markdown('<div class="sme-glossdiv">', unsafe_allow_html=True)
gloss = st.text_input("சொல் அகராதி / Glossary")
with st.container():
    st.markdown('<div class="sme-ansbox"><b>சரியான பதில் / Correct:</b> ', unsafe_allow_html=True)
    answ = st.selectbox("",["A","B","C","D"], key="sel_ans")
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
# Explanation compact
explan = st.text_area("விளக்கங்கள் :", height=44)
st.markdown('<br>', unsafe_allow_html=True)

# Reference blocks: absolutely no vertical space between!
st.markdown(f'<div class="sme-ref-tam"><b>தமிழ் அசல்</b> &nbsp; {smq_edit}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="sme-ref-eng"><b>English</b> &nbsp; Sample: What is a cell?</div>', unsafe_allow_html=True)
