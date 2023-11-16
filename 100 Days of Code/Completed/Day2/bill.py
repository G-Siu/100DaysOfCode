# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

bill = input("What was the total bill? ")
per_tip = input("Tip 10, 12, or 15%? ")
tip = (int(per_tip) / 100) + 1
people = input("Number of people to split the bill? ")
cost_per_person = round((float(bill) / int(people)) * tip, 2)
print(f"{cost_per_person:.2f}")
