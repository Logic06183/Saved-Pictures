import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.patches as mpatches
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 12))

# Define circles with positions and sizes to represent overlaps
circles_info = [
    # (Circle object, label text, x position, y position, font size, legend patch)
    (Circle((0, 0), 5, color='lightgray', alpha=0.5), 'AI', 0, 0, 20,
     mpatches.Patch(color='lightgray', alpha=0.5, label='Artificial Intelligence (AI)')),
    (Circle((-1, 1), 3.5, color='lightgreen', alpha=0.5), 'ML', -1, 1, 16,
     mpatches.Patch(color='lightgreen', alpha=0.5, label='Machine Learning (ML)')),
    (Circle((-1.5, 1.5), 2, color='lightcoral', alpha=0.5), 'DL', -1.5, 1.5, 14,
     mpatches.Patch(color='lightcoral', alpha=0.5, label='Deep Learning (DL)')),
    (Circle((1, 1.5), 2.5, color='skyblue', alpha=0.5), 'NLP', 1, 1.5, 14,
     mpatches.Patch(color='skyblue', alpha=0.5, label='Natural Language Processing (NLP)')),
    (Circle((-1, -1.5), 2.5, color='orange', alpha=0.5), 'CV', -1, -1.5, 14,
     mpatches.Patch(color='orange', alpha=0.5, label='Computer Vision (CV)')),
    (Circle((2, -1), 2.5, color='purple', alpha=0.5), 'Robotics', 2, -1, 14,
     mpatches.Patch(color='purple', alpha=0.5, label='Robotics')),
    (Circle((0, -3), 1.5, color='yellow', alpha=0.5), 'ES', 0, -3, 14,
     mpatches.Patch(color='yellow', alpha=0.5, label='Expert Systems (ES)')),
]

# Initialize empty lists to store the drawn circles, texts, and legend patches
drawn_circles = []
drawn_texts = []
drawn_legend_patches = []

# Function to initialize the animation
def init():
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.axis('off')
    plt.title('AI Ecosystem Venn Diagram', fontsize=22)
    return []

# Animation function
def animate(i):
    if i < len(circles_info):
        circle, label, x_text, y_text, fontsize, legend_patch = circles_info[i]
        ax.add_patch(circle)
        text = ax.text(x_text, y_text, label, fontsize=fontsize, ha='center', va='center')
        drawn_circles.append(circle)
        drawn_texts.append(text)
        drawn_legend_patches.append(legend_patch)
        # Update the legend
        ax.legend(handles=drawn_legend_patches, loc='upper right', bbox_to_anchor=(1.2, 1))
    return drawn_circles + drawn_texts

# Create the animation
ani = FuncAnimation(fig, animate, init_func=init, frames=len(circles_info), interval=5000, blit=True, repeat=False)

# Save the animation as an MP4 video file (optional)
ani.save('ai_ecosystem_animation_with_legend.mp4', writer='ffmpeg', fps=1)

# Display the animation
plt.show()
