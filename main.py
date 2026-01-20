# import csv
#
# with open("weather_data.csv") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     # weather_data = list(csv_reader)
#     # print(weather_data)
#     temperatures = []
#     for row in csv_reader:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
#
# print(data_dict)
#
# temp_list = data["temp"].values.tolist()
# print(len(temp_list))
# print(temp_list)
#
# print(data["temp"].mean())
#
# #Get a column
# print(data["condition"])
# print(data.condition)

#Get a row
print(data[data.day == "Monday"])



