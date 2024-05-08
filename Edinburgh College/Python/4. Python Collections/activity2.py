# Average of list

# Sample list
sample_list = [20, 30, 25, 35, -16, 60, -100]

# Initialise total
total = 0

# Loop through list
for number in sample_list:
    total += number  # Add number to total

# Get average
average = total / len(sample_list)

print("Average value of the list elements is:", round(average, 1))
