# Control statements

# Get first number
first_number = int(input("Enter first number: "))

# Get second number
second_number = int(input("Enter second number: "))

# Get third number
third_number = int(input("Enter third number: "))

if third_number > second_number > first_number:
    print("Increasing order")
elif third_number < second_number < first_number:
    print("Decreasing order")
else:
    print("Neither increasing or decreasing order")