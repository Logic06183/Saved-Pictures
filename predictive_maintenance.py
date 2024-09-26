# Re-import necessary libraries due to the code execution environment reset
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 200)

# Creating initial empty lines for sensor data (temperature, pressure, vibration, humidity, and sound)
temp_line, = ax.plot([], [], label='Temperature', color='r')
pressure_line, = ax.plot([], [], label='Pressure', color='b')
vibration_line, = ax.plot([], [], label='Vibration', color='g')
humidity_line, = ax.plot([], [], label='Humidity', color='orange')
sound_line, = ax.plot([], [], label='Sound', color='purple')

# Adding maintenance threshold lines (upper and lower bounds)
upper_threshold = ax.axhline(y=170, color='black', linestyle='--', label='Upper Maintenance Threshold')
lower_threshold = ax.axhline(y=30, color='black', linestyle='--', label='Lower Maintenance Threshold')

# Initializing variables for data storage
x_data = []
temp_data = []
pressure_data = []
vibration_data = []
humidity_data = []
sound_data = []

# Function to initialize the plot
def init():
    temp_line.set_data([], [])
    pressure_line.set_data([], [])
    vibration_line.set_data([], [])
    humidity_line.set_data([], [])
    sound_line.set_data([], [])
    return temp_line, pressure_line, vibration_line, humidity_line, sound_line, upper_threshold, lower_threshold

# Function to update the plot
def update(frame):
    # Simulate time axis
    x_data.append(frame)
    
    # Generate simulated sensor data using sine and cosine functions
    temp_data.append(50 + 20 * np.sin(frame * 0.1))  # Simulated temperature sensor data
    pressure_data.append(80 + 30 * np.cos(frame * 0.1))  # Simulated pressure sensor data
    vibration_data.append(60 + 15 * np.sin(frame * 0.15))  # Simulated vibration sensor data
    humidity_data.append(70 + 25 * np.cos(frame * 0.05))  # Simulated humidity sensor data
    sound_data.append(90 + 10 * np.sin(frame * 0.2))  # Simulated sound sensor data

    # Update line data
    temp_line.set_data(x_data, temp_data)
    pressure_line.set_data(x_data, pressure_data)
    vibration_line.set_data(x_data, vibration_data)
    humidity_line.set_data(x_data, humidity_data)
    sound_line.set_data(x_data, sound_data)
    
    return temp_line, pressure_line, vibration_line, humidity_line, sound_line

# Create the animation
animation = FuncAnimation(fig, update, frames=np.arange(0, 100, 1), init_func=init, blit=True, interval=100)

# Adding labels, title, and legend
plt.title('Predictive Maintenance Sensor Data Simulation with Maintenance Thresholds')
plt.xlabel('Time')
plt.ylabel('Sensor Readings')
plt.legend()

# Save the animation as a gif
gif_writer = PillowWriter(fps=10)  # Set fps (frames per second) for the gif
animation.save('/predictive_maintenance.gif', writer=gif_writer)

# Display the animation
plt.show()
