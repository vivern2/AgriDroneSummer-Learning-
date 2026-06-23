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
from drone_logger import log_flight, save_log
import random
import os
if __name__ == "__main__":
    full_log = []
    #below creates 5 glights with random distances, id numbers and battery level
    for x in range(5):
        log = log_flight(random.randint(0,20), random.randint(1,200), random.randint(20,100))
        full_log.append(log)
    #Below will make the folder flight logs if it does not exist
    os.makedirs("flight_logs", exist_ok=True)
    #below will do th save_log function
    save_log("flight_logs/drone_log.txt", full_log)