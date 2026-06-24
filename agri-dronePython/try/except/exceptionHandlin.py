import csv

# 🌱 Beginner
# 1. Safe Battery Setter
# Write a function set_battery(level) that:
# Raises a ValueError if the level is below 0 or above 100
# Returns the level if valid
# Wrap the function call in a try/except that prints a friendly error message if an invalid level is passed
# Test it with both a valid and invalid battery level.
def set_battery(level):
     if (level < 0) or (level > 100):
        raise  ValueError("battery level is invalid") #triggers the error inside the function
     return level       #only runs if level is valid
try:
    set_battery(-7)
except ValueError as e:
    print(f"Error: {e}") #catches the error here
        



# 2. Safe File Reader
# Write a function read_sensor_data(filename) that:
# Tries to open and read a file
# Catches FileNotFoundError and prints a helpful message instead of crashing
# Uses finally to print "File operation complete" regardless of success or failure
# Test it with both a real file and a fake filename.

def read_sensor(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"{filename} was found")
    except FileNotFoundError:  #bare except catches all errors error and specific error catches that specific error
        print(f"Error: Hey the system can not find the file:{filename}")
    finally:
        print("File operation complete")
        
read_sensor("myname.txt")
read_sensor("agri-dronePython/cropData2/agriculture_dataset.txt")




# 🌿 Intermediate
# 3. CSV Data Cleaner
# Re-do your CSV challenge (India Agriculture) but this time instead of checking if row["Production"] == "",
#  use try/except to catch the ValueError when converting to float. 
# Print how many rows were skipped due to bad data at the end.

with open("agri-dronePython/cropData2/India_Agriculture.csv", "r") as file:
    reader = csv.DictReader(file)
    #below is how we would see the file
    rows_skipped = 0
    for row in reader:
        try:
            if (row["Season"] == "Kharif") and (float(row["Production"]) > 5000):
                print(row)
        except ValueError:
            rows_skipped += 1
            continue
    print(f"{rows_skipped} rows were skipped")
             


# 4. Drone Command Validator
# Write a Drone class with a fly(distance) method that:
# Raises a ValueError if distance is negative
# Raises a TypeError if distance isn't a number
# Reduces battery by distance * 2 if valid
# Wrap all calls to fly() in try/except catching both error types with different messages


# 🌾 Advanced
# 5. Field Data Pipeline

# Write a function process_field_data(filename) that:

# Reads your agriculture_dataset.txt
# For each row, tries to convert Yield and Farm_Area to floats
# Catches any ValueError on bad rows and logs them to a separate errors.txt file
# At the end prints a summary: how many rows processed successfully, how many failed