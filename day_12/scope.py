################### Scope ####################

enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

#  local scope
#
# def drink_potion():
# 	potion_strength = 2
# 	print(potion_strength)
# drink_potion()
# print(potion_strength)

# global scope
#
# player_health = 10
# def game():
# 	def drink_potion():
# 		potion_strength = 2
# 		print(player_health)
# 	drink_potion()
#
# game()
# print(player_health)


# There is NO block scope
#
# game_level = 3
# def create_enemy():
# 	enemies = ['Skeleton', "Zombie", "Alien"]
#
# 	if game_level < 5:
# 		new_enemy = enemies[0]
#
# 	print(new_enemy)

# Modifying Global Scope

# def increase_enemies():
#   global enemies
#   enemies += 1
#   print(f"enemies inside function: {enemies}")


# def increase_enemies():
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")
def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")


# Global constant

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"
