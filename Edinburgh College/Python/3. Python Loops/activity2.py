# Multiplication table

# Get number from user
user_number = int(input("Enter number for multiplication table: "))

# Loop for up to 10 times table
for number in range(1, 11):
    print("%d x %d = %d" % (user_number, number, user_number * number))
