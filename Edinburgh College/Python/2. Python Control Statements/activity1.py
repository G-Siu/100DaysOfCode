# Control statements

# Get first number
first_number = int(input("Enter first number: "))

# Get second number
second_number = int(input("Enter second number: "))

# Get third number
third_number = int(input("Enter third number: "))

if first_number == second_number and first_number == third_number:
    print("All numbers are equal.")
elif (first_number != second_number and first_number != third_number and
      second_number != third_number):
    print("All numbers are different.")
else:
    print("Neither all are equal or different.")