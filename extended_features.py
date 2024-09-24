from fpdf import FPDF
from database import search_access_records, search_user_status

# Generate PDF report for a specific student ID
def generate_report(student_id=None, output_file="access_report.pdf"):
    # Fetch the student's status
    status = search_user_status(student_id)

    # Fetch access records for the student
    records = search_access_records(student_id=student_id)

    # Create a new PDF document
    pdf = FPDF()
    pdf.add_page()

    # Add title to the PDF
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="SUN Lab Access Report", ln=True, align='C')

    pdf.set_font("Arial", size=12)

    # Check if the student exists and display their status
    if status:
        pdf.cell(200, 10, txt=f"Student ID: {student_id}, Status: {status[0]}", ln=True)
    else:
        pdf.cell(200, 10, txt=f"Student ID: {student_id} not found.", ln=True)
        pdf.output(output_file)
        return

    pdf.ln(10)  # Add a line space

    # Check if access records exist
    if not records:
        pdf.cell(200, 10, txt=f"No access records found for Student ID: {student_id}.", ln=True)
    else:
        pdf.cell(200, 10, txt=f"Access records for Student ID: {student_id}", ln=True)
        pdf.ln(10)  # Add a line space

        # List all records for the student
        for record in records:
            pdf.cell(200, 10, txt=f"ID: {record[0]}, Time: {record[2]}", ln=True)

    # Save the PDF file
    pdf.output(output_file)

    print(f"Report saved as {output_file}")
