# Information Manager
# Name: Gary
# Date created: 29/03/24
# Manage student information with manager

# Adding new student
# name = input("Enter student name: ")
# age = input("Enter student age: ")
# grade = input("Enter student grade: ")

name = "Gary"
age = 29
grade = 81

students = []
student_information = (name, age, grade)
students.append(student_information)

# Display students
for student in enumerate(students):
    print(f"{student[0]} - {student[1][0]} is {student[1][1]} years old and "
          f"achieved grade {student[1][2]}.")


# Searching for student
def search(students):
    search_student = input("Enter name of student you are looking for: ")
    for student in students:
        if search_student == student[0]:
            print(f"{student[0]} is {student[1]} years old and achieved "
                  f"grade {student[2]}.")
    if search_student not in students:
        print("The name you are looking for is not a student.")


# Updating student information
def update(students):
    update_student = input("Enter name of student you want to update "
                           "information for: ")
    for student in students:
        if update_student == student[0]:
            index = students.index(student)
            print("Student found")
            new_age = input("Enter new age: ")
            new_grade = input("Enter new grade: ")
            new_student = (update_student, new_age, new_grade)
            students[index] = new_student
        else:
            print("No student of that name found")


# Deleting student information
def delete_student(students):
    delete_student = input("Enter name of student to delete their "
                           "information: ")
    for student in students:
        if delete_student == student[0]:
            index = students.index(student)
            students.pop(index)
            print(f"Student information deleted for {delete_student}")
        else:
            print("No student of that name found")


delete_student(students)