'''
Topics to be covered:
- Data read from CSV
- Data Frames
- U.S. States game
'''

# import csv

# with open("Day25\weather_data.csv","r") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         print(row)

# #Pandas - to perform data analysis on tabular data

# import pandas

# data = pandas.read_csv("Day25\weather_data.csv")
# print(data)

# # Primary Data Strucutres of Pandas- 
# # Series: Every single column is a Series, 
# # DataFrames: A DataFrame is kind of the equivalent of your whole table.

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["TEMPERATURE"].to_list()
# print(temp_list)

# average = sum(temp_list) / len(temp_list)
# print(average)

# # OR
# print(data["TEMPERATURE"].mean())
# print(data["TEMPERATURE"].max())

# # Get Data in Columns
# print(data["CONDITION"])
# print(data.CONDITION)

# # Get Data in Rows
# print(data[data.DAY == "Monday"])
# data.TEMPERATURE == (data["TEMPERATURE"].max())

# monday = data[data.DAY =="Monday"]
# print(monday.CONDITION)

# #Converting into Fahrenheit
# monday_temp = monday.TEMPERATURE[0]
# monday_temp_in_f = monday_temp * 9/5 + 32
# print(monday_temp_in_f)

# # Create a DataFrame from scratch
# data_dict = {"students" : ["A","B","C"], "scores" :[10,20,30]}

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")   # To convert DF into CSV


# TASK- Find the total gray,cinnamon,black colour squirrels  from the csv data provided and stored them in a separate csv file.
import pandas

data = pandas.read_csv("Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
GRAY = len(data[data["Primary Fur Color"] == "Gray"])
print(GRAY)

Cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(Cinnamon)

Black = len(data[data["Primary Fur Color"] == "Black"])
print(Black)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [GRAY, Cinnamon, Black]
}

data = pandas.DataFrame(data_dict)
data.to_csv("Day25/squirrel_count.csv")