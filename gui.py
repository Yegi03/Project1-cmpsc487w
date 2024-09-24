import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from database import search_access_records, update_user_status, search_user_status
from extended_features import generate_report

# Search function to filter by student ID, date, and time range
def search():
    student_id = student_id_entry.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()

    result_text.delete('1.0', tk.END)  # Clear previous results before showing new ones

    # Fetch and display the user's status (active/suspended)
    status = search_user_status(student_id)
    if status:
        result_text.insert(tk.END, f"Student ID: {student_id} is currently {status[0]}\n\n")
    else:
        result_text.insert(tk.END, "Student not found.\n")
        return

    try:
        start_date_parsed = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_parsed = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid dates in YYYY-MM-DD format.")
        return

    # Query the access records table with filters
    results = search_access_records(student_id, start_date_parsed, end_date_parsed)

    if not results:
        result_text.insert(tk.END, "No records found.\n")
    else:
        for record in results:
            result_text.insert(tk.END, f"ID: {record[0]}, Student ID: {record[1]}, Time: {record[2]}\n")


# Update status of a user (activate, suspend, reactivate)
def update_status():
    student_id = student_id_entry.get()
    new_status = status_entry.get()

    if new_status not in ['active', 'suspended']:
        messagebox.showerror("Error", "Status must be 'active' or 'suspended'")
        return

    update_user_status(student_id, new_status)
    messagebox.showinfo("Success", f"Status updated to '{new_status}' for Student ID {student_id}")
    search()  # Search again after updating status


# Generate PDF report for the student ID entered
def generate_pdf_report():
    student_id = student_id_entry.get()
    generate_report(student_id=student_id, output_file=f"{student_id}_access_report.pdf")
    messagebox.showinfo("Success", f"Report generated for Student ID {student_id}")


# Setting up the GUI
def create_gui():
    window = tk.Tk()
    window.title("SUN Lab Access Admin")

    global student_id_entry, status_entry, start_date_entry, end_date_entry, result_text

    # Entry field for Student ID
    student_id_label = tk.Label(window, text="Student ID:")
    student_id_label.pack()

    student_id_entry = tk.Entry(window)
    student_id_entry.pack()

    # Entry fields for start and end dates (YYYY-MM-DD)
    start_date_label = tk.Label(window, text="Start Date (YYYY-MM-DD):")
    start_date_label.pack()

    start_date_entry = tk.Entry(window)
    start_date_entry.pack()

    end_date_label = tk.Label(window, text="End Date (YYYY-MM-DD):")
    end_date_label.pack()

    end_date_entry = tk.Entry(window)
    end_date_entry.pack()

    # Search button
    search_button = tk.Button(window, text="Search", command=search)
    search_button.pack()

    # Text box to display search results
    result_text = tk.Text(window, height=10)
    result_text.pack()

    # Entry field for updating status
    status_label = tk.Label(window, text="Update Status (active/suspended):")
    status_label.pack()

    status_entry = tk.Entry(window)
    status_entry.pack()

    # Button to update user status
    status_button = tk.Button(window, text="Update Status", command=update_status)
    status_button.pack()

    # Button to generate PDF report
    report_button = tk.Button(window, text="Generate PDF Report", command=generate_pdf_report)
    report_button.pack()

    window.mainloop()
