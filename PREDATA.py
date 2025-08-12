import csv
import random

# CSV file name
CSV_FILE = "sample_traffic_data.csv"

# Sample data
names = ["Raj", "Priya", "Amit", "Sunita", "Arjun", "Kavita", "Rohan", "Neha", "Rahul", "Anjali",
         "Manish", "Sonia", "Karan", "Pooja", "Vikram", "Shreya", "Suresh", "Meera", "Nitin", "Rashmi"]
vehicle_numbers = [
    f"KA{random.randint(1, 99)} {random.randint(1000, 9999)}" for _ in range(20)
]
vehicle_types = ["Two Wheeler", "Four Wheeler"]
offenses = ["Drunk Drive", "Helmet", "Seat Belt", "Triple Riding"]
penalties = {
    "Drunk Drive": 10000,
    "Helmet": 500,
    "Seat Belt": 1000,
    "Triple Riding": 2000
}

# Function to create and populate the CSV file
def create_sample_csv():
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(["Driver Name", "Vehicle Number", "Vehicle Type", "Offense", "Penalty"])

        # Generate random data for 20 people
        for i in range(20):
            name = random.choice(names)
            vehicle_number = vehicle_numbers[i]
            vehicle_type = random.choice(vehicle_types)
            offense = random.choice(offenses)
            penalty = penalties[offense]

            writer.writerow([name, vehicle_number, vehicle_type, offense, penalty])

    print(f"Sample data written to {CSV_FILE}")

# Create the CSV
create_sample_csv()
