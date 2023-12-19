# Task - euro, pound conversion
# Date: 19th Dec 2023
# Name: G Siu

# Ask if to convert Pounds or Euro
currency = input("Convert Pounds or Euros: ").lower()
# Ask for amount to convert
amount = int(input("Enter amount to convert: "))
# Calculate conversion
if currency == "pounds":
    print(f"£{amount} converted to Euros = € {(amount * 0.87):.2f}")
elif currency == "euros":
    print(f"€{amount} converted to Pounds = £ {(amount * 1.14):.2f}")
