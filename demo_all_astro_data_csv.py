from vedastro import *  # install via pip
import datetime
import pandas as pd  # Install via pip if not already installed
import json

# PART 0 : Set API key
Calculate.SetAPIKey('FreeAPIUser')  # ⚡ unlimited speed API key from "vedastro.org/Account"

# PART 1 : PREPARE NEEDED DATA
# -----------------------------------

# Set birth location
geolocation = GeoLocation("Tokyo, Japan", 139.83, 35.65)

# Initial birth time string
birth_time_str = "23:40 31/12/2010 +08:00"

# Parse the initial birth time string into a datetime object
birth_datetime = datetime.datetime.strptime(birth_time_str, "%H:%M %d/%m/%Y %z")

# PART 2 : GENERATE TIME INSTANCES AND CALCULATE DATA
# -----------------------------------

# List to store all results
results = []

# Define the planet for which data is to be calculated
planet = PlanetName.Sun  # You can change this to other planets as needed

# Loop to create 100 time instances, incrementing by 1 hour each
for i in range(10):
    try:
        # Increment the time by 'i' hours
        current_datetime = birth_datetime + datetime.timedelta(hours=i)
        
        # Format the new datetime back to the string format expected by Vedastro's Time class
        current_time_str = current_datetime.strftime("%H:%M %d/%m/%Y %z")
        
        # Create a Time object with the new time
        current_time = Time(current_time_str, geolocation)
        
        # Calculate all planet data for the specified planet at the current time
        planet_data = Calculate.AllPlanetData(planet, current_time)
        
        # Flatten the planet_data if it's a nested dictionary
        # This step depends on the actual structure of planet_data
        # For demonstration, let's assume it's a flat dictionary
        flat_data = {
            "time": current_time_str,
            "planet": planet.value  # Assuming PlanetName is an Enum
        }
        
        # Update flat_data with planet_data
        if isinstance(planet_data, dict):
            for key, value in planet_data.items():
                # Handle nested dictionaries if necessary
                if isinstance(value, dict):
                    for sub_key, sub_value in value.items():
                        flat_data[f"{key}_{sub_key}"] = sub_value
                else:
                    flat_data[key] = value
        else:
            # If planet_data is not a dict, store it as a string
            flat_data["planet_data"] = str(planet_data)
        
        # Append the flattened data to the results list
        results.append(flat_data)
        
    except Exception as e:
        print(f"Error at iteration {i}: {e}")
        # Optionally, you can decide to continue or break the loop based on the error
        continue

# PART 3 : SAVE THE RESULTS TO A CSV FILE
# -----------------------------------

# Convert the results list to a pandas DataFrame
df = pd.DataFrame(results)

# Optional: Reorder columns if necessary
# For example, place 'time' and 'planet' first
cols = ['time', 'planet'] + [col for col in df.columns if col not in ['time', 'planet']]
df = df[cols]

# Save the DataFrame to a CSV file
csv_filename = 'planet_data_results.csv'
df.to_csv(csv_filename, index=False)

print(f"Data successfully saved to {csv_filename}")
