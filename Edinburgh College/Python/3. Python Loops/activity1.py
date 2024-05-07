# Fibonacci
fibonacci = [0, 1]

# Loop from 1 to 50
for index in range(1, 51):
    # Get next number in Fibonacci
    add_numbers = fibonacci[index] + fibonacci[index - 1]
    fibonacci.append(add_numbers)  # add new number to list

print(fibonacci)