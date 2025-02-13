import csv
import pandas

# with open("weather_data.csv","r") as data_file:
#     data = csv.reader(data_file)
#     tempratures=[]
#     index=0
#     for row in data:
#         if index >0:
#             tempratures.append(int(row[1]))
#         index+=1
#
#     print(tempratures)

data2 = pandas.read_csv("weather_data.csv")
print(data2)
print(data2["temp"])

data_dict=data2.to_dict()
print(data_dict)

temp_list= data2["temp"].to_list()
temp_total=sum(temp_list)
print(f"Average Temperature: {temp_total/len(temp_list)}")

#using pandas
print(f"Average using pandas series: {data2["temp"].mean()}")
print(f"Max using pandas series: {data2["temp"].max()}")

#Get Data in Row where Day is Monday
print(data2[data2.day == "Monday"]) #object approach
print(data2[data2["day"] == "Monday"]) # dictionary approach

#Get Data in Row where temp is max
max_temp=data2["temp"].max()
print(data2[data2.temp == max_temp])
print(data2[data2.temp == data2.temp.max()])



