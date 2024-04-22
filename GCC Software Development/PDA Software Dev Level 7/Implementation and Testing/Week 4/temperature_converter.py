# Temperature conversion
# Name: G Siu
# Date: 18th April 2024
# Date modified: 18th April 2024

def convert_temperatures(celsius_list):
    fahrenheit = lambda c: (c * 9/5) + 32
    fahrenheit_temperatures = map(fahrenheit, celsius_list)
    return celsius_list, list(fahrenheit_temperatures)


celsius_list = [0, 5, 15, 23, 30]
celsius, fahrenheit = convert_temperatures(celsius_list)
print(f"Celsius temperatures - {celsius}\n"
      f"Fahrenheit temperatures - {fahrenheit}")