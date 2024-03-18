# Library
import os

# Grade System
# Using Functions

# Global Variable
actualPassword = "Password"
name = ""
mark = ""

def Menu():
    global name
    global mark
    while True:
        os.system('cls')
        print("Welcome to Grading System")
        print("1..Enter Student Name")
        print("2..Enter Student Mark")
        print("3..Calculate Mark")
        print("4..Exit")
        choice = input("Please enter option from menu : ")
        if choice == "1":
            name = GetStudentName()
        elif choice == "2":
            mark = GetStudentMark()
        elif choice == "3":
            print(CalculateMark(name, mark))
            input("Press any key to continue.")
        elif choice == "4":
            break
        else:
            print("Invalid input option.")



def GetStudentName():
    name = input("Please enter the name of the student : ")
    return name



def GetStudentMark():
    mark = int(input("Please enter students mark : "))
    return mark



def CalculateMark(name, mark):
    if mark >= 70:
        result = f"{name} received a mark of A"
    elif mark >= 60:
        result = f"{name} received a mark of B"        
    elif mark >= 50:
        result = f"{name} received a mark of C"    
    else:
        result = f"{name} failed"
    return result
        

def main():
    os.system('cls')
    for attempts in range(3):
        enteredPassword = input("Please enter password : ")
        if enteredPassword != actualPassword:
            print("Sorry, invalid password entered!")
        else:
            Menu()
            break


if __name__ == "__main__":
    main()

