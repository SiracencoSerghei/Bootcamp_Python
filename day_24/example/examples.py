# file = open("my_text.txt")
# content = file.readline()
# content2 = file.readline()
# content3 = file.readline()
# print(f"{content = }")
# print(f"{content2 = }")
# print(f"{content3 = }")
# file.close()

with open("my_text.txt") as file:  # "r" by default
	for line_num, line in enumerate(file, start=1):
		print(line_num, line)
		
		
new_text = input("Input some text, please... ")

with open("my_text.txt", "a+") as file:  # "w" rewrite all in file
	file.write(f"\n{new_text}")