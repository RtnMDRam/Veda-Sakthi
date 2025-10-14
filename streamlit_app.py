import streamlit as st

SVG_CODE = '''
<svg width="700" height="900" viewBox="0 0 700 900" style="background: #fff;">
  <!-- Outer blue rectangle -->
  <rect x="10" y="10" width="680" height="880" rx="20" fill="none" stroke="blue" stroke-width="4"/>

  <!-- Partition percentages, measured within inner height (880 px from y=10 to y=890) -->
  <!-- Top bands: 8%, 4%, 3% -->
  <line x1="20" y1="80" x2="680" y2="80" stroke="red" stroke-width="2"/>   <!-- 8% of 880 = 70px; y=10+70=80 -->
  <line x1="20" y1="115" x2="680" y2="115" stroke="red" stroke-width="2"/> <!-- (8+4)%=12% of 880=105px; y=10+105=115 -->
  <line x1="20" y1="142" x2="680" y2="142" stroke="red" stroke-width="2"/> <!-- (8+4+3)=15% of 880=132px; y=10+132=142 -->

  <!-- Middle partition: 45% below top bands (from y=142 to y=538) -->
  <line x1="20" y1="538" x2="680" y2="538" stroke="red" stroke-width="2"/> <!-- 15%+45%=60% of 880=528px; y=10+528=538 -->

  <!-- Bottom partitions: 20% each -->
  <line x1="20" y1="714" x2="680" y2="714" stroke="red" stroke-width="2"/> <!-- 60%+20%=80% of 880=704px; y=10+704=714 -->
  <line x1="20" y1="890" x2="680" y2="890" stroke="red" stroke-width="2"/> <!-- last line at bottom border (100%) -->
</svg>
'''

st.markdown("## Frozen Panel Layout")
st.components.v1.html(SVG_CODE, height=900)
