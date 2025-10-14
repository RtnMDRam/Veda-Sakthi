import streamlit as st

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
.outer-panel-border {
    position: fixed;
    top: 3vh;
    left: 2vw;
    width: 96vw;
    height: 96vh;
    border: 3px solid #2a3a88;
    border-radius: 18px;
    background: #fff;
    box-sizing: border-box;
    z-index: 99;
}
</style>
<div class="outer-panel-border"></div>
""", unsafe_allow_html=True)
