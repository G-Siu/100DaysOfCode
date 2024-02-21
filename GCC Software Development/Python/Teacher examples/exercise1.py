#prompt user to enter type of pet
#if dog then 10pcm
#else if cat then 10pcm
#else 25pcm

# Logical Operators

# and = True if both conditions are true
# or = True if one of the conditions is true


insurance = input("Please enter type of pet : ").lower()
if insurance == "dog" or insurance == "cat" :
    print("£10pcm")
else:
    print("£25pcm")
