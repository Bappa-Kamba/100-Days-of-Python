from art import logo, vs
from game_data import data
from random import choice
from os import name, system

SCORE = 0

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# extract variables from data which is a list of dictionaries
def get_random_item(list_to_populate):
    
    if len(list_to_populate) < 1:
        for i in range(2):
            item = choice(data)
            if item in list_to_populate:
                i -= 1
            else:
                list_to_populate.append(item)
        return list_to_populate
    else:
        for i in range(1):
            item = choice(data)
            if item in list_to_populate:
                i -= 1
            else:
                list_to_populate.append(item)
                return list_to_populate
            

empty_list = []
account_list = get_random_item(empty_list)


def compare(user_choice, second_choice):
    global SCORE
    if user_choice > second_choice:
        SCORE += 1 
        return True
    else:
        return False

# print logo
print(logo)

def play_game():
    choice_A = account_list[0]
    choice_B = account_list[1]

    print(
        f"Compare A: {choice_A['name']}, a(n) {choice_A['description']}, from {choice_A['country']}.")

    # print vs
    print(vs)

    # print compare statement
    print(
        f"Against B: {choice_B['name']}, a(n) {choice_B['description']}, from {choice_B['country']}.")

    count_for_A = int(choice_A['follower_count'])
    count_for_B = int(choice_B['follower_count'])

    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_input == 'a':
        if compare(count_for_A, count_for_B) == 1:
            return 0
        else:
            return -1

    elif user_input == 'b':
        if compare(count_for_B, count_for_A) == 1:
            return 0
        else:
            print("You're wrong.")
            return -1

is_over = False
while not is_over:
    if play_game() == -1:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {SCORE}")
        is_over = True
    else:
        clear()
        account_list.pop(0)
        account_list = get_random_item(account_list)
        print(logo)
        print(f"You're right! Current score: {SCORE}.")
