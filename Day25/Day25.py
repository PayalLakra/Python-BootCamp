'''
Topics to be covered:
- Data read from CSV
- Data Frames
- U.S. States game
'''

import csv

with open("Day25\weather_data.csv","r") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        print(row)

#Pandas - to perform data analysis on tabular data

import pandas

data = pandas.read_csv("Day25\weather_data.csv")
print(data)