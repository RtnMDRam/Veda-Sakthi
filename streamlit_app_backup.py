import streamlit as st

st.markdown("""
<style>
.main .block-container {
    padding: 0 !important;
    margin: 0 !important;
}
html, body { height: 100vh; width: 100vw; margin: 0; padding: 0; overflow: hidden;}
</style>
""", unsafe_allow_html=True)

PANEL_WIDTH = 700
PANEL_HEIGHT = 960  # match device, eg. 100vh or slightly less

def y(percent):
    return 10 + (PANEL_HEIGHT-20) * percent / 100

SVG_CODE = f'''
<svg width="700" height="{PANEL_HEIGHT}" viewBox="0 0 700 {PANEL_HEIGHT}" style="display:block;margin:0 auto; background:#fff;">
  <rect x="10" y="10" width="680" height="{PANEL_HEIGHT-20}" rx="20" fill="none" stroke="blue" stroke-width="4"/>
  <line x1="20" y1="{y(8)}" x2="680" y2="{y(8)}" stroke="red" stroke-width="2"/>
  <line x1="20" y1="{y(12)}" x2="680" y2="{y(12)}" stroke="red" stroke-width="2"/>
  <line x1="20" y1="{y(15)}" x2="680" y2="{y(15)}" stroke="red" stroke-width="2"/>
  <line x1="20" y1="{y(60)}" x2="680" y2="{y(60)}" stroke="red" stroke-width="2"/>
  <line x1="20" y1="{y(80)}" x2="680" y2="{y(80)}" stroke="red" stroke-width="2"/>
</svg>
'''

st.components.v1.html(SVG_CODE, height=PANEL_HEIGHT, width=PANEL_WIDTH)

