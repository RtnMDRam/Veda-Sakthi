import streamlit as st

# Partition percentages - should sum to 100
part_percentages = [3, 4, 8, 45, 20, 20]
row_heights = ' '.join([f'{p}fr' for p in part_percentages])

st.markdown(
    f"""
    <div style="
        width: 600px;                 /* fixed width */
        height: 500px;                /* fixed height */
        border: 4px solid navy;
        border-radius: 20px;
        background: white;
        display: grid;
        grid-template-rows: {row_heights};
        margin: 40px auto 40px auto;  /* always centered */
        box-sizing: border-box;
        position: relative;           /* absolutely fixed on the page */
        overflow: hidden;             /* nothing spills out */
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
