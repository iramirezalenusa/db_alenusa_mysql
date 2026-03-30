import pandas as pd

# Load the CSV
df = pd.read_csv(r"C:\Repositories\db_alenusa\seeds\fct_costco_weather.csv")

# Rename columns
rename_map = {
    "Venue": "venue",
    "Item": "item",
    "Time": "periods",
    "MAX Temperature": "temp_max",
    "MIN Temperature": "temp_min",
    "AVG Temperature": "temp_avg",
    "Departure from Normal AVG Temperature": "temp_departure_from_normal",
    "Total Precipitation in Inches": "precipitation_total_in",
    "Daily AVG Precipitation in Inches": "precipitation_daily_avg_in",
    "Total Snowfall in Inches": "snowfall_total_in",
    "Daily AVG Snowfall in Inches": "snowfall_daily_avg_in",
}

# Apply to a DataFrame
df = df.rename(columns=rename_map)

# Extract date
df["week_ending"] = pd.to_datetime(
    df["periods"].str.extract(r'(\d{2}-\d{2}-\d{4})')[0], 
    format="%m-%d-%Y"
).dt.strftime("%Y-%m-%d")


# Set df to store 
writeCols = [
    "venue",
    "item",
    'periods',
    "week_ending",
    "temp_max",
    "temp_min",
    "temp_avg",
    "temp_departure_from_normal",
    "precipitation_total_in",
    "precipitation_daily_avg_in",
    "snowfall_total_in",
    "snowfall_daily_avg_in",
]

df = df[writeCols]

# Save back to the same file
df.to_csv(r"C:\Repositories\db_alenusa\seeds\fct_costco_weather.csv", index=False)

print("Done! Columns renamed successfully.")
print(df.columns.tolist())