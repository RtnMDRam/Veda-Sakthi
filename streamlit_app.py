import streamlit as st

st.set_page_config(
    layout="centered",  # or "wide" to expand if you need full width
    page_title="Frozen Panel",
    initial_sidebar_state="collapsed"
)

# Custom CSS to remove body margin/padding
st.markdown("""
    <style>
    body { margin: 0; padding: 0; }
    .main .block-container { padding-top: 0rem; padding-bottom: 0rem; }
    </style>
""", unsafe_allow_html=True)

PANEL_HEIGHT = 950
PANEL_WIDTH = 700
INNER_TOP = 10
def y(percent):
    return INNER_TOP + (PANEL_HEIGHT-2*INNER_TOP) * percent / 100

SVG_CODE = f'''
<svg width="{PANEL_WIDTH}" height="{PANEL_HEIGHT}" viewBox="0 0 {PANEL_WIDTH} {PANEL_HEIGHT}" style="background: #fff; display: block; margin: 0 auto;">
  <rect x="10" y="10" width="{PANEL_WIDTH-20}" height="{PANEL_HEIGHT-20}" rx="20" fill="none" stroke="blue" stroke-width="4"/>
  <line x1="20" y1="{y(4)}" x2="{PANEL_WIDTH-20}" y2="{y(4)}" stroke="red" stroke-width="2"/>
  <line x1="20" y1="{y(8)}" x2="{PANEL_WIDTH-20}" y2="{y(8)}" stroke="red" stroke-width="2"/>
  <line x1="20" y1="{y(15)}" x2="{PANEL_WIDTH-20}" y2="{y(15)}" stroke="red" stroke-width="2"/>
  <line x1="20" y1="{y(60)}" x2="{PANEL_WIDTH-20}" y2="{y(60)}" stroke="red" stroke-width="2"/>
  <line x1="20" y1="{y(80)}" x2="{PANEL_WIDTH-20}" y2="{y(80)}" stroke="red" stroke-width="2"/>
</svg>
'''

# Only show the SVG panel, nothing else
st.components.v1.html(SVG_CODE, height=PANEL_HEIGHT, width=PANEL_WIDTH)
