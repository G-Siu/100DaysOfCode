# Choose Arithmetic operator
# Date: 13 Dec 2023
# Name: G Siu

# Get two numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Ask whether to add or subtract
operand = input("Would you like to '+' or '-' : ")

# Condition dependent on operand chosen
if operand == "+":
    print(num1, "+", num2, "=", num1 + num2)
elif operand == "-":
    print(num1, "-", num2, "=", num1 - num2)
