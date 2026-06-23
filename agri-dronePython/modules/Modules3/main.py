# 🌿 Intermediate
# 3. Your Own Module
# Split your existing code into two files:
# sensor.py — contains your Sensor and Field classes from OOP challenge 6
# main.py — imports from sensor.py, creates a Field, adds 3 sensors, and prints the average moisture


from sensor import Sensor, Field

newField = Field("My field")
drone3 = Sensor(6,80,"wheat", 15)
drone4 = Sensor(3,70,"coconut",70)
drone5 = Sensor(5,50,"mango",30)
newField.add_sensor(drone3)
newField.add_sensor(drone4)
newField.add_sensor(drone5)
avg = newField.avg_moisture()
print(f"Average moisture for {newField.name}: {avg:.2f}%")