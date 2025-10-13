import streamlit as st
import pandas as pd
from datetime import datetime

# Pastel colors and panel widths (adjust as needed)
SME_BG = "#F5F6F9"
PASTEL_GREEN = "#CEF3D6"
PASTEL_BLUE = "#CFE8F6"
PASTEL_PURPLE = "#E6D4F1"
PASTEL_GREY = "#F7F8FA"
BORDER_COLOR = "#B0B8D1"
OFF_WHITE = "#FCFCFF"
PANEL_W = 1024
BUTTON_H = 42

st.set_page_config(page_title="SME iPad Panel", layout="centered")

st.markdown(f"""
    <style>
    html, body, [data-testid="stAppViewContainer"] {{
        background: {SME_BG} !important;
    }}
    .block-container {{
        max-width: {PANEL_W}px !important;
        margin-left: auto !important;
        margin-right: auto !important;
        padding-top: 8px !important;
        padding-bottom: 6px !important;
    }}
    .smepastel {{
        border:2.5px solid {BORDER_COLOR}; border-radius:14px; background: {PASTEL_GREY}; 
        margin-bottom:18px; padding:0;
    }}
    .smepane-title {{
        background: {PASTEL_GREEN}; border-radius:14px 14px 0 0; 
        padding:12px 35px 5px 18px; display:flex; 
        justify-content:space-between; align-items:center;
        font-size:1.15rem;font-weight:700;
    }}
    .sme-btn-bar button {{
        font-size:1.04rem;margin-right:8px;height:{BUTTON_H}px;
        border-radius:8px;border:none;font-weight:600;padding:0 19px;
        background: {PASTEL_PURPLE};color:#513568;
    }}
    .sme-btn-bar button.save {{
        background:{PASTEL_GREEN};color:#176655;
    }}
    .sme-btn-bar button.next {{
        background:{PASTEL_BLUE};color:#194365;
    }}
    .sme-btn-bar button.cont {{
        background:{PASTEL_PURPLE};color:#513568;
    }}
    .sme-upload-bar {{
        display: flex; gap: 16px; padding: 18px 10px; background: {PASTEL_BLUE}; border-radius: 0 0 14px 14px; margin-bottom:4px;
        align-items:center; min-height:54px;
    }}
    .sme-upload-link {{
        background: #ecf6fa; border:1.5px solid #a6b4ca; border-radius:7px; padding:8px 6px; font-size:1.02rem; width:300px;
    }}
    .sme-upload-file {{ flex:2; }}
    .sme-load-btn {{
        background: #c7f8eb; color:#14696f; border-radius:7px; min-width:70px;
        font-size:1.07rem; height:39px; border:none; font-weight:700; margin-left:10px;
    }}
    </style>
""", unsafe_allow_html=True)

# ----------- Top Layer 1: Title/date/time
now = datetime.now()
st.markdown(
    f"""
    <div class="smepane-title" style="width:{PANEL_W}px;margin-bottom:0;">
        <span>Veda-Sakthi SME Panel <span style='font-weight:400; font-size:0.89rem;'>&nbsp;&nbsp;| Subject Matter Expert (SME) Review</span></span>
        <span>
            {now.strftime("“%Y-%b-%d”")} &nbsp;|&nbsp; {now.strftime("“%H:%M”")}
        </span>
    </div>
    """, unsafe_allow_html=True
)

# ----------- Top Layer 2: Upload area (Paste link + local upload + Load)
st.markdown(f'<div class="smepastel" style="padding:0;">', unsafe_allow_html=True)
upload_cols = st.columns([2, 2, 1])
with upload_cols[0]:
    drive_link = st.text_input(
        "Paste Drive/Excel Link here", key="upload_drive_link",
        placeholder="https://drive.google.com/...",
        help="Paste link to an Excel/CSV file shared with link access."
    )
with upload_cols[1]:
    uploaded_file = st.file_uploader(
        "Or select file from device", type=["xlsx", "xls", "csv"], key="upload_local_file"
    )
with upload_cols[2]:
    if st.button("LOAD", key="load_btn_panel"):
        st.success("File/Link load requested (simulate logic here)")
st.markdown('</div>', unsafe_allow_html=True)

# Optionally, show what was loaded for confirmation.
if drive_link:
    st.markdown(
        f"<div style='background:#eaf7e6;padding:6px 8px;border-radius:7px;font-size:0.99rem;'>Loaded file link: {drive_link}</div>",
        unsafe_allow_html=True)
if uploaded_file is not None:
    st.markdown(
        f"<div style='background:#f9f6e4;padding:6px 8px;border-radius:7px;font-size:0.99rem;'>File uploaded: {uploaded_file.name}</div>",
        unsafe_allow_html=True
    )

# ----------- Top Layer 3: Button bar
st.markdown(f'<div class="smepastel"><div class="sme-btn-bar" style="padding:12px 18px 8px 18px;">', unsafe_allow_html=True)
colB = st.columns([1,1,1,1,1,1,1])
with colB[0]:
    st.button("Hi! Glossary", key="btn_glossary")
with colB[1]:
    st.button("Save & Cont.", key="btn_savecont", help="Save and continue editing")
with colB[2]:
    st.button("Row #A", key="btn_rowA")
with colB[3]:
    st.button("_id Number", key="btn_id")
with colB[4]:
    st.button("Row #Z", key="btn_rowZ")
with colB[5]:
    st.button("Save & Next", key="btn_next")
with colB[6]:
    st.button("Save File", key="btn_savefile")
st.markdown("</div></div>", unsafe_allow_html=True)

# ---- Central Editing/Table Panel ----
st.markdown(
    f"<div class='smepastel' style='min-height:390px;padding:25px 14px 20px 14px;'>"
    f"<div style='font-size:1.15rem;font-weight:600;margin-bottom:7px;'>கேள்வி :</div>", unsafe_allow_html=True)
tm_edit = st.text_area("Edit Tamil", value="உதாரணம்: ஒரு செல் என்றால் என்ன?", height=52)

# MCQ options (A+B, C+D) and glossary/answer
mcq1, mcq2 = st.columns([1,1])
with mcq1: st.markdown(f"<div style='background:{PASTEL_GREEN};padding:13px 8px;border-radius:8px;'>Auto 'A'<br>Option A</div>",unsafe_allow_html=True)
with mcq2: st.markdown(f"<div style='background:{PASTEL_GREEN};padding:13px 8px;border-radius:8px;'>Auto 'B'<br>Option B</div>",unsafe_allow_html=True)
mcq3, mcq4 = st.columns([1,1])
with mcq3: st.markdown(f"<div style='background:{PASTEL_BLUE};padding:13px 8px;border-radius:8px;'>Auto 'C'<br>Option C</div>",unsafe_allow_html=True)
with mcq4: st.markdown(f"<div style='background:{PASTEL_BLUE};padding:13px 8px;border-radius:8px;'>Auto 'D'<br>Option D</div>",unsafe_allow_html=True)

# Glossary and answer
st.markdown(
    f"<div style='display:flex;gap:17px;margin-top:13px;margin-bottom:7px;'>"
    f"<div style='background:{PASTEL_PURPLE};border-radius:7px;min-width:200px;padding:9px 7px;'>"
    f"<b>சொல் அகராதி / Glossary</b><br><input type='text' style='width:92%;padding:7px;border-radius:7px;'></div>"
    f"<div style='background:{PASTEL_PURPLE};border-radius:7px;min-width:200px;padding:9px 7px;'>"
    f"<b>சரியான பதில் / Correct</b><br><select style='width:88%;padding:7px;border-radius:7px;margin-top:3px;'><option>A</option><option>B</option><option>C</option><option>D</option></select></div>"
    f"</div>", unsafe_allow_html=True
)
st.text_area("விளக்கங்கள் :", value="", height=48)
st.markdown("</div>", unsafe_allow_html=True)

# --------- Bottom: Reference panels ---------
tamil_block = "உதாரணம்: ஒரு செல் என்றால் என்ன?"
eng_block = "Sample: What is a cell?"

st.markdown(f"""
<div class="smepastel" style="height:88px;background:{PASTEL_PURPLE};padding:10px 7px 4px 16px;">
<b>தமிழ் அசல்</b><br>{tamil_block}
</div>
<div class="smepastel" style="height:88px;background:{PASTEL_BLUE};padding:10px 7px 4px 16px;">
<b>English</b><br>{eng_block}
</div>
""", unsafe_allow_html=True)

st.info("Classic iPad SME panel: blocks/fields will auto-size for optimal iPad landscape fit. Further tweaks can be made after live review.")
