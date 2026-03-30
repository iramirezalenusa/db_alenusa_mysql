import pandas as pd

# Load the CSV
df = pd.read_csv(r"C:\Repositories\db_alenusa\seeds\dim_costco_items.csv")

# Rename columns
rename_map = {
    "Item": "item",
    "Category Code": "category_code",
    "Category Name": "category_name",
    "Department Code": "department_code",
    "Department Name": "department_name",
    "IRI Master Vendor Name": "iri_master_vendor_name",
    "IRI Parent Company Name": "iri_parent_company_name",
    "Item Description": "item_description",
    "Item Number": "item_number",
    "Segment Code": "segment_code",
    "Segment Name": "segment_name",
    "Sub Category Code": "sub_category_code",
    "Subcategory Name": "subcategory_name",
    "UPC": "upc",
    "Vendor Code": "vendor_code",
    "Vendor Name": "vendor_name",
    "Vendor Suffix": "vendor_suffix",
    "Count": "count",
    "Concentration Level": "concentration_level",
    "Total Count": "total_count",
    "Total Ounces": "total_ounces",
}


# Apply to a DataFrame
df = df.rename(columns=rename_map)

# Save back to the same file
df.to_csv(r"C:\Repositories\db_alenusa\seeds\dim_costco_items.csv", index=False)

print("Done! Columns renamed successfully.")
print(df.columns.tolist())