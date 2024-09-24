# SUN Lab Access System


## Overview

The **SUN Lab Access System** is a Python-based project designed to manage and track access to the **Student Unix Network (SUN) Lab**. This system allows the lab to record student ID numbers and timestamps when students swipe their cards to enter or exit the lab. The system also provides a graphical user interface (GUI) for administrators to search and browse student access records, manage user statuses (activate, suspend, reactivate), and generate PDF reports.

## Features

- **Track Access**: Every time a student swipes their card, the system records the **student ID** and **timestamp**.
- **User Status Management**: Admins can **activate**, **suspend**, or **reactivate** student accounts to control lab access.
- **Search and Filter**: Admins can search and filter access records by:
  - **Student ID**
  - **Date Range**
  - **Time Range**
- **PDF Report Generation**: The system allows admins to generate PDF reports for individual students, which includes the student’s **status** and **access history**.
- **Support for Multiple User Roles**: The system can be extended to handle multiple types of users (students, faculty, staff, janitors).
- **5-Year Record Retention**: Access records are stored for up to 5 years in the database.

## Technologies Used

- **Programming Language**: Python3
- **Database**: SQLite (for storing user and access records)
- **GUI Library**: Tkinter (for the user interface)
- **PDF Generation**: FPDF (for generating PDF reports)

## Project Structure

- **SUN-Lab-Access-System/**
  - `database.py`: Handles SQLite database operations
  - `gui.py`: GUI for admin interaction (search, status update, report generation)
  - `main.py`: Entry point to the system, runs test data generation and launches the GUI
  - `extended_features.py`: Generates PDF reports based on student access records
  - `generate_test_data.py`: Populates the database with test data for students and access records
  - `requirements.md`: High-level requirements for the system
  - `database_documentation.txt`: Explanation of the database schema and tables
  - **output/**
    - `screenshot1.png`: Example screenshot
    - `screenshot2.png`: Example screenshot
    - `screenshot3.png`: Example screenshot
    - `screenshot4.png`: Example screenshot 
    - `example_run.mp4`: Example video demo of system
    - `12345_access_report.pdf` : Example generated PDF
    - `88888_access_report.pdf` : Example generated PDF
    - `65654_access_report.pdf`: Example generated PDF
  - `requirements.txt`: Lists the Python dependencies required to run the project
  - `README.md`: This file
  - `database_documentation.md` : This file has detaled information of database 
  - `.gitignore`: Git ignore file to exclude unnecessary files

## Setup and Installation

### Prerequisites

- **Python 3.x** should be installed on your machine. You can download it from [here](https://www.python.org/downloads/).
- **SQLite** is used as the database, but no additional installation is needed as Python has a built-in SQLite module.

### Step-by-Step Guide

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YourUsername/SUN-Lab-Access-System.git
   cd SUN-Lab-Access-System
2. **Install Required Dependencies: Install the required Python libraries by using the requirements.txt file**:
   ```bash
   pip install -r requirements.txt

3. **Run the Application: You can run the project directly by executing the main.py script. This will generate test data and open the admin GUI**:
   ```bash
   python main.py

4. **Using the GUI**:
   - **Search**: Enter a **student ID** and a **date range** (YYYY-MM-DD) to search for access records.
   - **Update Status**: Enter a **student ID** and select the desired **status** (`active` or `suspended`) to update the user's status.
   - **Generate PDF Report**: Click the "Generate PDF Report" button to generate a PDF report for the entered student ID.


## How the System Works

### Access Management

Every time a student swipes their card at the lab entrance, the system records both the **student ID** and a **timestamp** in the `access_records` table.

- **Student Swipes**: This log helps the lab keep track of who enters or exits the lab and when.
- **Suspended Users**: If a student is marked as "suspended" in the system, they cannot access the lab. When they swipe their card, the system will block entry, and no access record will be saved.

### Admin Features

The system provides several features for administrators:

- **Search and Filter**: Admins can search for access records by **student ID**, or filter them by **start date** and **end date**. The results are displayed in the GUI, making it easy to track student activities.

- **Update User Status**: Admins have control over user statuses and can **activate**, **suspend**, or **reactivate** student accounts. After a status change, the updated information is immediately reflected in the system.

- **Generate Reports**: Admins can generate a detailed **PDF report** for any student. The report includes the student’s current **status** and **access history**, making it useful for tracking or record-keeping purposes.

---
## Database Overview

The SUN Lab Access System uses an SQLite database to manage user data and access records. 

- **users table**: Tracks users, their roles (e.g., student, staff), and their current status (active or suspended).
- **access_records table**: Logs each instance when a user accesses the lab, recording their student ID and the timestamp.

For detailed database structure and relationships, refer to the [Database Documentation](database_documentation.md).

---

## High-Level Requirements

The system follows these key requirements (refer to `requirements.md` for more details):

1. The system MUST track and store access records (student ID and timestamp) whenever a student enters or exits the lab.
2. The system MUST allow authorized users to search access records by student ID, date range, and time range.
3. The system MUST allow administrators to manage user statuses (activate, suspend, reactivate).
4. The system MUST support multiple user roles (students, faculty, staff, janitors).
5. The system SHALL NOT allow suspended users to access the lab.
6. The system MUST store access records for up to **5 years**.
7. The system MUST be implemented in **Python3** and use **SQLite** as the database.





