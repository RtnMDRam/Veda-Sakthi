import streamlit as st
import datetime

# Debug: Print entire session state
st.write("DEBUG SESSION STATE:", st.session_state)

# ---- SIMPLE AUTH STUB ----
USERNAME = "admin1"
PASSWORD = "Test123!"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("Login")

    # Text inputs for username/password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Debug: Print inputs as typed
    st.write(f"Username entered: '{username}'")
    st.write(f"Password entered: '{password}'")

    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.rerun()   # UPDATED to latest Streamlit standard
        else:
            st.error("Incorrect username or password.")
    st.stop()
else:
    st.success(f'Welcome {USERNAME}')  # Customizable

    # --- UTILITY FUNCTIONS FOR PANEL ELEMENTS ---
    def get_tamil_date():
        now = datetime.datetime.now()
        gregorian = now.strftime("%Y %b %d")
        tamil = "புரட்டாசி 29"  # Example placeholder, replace with your logic
        return f"{tamil} / {gregorian}"

    def get_time():
        return datetime.datetime.now().strftime("%H:%M")

    # --- PANEL START ---

    # Top Toolbar: Date | Panel Name & SME/Teacher | Time
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

    # Row 2: File and Glossary Links
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

    # --- Your SME panel UI and content below ---
