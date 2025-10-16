import streamlit as st
import datetime

USERNAME = "admin1"
PASSWORD = "Test123!"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Optional debug: see exactly what you typed
    st.write(f"Username entered: '{username}'")
    st.write(f"Password entered: '{password}'")

    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Incorrect username or password.")
    st.stop()
else:
    st.success(f'Welcome {USERNAME}')  # Show main SME panel

    def get_tamil_date():
        now = datetime.datetime.now()
        gregorian = now.strftime("%Y %b %d")
        tamil = "புரட்டாசி 29"  # Placeholder, set your logic
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

    # Add the rest of your SME panel UI/content here
