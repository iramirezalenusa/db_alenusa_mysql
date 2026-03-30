import pandas as pd

# Load the CSV
df = pd.read_csv(r"C:\Repositories\db_alenusa\seeds\fct_spectra_retailers.csv")

# Drop duplicate Address column before renaming
df = df.drop(columns=["Address.1"])

# Rename columns
rename_map = {
    "Store.Name": "store_name",
    "Store Number": "store_number",
    "State": "state",
    "Zip Code": "zip_code",
    "Address": "address",
    "ACV": "acv",
    "Cloralen Laundry Demand Index": "cloralen_laundry_di",
    "Pinalen Cleaners Demand Index": "pinalen_cleaners_di",
    "Budget Conscious": "segment_budget_conscious",
    "Heritage Scentimentalists": "segment_heritage_scentimentalists",
    "Proof Seeking Pros": "segment_proof_seeking_pros",
    "Savvy Experimenters": "segment_savvy_experimenters",
    "Well-Being Enthusiasts": "segment_well_being_enthusiasts",
    "Cloralen.DI": "cloralen_di",
    "Cloralen Cleaner Demand Index": "cloralen_cleaner_di",
    "Cloralen BC Triggers Demand Index": "cloralen_bc_triggers_di",
    "Cloralen TBC Demand Index": "cloralen_tbc_di",
    "Cloralen Aromas Laundry Demand Index": "cloralen_aromas_laundry_di",
    "Pinalen.DI": "pinalen_di",
    "Pinalen Dish Demand Index": "pinalen_dish_di",
    "Pinalen Max Aromas MPC Demand Index": "pinalen_max_aromas_mpc_di",
    "Enuseno Laundry Demand Index": "ensueno_laundry_di",
    "Ensueno.DI": "ensueno_di",
    "Lemi Shine GDC Demand Index": "lemi_shine_gdc_di",
    "Lemi Shine Total Cleaner & Supply Demand Index": "lemi_shine_total_cleaner_supply_di",
    "Lemi Shine Dishwasher Cleaner Demand Index": "lemi_shine_dishwasher_cleaner_di",
    "Lemi Shine Booster Demand Index": "lemi_shine_booster_di",
    "Lemi Shine Dish Demand Index": "lemi_shine_dish_di",
    "%income<10K": "pct_income_under_10k",
    "DI Income Under $10,000": "di_income_under_10k",
    "%income10k -14.9K": "pct_income_10k_14k",
    "DI Income $10,000 - $14,999": "di_income_10k_14k",
    "%income15k -24.9K": "pct_income_15k_24k",
    "DI Income $15,000 - $24,999": "di_income_15k_24k",
    "%income25k -34.9K": "pct_income_25k_34k",
    "DI Income $25,000 - $34,999": "di_income_25k_34k",
    "%income35k -49.9K": "pct_income_35k_49k",
    "DI Income $35,000 - $49,999": "di_income_35k_49k",
    "%income50k -74.9K": "pct_income_50k_74k",
    "DI Income $50,000 - $74,999": "di_income_50k_74k",
    "%income75k -99.9K": "pct_income_75k_99k",
    "DI Income $75,000 - $99,999": "di_income_75k_99k",
    "%income100k -149.9K": "pct_income_100k_149k",
    "DI Income $100,000 - $149,999": "di_income_100k_149k",
    "%income150k -199.9K": "pct_income_150k_199k",
    "DI Income $150,000 - $199,999": "di_income_150k_199k",
    "%income200k+": "pct_income_200k_plus",
    "DI Income $200,000 or More": "di_income_200k_plus",
    "%R:White": "pct_race_white",
    "DI Race: White (Non-Hispanic)": "di_race_white",
    "%R:Black": "pct_race_black",
    "DI Race: Black (Non-Hispanic)": "di_race_black",
    "%R:Hisp": "pct_race_hispanic",
    "Hispanic.DI": "di_race_hispanic",
    "%R:Asian": "pct_race_asian",
    "DI Race: Asian (Non-Hispanic)": "di_race_asian",
    "%R:Other": "pct_race_other",
    "DI Race: Other (Non-Hispanic)": "di_race_other",
    "%Hisp:Mexican": "pct_hisp_mexican",
    "DI of Hispanic: Mexican": "di_hisp_mexican",
    "%Hisp:Cuban": "pct_hisp_cuban",
    "DI of Hispanic: Cuban": "di_hisp_cuban",
    "%Hisp:Puerto.Rican": "pct_hisp_puerto_rican",
    "DI of Hispanic: Puerto Rican": "di_hisp_puerto_rican",
    "%Hisp:Other": "pct_hisp_other",
    "DI of Hispanic: Other Hispanic": "di_hisp_other",
    "City": "city",
    "Store.Format": "store_format",
    "Latitude": "latitude",
    "Longitude": "longitude",
    "Market Name": "market_name",
    "Total Selling Area": "total_selling_area_sqft",
    "Median Income (Households)": "median_household_income",
    "Geography Name (Nielsen Designated Market Area (DMA))": "geo_name_dma",
    "Geography Name (Core Based Statistical Area (CBSA))": "geo_name_cbsa",
    "Market Name (Nielsen Designated Market Area (DMA))": "market_name_dma",
    "Store.N.zip": "store_zip",
    "Corp.Mktg.HQ": "corp_mktg_hq",
}

# Apply to a DataFrame
df = df.rename(columns=rename_map)

# Uppercase
df[["address", "store_name", "state", "city"]] = df[["address", "store_name", "state", "city"]].apply(lambda x: x.str.upper())

# Set final df
write_cols = [
    # --- Store identifiers ---
    "store_number",
    "store_name",
    "store_format",
    "store_zip",
    "corp_mktg_hq",

    # --- Store location ---
    "address",
    "city",
    "state",
    "zip_code",
    "latitude",
    "longitude",

    # --- Store market / geography ---
    "market_name",
    "market_name_dma",
    "geo_name_dma",
    "geo_name_cbsa",
    "total_selling_area_sqft",
    "acv",

    # --- Consumer segments ---
    "segment_budget_conscious",
    "segment_heritage_scentimentalists",
    "segment_proof_seeking_pros",
    "segment_savvy_experimenters",
    "segment_well_being_enthusiasts",

    # --- Brand demand indices (top level) ---
    "cloralen_di",
    "pinalen_di",
    "ensueno_di",

    # --- Cloralen demand indices ---
    "cloralen_laundry_di",
    "cloralen_cleaner_di",
    "cloralen_bc_triggers_di",
    "cloralen_tbc_di",
    "cloralen_aromas_laundry_di",

    # --- Pinalen demand indices ---
    "pinalen_cleaners_di",
    "pinalen_dish_di",
    "pinalen_max_aromas_mpc_di",

    # --- Ensueno demand indices ---
    "ensueno_laundry_di",

    # --- Lemi Shine demand indices ---
    "lemi_shine_gdc_di",
    "lemi_shine_total_cleaner_supply_di",
    "lemi_shine_dishwasher_cleaner_di",
    "lemi_shine_booster_di",
    "lemi_shine_dish_di",

    # --- Income distribution (%) ---
    "pct_income_under_10k",
    "pct_income_10k_14k",
    "pct_income_15k_24k",
    "pct_income_25k_34k",
    "pct_income_35k_49k",
    "pct_income_50k_74k",
    "pct_income_75k_99k",
    "pct_income_100k_149k",
    "pct_income_150k_199k",
    "pct_income_200k_plus",

    # --- Income demand indices ---
    "di_income_under_10k",
    "di_income_10k_14k",
    "di_income_15k_24k",
    "di_income_25k_34k",
    "di_income_35k_49k",
    "di_income_50k_74k",
    "di_income_75k_99k",
    "di_income_100k_149k",
    "di_income_150k_199k",
    "di_income_200k_plus",

    # --- Race distribution (%) ---
    "pct_race_white",
    "pct_race_black",
    "pct_race_hispanic",
    "pct_race_asian",
    "pct_race_other",

    # --- Race demand indices ---
    "di_race_white",
    "di_race_black",
    "di_race_hispanic",
    "di_race_asian",
    "di_race_other",

    # --- Hispanic subgroup distribution (%) ---
    "pct_hisp_mexican",
    "pct_hisp_cuban",
    "pct_hisp_puerto_rican",
    "pct_hisp_other",

    # --- Hispanic subgroup demand indices ---
    "di_hisp_mexican",
    "di_hisp_cuban",
    "di_hisp_puerto_rican",
    "di_hisp_other",

    # --- Household income ---
    "median_household_income",
]

df = df[write_cols]

# Save back to the same file
df.to_csv(r"C:\Repositories\db_alenusa\seeds\fct_spectra_retailers.csv", index=False)

print("Done! Columns renamed successfully.")
print(df.columns.tolist())