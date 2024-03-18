# Author : Paul Dorman
# Description : Stock System
# Date : 6th Feb 2024

# Import OS library
# This will allow me to clear the screen
import os


# Read the individual data files into lists
def readFiles():

    # Read item.txt
    with open('item.txt', 'r') as file:
        itemList = file.read().splitlines()

    # Read amount.txt
    with open('amount.txt', 'r') as file:
        amountList = file.read().splitlines()

    # Read cost.txt
    with open('cost.txt', 'r') as file:
        costList = file.read().splitlines()

    # Combine Lists
    combinedList = list(zip(itemList, amountList, costList))
    
    #return combinedList
    return combinedList

# Display Menu
# Loop around until option 7 is selected
def menu():
    combinedList = readFiles()
    while True:
        os.system('cls')
        print("Menu\n====\n")
        print("1..Show total value of stock")
        print("2..Show all current stock items and quantity")
        print("3..Show stock items with less than 30 in stock")
        print("4..Show the average stock price")
        print("5..Show the maximum stock price")
        print("6..Show the minimum stock price")
        print("7..Exit")
        choice = input("\nPlease select option : ")
        if choice == "1":
            totalValue(combinedList)
        elif choice == "2":
            showAllStock(combinedList)
        elif choice == "3":
            showLessThan30(combinedList)
        elif choice == "4":
            average(combinedList)
        elif choice == "5":
            maximum(combinedList)
        elif choice == "6":
            minimum(combinedList)
        elif choice == "7":
            return      
        else:
            print("Invalid option. Press Enter to continue.")
            input()


# Display the total value of stock
def totalValue(combinedList):
    os.system('cls')
    print("Total Value of Stock")
    print("--------------------\n")
    totalValueOfStock = 0 # Variable to store running value of stock
    for item in combinedList:
        # multiply amount with cost for each item
        stockValue = float(item[1]) * float(item[2])
        # add stockValue to totalValueOfStock
        totalValueOfStock += stockValue
        print(f"{item[0]} has a total value of £{stockValue:.2f}")
    print(f"\nTotal value of stock is £{totalValueOfStock:.2f}")
    input("\n Press Enter to return to menu")

# Show all stock items
def showAllStock(combinedList):
    os.system('cls')
    print("Show all Stock with Quantity")
    print("----------------------------\n")
    # Loop around items in list
    # displaying each item
    for item in combinedList:
        print(f"{item[0]} has a quantity of {item[1]}")
    input("\n Press Enter to return to menu")        

# Show stock amount < 30
def showLessThan30(combinedList):
    os.system('cls')
    print("Show all Stock Less Than 30")
    print("---------------------------\n")
    # Loop around items in list
    for item in combinedList:
        # if amount is < 30 print item
        if int(item[1]) < 30:
            print(f"{item[0]} has a quantity of {item[1]}")
    input("\n Press Enter to return to menu")      

# Show the average cost of all items
def average(combinedList):
    os.system('cls')
    print("Show average cost")
    print("-----------------\n")
    count = 0 # variable to count the number of items in list
    totalCost = 0 # variable to store running cost of all items
    for item in combinedList:
        # Add cost to running total
        totalCost =+ float(item[2])
        # Add one to count
        count =+ 1
    # work out the average cost
    average = totalCost / count
    print(f"Average cost is £{average:.2f}")
    input("\n Press Enter to return to menu") 

# Show the maximum cost item
def maximum(combinedList):
    os.system('cls')
    print("Show maximum cost")
    print("-----------------\n")
    maxCost = float(combinedList[0][2])
    itemName = combinedList[0][0]
    for item in combinedList:
        # check if next item is greater than maxCost
        if maxCost < float(item[2]):
            # maxCost = next item
            maxCost = float(item[2])
            # move item name to variable
            itemName = item[0]
    print(f"{itemName} has the Maximum cost of {maxCost}")
    input("\n Press Enter to return to menu")   

def minimum(combinedList):
    os.system('cls')
    print("Show minimum cost")
    print("-----------------\n")
    minCost = float(combinedList[0][2])
    itemName = combinedList[0][0]
    for item in combinedList:
        # check if next item is less than minCost
        if minCost > float(item[2]):
            # minCost = next item
            minCost = float(item[2])
            # move item name to variable
            itemName = item[0]
    print(f"{itemName} has the Minimum cost of {minCost}")
    input("\n Press Enter to return to menu")  

# Call menu() function
menu()