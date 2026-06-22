# 🌱 Beginner
# 1. Basic Drone Class
# Create a Drone class with attributes id, battery, and altitude (default 0). Add a method status() that prints all three values in a readable sentence.
# 2. Charging Method
# Add a charge() method to your Drone class that adds 25% to the battery, but never lets it go above 100%.
#  Print the new battery level after charging.

class Drone:
    def __init__(self, id, battery, altitude = 0):
        self.id = id
        self.battery = battery
        self.altitude = altitude

    def status(self): 
        print(f"drone #{self.id} has a battery of {self.battery}% and is flying at an altitude of {self.altitude}.")

    def charge(self):
        self.battery += 25
        self.battery = min (self.battery, 100)
        
idNum = 119
battery = 25
altitude = 115
drone1 = Drone(idNum, battery, altitude) # this is an object 
drone1.charge()
drone1.charge()
drone1.status()


# 🌿 Intermediate
# 3. Field Sensor Class
# Create a Sensor class with attributes zone, moisture, and crop_type. Add a method is_dry() 
# that returns True if moisture is below 40, and a method report() that prints a warning if the zone is dry,
#  or a confirmation if it's fine.
# 4. Multiple Drones
# Create 3 Drone objects with different battery levels. Loop through them (put them in a list first) and print which ones need charging (battery below 20%).

class Sensor:
    def __init__(self, zone, moisture, crop_type, battery):
        self.zone = zone
        self.moisture = moisture
        self.crop_type = crop_type
        self.battery = battery

    def is_dry(self): 
        if self.moisture < 40:
            return True
        else:
            return False
        
    
    def report(self):
        if self.is_dry() == True:
            print("WARNING!!!! This zone is dry!")
        else: 
            print("This zone is good everything is fine")
        if self.battery <= 20:
            print("This drone has a low battery and needs to charge!\n")
        else:
            print("this drones battery is good\n")

#below are the drone objects 
droneInZone = []
drone3 = Sensor(6,80,"wheat", 15)
drone4 = Sensor(3,20,"coconut",70)
drone5 = Sensor(5,23,"mango",30)

droneInZone.append(drone3)
droneInZone.append(drone4)
droneInZone.append(drone5)
for x in droneInZone:
    print(f" drone in zone #{x.zone} Report: ")
    x.report()

        
     

     
          
     
# 🌾 Advanced
# 5. Flight Log Class
# Create a Drone class with id, battery, and a log attribute that starts as an empty list. Add a fly(distance) method that:
# Reduces battery by distance * 2 (capped at 0, never negative)
# Appends a string describing the flight to self.log
# Then create one drone, call fly() three times with different distances, and print the full log at the end.


# 6. Field Manager
# Create a Field class that has a name and a sensors list (starts empty). Add a method add_sensor(sensor) that appends a Sensor object (reuse your class from #3) to the list, and a method average_moisture() that calculates the average moisture across all sensors in the field.