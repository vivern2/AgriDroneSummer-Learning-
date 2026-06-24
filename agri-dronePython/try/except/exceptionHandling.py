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
class Drone: 
    def __init__(self, id, battery = 100):
        self.id = id
        self.battery = battery
    def fly(self, distance):
        try:
            self.distance = distance
            #below cheks for the errrors first
            if not isinstance(distance, (int, float)):
                raise TypeError("distance must be a number")
            if distance < 0: 
                raise ValueError("distance cannot be negative")
            
            #Below is the actual code that needs to work
            self.battery -= (distance * 2)
            print(f"battery is now :{self.battery}%")
        
        except ValueError as e:
            print(f"Error: {e}")
        except TypeError as t:
            print(f"Error: {t}")

            
drone1 = Drone(331, 70)
drone2 = Drone(221, 80)
drone3 = Drone(113, 90)
drone1.fly("Hello")
drone2.fly(10)
drone3.fly(-3)


# 🌾 Advanced
# 5. Field Data Pipeline

# Write a function process_field_data(filename) that:
# Reads your agriculture_dataset.txt
# For each row, tries to convert Yield and Farm_Area to floats
# Catches any ValueError on bad rows and logs them to a separate errors.txt file
# At the end prints a summary: how many rows processed successfully, how many failed


with open ("agri-dronePython/cropData2/agriculture_dataset.txt", "r") as file:
    content = file.read()
    #below will split it at the \n character
    rows = content.split("\n")
    #Below skips the header row as that data is not needed
    rows = rows[1:]
    goodRows = 0
    badRows = 0
    for row in rows:
        try:
            columns = row.split("\t") #will split on \t
            yieldNum = float(columns[6]) #converts the string in the array to a num we can use
            FarmArea = float(columns[2])
            goodRows += 1
        except ValueError:
            badRows += 1
    print(f"good rows: {goodRows}, bad rows: {badRows}")