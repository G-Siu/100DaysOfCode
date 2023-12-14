# Hiding password & tickets
# Date: 13 Dec 2023
# Name: G Siu

# getpass allow user to enter a password and blank the input
import getpass



# Display menu of ticket options
print("1. Adult\n2. Child\n3. Student\n4. OAP\n5. Exit")
# Ask for user choice
choice = input("Choose from the above ticket options: ").title()

# Conditions for user choice
if choice == "1" or choice == "Adult":
    print("Adult - £19.95")
elif choice == "2" or choice == "Child":
    print("Child - £9.95")
elif choice == "3" or choice == "Student":
    print("Student - £17.95")
elif choice == "4" or choice == "OAP":
    print("OAP - £9.95")
elif choice == "5" or choice == "Exit":
    print("Goodbye")
else:
    print("Invalid option")
