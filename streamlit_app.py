import streamlit as st

# Custom CSS for panel and buttons
st.markdown("""
    <style>
    .sme-panel {
        background: #fff;
        border-radius: 12px;
        box-shadow: 0 3px 8px rgba(0,0,0,0.05);
        padding: 32px 24px;
        margin: 24px 0;
        max-width: 600px;
    }
    .sme-row {
        display: flex;
        gap: 14px;
        margin-bottom: 18px;
        flex-wrap: wrap;
    }
    .sme-btn {
        background: #f7f1fa;
        border: 2px solid #ada9bb;
        border-radius: 8px;
        color: #484069;
        padding: 8px 18px;
        cursor: pointer;
        font-size: 1em;
        font-weight: 500;
        transition: background 0.2s;
        margin-bottom: 8px;
    }
    .sme-btn:hover {
        background: #ebe2f5;
    }
    .sme-label {
        font-weight: bold;
        margin-bottom: 5px;
        display: block;
        color: #351e48;
        font-size: 1.03em;
    }
    </style>
""", unsafe_allow_html=True)

# Top row of SME panel buttons
st.markdown("""
    <div class="sme-row">
        <button class="sme-btn">Hi! Glossary</button>
        <button class="sme-btn">Save &amp; Cont.</button>
        <button class="sme-btn">Row #A</button>
        <button class="sme-btn">_id Number</button>
        <button class="sme-btn">Row #Z</button>
        <button class="sme-btn">Save &amp; Next</button>
        <button class="sme-btn">Save File</button>
    </div>
""", unsafe_allow_html=True)

# SME Panel card, editable fields 
st.markdown('<div class="sme-panel">', unsafe_allow_html=True)
st.markdown('<span class="sme-label">Edit Tamil (editable)</span>', unsafe_allow_html=True)
st.text_area(" ", "உதாரணம்: ஒரு செல்என்றால் என்ன?", height=40, key="tamil_q")

opts = ["Auto A Option A", "Auto B Option B", "Auto C Option C", "Auto D Option D"]
for opt in opts:
    st.text_input("", value=opt, key=opt)

col1, col2 = st.columns([1,1])
with col1:
    st.text_input("சொல் அகராதி / Glossary")
with col2:
    st.selectbox("சரியான பதில் / Correct", ("A", "B", "C", "D"))

st.text_area("விநாகங்கள் :", "")

st.markdown('</div>', unsafe_allow_html=True)

# Display Tamil and English reference sample for review
st.markdown("**தமிழ்†அசல்**: உதாரணம்: ஒரு செல்என்றால் என்ன?  \n**English** Sample: What is a cell?")

