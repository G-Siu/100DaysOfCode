print("Menu Options\n===========")
print("1..Option 1")
print("2..Option 2")
print("3..Option 3")
choice = int(input("\nPlease select an option from above : "))

match choice:
    case 1:
        print("Option 1")
    case 2:
        print("Option 2")
    case 3:
        print("Option 3")
    case _:
        print("Invalid Option")


