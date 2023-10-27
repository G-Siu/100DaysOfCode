def computepay(h, r):
    if h > 40:
        overtime = h - 40
        over_pay = overtime * (r * 1.5)
        pay = 40 * r + over_pay
    return str(pay)

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
p = computepay(hrs, rate)
print("Pay", p)