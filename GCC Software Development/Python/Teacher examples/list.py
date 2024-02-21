# Lists

# List containing strings
names = ['Paul','Jimmy','Betty','Toni','Millie']

# List containing integers
numbers = [10, 50, 25, 35, 6]

# List of different data types
mixed = ['Paul', 51, True]

# Access list value using index
print(names[3]) # This would print Toni

print(numbers[3]) # This would print 40

print(mixed[1]) # This would print 51

# Iterate (loop) through list

for name in names:
    print(name) # This will print all values in the names list

max = numbers[0]
min = numbers[0]
count = 0
total = 0

for number in numbers:
    # Find the maximum number within list
    if number > max:
        max = number
    
    # Find the lowest number in the list
    if number < min:
        min = number

    count += 1

    total += number

average = total / count

print(f"There are {count} elements in the list")
print(f"Highest number in list is {max}")
print(f"Lowest number in list is {min}")
print(f"Total value of elements in list is {total}")
print(f"The average value of list is {total / count}")


# Change value in list
numbers[0] = 99
print(numbers[0])

# Combine Lists

namesAndNumber = zip(names, numbers, mixed)
for item in namesAndNumber:
    print(f"{item[0]} {item[1]} {item[2]}")