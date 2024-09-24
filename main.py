import subprocess
from gui import create_gui
from database import create_tables

# Step 1: Set up the database (run this once to initialize the tables)
create_tables()

# Step 2: Automatically run the test data generation script
try:
    print("Generating test data...")
    subprocess.run(["python", "generate_test_data.py"], check=True)
    print("Test data generation complete.")
except subprocess.CalledProcessError as e:
    print(f"Error generating test data: {e}")

# Step 3: Launch the GUI
create_gui()
