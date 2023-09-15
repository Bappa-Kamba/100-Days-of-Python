from os import system, name
from art import logo
# HINT: You can call clear() to clear the output in the console.


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def main():
    print(logo)
    print("Welcome to the secret auction program.")

    more_bidders = True
    bidders = {}
    while more_bidders:
        user_name = input("What is your name?: ")
        user_bid = float(input("What's your bid?: $"))
        bidders[user_name] = user_bid
        next_bid = input("Are there any other bidders? Type 'yes' or 'no'. ")
        if next_bid == 'no':
            more_bidders = False
            for key in bidders:
                max_bid = 0
                if bidders[key] > max_bid:
                    max_bid = bidders[key]
            print(f"The winner is {key} with a bid of ${bidders[key]}")
        else:
            clear()
main()