import os

while True:
    os.system("cls")
    print("Menu\n"
          "1. Option 1\n"
          "2. Option 2\n"
          "3. Option 3\n"
          "4. Option 4")
    user_input = input("Enter 'exit' to quit: ").lower()
    match user_input:
        case "1":
            print("Option 1")
            input("Press Enter to continue")
        case "2":
            print("Option 2")
            input("Press Enter to continue")
        case "3":
            print("Option 3")
            input("Press Enter to continue")
        case "4":
            print("Option 4")
            input("Press Enter to continue")
        case "exit":
            print("Exiting menu")
            break
        case _:
            print("Invalid option")
            input("Press Enter to continue")
