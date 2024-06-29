#
#
# with open("weather_data.csv") as df:
# 	data = df.readlines()
# 	print(type(data))
# 	print(data)
# 	new_data = []
# 	for line in data:
# 		line = tuple(line.strip().split(","))
# 		print(line)
# 		new_data.append(line)
# 	data = new_data
# 	print(type(data))
# 	print(data)

import csv

import pandas

with open("weather_data.csv") as df:
    # print("Use built-in csv")
    # data = csv.reader(df)
    # print(type(data))
    # print(data)
    # temperature = []
    # for row in data:
    # 	print(row)
    # 	if row[1] != "temp":
    # 		temperature.append(int(row[1]))
    # print(temperature)

    print("Use pandas")
    data = pandas.read_csv("weather_data.csv")
    print("type")
    print(type(data))

    print(data)
    print(data["temp"][1])

    print("dict")
    data_dict = data.to_dict()
    print(data_dict)

    print("list")
    temp_list = data["temp"].to_list()
    print(temp_list)
    print(len(temp_list))

    print(data["temp"].mean())
    print(data["temp"].max())

    # Get Data in Columns
    print("Get Data in Columns")
    print(data["condition"])
    print(data.condition)

    # Get Data in Row
    print("Get Data in Row")
    print(f"  {str(data[data.day == 'Monday']) = }  ")
    print(data[data.day == "Monday"])
    print(data[data.temp == data.temp.max()])

    # # Get Row data value
    # monday = data[data.day == "Monday"]
    # # monday_temp = int(monday.temp)  # FutureWarning: Calling int on a single element Series is deprecated and will raise a TypeError in the future. Use int(ser.iloc[0]) instead
    # #   monday_temp = int(monday.temp)
    # monday_temp = int(monday.temp.iloc[0])
    # monday_temp_F = monday_temp * 9 / 5 + 32
    # print(monday_temp_F)
    #
    # # Create a dataframe from scratch
    # data_dict = {
    # 	"students": ["Amy", "James", "Angela"],
    # 	"scores": [76, 56, 65]
    # }
    # data = pandas.DataFrame(data_dict)
    # data.to_csv("new_data.csv")
    #
    # # Central Park Squirrel Data Analysis
    # import pandas
    #
    # data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    # grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
    # red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
    # black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
    # print(f"{grey_squirrels_count = }")
    # print(f"{red_squirrels_count = }")
    # print(f"{black_squirrels_count = }")
    #
    # data_dict = {
    # 	"Fur Color": ["Gray", "Cinnamon", "Black"],
    # 	"Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count],
    # 	"Count2": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
    # 	# "Count2": [grey_squirrels_count, red_squirrels_count, black_squirrels_count, "hahaha"]  # ValueError: All arrays must be of the same length
    # }
    #
    # df = pandas.DataFrame(data_dict)
    # print(df)
    # df.to_csv("squirrel_count.csv")
    #
    #
