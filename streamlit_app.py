import matplotlib.pyplot as plt

# Dimensions
width = 1.0
height = 1.0

# Fixed outer border (do not change)
fig, ax = plt.subplots(figsize=(6,8))
ax.plot([0, width], [0, 0], color='navy')       # bottom border
ax.plot([0, width], [height, height], color='navy') # top border
ax.plot([0, 0], [0, height], color='navy')      # left border
ax.plot([width, width], [0, height], color='navy')  # right border

# Partition percentages (must sum to 1 or 100%)
part_percentages = [0.03, 0.04, 0.08, 0.45, 0.20, 0.20]

# Draw partition lines at cumulative positions
y_positions = [sum(part_percentages[:i+1]) * height for i in range(len(part_percentages))]

for y in y_positions[:-1]:  # skip last; it's the bottom border
    ax.plot([0, width], [y, y], color='red')

ax.set_xlim(-0.05, 1.05)
ax.set_ylim(-0.05, 1.05)
ax.set_xticks([])
ax.set_yticks([])
plt.show()
