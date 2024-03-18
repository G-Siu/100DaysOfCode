# Ticket cost Revision Exercise
# Date: 07 Dec 2023
# Name: G Siu
# Calculate total cost of tickets

# Ask how many tickets wanted
tickets = int(input("How many tickets would you like: "))
# Calculate cost of tickets
cost = tickets * 19.99
# Display cost of tickets
print(f"Total cost comes to £{"{0:.2f}".format(cost)} for {tickets} tickets")
