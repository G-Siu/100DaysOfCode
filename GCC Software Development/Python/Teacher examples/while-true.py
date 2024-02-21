import os

while True:
    os.system("cls")
    print("Menu")
    print("1..Option 1")
    print("2..Option 2")
    user_input = input("Enter 'exit' to quit: ")
    match user_input :
        case "1" :
            print("Option 1")
            input("Press 'Enter' to continue")
        case "2" :
            print("Option 2")
            input("Press 'Enter' to continue")
        case "exit" :
            print("Goodbye")
            break
        case _ : 
            print("Invalid option")
            input("Press 'Enter' to continue")