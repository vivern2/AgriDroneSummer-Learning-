import random

# 🌱 Beginner
# 1. Crop Inventory
# You have a list of crops being monitored by a drone:
# pythoncrops = ["wheat", "corn", "soybean", "rice", "barley"]

# Print each crop with its index number
# Add "millet" to the end
# Remove "corn" from the list
# Print the final list
pythoncrops = ["wheat", "corn", "soybean", "rice", "barley"]

for x, n in enumerate(pythoncrops):
    print(f"crop name: {n}, index number: {x} ")
pythoncrops.append("millet")
pythoncrops.remove("corn")
print(pythoncrops)



# 2. Drone Status
# Create a dictionary for a drone with these fields: model, battery, altitude, speed. Print each key and value on its own line.
drone_stats = {
    "model": " DJI Tello",
    "battery": 90,
    "altitude" : 100, 
    "speed" : 30
}

for key, value in drone_stats.items():
    print(f"{key}: {value}")




# 🌿 Intermediate
# 3. Moisture Alert
# You have a list of dictionaries, one per sensor zone:
# pythonsensors = [
#     {"zone": "A1", "moisture": 72},
#     {"zone": "A2", "moisture": 31},
#     {"zone": "A3", "moisture": 88},
#     {"zone": "A4", "moisture": 19},
#     {"zone": "A5", "moisture": 65},
# ]
# Loop through and print a warning for any zone with moisture below 40.
pythonsensors = [
    {"zone": "A1", "moisture": 72},
    {"zone": "A2", "moisture": 31},
    {"zone": "A3", "moisture": 88},
    {"zone": "A4", "moisture": 19},
    {"zone": "A5", "moisture": 65},
]

for sensor in pythonsensors:
    if sensor['moisture'] < 40:
        print(f"Warning Zone {sensor['zone']} moisture below optimal level")  



# 4. Fleet Tracker
# You have a list of drones, each with a id and battery level:
# pythonfleet = [
#     {"id": "DR01", "battery": 85},
#     {"id": "DR02", "battery": 12},
#     {"id": "DR03", "battery": 67},
#     {"id": "DR04", "battery": 8},
#     {"id": "DR05", "battery": 91},
# ]
# Print drones that need charging (battery below 20)
# Print the drone with the highest battery level
pythonfleet = [
    {"id": "DR01", "battery": 85},
    {"id": "DR02", "battery": 12},
    {"id": "DR03", "battery": 67},
    {"id": "DR04", "battery": 8},
    {"id": "DR05", "battery": 91},
]
# use below to use list max function on a dictionary by using lambda
largest = max(pythonfleet, key=lambda x: x['battery'])
for fleet in pythonfleet: 
    if fleet['battery'] < 20: 
        print(f"{fleet['id']} battery is {fleet['battery']} and needs charging")
print(f"{largest['id']} has the highest battery level at {largest['battery']}%")



# 🌾 Advanced
# 5. Crop Health Summary
# You have scan results from multiple field zones:
# pythonscans = [
#     {"zone": "B1", "crop": "wheat", "health": 8},
#     {"zone": "B2", "crop": "corn", "health": 4},
#     {"zone": "B3", "crop": "wheat", "health": 6},
#     {"zone": "B4", "crop": "corn", "health": 9},
#     {"zone": "B5", "crop": "wheat", "health": 3},
#     {"zone": "B6", "crop": "corn", "health": 7},
# ]
# Calculate and print the average health score per crop type — so one average for wheat and one for corn.
pythonscans = [
    {"zone": "B1", "crop": "wheat", "health": 8},
    {"zone": "B2", "crop": "corn", "health": 4},
    {"zone": "B3", "crop": "wheat", "health": 6},
    {"zone": "B4", "crop": "corn", "health": 9},
    {"zone": "B5", "crop": "wheat", "health": 3},
    {"zone": "B6", "crop": "corn", "health": 7},
]
totalWht = 0
totalCorn = 0
countWht = 0
countCorn = 0
for n in pythonscans: 
    if n["crop"] == "wheat": 
        totalWht += n['health']
        countWht += 1
    else:
        totalCorn += n['health']
        countCorn += 1
cornAvg = totalCorn / countCorn
wheatAvg = totalWht / countWht
print(f"Average Health score for corn: {cornAvg:.2f}")
print(f"Average Health score for wheat: {wheatAvg:.2f}")

totals = {}
counts = {}
for n in pythonscans:
    crop = n['crop']
    print(crop)   
    if crop not in totals:
        totals[crop] = 0
        counts[crop] = 0
    totals[crop] += n['health']
    counts[crop] += 1
print(totals['wheat'] / counts['wheat'])
print(totals['corn'] / counts['corn'])

        

# 6. Waypoint Logger
# A drone flies over 5 waypoints. For each waypoint, generate a random health score (1–10) and store each waypoint as a dictionary with id, 
# coordinates, and health_score in a list. After the flight, print the full log and highlight the waypoint with the lowest health score for follow-up inspection.


waypointData = [
    {"id": 359,
    "coordinates": (-930,432),
    "waypointName": "waypoint1"},
    {"id": 256,
    "coordinates": (3,900),
    "waypointName": "waypoint2"},
    {"id": 232,
    "coordinates": (-590, 900),
    "waypointName": "waypoint3"},
    {"id": 243,
    "coordinates": (-20,300),
    "waypointName": "waypoint4"},
    {"id": 277,
    "coordinates": (-630,332),
    "waypointName": "waypoint5"}
]

# Build the flight log dynamically
waypoints = []
for wp in waypointData:
    waypoints.append({
        "id": wp["id"],
        "coordinates": wp["coordinates"],
        "waypointName": wp["waypointName"],
        "healthscore": random.randint(1, 10)  # generated here, not before
    })


# use below to use list max function on a dictionary by using lambda
smallest = min(waypoints, key=lambda x:x['healthscore'])
print("Flight Log: \n")
for x in waypoints:
    if x['healthscore'] == smallest['healthscore']:
        print(f"{x['waypointName']}\n drone #{x['id']}\n Health:{x['healthscore']} bad needs inspection\ncoordinates:{x['coordinates']}\n")
    else:
        print(f"{x['waypointName']}\n drone #{x['id']}\n Health:{x['healthscore']} good\ncoordinates:{x['coordinates']}\n")
    
