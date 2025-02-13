import pandas as pd

sq_data=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250128.csv")

fur_colors= sq_data["Primary Fur Color"]
distinct_colors= fur_colors.value_counts()

print(distinct_colors)
distinct_colors.to_csv("data_out.csv")


