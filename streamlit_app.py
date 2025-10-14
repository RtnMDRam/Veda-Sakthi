import streamlit as st

# Partition percentages (must sum to 100 for proportional grid)
part_percentages = [3, 4, 8, 45, 20, 20]
row_heights = ' '.join([f'{p}fr' for p in part_percentages])

st.markdown(
    f"""
    <div style="
        width: 90vw;                 /* 90% of the viewport width */
        height: 90vh;                /* 90% of the viewport height */
        border: 4px solid navy;
        border-radius: 20px;
        background: white;
        display: grid;
        grid-template-rows: {row_heights};
        margin: auto;
        box-sizing: border-box;
        overflow: hidden;
        position: relative;
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
