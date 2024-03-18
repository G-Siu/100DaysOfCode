age = int(input("Enter your age: "))

if age >= 17:
    licence = input("Do you have a licence : ").lower()
    if licence == "yes" :
        print("You are eligible to drive a car.")
    else:
        print("Sorry, you need a licence to drive.")
else:
    print("You are not old enough to drive.")