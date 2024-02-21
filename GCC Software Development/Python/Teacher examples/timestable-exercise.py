# ask user to enter their times table
# for loop using range 0 to 10
#    print table * range

table = int(input("Enter the times table you want to display : "))
for x in range(20) :
    if x == 5 :
        continue
    print(f"{table} x {x} = {table * x}")