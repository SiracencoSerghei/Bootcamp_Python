import random

from clear import clear
from art import logo, vs
from game_data import data

#
# def main():
# 	compare_A = random.choice(data)
# 	print(compare_A)
# 	is_game_over = False
# 	current_score = 0
# 	print(logo)
#
# 	while not is_game_over:
# 		remaining_data = [item for item in data if item != compare_A]
# 		against_B = random.choice(remaining_data)
# 		print(f"Compare A: {compare_A["name"]}, a {compare_A["description"]}, from {compare_A["country"]}.")
# 		print(vs)
# 		print(f"Against B: {against_B["name"]}, a {against_B["description"]}, from {against_B["country"]}.")
# 		response = input("Who has more followers? Type 'A' or 'B': ")
# 		if (compare_A['follower_count'] > against_B['follower_count'] and response == 'A') or (compare_A['follower_count'] < against_B['follower_count'] and response == 'B'):
# 			current_score += 1
# 			compare_A = against_B
# 		elif (compare_A['follower_count'] < against_B['follower_count'] and response == 'A') or (compare_A['follower_count'] > against_B['follower_count'] and response == 'B'):
# 			clear()
# 			print(logo)
# 			print(f"Sorry, that's wrong. Final score: {current_score}")
# 			is_game_over = True
# 			break
# 		else:
# 			print("Uups, something wrong happened!?")
# 		clear()
# 		print(logo)
# 		print(f"You're right! Current score: {current_score}.")
#
# main()

def get_random_account():
	"""Get data from random account"""
	return random.choice(data)

def format_data(account):
	"""Format account data into printable format: name, description, country"""
	name = account['name']
	description = account['description']
	country = account['country']
	return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
	"""Check followers against user's guess
	and return True if they got it right.
	Or False if they got it wrong."""
	if a_followers > b_followers:
		return guess == "a"
	else:
		return guess == "b"
	
def game():
	"""Principale logic of game"""
	print(logo)
	score = 0
	game_should_continue = True
	account_a = get_random_account()
	account_b = get_random_account()
	
	while game_should_continue:
		account_a = account_b
		account_b = get_random_account()
		if account_a == account_b:
			while account_a == account_b:
				account_b = get_random_account()
		print(f"Compare A: {format_data(account_a)}.")
		print(vs)
		print(f"Against B: {format_data(account_b)}.")
		
		guess = input("Who has more followers? Type 'A' or 'B': ").lower()
		a_follower_count = account_a["follower_count"]
		b_follower_count = account_b["follower_count"]
		is_correct = check_answer(guess, a_follower_count, b_follower_count)
	
		clear()
		print(logo)
		if is_correct:
			score += 1
			print(f"You're right! Current score: {score}.")
		else:
			game_should_continue = False
			print(f"Sorry, that's wrong. Final score: {score}")

game()
	