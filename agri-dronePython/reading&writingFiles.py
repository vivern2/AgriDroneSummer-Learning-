import csv
import json

# 📄 TXT File — agriculture_dataset.txt

# 1. High Yield Farms
# Read the txt file and print the Farm_ID and Yield of any farm with a yield above 40 tons.
# (Hint: you'll need to split each line and skip the header)
with open ("agri-dronePython/cropData2/agriculture_dataset.txt", "r") as file:
    content = file.read()
    #below will split it at the \n character
    rows = content.split("\n")
    #Below skips the header row as that data is not needed
    rows = rows[1:]

    for row in rows:
        if row == "": #this skips any empty rows
            continue
        columns = row.split("\t") #will split on \t
        yieldNum = float(columns[6]) #converts the string in the array to a num we can use
        if yieldNum > 40:
            print(f"Farm:{columns[0]}, yeild:{columns[6]}")
        
    
# 2. Irrigation Summary
# Read the txt file and count how many farms use each irrigation type (Drip, Flood, Sprinkler, Rain-fed, Manual).
#  Print the totals. (Hint: use a dictionary to keep counts)
with open ("agri-dronePython/cropData2/agriculture_dataset.txt", "r") as file:
    totalIrrigation = {}
    tDrip = 0
    tFlood = 0
    tSprink = 0
    tRainfed = 0
    tManual = 0
    readIrrigation = file.read()
    #below will split it at the \n character
    rows2 = readIrrigation.split("\n")
    #Below will skip the header row as that data is not needed
    for rowNew in rows2: 
        if rowNew == "":
            continue
        col = rowNew.split("\t")
        totalIrrigation[rowNew] = col[3]

    for i in totalIrrigation:
        if totalIrrigation[i] == "Drip":
            tDrip += 1
        if totalIrrigation[i] == "Flood":
            tFlood += 1
        if totalIrrigation[i] == "Sprinkler":
            tSprink += 1
        if totalIrrigation[i] == "Rain-fed":
            tRainfed += 1
        if totalIrrigation[i] == "Manual":
            tManual += 1   
    print(f'{tDrip} Farms use Drip irrigation')
    print(f'{tFlood} Farms use Flood irrigation')
    print(f'{tSprink} Farms use Sprinkler irrigation')
    print(f'{tRainfed} Farms use Rain-fed irrigation')
    print(f'{tManual} Farms use Manual irrigation') 

        
            




# 📊 CSV File — Inda_Agriculture.csv
# 3. Season Filter
# Read the CSV using csv.DictReader and print all rows where the Season is "Kharif" and Production is above 5000 tonnes.

with open("agri-dronePython/cropData2/India_Agriculture.csv", "r") as file:
    reader = csv.DictReader(file)
    #below is how we would see the file
    for row in reader:
        if row["Production"] == "":
            continue
        if(row["Season"] == "Kharif") and (float(row["Production"]) > 5000) :
            print(row)
    


# 4. Top Yield by State
# Read the CSV and find the row with the highest Yield value. Print the State, Crop, and Yield.

# 📦 JSON File — Global_Agriculture.json
# 5. Region Filter
# Read the JSON file and print all entries where region is "South Asia" and year is 2000. Print the country_name and value.

# 6. Country Tracker
# Read the JSON and find the average agriculture value for a country of your choice across all years it appears. Print the country name and its average value rounded to 2 decimal places.

# 🌾 Combined Challenge
# 7. Cross File Report

# From the txt file, calculate the average yield across all 50 farms
# From the JSON file, find the highest agriculture value recorded globally and which country it belongs to
# Print both results as a mini summary report