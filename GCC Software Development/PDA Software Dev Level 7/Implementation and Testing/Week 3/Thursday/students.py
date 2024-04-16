# Task: Average grade of each student from JSON file
# Name: G Siu
# Date: 16th April 2024

import json

# Open JSON file
with open("students.json", "r") as f:
    students = json.load(f)  # Load the file content

# Loop through each student in list
for student in students:
    # Calculate average grade
    average_grade = sum(student["grades"]) / len(student["grades"])
    print(f"{student['name']} is {student['age']} years old and scored an "
          f"average of {average_grade:.0f}.")
