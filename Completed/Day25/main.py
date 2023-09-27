# Comma Separated Values

# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

import pandas
#
data = pandas.read_csv("weather_data.csv")
# print(data["temp"])  # Takes the "temp" header and prints the values under that column

# data_dict = data.to_dict()  # Change to dictionary
#
# temp_list = data["temp"].to_list()  # Much easier method using pandas to creating list of temp values than csv method
# print(temp_list)
#
# print(data["temp"].mean())  # Calculate average
#
# print(data["temp"].max())
#
# # Get data in columns
# print(data["condition"])  # Prints condition column values
# print(data.condition)  # Does the same as pandas automatically creates attributes from the headings

# Get data in row
# print(data[data.day == "Monday"])  # Print row with Monday
# print(data[data.temp == data.temp.max()])  # Print row with max temp

monday = data[data.day == "Monday"]  # Assign Monday row to monday
# # print(monday.condition)  # Print the condition from the monday row
monday_temp = monday.temp[0]
print(monday.temp)
# monday_temp_F = (monday_temp * 9/5) + 32
# print(monday_temp_F)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)  # Convert the manual generated dictionary into DataFrame
# data.to_csv("new_data.csv")  # Convert that DataFrame into csv and save into new_data.csv (created if non-existent)
