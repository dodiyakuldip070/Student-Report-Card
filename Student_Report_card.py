import pandas as pd
import numpy as np

# Function to collect student data
def collect_student_data():
    student_name = input("Enter Student Name: ")
    enrollment_no = input("Enter Enrollment Number: ")
    std = input("Enter Standard (e.g., 10th, 12th): ")
    year = input("Enter Academic Year (e.g., 2024-2025): ")
    month = input("Enter Exam Month (e.g., March): ")
    
    # Collecting subject-wise marks
    num_subjects = int(input("Enter the number of subjects: "))
    subjects = []
    marks = []

    for _ in range(num_subjects):
        subject = input("Enter Subject Name: ")
        mark = int(input(f"Enter Marks for {subject} (out of 100): "))
        subjects.append(subject)
        marks.append(mark)
    
    return {
        "Name": student_name,
        "Enrollment No": enrollment_no,
        "Standard": std,
        "Year": year,
        "Month": month,
        "Subjects": subjects,
        "Marks": marks
    }

# Function to generate the report card
def generate_report_card(student_data):
    # Creating a DataFrame for subjects and marks
    df = pd.DataFrame({
        "Subject": student_data["Subjects"],
        "Marks": student_data["Marks"]
    })

    # Adding total and percentage
    total_marks = df["Marks"].sum()
    percentage = np.round((total_marks / (100 * len(student_data["Subjects"]))) * 100, 2)

    print("\n--- Report Card ---")
    print(f"Name: {student_data['Name']}")
    print(f"Enrollment No: {student_data['Enrollment No']}")
    print(f"Standard: {student_data['Standard']}")
    print(f"Year: {student_data['Year']}")
    print(f"Month: {student_data['Month']}\n")
    print(df)
    print("\nTotal Marks:", total_marks)
    print("Percentage:", percentage, "%")

    # Add a grade based on the percentage
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"
    
    print("Grade:", grade)

# Main Function
def main():
    print("Welcome to Student Report Card Generator!")
    student_data = collect_student_data()
    generate_report_card(student_data)

# Run the app
if __name__ == "__main__":
    main()
