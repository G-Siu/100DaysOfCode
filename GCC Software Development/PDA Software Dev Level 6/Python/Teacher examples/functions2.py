# Passing Data to Functions

# Global Variable
vatRate = 20

def CalculateVAT(rate):
    sales = int(input("Enter sales : "))
    vat = (sales / 100) * rate
    return vat

print(CalculateVAT(vatRate))
