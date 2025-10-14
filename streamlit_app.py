import streamlit as st
import pandas as pd

# Custom CSS to minimize vertical space
st.markdown("""
    <style>
    /* Reduce spacing between markdown blocks */
    .block-container h2, .block-container h3 {
        margin-bottom: 0.25rem;
        margin-top: 0.5rem;
    }
    .block-container p {
        margin-bottom: 0.15rem;
        margin-top: 0.15rem;
    }
    .block-container ul, .block-container ol {
        margin-block-start: 0.2rem;
        margin-block-end: 0.2rem;
    }
    /* Remove space after containers */
    .block-container > div {
        margin-bottom: 0.3rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Bilingual Content Preview")

uploaded_file = st.file_uploader("Upload a bilingual Excel file (.xlsx)", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.success("File uploaded successfully!")

    # Show first row only (for now)
    row = df.iloc[0]

    # தமிழ் (top box, tight spacing)
    with st.container():
        st.header("[translate:தமிழ்]")
        st.markdown(f"**கேள்வி:** {row.get('கேள்வி', '')}")
        st.markdown(f"**விருப்பங்கள்:** {row.get('விருப்பங்கள் ', '')}")
        st.markdown(f"**பதில்:** {row.get('பதில் ', '')}")
        st.markdown(f"**விளக்கம்:** {row.get('விளக்கம் ', '')}")

    # English (bottom box, tight spacing)
    with st.container():
        st.header("English")
        st.markdown(f"**Question:** {row.get('question ', '')}")
        st.markdown(f"**Options:** {row.get('questionOptions', '')}")
        st.markdown(f"**Answer:** {row.get('answers ', '')}")
        st.markdown(f"**Explanation:** {row.get('explanation', '')}")

else:
    st.info("Please upload your bilingual Excel file to begin.")
