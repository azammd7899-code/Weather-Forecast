import tkinter as tk
from tkinter import messagebox
import csv
import pandas as pd
import matplotlib.pyplot as plt

# Penalty details as per Indian traffic rules
PENALTIES = {
    "Drunk Drive": 10000,
    "Helmet": 500,
    "Seat Belt": 1000,
    "Triple Riding": 2000
}

# CSV file name
CSV_FILE = "sample_traffic_data.csv"


# Ensure CSV file has headers
def initialize_csv():
    try:
        with open(CSV_FILE, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Driver Name", "Vehicle Number", "Vehicle Type", "Offense", "Penalty"])
    except FileExistsError:
        pass


# Save data to CSV
def save_to_csv(data):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


# Analyze data and display confusion matrix and plot
def analyze_data():
    try:
        df = pd.read_csv(CSV_FILE)

        # Count offenses
        offense_counts = df['Offense'].value_counts()

        # Display graph
        plt.figure(figsize=(10, 5))
        offense_counts.plot(kind='bar', color='skyblue', title='Offenses Count')
        plt.xlabel('Offense')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.show()

        # Confusion matrix-like summary
        summary = offense_counts.to_frame(name='Count')
        messagebox.showinfo("Analysis Summary", summary.to_string())

    except Exception as e:
        messagebox.showerror("Error", f"Error in analysis: {str(e)}")


# Submit form data
def submit():
    driver_name = entry_driver_name.get()
    vehicle_number = entry_vehicle_number.get()
    vehicle_type = vehicle_type_var.get()
    offense = offense_var.get()

    if not driver_name or not vehicle_number or not vehicle_type or not offense:
        messagebox.showerror("Error", "All fields are required!")
        return

    penalty = PENALTIES.get(offense, 0)

    save_to_csv([driver_name, vehicle_number, vehicle_type, offense, penalty])

    messagebox.showinfo("Success", f"Data saved successfully! Penalty: Rs. {penalty}")
    entry_driver_name.delete(0, tk.END)
    entry_vehicle_number.delete(0, tk.END)
    vehicle_type_var.set("")
    offense_var.set("")


# Initialize CSV
initialize_csv()

# Create GUI
root = tk.Tk()
root.title("Indian Traffic Rules Violation")

# Driver Name
label_driver_name = tk.Label(root, text="Driver Name:")
label_driver_name.grid(row=0, column=0, padx=10, pady=10)
entry_driver_name = tk.Entry(root)
entry_driver_name.grid(row=0, column=1, padx=10, pady=10)

# Vehicle Number
label_vehicle_number = tk.Label(root, text="Vehicle Number:")
label_vehicle_number.grid(row=1, column=0, padx=10, pady=10)
entry_vehicle_number = tk.Entry(root)
entry_vehicle_number.grid(row=1, column=1, padx=10, pady=10)

# Vehicle Type
label_vehicle_type = tk.Label(root, text="Vehicle Type:")
label_vehicle_type.grid(row=2, column=0, padx=10, pady=10)
vehicle_type_var = tk.StringVar()
vehicle_type_two = tk.Radiobutton(root, text="Two Wheeler", variable=vehicle_type_var, value="Two Wheeler")
vehicle_type_four = tk.Radiobutton(root, text="Four Wheeler", variable=vehicle_type_var, value="Four Wheeler")
vehicle_type_two.grid(row=2, column=1, sticky="W", padx=10)
vehicle_type_four.grid(row=2, column=1, sticky="E", padx=10)

# Offense
label_offense = tk.Label(root, text="Offense:")
label_offense.grid(row=3, column=0, padx=10, pady=10)
offense_var = tk.StringVar()
offense_menu = tk.OptionMenu(root, offense_var, *PENALTIES.keys())
offense_menu.grid(row=3, column=1, padx=10, pady=10)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Analyze Button
analyze_button = tk.Button(root, text="Analyze Data", command=analyze_data)
analyze_button.grid(row=5, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()
