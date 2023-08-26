import csv
import pandas

df = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# use value_counts() to calculate each color's amounts
category_counts = df["Primary Fur Color"].value_counts()

# transform the color and counts into new DataFrame
new_df = pandas.DataFrame({'Fur Color': category_counts.index, 'Counts': category_counts.values})

# transform to csv
new_df.to_csv("squirrel_count.csv")

print(new_df)




