import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
random_choice = random.randint(0,2)
variants = [rock, paper, scissors]
computer_variant = variants[random_choice]

# Prompt the user for their choice, ensuring it is valid
while True:
    try:
        personal_choice = int(
            input(
                "What is your choice? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"
            )
        )
        if personal_choice in [0, 1, 2]:
            break
        else:
            print("Invalid choice. Please enter 0, 1, or 2.")
    except ValueError:
        print("Invalid input. Please enter a number.")

personal_variant = variants[personal_choice]
print(personal_variant)
print("Computer chose:")
print(computer_variant)
# if personal_choise == random_choice:
# 	print("the match ended in a draw")
# elif (personal_choise == 0 and random_choice == 2) or (personal_choise == 1 and random_choice == 0) or (personal_choise == 2 and random_choice == 1):
#     print("You won!")
# else:
#     print("You lost!")


# List of winning combinations (player_choice, computer_choice)
winning_combinations = [(0, 2), (1, 0), (2, 1)]
# Determine the result
if personal_choice == random_choice:
    print("The match ended in a draw.")
elif (personal_choice, random_choice) in winning_combinations:
    print("You win!")
else:
    print("You lose!")
