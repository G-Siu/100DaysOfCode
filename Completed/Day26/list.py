# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
#
# name = "Gary"
# new_list = [letter for letter in name]
#
# range_list = [n * 2 for n in range(1, 5)]
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# cap_names = [name.upper() for name in names if len(name) > 5]

student_dict = {
    "student": ["Harry", "Ron", "Hermoine"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
    # print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Hermoine":
        print(row.score)
