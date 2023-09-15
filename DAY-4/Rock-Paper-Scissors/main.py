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
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
options = [rock, paper, scissors]
print(options[user_choice])

print("\n*********************************")
print("*********************************\n")
computer_choice = random.randint(0, 2)
print(f"Computer chooses:\n{options[computer_choice]}")

if (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) \
        or (user_choice == 2 and computer_choice == 1):
    print("You win!")
elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2)\
        or (user_choice == 2 and computer_choice == 0):
    print("You lose!")
else:
    print("You drew.")
