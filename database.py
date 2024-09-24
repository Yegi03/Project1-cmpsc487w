import sqlite3
from datetime import datetime, timedelta

# Create tables for access records and users
def create_tables():
    conn = sqlite3.connect('sun_lab_access.db')
    cursor = conn.cursor()

    # Table to store access records (records only kept for 5 years)
    cursor.execute('''CREATE TABLE IF NOT EXISTS access_records (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id TEXT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                    )''')

    # Table to store user information (students, faculty, staff, janitors)
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id TEXT UNIQUE,
                        role TEXT DEFAULT 'student',
                        status TEXT DEFAULT 'active'
                    )''')

    conn.commit()
    conn.close()

# Insert a new access record (when a user swipes their card)
def add_access_record(student_id):
    conn = sqlite3.connect('sun_lab_access.db')
    cursor = conn.cursor()

    # Ensure the student exists in the users table before adding a record
    cursor.execute("SELECT status FROM users WHERE student_id = ?", (student_id,))
    result = cursor.fetchone()

    if result is None:
        print(f"User {student_id} not found. Please register the user first.")
    elif result[0] == 'suspended':
        print(f"User {student_id} is suspended and cannot access the lab.")
    else:
        cursor.execute("INSERT INTO access_records (student_id) VALUES (?)", (student_id,))
        conn.commit()

    conn.close()

# Search access records by student ID, date, and time range
def search_access_records(student_id=None, start_date=None, end_date=None):
    conn = sqlite3.connect('sun_lab_access.db')
    cursor = conn.cursor()

    query = "SELECT * FROM access_records WHERE 1=1"
    params = []

    if student_id:
        query += " AND student_id = ?"
        params.append(student_id)

    if start_date and end_date:
        query += " AND timestamp BETWEEN ? AND ?"
        params.append(start_date)
        params.append(end_date)

    cursor.execute(query, params)
    results = cursor.fetchall()

    conn.close()
    return results

# Activate, suspend, or reactivate a user by ID
def update_user_status(student_id, new_status):
    conn = sqlite3.connect('sun_lab_access.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET status = ? WHERE student_id = ?", (new_status, student_id))
    conn.commit()
    conn.close()

# Register a new user
def register_user(student_id, role='student'):
    conn = sqlite3.connect('sun_lab_access.db')
    cursor = conn.cursor()

    cursor.execute("INSERT OR IGNORE INTO users (student_id, role) VALUES (?, ?)", (student_id, role))
    conn.commit()
    conn.close()

# Remove old records (older than 5 years)
def remove_old_records():
    conn = sqlite3.connect('sun_lab_access.db')
    cursor = conn.cursor()

    five_years_ago = datetime.now() - timedelta(days=5*365)
    cursor.execute("DELETE FROM access_records WHERE timestamp < ?", (five_years_ago,))
    conn.commit()
    conn.close()
def search_user_status(student_id):
    conn = sqlite3.connect('sun_lab_access.db')
    cursor = conn.cursor()

    cursor.execute("SELECT status FROM users WHERE student_id = ?", (student_id,))
    result = cursor.fetchone()

    conn.close()
    return result
