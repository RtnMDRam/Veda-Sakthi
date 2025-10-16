from pathlib import Path

import pandas as pd
import streamlit as st

hide_streamlit_style = """
    <style>
        [data-testid="stSidebar"] {display: none !important;}
        [data-testid="stHeader"] {z-index: 1;}
        .main .block-container {padding-top: 2rem;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "whoami" not in st.session_state:
    st.session_state.whoami = ""

# Read SME display name from "SME Name" column in SME data file (CSV/XLSX)
DATA_DIR = Path(__file__).resolve().parent
SME_DATA_PATHS = [DATA_DIR / "SME_Data.csv", DATA_DIR / "SME_Data.xlsx"]


# Cache SME lookup to avoid re-reading the spreadsheet on every rerun.
@st.cache_data
def get_sme_name(username):
    data_path = next((path for path in SME_DATA_PATHS if path.exists()), None)
    if data_path is None:
        return username

    try:
        if data_path.suffix.lower() == ".csv":
            df = pd.read_csv(data_path)
        else:
            df = pd.read_excel(data_path)
    except ValueError as exc:
        st.warning(f"Unable to read SME data file '{data_path.name}': {exc}")
        return username
    except Exception as exc:
        st.warning(f"Unexpected error while reading '{data_path.name}': {exc}")
        return username

    row = df[df["username"] == username]
    if not row.empty:
        return row.iloc[0]["SME Name"]   # <-- Changed here!
    return username

if not st.session_state.logged_in:
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username and password == "Test123!":
            st.session_state.logged_in = True
            st.session_state.whoami = username
            st.rerun()
        else:
            st.error("Incorrect username or password.")
    st.stop()
else:
    sme_display_name = get_sme_name(st.session_state.whoami)
    st.markdown(
        f"<h3 style='text-align: center;'>Subject Matter Expert (SME) Panel for <u>{sme_display_name}</u></h3>",
        unsafe_allow_html=True,
    )
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

    b_col1, b_col2, b_col3 = st.columns([1.15, 2.6, 1.15])
    with b_col1:
        pass
    with b_col2:
        pass
    with b_col3:
        if st.button("Save File", key="save_file"):
            st.session_state['save_file'] = True

    # ... further SME panel logic ...
