import csv
import pandas

with open("weather_data.csv") as file:
    data = csv.reader(file)
    next(data)  # skip the first line
    temperature = []
    for row in data:
        temperature.append(int(row[1]))

    print(temperature)
