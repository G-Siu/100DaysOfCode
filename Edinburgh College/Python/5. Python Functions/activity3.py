# Function to check prime numbers
def prime_number(number):
    # Check if valid number
    if number < 1:
        return "Invalid number"
    elif number == 1:
        return "Not prime number as only one factor"
    # Loop through numbers
    for integer in range(2, number):
        # Check if remainder
        if number % integer == 0:
            return "Not prime number"
        else:
            return "Prime number"


# Get user input
user_number = int(input("Enter number: "))
# Call function and print result
print(prime_number(user_number))
