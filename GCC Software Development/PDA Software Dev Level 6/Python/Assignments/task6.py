# Author: Gary Siu
# Date: 19th Feb 2024
# Description: Calculate students' grades from external files

# Function to read data from external files
def read_files():
    # Open names.txt and read contents
    with open("names.txt", "r") as f:
        # Read each line in file and append to list
        names = f.read().splitlines()
    with open("mark1.txt", "r") as f:
        mark1 = f.read().splitlines()
    with open("mark2.txt", "r") as f:
        mark2 = f.read().splitlines()
    # Initialise empty list
    students = []
    # For loop to iterate over the length of the "names" list
    for i in range(len(names)):
        # Create list of student name, mark1, mark2
        student = [names[i], mark1[i], mark2[i]]
        # Create nested list of students
        students.append(student)
    return students


# Function to calculate mark percentage
def calculate_percentage():
    # Call read_files(), assign students with respective marks to "students"
    students = read_files()
    # Initialise empty list
    students_grade = []
    # Loop each student in students list
    for student in students:
        # Use student's coursework and prelim marks to calculate percentage
        percentage = int(((int(student[1]) + int(student[2])) * 100) / 150)
        # Call determine_grade function and pass percentage as parameter
        grade = determine_grade(percentage)
        # Create list with student name, percentage, and grade
        student_grade = [student[0], percentage, grade]
        # Create nested list of students with their percentages and grades
        students_grade.append(student_grade)
    return students_grade


# Function to return student grade
def determine_grade(percentage):
    # IF conditionals to determine grade achieved
    if percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 45:
        return "D"
    else:
        return "Fail"


def main():
    # Display list of students returned from calculate_percentage()
    print(calculate_percentage())


# Call main to start the program
main()
