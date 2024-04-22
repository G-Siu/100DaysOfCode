# List statistics
# Name: G Siu
# Date: 18th April 2024
# Date modified: 18th April 2024

numbers = [1, 2, 3, 4, 5]
square = lambda x: x ** 2
squared_numbers = map(square, numbers)
list_numbers = list(squared_numbers)
minimum = min(list_numbers)
maximum = max(list_numbers)

print(f"Original list - {numbers}\n"
      f"Squared numbers - {list_numbers}\n"
      f"Minimum value - {minimum}\n"
      f"Maximum value - {maximum}")
