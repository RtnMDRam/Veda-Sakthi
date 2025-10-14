import streamlit as st

# Define partition percentages
part_percentages = [3, 4, 8, 45, 20, 20]  # these are percent values; must sum to 100

# Convert to string for CSS grid-rows
row_heights = ' '.join([f'{p}fr' for p in part_percentages])

st.markdown(
    f"""
    <div style="
        width: 100%;
        height: 600px;
        border: 4px solid navy;
        border-radius: 20px;
        display: grid;
        grid-template-rows: {row_heights};
        margin-bottom: 2rem;
        background: white;
    ">
        <div style="border-bottom: 2px solid red;"></div>
        <div style="border-bottom: 2px solid red;"></div>
        <div style="border-bottom: 2px solid red;"></div>
        <div style="border-bottom: 2px solid red;"></div>
        <div style="border-bottom: 2px solid red;"></div>
        <div></div>
    </div>
    """,
    unsafe_allow_html=True
)
