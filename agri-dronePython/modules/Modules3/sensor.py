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


class Field:
    def __init__(self,name):
        self.name = name
        self.sensors = []

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def avg_moisture(self):
        n_sensors = len(self.sensors)
        total = 0
        for x in self.sensors:  # x is each Sensor object
            total += x.moisture # access moisture ON that object
        return total / n_sensors           
    
# This signals to anyone reading the file that it's designed to be imported, not run directly.
if __name__ == "__main__":
    # test code here if you want to run sensor.py directly
    pass