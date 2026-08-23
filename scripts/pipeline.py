import subprocess
import os

print("=" * 50)
print("Starting Sales Data Pipeline...")
print("=" * 50)

# Get the folder where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Step 1: Run data cleaning
print("\nStep 1: Cleaning data...")
subprocess.run(
    ["python", os.path.join(script_dir, "data_cleaning.py")],
    check=True
)

# Step 2: Load data into MySQL
print("\nStep 2: Loading data into MySQL...")
subprocess.run(
    ["python", os.path.join(script_dir, "load_to_mysql.py")],
    check=True
)

print("\n" + "=" * 50)
print("Pipeline completed successfully!")
print("=" * 50)