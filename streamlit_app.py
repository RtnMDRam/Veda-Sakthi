import streamlit as st

# Partition percentages (should sum to 100)
part_percentages = [3, 4, 8, 45, 20, 20]
row_heights = ' '.join([f'{v}fr' for v in part_percentages])

st.markdown(
    f"""
    <div style="
        width: 600px;                /* Fixed minimal width */
        height: 500px;               /* Fixed minimal height */
        border: 4px solid navy;
        border-radius: 20px;
        background: white;
        display: grid;
        grid-template-rows: {row_heights};
        margin: 40px auto;
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
