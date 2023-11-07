hours = input("Enter hours: ")
rate = input("Enter rate: ")
try:
    fHours = float(hours)
    fRate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()
if fHours > 40:
    reg = fRate * fHours
    otp = (fHours - 40.0) * (fRate * 0.5)
    pay = reg + otp
else:
    print("Regular")
    pay = fHours * fRate
print("Pay:", pay)
