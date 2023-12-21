def computepay(h, r):
    # print("In computepay", h, r)
    if h > 40:
        reg = r * h
        otp = (h - 40.0) * (r * 0.5)
        p = reg + otp
    else:
        p = h * r
        # print("Returning", p)
        return p


hours = input("Enter hours: ")
rate = input("Enter rate: ")
fHours = float(hours)
fRate = float(rate)
pay = computepay(fHours, fRate)

print("Pay:", pay)
