# Task 2 - Using For & Break
# Date:  19th Dec 2023
# Name: G Siu

for _ in range(4):
    # Ask user for username and password
    username = input("Enter username: ")
    password = input("Enter password: ")
    # Check username and password
    if username == "yourname" and password == "glasgow":
        # If correct, break
        print("Successful login")
        break
    # If wrong, loop again
    print("Wrong username or password")