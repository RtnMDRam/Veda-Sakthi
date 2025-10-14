import streamlit as st

PANEL_HEIGHT = 900
PANEL_WIDTH = 700
INNER_TOP = 10          # Margin from outer border
INNER_BOTTOM = PANEL_HEIGHT - 10

def y(percent):
    # Maps percentage (0-100) to SVG y-position within inner borders (10px to 890px)
    return INNER_TOP + (PANEL_HEIGHT-20) * percent / 100

SVG_CODE = f'''
<svg width="{PANEL_WIDTH}" height="{PANEL_HEIGHT}" viewBox="0 0 {PANEL_WIDTH} {PANEL_HEIGHT}" style="background: #fff;">
  <!-- Outer blue rectangle -->
  <rect x="10" y="10" width="{PANEL_WIDTH-20}" height="{PANEL_HEIGHT-20}" rx="20" fill="none" stroke="blue" stroke-width="4"/>
  
  <!-- Partition lines based on user percentages -->
  <line x1="20" y1="{y(8)}" x2="{PANEL_WIDTH-20}" y2="{y(8)}" stroke="red" stroke-width="2"/>
  <line x1="20" y1="{y(12)}" x2="{PANEL_WIDTH-20}" y2="{y(12)}" stroke="red" stroke-width="2"/>
  <line x1="20" y1="{y(15)}" x2="{PANEL_WIDTH-20}" y2="{y(15)}" stroke="red" stroke-width="2"/>
  <line x1="20" y1="{y(60)}" x2="{PANEL_WIDTH-20}" y2="{y(60)}" stroke="red" stroke-width="2"/>
  <line x1="20" y1="{y(80)}" x2="{PANEL_WIDTH-20}" y2="{y(80)}" stroke="red" stroke-width="2"/>
</svg>
'''

st.components.v1.html(SVG_CODE, height=PANEL_HEIGHT, width=PANEL_WIDTH)
