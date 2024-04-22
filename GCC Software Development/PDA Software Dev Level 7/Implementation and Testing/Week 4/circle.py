# Area and Circumference Calculator
# Name: G Siu
# Date: 18th April 2024
# Date modified: 18th April 2024

import math


def calculate_area_circumference(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference


print(calculate_area_circumference(4))
