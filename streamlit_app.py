import streamlit as st

# Partition percentages, must total 100
part_percentages = [3, 4, 8, 45, 20, 20]
row_heights = ' '.join([f'{p}fr' for p in part_percentages])

st.markdown(
    f"""
    <div style="
        width: 95vw;                /* Full browser width */
        height: 80vh;               /* Full browser height */
        border: 4px solid navy;
        border-radius: 24px;
        background: white;
        display: grid;
        grid-template-rows: {row_heights};
        margin: auto;
        box-sizing: border-box;
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
