import streamlit as st

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
.outer-panel-border-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100vw;
    height: 100vh;
    box-sizing: border-box;
}
.outer-panel-border {
    width: 90vw;
    height: 85vh;
    border: 4px solid #2a3a88;
    border-radius: 18px;
    background: #fff;
    box-sizing: border-box;
}
</style>
<div class="outer-panel-border-wrapper">
  <div class="outer-panel-border"></div>
</div>
""", unsafe_allow_html=True)
