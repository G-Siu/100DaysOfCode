# Scenario
"""
There is to me a menu that has 3 options; 
1 - Add Name to List
2 - Write List to File
3 - Exit

Option 1 - will ask the user to enter a name which will be added to a list
Option 2 - will then write the list out to a file
Option 3 - will exit the application
"""

# Global Variables
names = []  # Creating a list for names

def menu():
    while True:
        print("Menu")
        print("1..Add name to list")
        print("2..Write list to file")
        print("3..Exit")
        choice = input("Please select an option : ")
        if choice == "1":
            inputNames()
        elif choice == "2":
            writeFile()
        elif choice == "3":
            return
        else:
            input("Invalid option. Press any key to continue.")


def inputNames():
    global names
    name = input("Please enter name : ")
    names.append(name)
    
def writeFile():
    global names
    with open("names.txt", 'w') as file:
        for name in names:
            file.write(f"{name}\n")

menu()
