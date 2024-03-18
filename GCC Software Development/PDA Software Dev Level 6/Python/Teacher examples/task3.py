# Task 3 and 4 Example
# For this example I am going to ask the user to enter two numbers
# i will then calculate the sum of those two numbers
# 
# I writing this app I will use functions and pass data between them
# I will also use comments to describe the statements and
# meaningful variable names

# Author : Paul Dorman
# Date : 30th Jan 2024
# Description : Calculate Two Numbers

# This function prompts the user to enter two numbers
# it then passes these two numbers to calculateSum
# and then passes the result to displaySum
def inputNumbers(): 
    num1 = -1
    num2 = -1
    while num1 < 0 or num1 > 100: # validate num1
        num1 = int(input("Please enter first number : "))  # num1 = 10
    while num2 < 0 or num2 > 100: # validate num2
        num2 = int(input("Please enter second number : ")) # num2 = 10
    sum = calculateSum(num1, num2)  # pass num1, num2 (10, 10)
    # sum will recieve the value 20
    displaySum(sum) # pass 20

# This function recieves the two numbers from inputNumbers and
# calculates the sum, returning the value back to inputNumbers
def calculateSum(num1, num2):
    sum = num1 + num2  # sum = 20
    return sum  # return 20

# This function will recieve the sum from the inputNumbers function
# and display the result
def displaySum(sum):
    print(sum) # print 20


inputNumbers()
