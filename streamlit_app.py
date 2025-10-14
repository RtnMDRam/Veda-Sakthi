import streamlit as st

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
.outer-panel-border {
    position: fixed;
    top: 6vh;
    left: 1vw;
    width: 98vw;
    height: 91vh;
    border: 4px solid #2a3a88;
    border-radius: 18px;
    background: #fff;
    box-sizing: border-box;
    z-index: 99;
}
</style>
<div class="outer-panel-border"></div>
""", unsafe_allow_html=True)
