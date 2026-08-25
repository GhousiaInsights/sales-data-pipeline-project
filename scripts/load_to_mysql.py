import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Project folder
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables from the project root
load_dotenv(os.path.join(project_dir, ".env"))

# Load cleaned CSV
input_path = os.path.join(
    project_dir,
    "data",
    "processed",
    "clean_sales_data.csv"
)

df = pd.read_csv(input_path)

# MySQL connection settings
username = os.getenv("MYSQL_USERNAME")
password = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST")
database = os.getenv("MYSQL_DATABASE")

# Validate environment variables
if not all([username, password, host, database]):
    raise ValueError(
        "MySQL environment variables are missing. "
        "Check the .env file in the project root."
    )

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