# Scope

# Global Variable
vatRate = 20

def CalculateVAT():
    global vatRate
    sales = int(input("Please enter total sales : "))
    vat = (sales / 100) * vatRate # Local Variable
    print(vat)


CalculateVAT()