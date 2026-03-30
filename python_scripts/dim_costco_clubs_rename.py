import pandas as pd

# Load the CSV
df = pd.read_csv(r"C:\Repositories\db_alenusa\seeds\dim_costco_clubs.csv")

# Rename columns
rename_map = {
    "Venue": "warehouse",
    "State or Province": "state",
    "Region Name": "region_name",
    "City": "city",
    "Address": "address",
    "Postal Code": "zip_code",
    "Store Open Date": "store_open_date",
    "Gas Flag": "gas_flag",
    "Warehouse Status": "warehouse_status",
    "Region Code": "region_code",
    "Warehouse Code": "warehouse_code",
    "Warehouse Name": "warehouse_name",
    "Latitude": "latitude",
    "Longitude": "longitude",
}

# Apply to a DataFrame
df = df.rename(columns=rename_map)

# Format dates
df["store_open_date"] = pd.to_datetime(
    df["store_open_date"], format="mixed", errors="coerce"  # coerce turns invalid dates into NaT
).dt.strftime("%Y-%m-%d")

# NaT becomes "NaT" string after strftime, replace with None/empty
df["store_open_date"] = df["store_open_date"].replace("NaT", None)


# Save back to the same file
df.to_csv(r"C:\Repositories\db_alenusa\seeds\dim_costco_clubs.csv", index=False)

print("Done! Columns renamed successfully.")
print(df.columns.tolist())