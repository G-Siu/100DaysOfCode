import re

name = input("Enter file: ")
if name == "0":
    name = "regex_sum_42.txt"
elif name == "1":
    name = "regex_sum_1915208.txt"

num_list = list()
with open(name) as file:
    numbers = re.findall("[0-9]+", file.read())
    for n in numbers:
        num_list.append(int(n))
    print(sum(num_list))
