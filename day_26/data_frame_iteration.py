

student_dict = {
	"student": ["Angela", "Sergio", "James", "Lily"],
	"score": [56, 75, 76, 98]
}
#
# for (key, value) in student_dict.items():
# 	print(key)
# 	print(value)
	
import pandas
print(type(student_dict))
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
print((type(student_data_frame)))

# for key, value in student_data_frame.items():
# 	print(key)
# 	print(value)
	
print("++++++++++")

for index, row in student_data_frame.iterrows():
	if row.student == "Sergio":
		print(row.student)
		print(row.score)
	