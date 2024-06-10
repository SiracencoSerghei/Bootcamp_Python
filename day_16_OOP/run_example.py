import another_module
print(another_module.another_variable)
#
# import turtle
# tinny = turtle.Turtle()
# print(tinny)
# tinny.shape("turtle")
# tinny.color("coral")
# tinny.forward(100)
#
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
# table.field_names = ["Pokemon Name", "Type"]
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Squirtle", "Water"])
# table.add_row(["Charmander", "Fire"])

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander",], "l")
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
table.align["Type"] = "r"
print(table)
