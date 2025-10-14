import streamlit as st
import pandas as pd

# Read the file (assuming it's loaded as 'bl_bio_bot_unit_4_chap_9_the_tissues_qb.xlsx')
df = pd.read_excel('bl_bio_bot_unit_4_chap_9_the_tissues_qb.xlsx', sheet_name="Cleaned_Bilingual")

# Pick the first row to display
row = df.iloc[0]

# Layout: ENGLISH version (bottom box)
with st.container():
    st.markdown("### English Version (Bottom Box)")
    st.markdown(f"**Question:** {row['question ']}") 
    st.markdown(f"**Options:** {row['questionOptions']}")
    st.markdown(f"**Answer:** {row['answers ']}")
    st.markdown(f"**Explanation:** {row['explanation']}")
    st.markdown("---")

# Layout: TAMIL version (box above English)
with st.container():
    st.markdown("### Tamil Version (Above Box)")
    st.markdown(f"**[translate:கேள்வி]:** [translate:{row['கேள்வி']}]")
    st.markdown(f"**[translate:விருப்பங்கள்]:** [translate:{row['விருப்பங்கள் ']}]")
    st.markdown(f"**[translate:பதில்]:** [translate:{row['பதில் ']}]")
    st.markdown(f"**[translate:விளக்கம்]:** [translate:{row['விளக்கம் ']}]")
    st.markdown("---")

