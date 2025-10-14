import streamlit as st

# Partition percentages
part_percentages = [3, 4, 8, 45, 20, 20]
row_heights = ' '.join([f'{p}fr' for p in part_percentages])

st.markdown(
    f"""
    <div style="
        width: 90vw;
        height: 90vh;
        border: 4px solid navy;
        border-radius: 20px;
        background: white;
        display: grid;
        grid-template-rows: {row_heights};
        box-sizing: border-box;
        overflow: hidden;
        position: fixed;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
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
