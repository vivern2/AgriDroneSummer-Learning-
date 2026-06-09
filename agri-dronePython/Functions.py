import random

#Challenge 1 — Battery Check
#Write a function that takes a drone's current battery percentage and returns "Safe to fly" if it's 20% or above, and "Return to base" if it's below 20%.
def Battery_Check(percentage):
    if percentage <= .20:
        return "return to base"
    else:
        return "safe to fly"
percent = random.random()
print(f'my drone is {percent * 100:.2f}%')
print(Battery_Check(percent))

    
#Challenge 2 — Distance to Waypoint
#Write a function that takes two (x, y) coordinates — the drone's current position and a target waypoint — and returns the straight-line distance between them.
def way_point(x,y,x_new,y_new):
    distance = ((x_new - x)**2 + (y_new - y)**2)**0.5
    return distance
x = random.uniform(-300,300)
y = random.uniform(-300,300)
z = random.uniform(-300,300)
d = random.uniform(-300,300)
first_coordinate = (x,y)
second_coordinates = (z,d)
print(f"your begining coordinates were {first_coordinate}")
print(f"your ending coordinates were {second_coordinates}")
print(f'your distance traveled is {way_point(x,y,z,d):.2f} miles')
    
#Challenge 3 — Crop Health Flag
#Write a function that takes a crop moisture level (a float between 0 and 1) and returns:
#"Critical" if below 0.2
#"Low" if between 0.2 and 0.5
#"Healthy" if above 0.5

def cropHealthFlag(moisture_lvl):
    if moisture_lvl < 0.2:
        return "Critical"
    elif moisture_lvl < 0.5:
        return "Low"
    else: 
        return "Healthy"

plantMstLvl = random.random()
print(f'The plant moisture level is {plantMstLvl}')
print(f'That is {cropHealthFlag(plantMstLvl)}')

#Challange 4
#Write a function acre_to_hectares(acres) that converts acres to hectares.
# Remember (1 acre = 0.404686 hectares) return the value rounded to 2 decimal places
def acre_to_hectares(acre):
    hectare = round(acre * 0.404686, 2)
    return hectare

farmer_acre = random.uniform(.2,100)
print(f'I have {farmer_acre} acres that converts to {acre_to_hectares(farmer_acre)} hectares ')

        
