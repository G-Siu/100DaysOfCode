months = ("January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December")
# print(months[2])

tuple1 = (1, 2, 3)
tuple2 = (4, 5 ,6)
new_tuple = tuple1 + tuple2
# print(new_tuple)

tuple_to_unpack = (1, 2, 3, 4)
one, two, three, four = tuple_to_unpack
# print(one, two, three, four)


def add(numbers):
    return sum(numbers)


numbers = (1, 2, 3, 4, 5)
print(add(numbers))