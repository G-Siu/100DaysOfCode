# Factorial from function

# Function to get factorial
def factorial(number):
    # Initialise total variable
    total = 1
    # Check if number is 0
    if number == 0:
        return 1
    # Check if number is less than 0
    elif number < 0:
        return "Invalid number"
    # Loop from 1 to user number
    for integer in range(1, number + 1):
        # Multiply current number per iteration
        total *= integer
    return total


# Get number from user
user_number = int(input("Enter number: "))
# Get the returned value from function with user input parameter
factorial_number = factorial(user_number)
# Check if the value returned is string
if type(factorial_number) is str:
    print(factorial_number)
# If not, then print factorial as normal
else:
    print(f"Factorial of {user_number} is {factorial_number}")