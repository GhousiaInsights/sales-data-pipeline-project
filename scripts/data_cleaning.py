import pandas as pd
import os

# Project folder
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load raw sales data
input_path = os.path.join(
    project_dir,
    "data",
    "raw",
    "sales_data.csv"
)

df = pd.read_csv(
    input_path,
    encoding='latin1'
)

# Show first 5 rows
print(df.head())

# Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Convert dates
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)
df['ship_date'] = pd.to_datetime(df['ship_date'], dayfirst=True)

# Convert sales to numeric
df['sales'] = pd.to_numeric(df['sales'])

# Remove duplicates
df = df.drop_duplicates()

# Fill missing postal codes
df['postal_code'] = df['postal_code'].fillna(0)

# Feature Engineering
df['delivery_days'] = (
    df['ship_date'] - df['order_date']
).dt.days

df['order_year'] = df['order_date'].dt.year
df['order_month'] = df['order_date'].dt.month

# Save cleaned data
output_path = os.path.join(
    project_dir,
    "data",
    "processed",
    "clean_sales_data.csv"
)

df.to_csv(output_path, index=False)

print("Data cleaned successfully!")
print("Clean file saved in processed folder.")