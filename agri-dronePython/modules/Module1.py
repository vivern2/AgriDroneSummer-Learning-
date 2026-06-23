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





