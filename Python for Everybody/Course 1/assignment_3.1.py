hrs = input("Enter Hours:")
h = float(hrs)
rate = float(input("Enter Rate:"))
if h > 40:
    overtime = h - 40
    over_pay = overtime * (rate * 1.5)
    pay = 40 * rate
    total = over_pay + pay
    print(total)