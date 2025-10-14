import streamlit as st
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 11))
plt.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Draw the outer rectangle close to the edge
rect = plt.Rectangle((0.01, 0.01), 0.98, 0.98, fill=None, edgecolor='blue', linewidth=2)
ax.add_patch(rect)

# Red horizontal lines with visible top margin
y_positions = [0.96, 0.92, 0.88, 0.30, 0.16]  # Adjust as required for your layout needs
for y in y_positions:
    ax.plot([0.02, 0.98], [y, y], color='red', linewidth=1)

# Display in Streamlit - the panel will be frozen/static
st.pyplot(fig)
