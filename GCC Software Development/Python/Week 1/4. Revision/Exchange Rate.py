# Exchange Rate Revision Exercise
# Date: 07 Dec 2023
# Name: G Siu
# Calculate exchange rate from GBP to Euro

# Ask how much to convert to Euro
pounds = float(input("How much GBP would you like to convert to Euro: £"))
# Calculate Euro
euro = pounds * 1.16
# Display Euro converted from pounds
print(f"£{"{0:.2f}".format(pounds)} exchanges for €{"{0:.2f}".format(euro)}")
