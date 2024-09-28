import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import networkx as nx

# Define the neural network structure
layers = [3, 4, 2]  # 3 inputs, 4 neurons in hidden layer, 2 outputs

# Create a directed graph to represent the neural network
G = nx.DiGraph()
positions = {}
node_labels = {}
node_colors = []

# Assign positions and labels to nodes
vertical_spacing = 1.5
horizontal_spacing = 3

for layer_idx, num_nodes in enumerate(layers):
    x = layer_idx * horizontal_spacing
    y_start = - (num_nodes - 1) * vertical_spacing / 2
    for node_idx in range(num_nodes):
        node_id = f"L{layer_idx}N{node_idx}"
        y = y_start + node_idx * vertical_spacing
        positions[node_id] = (x, y)
        node_labels[node_id] = ''
        node_colors.append('lightgray')
        G.add_node(node_id)

# Add edges between nodes of consecutive layers
for layer_idx in range(len(layers) - 1):
    for src_idx in range(layers[layer_idx]):
        src_node = f"L{layer_idx}N{src_idx}"
        for dst_idx in range(layers[layer_idx + 1]):
            dst_node = f"L{layer_idx +1}N{dst_idx}"
            G.add_edge(src_node, dst_node)

# Initialize figure
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')

# Function to initialize the animation
def init():
    nx.draw_networkx_nodes(G, positions, ax=ax, node_size=1000, node_color='lightgray')
    nx.draw_networkx_edges(G, positions, ax=ax, arrows=False, edge_color='gray')
    return []

# Simulate input data
input_data = np.array([0.9, -0.4, 0.1])

# Random weights and biases for demonstration
np.random.seed(42)
weights = [
    np.random.uniform(-1, 1, size=(layers[0], layers[1])),  # Weights between input and hidden layer
    np.random.uniform(-1, 1, size=(layers[1], layers[2]))   # Weights between hidden and output layer
]
biases = [
    np.random.uniform(-0.5, 0.5, size=(layers[1])),  # Biases for hidden layer
    np.random.uniform(-0.5, 0.5, size=(layers[2]))   # Biases for output layer
]

activations = []

# Perform forward propagation and store activations
def forward_propagation():
    activation = input_data
    activations.append(activation)
    for W, b in zip(weights, biases):
        z = np.dot(activation, W) + b
        activation = np.tanh(z)  # Activation function
        activations.append(activation)

forward_propagation()

# Animation function
def animate(i):
    ax.clear()
    ax.axis('off')

    # Draw edges
    nx.draw_networkx_edges(G, positions, ax=ax, arrows=False, edge_color='gray')

    # Update node colors and labels based on activation values
    current_layer = min(i, len(activations) - 1)
    node_colors = []
    for layer_idx, num_nodes in enumerate(layers):
        for node_idx in range(num_nodes):
            node_id = f"L{layer_idx}N{node_idx}"
            if layer_idx <= current_layer:
                # Get activation value
                value = activations[layer_idx][node_idx] if layer_idx > 0 else input_data[node_idx]
                # Map value to color
                color = plt.cm.RdYlGn((value + 1) / 2)
                label = f"{value:.2f}"
            else:
                color = 'lightgray'
                label = ''
            node_colors.append(color)
            node_labels[node_id] = label

    # Draw nodes
    nx.draw_networkx_nodes(G, positions, ax=ax, node_size=1000, node_color=node_colors)
    nx.draw_networkx_labels(G, positions, labels=node_labels, font_size=8)

    # Add layer labels
    for idx, layer in enumerate(['Input Layer', 'Hidden Layer', 'Output Layer']):
        x = idx * horizontal_spacing
        y = max(positions.values(), key=lambda t: t[1])[1] + vertical_spacing
        ax.text(x, y, layer, fontsize=12, ha='center')

    return []

# Create the animation
ani = FuncAnimation(fig, animate, init_func=init, frames=len(activations), interval=1000, blit=True, repeat=False)

# Display the animation
plt.show()
