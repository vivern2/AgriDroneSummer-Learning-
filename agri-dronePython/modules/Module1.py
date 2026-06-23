# 🌱 Beginner
# 1. Flight Timer
# Using the datetime module, write a function that:
# Records the current time as a flight start time
# Prints a formatted start time like "Flight started at 2026-06-23 14:32"
from datetime import datetime
def flight_timer():
    now = datetime.now()
    print(f"Flight started at {now.strftime('%Y-%m-%d %H:%M')}")
flight_timer()


# 2. Field Math
# Using the math module, write a function field_stats(length, width) that:
# Calculates the field area (length × width)
# Calculates the diagonal distance across the field using math.sqrt
# Prints both results rounded to 2 decimal places
import math 
def field_stats(length, width):
    field_area = length * width
    diagonal_dist = math.sqrt(length**2 + width**2)
    print(f"Field area: {field_area:.2f} diagonal distance: {diagonal_dist:.2f}")
field_stats(30, 50)


# 🌿 Intermediate
# 3. Your Own Module
# Split your existing code into two files:
# sensor.py — contains your Sensor and Field classes from OOP challenge 6
# main.py — imports from sensor.py, creates a Field, adds 3 sensors, and prints the average moisture

# 4. Random Field Generator
# Using random and os:
# Generate a 4×4 grid of random moisture readings (1–100)
# Create a folder called field_logs using os.makedirs() if it doesn't already exist
# Write the grid to a file called field_logs/moisture_grid.txt


# 🌾 Advanced
# 5. Drone Logger Module

# Create a module called drone_logger.py that contains:

# A log_flight(drone_id, distance, battery) function that returns a formatted log string including the current timestamp using datetime
# A save_log(filename, logs) function that writes a list of log strings to a txt file

# Then in main.py:

# Import both functions from drone_logger
# Simulate 5 flights with random distances
# Save the log to flight_logs/drone_log.txt
# Use if __name__ == "__main__" correctly