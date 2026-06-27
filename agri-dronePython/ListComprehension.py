# 🌱 Beginner
# 1. Yield Extractor
# Given this list of farm dictionaries, use a list comprehension to extract just the yield values into a new list, then print it:
pythonfarms = [
    {"id": "F001", "crop": "Cotton", "yield": 14.44},
    {"id": "F002", "crop": "Carrot", "yield": 42.91},
    {"id": "F003", "crop": "Sugarcane", "yield": 33.44},
    {"id": "F004", "crop": "Tomato", "yield": 34.08},
    {"id": "F005", "crop": "Tomato", "yield": 43.28},
]

yields  = [f["yield"] for f in pythonfarms]
print(yields)


# 2. High Yield Filter
# Using the same farms list, use a list comprehension to get the id of every farm with a yield above 35. Print the result.
bigYeilds = [b["id"] for b in pythonfarms if b["yield"] > 35]
print(bigYeilds)

# 🌿 Intermediate
# 3. Moisture Converter
# You have raw moisture readings as strings. Use a list comprehension to convert them all to floats in one line:
pythonraw_readings = ["72.5", "45.1", "88.3", "60.0", "23.7", "91.2"]
fReadings = [float(n) for n in pythonraw_readings]
print(fReadings)


# 4. Drone Status List
# Given this fleet list, use a list comprehension to 
# build a new list of formatted strings for drones that need charging (battery below 30):
# Output should look like:
# ['DR02 needs charging (12%)', 'DR04 needs charging (8%)']
pythonfleet = [
    {"id": "DR01", "battery": 85},
    {"id": "DR02", "battery": 12},
    {"id": "DR03", "battery": 67},
    {"id": "DR04", "battery": 8},
    {"id": "DR05", "battery": 91},
]

fleetMessage = [(f'{n["id"]} needs charging ({n["battery"]}%)')  for n in pythonfleet if n["battery"] < 30]
print(fleetMessage)



# 🌾 Advanced
# 5. Real Data Filter
# Read your agriculture_dataset.txt and use a list comprehension to build a list of tuples (Farm_ID, Yield)
#  for every farm where the yield is above 40. Print the result.
with open ("agri-dronePython/cropData2/agriculture_dataset.txt", "r") as file:
    content = file.read()
    #below will split it at the \n character
    rows = content.split("\n")
    #Below skips the header row as that data is not needed
    rows = rows[1:]

    aggTuples = [
    (row.split("\t")[0], float(row.split("\t")[6]))  # tuple of (Farm_ID, Yield)
    for row in rows                                    # for each row
    if row != "" and float(row.split("\t")[6]) > 40  # filter condition
]
    print(aggTuples)
        
        