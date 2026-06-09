import random

#Question 1 Below  and printing values
name = 'South Field'
healthy = False
area_acres = 23.5
    #below are fstrings to print the values of the variables in a readable format
print(f'Field Name: {name}')
print(f'Healthy: {healthy}')
print(f'Area (acres): {area_acres}')    


#Question 2 below 
# what data type would you use to store gps coordinates of a drone
x = random.uniform(-180, 180) #latitude 
y = random.uniform(-180, 180) # longitude
drone_cordinates = (x, y)
print(f' The Drone is at these coordinates: {drone_cordinates}')
print('the drone is now flying to the next location')
x_new = random.uniform(-180, 180) #latitude 
y_new = random.uniform(-180, 180) # longitude
drone_cordinates_new = (x_new, y_new)
distance = ((x_new - x)**2 + (y_new - y)**2)**0.5
print(f'The drone is now at these coordinates: {drone_cordinates_new}')
print(f'the drone flyed {distance} miles')


