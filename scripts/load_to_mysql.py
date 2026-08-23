import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load cleaned CSV
df = pd.read_csv(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "data",
        "processed",
        "clean_sales_data.csv"
    )
)

# MySQL connection settings
username = os.getenv("MYSQL_USERNAME")
password = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST")
database = os.getenv("MYSQL_DATABASE")

# Create MySQL connection
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

# Load data into MySQL
df.to_sql(
    name="sales_data",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data loaded into MySQL successfully!")