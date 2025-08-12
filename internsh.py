import tkinter as tk
from tkinter import messagebox, ttk

# List of Indian cities (capitalized properly)
INDIAN_CITIES = [
    "Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Ahmedabad",
    "Chennai", "Kolkata", "Pune", "Jaipur", "Lucknow",
    "Davangere", "Bellary", "Chitradurga"
]

# Pre-loaded fallback weather data (corrected typos in city names)
FALLBACK_DATA = {
    "Mumbai": {"temp": 30, "desc": "Clear Sky", "humidity": 70, "wind_speed": 4.5},
    "Delhi": {"temp": 32, "desc": "Haze", "humidity": 40, "wind_speed": 3.2},
    "Bengaluru": {"temp": 27, "desc": "Partly Cloudy", "humidity": 60, "wind_speed": 2.8},
    "Hyderabad": {"temp": 28, "desc": "Sunny", "humidity": 55, "wind_speed": 3.0},
    "Ahmedabad": {"temp": 33, "desc": "Hot", "humidity": 45, "wind_speed": 4.0},
    "Chennai": {"temp": 31, "desc": "Humid", "humidity": 80, "wind_speed": 5.1},
    "Kolkata": {"temp": 29, "desc": "Rainy", "humidity": 85, "wind_speed": 4.8},
    "Pune": {"temp": 26, "desc": "Cool Breeze", "humidity": 50, "wind_speed": 3.5},
    "Jaipur": {"temp": 34, "desc": "Hot and Dry", "humidity": 30, "wind_speed": 3.8},
    "Lucknow": {"temp": 28, "desc": "Cloudy", "humidity": 65, "wind_speed": 3.3},
    "Davangere": {"temp": 28, "desc": "Hot", "humidity": 45, "wind_speed": 4.0},
    "Bellary": {"temp": 21, "desc": "Cloudy", "humidity": 65, "wind_speed": 3.3},
    "Chitradurga": {"temp": 20, "desc": "Cool Breeze", "humidity": 85, "wind_speed": 4.8},
}

# Weather color mapping based on description
WEATHER_COLORS = {
    "rain": "#74b9ff",
    "shower": "#74b9ff",
    "cloud": "#b2bec3",
    "sunny": "#ffeaa7",
    "clear": "#ffeaa7",
    "hot": "#ff7675",
    "humid": "#55efc4"
}

def get_weather(city):
    city_title = city.strip().title()  # Ensure city names are formatted correctly
    if city_title in FALLBACK_DATA:
        fallback = FALLBACK_DATA[city_title]
        return {
            "city": city_title,
            "country": "India",
            "temp": fallback["temp"],
            "desc": fallback["desc"],
            "humidity": fallback["humidity"],
            "wind_speed": fallback["wind_speed"],
            "source": "Fallback Data"
        }
    return None

def show_weather():
    selected_city = city_combo.get()
    if selected_city != "Select City":
        weather_data = get_weather(selected_city)
        if weather_data:
            desc_lower = weather_data["desc"].lower()
            msg_bg = "#dfe6e9"  # Default background color

            # Determine the background color based on description
            for key in WEATHER_COLORS:
                if key in desc_lower:
                    msg_bg = WEATHER_COLORS[key]
                    break

            # Prepare the weather message
            weather_message = (
                f"📍 Weather Report for {weather_data['city']}\n\n"
                f"Description: {weather_data['desc']}\n"
                f"City: {weather_data['city']}, {weather_data['country']}\n"
                f"Temperature: {weather_data['temp']}°C\n"
                f"Humidity: {weather_data['humidity']}%\n"
                f"Wind Speed: {weather_data['wind_speed']} m/s\n"
                f"Data Source: {weather_data['source']}"
            )

            # Show the popup message and update the result label
            messagebox.showinfo("Weather Report", weather_message)
            result_label.config(text=weather_message, bg=msg_bg)
        else:
            messagebox.showerror("Error", "No weather data available for this city.")
    else:
        messagebox.showerror("Input Error", "Please select a valid city from the list!")

# GUI setup
root = tk.Tk()
root.title("Weather App - India Edition")
root.geometry("440x440")
root.config(bg="#dfe6e9")

# Title Label
title_label = tk.Label(root, text="🌤️ Weather App", font=("Arial", 18, "bold"), bg="#dfe6e9", fg="#2d3436")
title_label.pack(pady=10)

# Dropdown Label
dropdown_label = tk.Label(root, text="Select a city:", font=("Arial", 12), bg="#dfe6e9")
dropdown_label.pack(pady=5)

# City Dropdown
city_combo = ttk.Combobox(root, values=INDIAN_CITIES, font=("Arial", 12), state="readonly")
city_combo.set("Select City")
city_combo.pack(pady=5)

# Get Weather Button
get_weather_btn = tk.Button(root, text="Get Weather", font=("Arial", 12), bg="#00b894", fg="white", command=show_weather)
get_weather_btn.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#dfe6e9", justify="left", wraplength=370)
result_label.pack(pady=20)

# Run the app
root.mainloop()
