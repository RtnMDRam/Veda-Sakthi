import streamlit as st

# Set page config for portrait, restrict max width and height
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
.sme-mainbox {
    width: 1500px;
    height: 2200px;
    margin: 0 auto;
    background: #fff;
    border-radius: 18px;
    border: 1.8px solid #e2e3ea;
    box-shadow: 0 4px 22px rgba(24,28,34,0.06);
    padding: 35px 32px 22px 32px;
    overflow-y: hidden;
    font-family: 'Segoe UI',Arial,sans-serif;
}
.sme-headrow {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 13px;
}
.sme-title {font-size:1.22em; font-weight:700; color:#2d364d;}
.sme-btnrow {display: flex; flex-wrap: wrap; gap: 11px; margin-bottom: 17px;}
.sme-btn {
    padding: 9px 27px;
    background: #e8ebf6;
    color: #494676;
    border: 1.2px solid #bdbecb;
    border-radius: 8px;
    font-weight: 500;
    font-size: 1em;
}
.sme-btn:hover {background:#cfd1e1;}
.sme-section {margin-bottom:12px;}
.sme-label {font-weight:500;color:#383836;font-size:1.08em;}
.sme-rowopts {display: flex; gap:30px;}
.sme-optcell {width:48%;}
.sme-short {width:48%; display:inline-block;}
.sme-widelong {height: 120px;}
.sme-explain {height:140px;}
.sme-ta-long {height:160px;}
</style>
<div class="sme-mainbox">
  <div class="sme-headrow">
    <span class="sme-label">Date</span>
    <span class="sme-title">பாட பொருள் நிபுணர் குழு / Subject Matter Expert (SME) Panel</span>
    <span class="sme-label">Time</span>
  </div>
  <div class="sme-section" style="display:flex; gap:13px;">
    <span>Paste the CSV/XLSX Link Given by Admin</span>
    <button class="sme-btn">Load</button>
    <span>Upload the CSV/XLSX file from Drive or Storage</span>
    <button class="sme-btn">Load</button>
  </div>
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
  <div class="sme-section">
    <span class="sme-label">கேள்வி :</span>
    <textarea class="sme-ta-long" style="width:100%;" rows="2"></textarea>
  </div>
  <div class="sme-rowopts sme-section">
    <div class="sme-optcell">
      <span class="sme-label">option "A"</span>
      <input type="text" style="width:100%;height:34px;">
    </div>
    <div class="sme-optcell">
      <span class="sme-label">option "C"</span>
      <input type="text" style="width:100%;height:34px;">
    </div>
  </div>
  <div class="sme-rowopts sme-section">
    <div class="sme-optcell">
      <span class="sme-label">option "B"</span>
      <input type="text" style="width:100%;height:34px;">
    </div>
    <div class="sme-optcell">
      <span class="sme-label">option "D"</span>
      <input type="text" style="width:100%;height:34px;">
    </div>
  </div>
  <div class="sme-rowopts sme-section">
    <div class="sme-short">
      <span class="sme-label">சொல் அகராதி / Glossary</span>
      <input type="text" style="width:100%;" placeholder="Type the word for Glossary check">
    </div>
    <div class="sme-short">
      <span class="sme-label">பதில் / Answer</span>
      <input type="text" style="width:100%;" placeholder="Auto Display from Option's">
    </div>
  </div>
  <div class="sme-section">
    <span class="sme-label">விளக்கம் :</span>
    <textarea class="sme-explain" style="width:100%;"></textarea>
  </div>
  <div class="sme-section">
    <span class="sme-label">தமிழ் பதிப்பு</span>
    <textarea class="sme-widelong" style="width:100%;"></textarea>
  </div>
  <div class="sme-section">
    <span class="sme-label">English Version</span>
    <textarea class="sme-widelong" style="width:100%;"></textarea>
  </div>
</div>
""", unsafe_allow_html=True)
