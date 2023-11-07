hours = input("Enter hours: ")
rate = input("Enter rate: ")
fHours = float(hours)
fRate = float(rate)
# print(fHours, fRate)
if fHours > 40:
    # print("Overtime")
    reg = fRate * fHours
    otp = (fHours - 40.0) * (fRate * 0.5)
    # print(reg, otp)
    pay = reg + otp
else:
    print("Regular")
    pay = fHours * fRate
print("Pay:", pay)
