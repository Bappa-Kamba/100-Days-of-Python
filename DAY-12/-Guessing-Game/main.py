import random

actual_number = random.randint(1, 101)
print(actual_number)
turns = 0

# Number Guessing Game Objectives:

# Include an ASCII art logo.
print("logo\n")

retry = True
while retry:
    game_mode = input(
        "Choose a game mode. ['Easy' or 'Hard']? ").lower()
    if game_mode == "easy":
        turns = 10
        retry = False
    elif game_mode == "hard":
        turns = 5
        retry = False
    else:
        print("Sorry wrong input. Try 'Easy' or 'Hard'")


# Allow the player to submit a guess for a number between 1 and 100.

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
is_over = False
while not is_over and turns != 0:
    user_guess = int(input("Submit a guess from 1 - 100: "))

    if user_guess > actual_number:
        print("Too high.")
        turns -= 1
    elif user_guess < actual_number:
        print("Too low.")
        turns -= 1
    else:
        print(f"You're correct. The number is {actual_number}")
        is_over = True

if turns == 0:
    print("You've run out of tries. Try your luck next time.")
    is_over = True

# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
