import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the cost function (e.g., f(x) = x^2)
def cost_function(x):
    return x ** 2

# Define the gradient of the cost function
def gradient(x):
    return 2 * x

# Initialize parameters
x_start = 8  # Starting point
learning_rate = 0.1
num_iterations = 50

# Store the x values and cost function values
x_values = [x_start]
y_values = [cost_function(x_start)]

# Perform gradient descent
x = x_start
for i in range(num_iterations):
    grad = gradient(x)
    x = x - learning_rate * grad
    x_values.append(x)
    y_values.append(cost_function(x))

# Prepare the figure
fig, ax = plt.subplots(figsize=(8, 6))
x_plot = np.linspace(-10, 10, 400)
y_plot = cost_function(x_plot)
ax.plot(x_plot, y_plot, label='Cost Function')
point, = ax.plot([], [], 'ro', label='Current Position')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()

# Animation function
def animate(i):
    point.set_data([x_values[i]], [y_values[i]])  # Wrap the values in lists
    ax.set_title(f'Iteration {i}: x = {x_values[i]:.4f}, f(x) = {y_values[i]:.4f}')
    return point,

# Create the animation
ani = FuncAnimation(fig, animate, frames=num_iterations + 1, interval=200, blit=True, repeat=False)

# Display the animation
plt.show()
