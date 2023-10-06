# def add(*args):  # *args places elements into tuple
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(1, 2, 3, 9))

# def calculate(n, **kwargs):  # keyword arguments
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs)
    # print(kwargs["add"])
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")  # get allows this attribute to be optional
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.make)
