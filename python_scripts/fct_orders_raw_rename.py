import pandas as pd

# Load the CSV
df = pd.read_csv(r"C:\Repositories\db_alenusa_mysql\seeds\fct_orders.csv")

# Rename columns
df.columns = [
    "edi_date_weekday_num",
    "edi_date_weekday_name",
    "edi_date_week_start",
    "edi_date_week_end",
    "edi_date_period_weeks",
    "us_edi_date",
    "material_description",
    "cs_requested",
    "cs_shipped",
    "sales_status",
    "sales_order",
    "order_position",
    "customer_po",
    "month",
    "net_value",
    "gross_weight",
    "customer_id",
    "customer",
    "ship_to",
    "city_ship_to",
    "region",
    "area",
    "kam",
    "obd",
    "us_entry_date",
    "plant_goods_movement",
    "invoice",
    "billing_date",
    "mx_purchase_ord",
    "outbound_delivery",
    "plant",
    "plant_name",
    "mx_entry_date",
    "original_due_date",
    "due_date",
    "appt",
    "appt_time",
    "confirmation",
    "second_appt",
    "second_appt_time",
    "delivery_date",
    "sku",
    "additional_comments"
]

# Save back to the same file
df.to_csv(r"C:\Repositories\db_alenusa_mysql\seeds\fct_orders.csv", index=False)

print("Done! Columns renamed successfully.")
print(df.columns.tolist())