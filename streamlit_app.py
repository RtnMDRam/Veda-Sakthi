import streamlit as st

# Add custom CSS for rounded SME panel look
st.markdown("""
    <style>
    .sme-panel {
        background: #fff;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
        padding: 24px;
        margin-top: 20px;
        margin-bottom: 20px;
        max-width: 500px;
        font-family: Arial, sans-serif;
    }
    .sme-header {
        font-size: 1.3em;
        font-weight: bold;
        color: #333;
        margin-bottom: 14px;
    }
    .sme-field {
        margin-bottom: 10px;
    }
    .sme-label {
        font-weight: bold;
        color: #0072c6;
        display: inline-block;
        min-width: 120px;
    }
    .sme-value {
        color: #444;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

# Render the SME panel
st.markdown("""
    <div class="sme-panel">
        <div class="sme-header">Subject Matter Expert Panel</div>
        <div class="sme-field"><span class="sme-label">Name:</span>
             <span class="sme-value">TR Mr. Karthik</span></div>
        <div class="sme-field"><span class="sme-label">Expertise:</span>
             <span class="sme-value">Education Content Development</span></div>
        <div class="sme-field"><span class="sme-label">Email:</span>
             <span class="sme-value">karthik@example.com</span></div>
    </div>
""", unsafe_allow_html=True)

# Add more Streamlit widgets below (editable fields etc)
st.text_input("Add SME Glossary or Note")
