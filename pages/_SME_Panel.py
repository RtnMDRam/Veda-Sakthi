import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import datetime
import pandas as pd

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .block-container { padding-top: 0 !important; margin-top: 0 !important; }
    header, footer { display: none !important; }
    .main { margin-top: 0 !important; }
    .editable-vh45 {
        height: 45vh !important;
        min-height: 45vh !important;
        max-height: 45vh !important;
        overflow-y: auto; overflow-x: hidden;
        margin-top: 0 !important; margin-bottom: 0 !important;
        padding-top: 0 !important; padding-bottom: 0 !important;
        box-sizing: border-box; background: none;
    }
    .tight-label { font-size: 0.85em !important; font-weight: 500 !important; line-height: 1.08;
        margin-bottom: -0.34em !important; margin-top: -0.51em !important;
        padding-bottom:0 !important; padding-top:0 !important;}
    .stTextArea { margin-top: -0.44em !important; margin-bottom: -0.55em !important;}
    textarea[data-baseweb="textarea"] { min-height: 44px !important; font-size: 0.98em !important; }
    .stTextArea label { display:none !important; }
    .cw-40-fixed { height: 40vh !important; min-height: 40vh !important; max-height: 40vh !important;
        display: flex; flex-direction: column; justify-content: flex-start;
        font-size: 1.035em !important; line-height: 1.14 !important;
        margin: 0 !important; padding: 0 0.09em 0.28em 0.09em !important;
        overflow-y: auto; overflow-x: hidden; box-sizing: border-box; background: none;}
    .cw-40-fixed strong { font-weight: 600 !important; }
    </style>
""", unsafe_allow_html=True)

# --- AUTHENTICATION LOGIC ---
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    st.success(f'Welcome {name}')
    
    # --- Toolbar/Panel Info ---
    def get_tamil_date():
        now = datetime.datetime.now()
        gregorian = now.strftime("%Y %b %d")
        tamil = "புரட்டாசி 29"  # Example; build real Tamil date logic as needed
        return f"{tamil} / {gregorian}"

    def get_time():
        return datetime.datetime.now().strftime("%H:%M")

    col1, col2, col3 = st.columns([1.3, 2.7, 1])
    with col1:
        st.write("**Date**")
        st.write(get_tamil_date())
    with col2:
        st.write("**Subject Matter Expert (SME) Panel for <Tr/Ta Name>**")
    with col3:
        st.write("**Time**")
        st.write(get_time())
    st.markdown("---", unsafe_allow_html=True)

    col_link1, col_link_mid, col_link2 = st.columns([2.2, 1, 2.2])
    with col_link1:
        file_link = st.text_input("Paste the CSV/XLSX Link Given by Admin", "")
    with col_link_mid:
        load_file = st.button("Load", key="load_file")
    with col_link2:
        gloss_link = st.text_input("Glossary Upload Link from Drive", "")
        load_gloss = st.button("Load", key="load_glossary")
    st.markdown("---", unsafe_allow_html=True)

    # Row 3: Action Buttons & Row Info
    bt_col1, bt_col2, bt_col3, bt_col4, bt_col5, bt_col6 = st.columns([1.3, 1.6, 1.1, 1.1, 1.6, 1.3])
    with bt_col1:
        if st.button("Hi! Glossary"):
            st.session_state['show_glossary'] = True
    with bt_col2:
        st.button("Save & Cont..", key="save_continue")
    with bt_col3:
        st.write("Row # A")
    with bt_col4:
        st.write("_id Number")
    with bt_col5:
        st.write("Row # z")
    with bt_col6:
        if st.button("Save & Next"):
            st.session_state['save_and_next'] = True

    # Bottom Save Final Button
    b_col1, b_col2, b_col3 = st.columns([1.15, 2.6, 1.15])
    with b_col1:
        pass
    with b_col2:
        pass
    with b_col3:
        if st.button("Save File", key="save_file"):
            st.session_state['save_file'] = True

    # --- Editable & Non-Editable Panel ---
    uploaded_file = st.file_uploader("Upload a bilingual Excel file (.xlsx)", type="xlsx")
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.success("File uploaded successfully!")
        row = df.iloc[0]
        vilakkam_val = row.get('விளக்கம்', '') or row.get('விளக்கம் ', '')

        # Editable block
        st.markdown('<div class="editable-vh45">', unsafe_allow_html=True)
        st.markdown('<div class="tight-label">கேள்வி</div>', unsafe_allow_html=True)
        tamil_q = st.text_area("", value=row.get('கேள்வி', ''), height=52, key="edit_q", label_visibility='collapsed')
        st.markdown('<div class="tight-label">விருப்பங்கள்</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2, gap="small")
        with col1:
            optA = st.text_area("", value="", key="optA", height=40, label_visibility='collapsed')
        with col2:
            optB = st.text_area("", value="", key="optB", height=40, label_visibility='collapsed')
        col3, col4 = st.columns(2, gap="small")
        with col3:
            optC = st.text_area("", value="", key="optC", height=40, label_visibility='collapsed')
        with col4:
            optD = st.text_area("", value="", key="optD", height=40, label_visibility='collapsed')
        cols = st.columns(2, gap="small")
        with cols[0]:
            st.markdown('<div class="tight-label">Glossary</div>', unsafe_allow_html=True)
            gloss = st.text_area("", value="", key="gloss", height=40, label_visibility='collapsed')
        with cols[1]:
            st.markdown('<div class="tight-label">Answer</div>', unsafe_allow_html=True)
            ans = st.text_area("", value=row.get('பதில் ', ''), key="ans", height=40, label_visibility='collapsed')
        st.markdown('<div class="tight-label">விளக்கம்</div>', unsafe_allow_html=True)
        tamil_exp = st.text_area("", value=vilakkam_val, height=175, key="edit_exp", label_visibility='collapsed')
        st.markdown('</div>', unsafe_allow_html=True)

        # Reference/display block
        st.markdown(f"""
        <div class="cw-40-fixed" style="margin-top:0!important; padding-top:0!important;">
            <hr style="height:1.8px;border:none;background:#666;margin:0 0 0 0;padding:0;">
            <div style="margin-top:0;margin-bottom:0;"><b>தமிழ்</b></div>
            <div><strong>கேள்வி:</strong> {row.get('கேள்வி', '')}</div>
            <div><strong>விருப்பங்கள்:</strong> {row.get('விருப்பங்கள் ', '')}</div>
            <div><strong>பதில்:</strong> {row.get('பதில் ', '')}</div>
            <div><strong>விளக்கம்:</strong> {vilakkam_val}</div>
            <div style="height:0.13em"></div>
            <div><b>English</b></div>
            <div><strong>Question:</strong> {row.get('question ', '')}</div>
            <div><strong>Options:</strong> {row.get('questionOptions', '')}</div>
            <div><strong>Answer:</strong> {row.get('answers ', '')}</div>
            <div><strong>Explanation:</strong> {row.get('explanation', '')}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("Please upload your bilingual Excel file to begin.")

elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')
