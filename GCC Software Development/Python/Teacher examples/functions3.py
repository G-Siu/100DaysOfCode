import os

def ShowList():
    for item in InfoList:
        print(item)
    input("Press any key to continue")

def AppendList():
    appendItem = input("What do you want to append : ")
    InfoList.append(appendItem)

def InsertList():
    insertIndex = int(input("Where do you want to insert item : "))
    insertValue = input("What do you want to insert :")
    InfoList.insert(insertIndex, insertValue)

def DisplayList():
    count = 0
    for item in InfoList:
        count += 1
    print(f"Number of items in list is {count}")
    input("Press any key to continue")

def ShowMenu():
    os.system('cls')
    print("1..Show List")
    print("2..Append to List")
    print("3..Insert into List")
    print("4..Display length of List")
    print("5..Exit")

InfoList = [33, 4, "Hello", 3.14, "Sunshine"]
choice = 0
while choice != 5:
    ShowMenu()
    choice = int(input("Please enter option : "))
    if choice == 1:
        ShowList()
    elif choice == 2:
        AppendList()
    elif choice == 3:
        InsertList()
    elif choice == 4:
        DisplayList()
    elif choice == 5:
        print("Goodbye")
    else:
        print("Wrong option.")