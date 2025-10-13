import streamlit as st
import pandas as pd
from datetime import datetime

# Pastel color palette
PASTEL_GREEN = "#CDE6D0"
PASTEL_BLUE = "#CEE7F5"
PASTEL_PURPLE = "#DED1E8"
BUTTON_BG = "#D3B5E6"
BORDER_COLOR = "#8FA6C1"
OFF_WHITE = "#FBFBFD"
HEADER_BG = "#BFEDEA"

st.set_page_config(page_title="SME Panel", layout="wide")
st.markdown(f"""
<style>
#MainMenu, header, footer {{visibility: hidden;}}
[data-testid="stSidebar"] {{ display: none !important; }}
.block-container {{ padding-top: 0.8rem; }}
</style>
""", unsafe_allow_html=True)

now = datetime.now()
date_str = now.strftime("“%Y-%b-%d”")
time_24 = now.strftime("“%H:%M”")

st.markdown(f"""
<div style="background:{HEADER_BG};border-radius:13px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;padding:16px 18px 8px 18px;margin-bottom:8px;">
  <span style="font-size:1.25rem;font-weight:700;color:#23504d;">Veda-Sakthi SME Panel</span>
  <span style="font-size:1.08rem;color:#1e394c;">{date_str} | {time_24}</span>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload bilingual Excel (.xlsx)", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
else:
    df = pd.DataFrame({
        "question": ["Sample: What is a cell?", "Sample: Explain tissue organization."],
        "கேள்வி": ["உதாரணம்: ஒரு செல் என்றால் என்ன?", "உதாரணம்: திசு அமைப்பு விளக்குக."],
        "A": ["Option A", "Option A2"],
        "B": ["Option B", "Option B2"],
        "C": ["Option C", "Option C2"],
        "D": ["Option D", "Option D2"],
        "_id": [1, 2]
    })

if 'edited_tamil' not in st.session_state:
    st.session_state.edited_tamil = list(df["கேள்வி"])
if 'row_index' not in st.session_state:
    st.session_state.row_index = 0

row_idx = st.session_state.row_index
total_questions = len(df)

# Top button bar
st.markdown(f"""
<div style="display:flex;gap:8px;margin-bottom:12px;">
  <button style="background:{PASTEL_GREEN};color:#185735;font-size:1rem;border:none;padding:7px 18px;border-radius:8px;font-weight:600;">Hi! Glossary</button>
  <button style="background:{PASTEL_PURPLE};color:#54315b;border:none;padding:7px 18px;border-radius:8px;font-weight:700;">Save & Cont.</button>
  <span style="background:{OFF_WHITE};border:1px solid {BORDER_COLOR};padding:7px 14px;border-radius:8px;">Row #A: {row_idx+1}</span>
  <span style="background:{OFF_WHITE};border:1px solid {BORDER_COLOR};padding:7px 14px;border-radius:8px;">_id: {df.loc[row_idx, '_id'] if '_id' in df.columns else row_idx+1}</span>
  <span style="background:{OFF_WHITE};border:1px solid {BORDER_COLOR};padding:7px 14px;border-radius:8px;">Row #Z: {total_questions-row_idx}</span>
  <button style="background:{PASTEL_BLUE};color:#18355d;border:none;padding:7px 18px;border-radius:8px;font-weight:700;">Save & Next</button>
  <button style="background:{PASTEL_GREEN};color:#367d51;border:none;padding:7px 18px;border-radius:8px;font-weight:700;">Save File</button>
</div>
""", unsafe_allow_html=True)

st.markdown(f"<div style='background:{OFF_WHITE}; border-radius:13px; border:1px solid {BORDER_COLOR}; padding:18px;'>", unsafe_allow_html=True)
st.markdown("<strong>கேள்வி :</strong>", unsafe_allow_html=True)

edited_tamil = st.text_area("Edit Tamil Text", value=st.session_state.edited_tamil[row_idx], height=54)
if st.button("Save Edit", key="save_edit"):
    st.session_state.edited_tamil[row_idx] = edited_tamil
    st.success("Saved edit for this question.")

st.markdown(f"""
<div style="display:flex;gap:7px;margin-bottom:10px;">
    <div style="flex:1;background:{PASTEL_GREEN};border-radius:8px;padding:12px 8px;">Auto Display "A"<br>{df.iloc[row_idx]['A'] if 'A' in df.columns else ""}</div>
    <div style="flex:1;background:{PASTEL_GREEN};border-radius:8px;padding:12px 8px;">Auto Display "B"<br>{df.iloc[row_idx]['B'] if 'B' in df.columns else ""}</div>
    <div style="flex:1;background:{PASTEL_BLUE};border-radius:8px;padding:12px 8px;">Auto Display "C"<br>{df.iloc[row_idx]['C'] if 'C' in df.columns else ""}</div>
    <div style="flex:1;background:{PASTEL_BLUE};border-radius:8px;padding:12px 8px;">Auto Display "D"<br>{df.iloc[row_idx]['D'] if 'D' in df.columns else ""}</div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="display:flex;gap:16px;margin-bottom:9px;">
    <div style="background:{PASTEL_PURPLE};border-radius:7px;padding:11px 7px;min-width:180px;">
        <label style="font-weight:600;color:#553cb4;">சொல் அகராதி / Glossary</label><br>
        <input type="text" style="width:95%;padding:7px;border-radius:8px;" placeholder="Type the word">
    </div>
    <div style="background:{PASTEL_PURPLE};border-radius:7px;padding:11px 7px;min-width:180px;">
        <label style="font-weight:600;color:#363c86;">சரியான பதில் / Correct Answer</label><br>
        <select style="width:88%;padding:7px;border-radius:8px;margin-top:3px;">
            <option>A</option>
            <option>B</option>
            <option>C</option>
            <option>D</option>
        </select>
    </div>
</div>
""", unsafe_allow_html=True)

explanation = st.text_area("விளக்கங்கள் :", value="", height=45)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"<div style='font-weight:600;'>தமிழ் அசல்</div>", unsafe_allow_html=True)
st.markdown(f"<div style='background:{PASTEL_PURPLE};border-radius:8px;padding:10px;'>{df.iloc[row_idx]['கேள்வி']}</div>", unsafe_allow_html=True)
st.markdown("<div style='font-weight:600;'>English</div>", unsafe_allow_html=True)
st.markdown(f"<div style='background:{PASTEL_BLUE};border-radius:8px;padding:10px;'>{df.iloc[row_idx]['question']}</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if row_idx > 0:
        if st.button("Previous", key="prev"):
            st.session_state.row_index -= 1
with col2:
    if row_idx < len(df) - 1:
        if st.button("Next", key="next"):
            st.session_state.row_index += 1

if st.button("Finish", key="finish"):
    df["கேள்வி"] = st.session_state.edited_tamil
    df.to_excel("SME_Reviewed_bilingual.xlsx", index=False)
    st.success("All edits saved locally as SME_Reviewed_bilingual.xlsx.")

st.markdown("</div>", unsafe_allow_html=True)
st.info("Classic pastel color, touch-friendly SME panel for easy iPad review of bilingual Excel. Enhance/revise layout anytime.")
