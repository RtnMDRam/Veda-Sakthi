import matplotlib.pyplot as plt

# Canvas size parameters
width = 1.0
height = 1.0

# Partition size fractions (adjust or reuse as you wish, total = 1.0)
part_percentages = [0.03, 0.04, 0.08, 0.45, 0.20, 0.20]

# Get cumulative positions for partition lines (as Y coordinates)
y_positions = [sum(part_percentages[:i+1])*height for i in range(len(part_percentages))]

fig, ax = plt.subplots(figsize=(6,8))

# Draw border (navy)
ax.plot([0, width], [0, 0], color='navy', linewidth=2)             # bottom border
ax.plot([0, width], [height, height], color='navy', linewidth=2)   # top border
ax.plot([0, 0], [0, height], color='navy', linewidth=2)            # left border
ax.plot([width, width], [0, height], color='navy', linewidth=2)    # right border

# Draw partition lines (red)
for y in y_positions[:-1]:  # skip last line (bottom border already present)
    ax.plot([0, width], [y, y], color='red', linewidth=2)

ax.set_xlim(-0.05, 1.05)
ax.set_ylim(-0.05, 1.05)
ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout()
plt.show()
