# Create a module called drone_logger.py that contains:
# A log_flight(drone_id, distance, battery) function that returns a formatted log string including the current timestamp using datetime
# A save_log(filename, logs) function that writes a list of log strings to a txt file
from datetime import datetime

def log_flight(drone_id, distance, battery):
    now = datetime.now()
    return(f"\ndrone: #{drone_id}\n flyed:{distance}ft\n current battery:{battery}% \n current time flown:{now.strftime('%Y-%m-%d %H:%M')}\n\n")

def save_log(filename, logs):
    with open(f"{filename}", "w") as file:
        for x in logs:
            file.write(f"{x}")

#below means only run this code if you're running THIS file directly, not if it's being imported
if __name__ == "__main__":
    #test log below to see if it is working correctly
    test_log = log_flight("DR01", 15, 75)
    print(test_log)