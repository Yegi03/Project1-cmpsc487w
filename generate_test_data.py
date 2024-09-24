import random
from datetime import datetime, timedelta
from database import create_tables, register_user, add_access_record

# Initialize the database and create tables
create_tables()

# Sample student IDs for testing
students = [
    {"student_id": "12345", "role": "student"},
    {"student_id": "54321", "role": "student"},
    {"student_id": "11111", "role": "student"},
    {"student_id": "22222", "role": "student"},
    {"student_id": "33333", "role": "student"},
    {"student_id": "44444", "role": "student"},
    {"student_id": "55555", "role": "student"},
    {"student_id": "66666", "role": "student"},
    {"student_id": "77777", "role": "student"},
    {"student_id": "88888", "role": "student"}
]

# Function to simulate multiple access records
def generate_access_records(student_id, num_records=5):
    for _ in range(num_records):
        # Generate a random timestamp within the past 30 days
        days_ago = random.randint(0, 30)
        random_time = datetime.now() - timedelta(days=days_ago)
        # Add access record for the student
        add_access_record(student_id)
        print(f"Access record added for {student_id} at {random_time}")

# Register the students and generate test records
for student in students:
    register_user(student["student_id"], student["role"])
    generate_access_records(student["student_id"], num_records=10)

print("Test data generation complete.")
