import pandas as pd

# Load CSV file
df = pd.read_csv(r"C:\Users\sghou\Desktop\sales-data-pipeline-project\data\raw\sales_data.csv", encoding='latin1')

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
df.to_csv(
    r"C:\Users\sghou\Desktop\sales-data-pipeline-project\data\processed\clean_sales_data.csv",
    index=False
)

print("Data cleaned successfully!")
print("Clean file saved in processed folder.")