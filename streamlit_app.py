import streamlit as st
import pandas as pd

st.title("Bilingual Content Preview")

uploaded_file = st.file_uploader("Upload a bilingual Excel file (.xlsx)", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.success("File uploaded successfully!")

    # Show first row only for now (you can expand to more rows as needed)
    row = df.iloc[0]

    # Tamil box (above)
    with st.container():
        st.subheader("Tamil")
        st.markdown(f"**கேள்வி:** {row.get('கேள்வி', '')}")
        st.markdown(f"**விருப்பங்கள்:** {row.get('விருப்பங்கள் ', '')}")
        st.markdown(f"**பதில்:** {row.get('பதில் ', '')}")
        st.markdown(f"**விளக்கம்:** {row.get('விளக்கம் ', '')}")
        st.markdown("---")

    # English box (bottom)
    with st.container():
        st.subheader("English")
        st.markdown(f"**Question:** {row.get('question ', '')}")
        st.markdown(f"**Options:** {row.get('questionOptions', '')}")
        st.markdown(f"**Answer:** {row.get('answers ', '')}")
        st.markdown(f"**Explanation:** {row.get('explanation', '')}")
        st.markdown("---")

else:
    st.info("Please upload your bilingual Excel file to begin.")
