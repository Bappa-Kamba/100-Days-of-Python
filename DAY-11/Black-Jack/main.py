from art import logo
import random
from os import name, system


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
blackjack_hand = [10, 11]
user_hand = []
dealer = []


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def deal_card():
    return random.choice(cards)


def add_cards(card_list):
    total = sum(card_list)
    if [10, 11] in card_list or [11, 10] in card_list:
        return 0

    if (total > 21) and (11 in card_list):
        card_list[card_list.index(11)] = 1
        total = sum(card_list)

    return total


def prompt():
    response = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    return response

def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "It is a tie!"
    elif user_score == 0:
        return "User wins"
    elif dealer_score == 0:
        return "User lose"
    elif user_score > 21:
        return "User lose"
    elif dealer_score > 21:
        return "User wins"
    else:
        if user_score > dealer_score:
            return "User wins"
        else:
            return "User lose"

def blackjack():
    res = prompt()

    if res == 'y':
        print(logo)

        user_hand.append(deal_card())
        user_hand.append(deal_card())
        dealer.append(deal_card())
        dealer.append(deal_card())

        user_score = add_cards(user_hand)
        dealer_score = add_cards(dealer)

        print(f"{user_hand} - {user_score}")
        print(dealer[0])

        is_over = False
        while not is_over:
            if user_score == 0 or dealer_score == 0 or user_score > 21:
                is_over = True
                
                print(f"{user_hand} - {user_score}")
                print(f"{dealer} - {dealer_score}")
                print("You lose.")

            else:
                if input("Hit or Stand? ").lower() == "hit":
                    user_hand.append(deal_card())
                    user_score = add_cards(user_hand)
                    print(f"{user_hand} - {user_score}")
                    print(dealer[0])
                else:
                    while dealer_score < 17:
                        dealer.append(deal_card())
                        dealer_score = add_cards(dealer)
                    print(compare(user_score, dealer_score))
                    print(f"{user_hand} - {user_score}")
                    print(f"{dealer} - {dealer_score}")
                    is_over = True
    else:
        print("Goodbye!")

blackjack()
play_again = True
while play_again:
    response = input("Do you want to play again? "). lower()
    if response == 'yes':
        clear()
        user_hand = []
        dealer = []
        blackjack()
    else: 
        play_again = False
    


