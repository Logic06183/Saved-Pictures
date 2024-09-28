import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.patches as mpatches
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 12))

# Define circles with positions and sizes to represent overlaps
circles_info = [
    {'center': (0, 0), 'radius': 5, 'color': 'lightgray', 'alpha': 0.5,
     'label': 'AI', 'x_text': 0, 'y_text': 0, 'fontsize': 20,
     'legend_patch': mpatches.Patch(color='lightgray', alpha=0.5, label='Artificial Intelligence (AI)')},
    {'center': (-1, 1), 'radius': 3.5, 'color': 'lightgreen', 'alpha': 0.5,
     'label': 'ML', 'x_text': -1, 'y_text': 1, 'fontsize': 16,
     'legend_patch': mpatches.Patch(color='lightgreen', alpha=0.5, label='Machine Learning (ML)')},
    {'center': (-1.5, 1.5), 'radius': 2, 'color': 'lightcoral', 'alpha': 0.5,
     'label': 'DL', 'x_text': -1.5, 'y_text': 1.5, 'fontsize': 14,
     'legend_patch': mpatches.Patch(color='lightcoral', alpha=0.5, label='Deep Learning (DL)')},
    {'center': (1, 1.5), 'radius': 2.5, 'color': 'skyblue', 'alpha': 0.5,
     'label': 'NLP', 'x_text': 1, 'y_text': 1.5, 'fontsize': 14,
     'legend_patch': mpatches.Patch(color='skyblue', alpha=0.5, label='Natural Language Processing (NLP)')},
    {'center': (-1, -1.5), 'radius': 2.5, 'color': 'orange', 'alpha': 0.5,
     'label': 'CV', 'x_text': -1, 'y_text': -1.5, 'fontsize': 14,
     'legend_patch': mpatches.Patch(color='orange', alpha=0.5, label='Computer Vision (CV)')},
    {'center': (2, -1), 'radius': 2.5, 'color': 'purple', 'alpha': 0.5,
     'label': 'Robotics', 'x_text': 2, 'y_text': -1, 'fontsize': 14,
     'legend_patch': mpatches.Patch(color='purple', alpha=0.5, label='Robotics')},
    {'center': (0, -3), 'radius': 1.5, 'color': 'yellow', 'alpha': 0.5,
     'label': 'ES', 'x_text': 0, 'y_text': -3, 'fontsize': 14,
     'legend_patch': mpatches.Patch(color='yellow', alpha=0.5, label='Expert Systems (ES)')},
]

# Initialize the animation parameters
frames_per_circle = 20  # Increased number of frames to slow down the animation
total_frames = len(circles_info) * frames_per_circle

# Function to initialize the animation
def init():
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.axis('off')
    plt.title('AI Ecosystem Venn Diagram', fontsize=22)
    
    # Initialize circle patches and text
    for info in circles_info:
        circle = Circle(info['center'], 0, color=info['color'], alpha=info['alpha'])
        info['patch'] = circle  # Store the circle patch
        ax.add_patch(circle)
        text = ax.text(info['x_text'], info['y_text'], '', fontsize=info['fontsize'],
                       ha='center', va='center')
        info['text'] = text  # Store the text artist
    return []

# Animation function
def animate(i):
    circle_index = i // frames_per_circle
    progress_fraction = (i % frames_per_circle) / frames_per_circle
    progress = progress_fraction  # Linear easing; you can apply easing functions here if desired

    for idx, info in enumerate(circles_info):
        circle = info['patch']
        text = info['text']
        if idx < circle_index:
            # Previous circles, set to full size
            circle.set_radius(info['radius'])
            text.set_text(info['label'])
        elif idx == circle_index:
            # Current circle, animate radius
            circle.set_radius(info['radius'] * progress)
            if progress > 0.5:
                text.set_text(info['label'])
            else:
                text.set_text('')
        else:
            # Future circles, radius zero
            circle.set_radius(0)
            text.set_text('')

    # Update the legend with visible circles
    visible_patches = [info['legend_patch'] for idx, info in enumerate(circles_info) if idx <= circle_index]
    ax.legend(handles=visible_patches, loc='upper right', bbox_to_anchor=(1.2, 1))

    return [info['patch'] for info in circles_info] + [info['text'] for info in circles_info]

# Create the animation
ani = FuncAnimation(fig, animate, init_func=init, frames=total_frames,
                    interval=200, blit=True, repeat=False)

# Save the animation as an MP4 video file with reduced fps to slow down playback
ani.save('ai_ecosystem_animation_with_legend.mp4', writer='ffmpeg', fps=10)

# Display the animation
plt.show()
