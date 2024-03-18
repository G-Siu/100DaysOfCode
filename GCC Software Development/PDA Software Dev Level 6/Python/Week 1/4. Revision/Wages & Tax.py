# Wages & Tax Revision Exercise
# Date: 07 Dec 2023
# Name: G Siu

# Ask for name
name = input("Please enter your name: ")
# Ask for hours worked
hours = int(input("Please enter your hours: "))
# Ask for pay rate
rate = float(input("Please enter your pay rate: "))
# Calculate wages
wages = hours * rate
# Calculate tax
tax = wages * 20 / 100
# Calculate take home pay
net_pay = wages - tax
# Display message with take home pay
print(name + f", your take home pay comes to: £{"{0:.2f}".format(net_pay)} "
             f"({"{0:.2f}".format(wages)} - {"{0:.2f}".format(tax)})")
