import os

def Menu():
    print("Menu Options\n===========")
    print("1..Enter Name")
    print("2..Enter Date of Birth")
    print("3..Enter Address")
    print("4..Exit")
    choice = int(input("\nPlease select an option from above : "))

    match choice:
        case 1:
            EnterName()
        case 2:
            EnterDoB()
        case 3:
            EnterAddress()
        case 4:
            print("Goodbye")
        case _:
            print("Invalid Option")

def EnterName():
    name = input("Please enter your name : ")
    print(name)

def EnterDoB():
    dob = input("Please enter date of birth : ")
    print(dob)

def EnterAddress():
    address = input("Please enter address : ")
    print(address)

while True:
    os.system('cls')
    Menu()

