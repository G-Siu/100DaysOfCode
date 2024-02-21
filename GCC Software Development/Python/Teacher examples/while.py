#count = 0

#while count < 5:
#    print(f"Count is {count}")
#    count += 1

# Using continue and break in a while loop to find the first even number greater than 5
num = 1

while num <= 10:
    if num <= 5:
        num += 1
        continue  # Skip numbers less than or equal to 5
    if num % 2 == 0:
        print(f"The first even number greater than 5 is {num}")
        break  # Exit the loop when the first even number greater than 5 is found
    num += 1