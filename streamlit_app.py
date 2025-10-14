import streamlit as st

SVG_CODE = '''
<svg width="700" height="900" viewBox="0 0 700 900" style="background: #fff;">
  <!-- Outer blue rectangle -->
  <rect x="10" y="10" width="680" height="880" rx="20" fill="none" stroke="blue" stroke-width="4"/>

  <!-- Inner red horizontal lines, all inside the blue rectangle -->
  <line x1="20" y1="50" x2="680" y2="50" stroke="red" stroke-width="2"/>
  <line x1="20" y1="90" x2="680" y2="90" stroke="red" stroke-width="2"/>
  <line x1="20" y1="130" x2="680" y2="130" stroke="red" stroke-width="2"/>
  <line x1="20" y1="500" x2="680" y2="500" stroke="red" stroke-width="2"/>
  <line x1="20" y1="820" x2="680" y2="820" stroke="red" stroke-width="2"/>
</svg>
'''

st.write("## Frozen Panel Output")
st.components.v1.html(SVG_CODE, height=900)
