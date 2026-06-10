import random

# #🌱 Beginner
# #1. Field Row Scanner
# #A drone scans a field with 8 rows. Print each row number and whether it's an odd or even row.
for row in range (8):
    if row % 2 == 0:
        print("even ")
    else: 
        print("odd ")
    

# 2. Battery Check
# A drone starts with 100% battery and loses 12% per flight. Use a while loop to print the battery level before each flight, stopping when it drops below 20%.
batteryLvl = 100
while batteryLvl > 20:
    if batteryLvl == 100:
        print(f"drone at {batteryLvl}% before flight")
    batteryLvl -= 12
    print(f"drone at {batteryLvl}% before flight")
    if batteryLvl < 20:
        print(f"drone battery too low to fly")

# 🌿 Intermediate
# 3. Crop Grid Survey
# A field is a 5×5 grid. The drone visits every cell. Print each coordinate (row, col) — but skip the corners (they're obstacles).
# end parameter makes everything on the same line
for row in range (5):
    for col in range (5):
        #below means if (row == 0 or row == 4) and (col == 0 or col == 4)
        if row in (0, 4) and col in (0, 4):
            print(f"({row}, {col})", end=" ")
    print()


# think of outer loop is iteration of how many times to execute inner loop
for x in range (3):
    for y in range(1, 10):
        print (f"({x},{y})", end=" ")
    print()

# 4. Moisture Readings
# You have a list of soil moisture readings from 10 sensors:
# pythonreadings = [72, 45, 88, 60, 23, 91, 55, 38, 76, 41]
# Loop through and print which zones are dry (below 50), optimal (50–75), or wet (above 75).
pythonreadings = [72, 45, 88, 60, 23, 91, 55, 38, 76, 41]
for n in pythonreadings:
    if n > 75 :
        print(f"{n} is a wet zone ")
    elif (n >= 50) and (n <= 75):
        print(f"{n} is a optimal zone ")
    else: 
        print(f"{n} is a dry zone ")    
    
    


# 🌾 Advanced
# # 5. Zigzag Flight Path
# Drones often fly in a zigzag pattern over a grid to cover every row efficiently.
#  For a 4×6 grid, print the coordinates in zigzag order — left to right on even rows, right to left on odd rows.
for x in range (4):
    if x % 2 == 0:
        cols = range(6)     
    else: 
        cols = range(5, -1, -1)    
    for y in cols:
        print (f"({x},{y})", end=" ")
    print()


# 6. Yield Estimator
# A drone scans a 3×4 field grid. Assign a random crop health score (1–10) to each cell and calculate the total and average yield score for the whole field.

total = 0
for x in range (3):
    for y in range (4):
        cropScore = random.randint(1, 10)
        # adds cropScore into total each iteration
        total += cropScore
        print(cropScore, end=" ")
    print()
print(f"Total Yeild score is {total}")
print(f"Average Yeild score is {total / 12:.2f}")
