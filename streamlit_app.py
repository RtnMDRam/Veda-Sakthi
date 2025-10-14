import streamlit as st

# Page settings for iPad-fit width
st.set_page_config(layout="wide")

# HEADER
st.markdown("""
<style>
.sme-table {width: 99vw;}
.sme-topcell {background: #f7ffee; border: 1px solid #d5c4e0; padding: 4px 8px; text-align: center; font-size: 1.08em;}
.sme-btnrow {display: flex; flex-wrap: wrap; gap: 6px; margin-top: 8px;}
.sme-btn {padding:6px 18px; background:#e6eaf3; color:#46446b; border:1px solid #bdbecb; border-radius:7px; font-weight:500;}
.sme-hlabel {font-size: 1.04em; font-weight:bold;}
.sme-label {font-weight: 500;}
.sme-box {background: #f5f5fa; border: 1.2px solid #b5bfa3; border-radius: 5px; padding: 7px 12px;}
hr {margin-top:1px;margin-bottom:7px;border:.3px solid #b5bfa3;}
</style>
<div class="sme-table">
  <table style="width:100%;border-collapse:collapse;table-layout:fixed;">
    <tr>
      <td style="width:15%;border:1px solid #bbb;"><b>Date</b></td>
      <td class="sme-topcell" style="width:63%;"><b>பாட பொருள் நிபுணர் குழு / Subject Matter Expert (SME) Panel</b></td>
      <td class="sme-topcell" style="width:10%;">Time</td>
    </tr>
    <tr>
      <td colspan="2" style="border:1px solid #bbb;">
        Paste the CSV/XLSX Link Given by Admin 
        <span style="margin-left:20px;"></span>
        <button class="sme-btn">Load</button>
        <span style="margin-left:20px;"></span>
        Upload the CSV/XLSX file from Drive or Storage
        <button class="sme-btn">Load</button>
      </td>
      <td style="border:1px solid #bbb;"></td>
    </tr>
  </table>
</div>
""", unsafe_allow_html=True)

# TOP BUTTONS ROW
st.markdown("""
<div class="sme-btnrow">
  <button class="sme-btn">Hi! Glossary</button>
  <button class="sme-btn">Save &amp; Cont..</button>
  <button class="sme-btn">Row #A</button>
  <button class="sme-btn">_id Number</button>
  <button class="sme-btn">Row # z</button>
  <button class="sme-btn">Save &amp; Next</button>
  <button class="sme-btn">Save File</button>
</div>
<hr>
""", unsafe_allow_html=True)

# MAIN CONTENT—QUESTION BLOCK
st.markdown('<div class="sme-hlabel">கேள்வி :</div>', unsafe_allow_html=True)
q = st.text_area("", "", key="question", height=28)

# FOUR OPTIONS, MATCHED AS PER EXCEL
colA, colC = st.columns(2)
with colA:
    optA = st.text_input('option "A"', key="optA")
    optB = st.text_input('option "B"', key="optB")
with colC:
    optC = st.text_input('option "C"', key="optC")
    optD = st.text_input('option "D"', key="optD")

# GLOSSARY AND ANSWER
colG, colAns = st.columns(2)
with colG:
    st.text_input("சொல் அகராதி / Glossary", placeholder="Type the word for Glossary check")
with colAns:
    st.text_input("பதில் / Answer", placeholder="Auto Display from Option's")

# EXPLANATION BOX
st.markdown('<div class="sme-label">விளக்கம் :</div>', unsafe_allow_html=True)
st.text_area("", "", key="explanation", height=74)

# TAMIL VERSION
st.markdown('<div style="margin-top:8px;font-weight:bold;">தமிழ் பதிப்பு</div>', unsafe_allow_html=True)
st.text_area("", "", key="ta_version", height=70)

# ENGLISH VERSION
st.markdown('<div style="margin-top:6px;color:#222;">English Version</div>', unsafe_allow_html=True)
st.text_area("", "", key="en_version", height=28)
