# Database Documentation

## Overview

The SUN Lab Access System uses an SQLite database to manage data related to users and their access to the lab. The database consists of two main tables: `users` and `access_records`. These tables track user information, roles, statuses, and lab access logs.

---

## Tables

### 1. users
This table stores information about each user who may access the SUN Lab.

- **Columns**:
  - `user_id`: Auto-incrementing primary key.
  - `student_id`: A unique identifier for each student.
  - `role`: The role of the user (e.g., student, faculty, staff, janitor). Defaults to "student" but can be extended to other roles.
  - `status`: Indicates whether the user is active or suspended.

---

### 2. access_records
This table logs every time a student swipes their card to enter or exit the lab, tracking their `student_id` and the exact time.

- **Columns**:
  - `id`: Auto-incrementing primary key.
  - `student_id`: Foreign key linking to the `student_id` in the `users` table.
  - `timestamp`: Records the exact time when the student accessed the lab.

---

## Relationships

The `access_records` table is related to the `users` table via the `student_id` field. This relationship allows the system to log and track lab access for each user, and ensure that only authorized (active) users can access the lab.

- The `student_id` in the `access_records` table refers to the corresponding `student_id` in the `users` table.
- If a user is suspended in the `users` table, their access attempts will still be logged, but the system can prevent them from entering the lab.

---

## Data Retention

- **Retention Policy**: Access records are stored in the system for up to 5 years to ensure data availability for audits or other future reference needs.
- This retention period is managed within the system by automatically removing records older than 5 years.

---

## Notes

- The **users** table allows the system to track the status of each user (active, suspended), which can prevent or allow access to the lab.
- The **access_records** table stores detailed logs of when and by whom the lab was accessed.
- This database structure supports future extensibility, such as adding more roles (faculty, staff) or more operations (e.g., additional user management features).

