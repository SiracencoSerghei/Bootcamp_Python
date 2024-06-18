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

with open('weather_data.csv') as df:
	data = csv.reader(df)
	print(data)
	temperature = []
	for row in data:
		print(row)
		if row[1] != "temp":
			temperature.append(int(row[1]))
	print(temperature)
	