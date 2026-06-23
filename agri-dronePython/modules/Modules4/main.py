# 4. Random Field Generator
# Using random and os:
# Generate a 4×4 grid of random moisture readings (1–100)
# Create a folder called field_logs using os.makedirs() if it doesn't already exist
# Write the grid to a file called field_logs/moisture_grid.txt
import random 
import os

#Below will make folder called field_logs if it already does not exist
os.makedirs("field_logs", exist_ok=True)


#below creates the field 
def create_field():
    with open("field_logs/moisture_grids.txt", "w") as file:
        for row in range (4):
            for col in range (4):
                n_moisture = random.randint(1, 100)
                file.write(f"{n_moisture} ")
            file.write("\n")


if __name__ == "__main__":
    create_field()
    print("Field moisture grid saved to field_logs/moisture_grids.txt")

    
