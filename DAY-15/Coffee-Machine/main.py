MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins_inserted = {
    "quaters" : {
        "value" : .25 ,
        "amount" : 0,
    },
    "dimes" : {
        "value" : 0.10 ,
        "amount" : 0,
    },
    "nickles" : {
        "value" : 0.05 ,
        "amount" : 0,
    },
    "pennies" : {
        "value" : 0.01 ,
        "amount" : 0,
    },
}

cash_register = 0

def report():
    '''Prints a report of the current resources available'''
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${cash_register}")

def check_resources(user_input, drink):
    '''Checks whether resources are enough for the drink'''
    for resource in drink['ingredients']:
        if resource == 'milk' and user_input == 'espresso':
            drink['ingredients']['milk'] = 0
        if resources[resource] < drink['ingredients'][resource]:
            return resource
    return True

def make_drink(user_input, drink):
    '''Makes a drink from the menu'''
    global cash_register
    cash_register += drink['cost']

    for resource in resources:
        resources[resource] -= drink['ingredients'][resource]
    return f'Here is your {user_input} ☕️. Enjoy!'

def pay(drink):
    ''' Calculates coins inserted and returns `success` or `failed` '''
    print("Please insert coins.")
    coins_in_dollars = 0
    for coin in coins_inserted:
        coins_inserted[coin]["amount"] = int(input(f"How many {coin}? "))
        coins_in_dollars += coins_inserted[coin]['amount'] * \
            coins_inserted[coin]['value']
    if coins_in_dollars < drink['cost']:
        return "failed"
    change = round(coins_in_dollars - drink['cost'], 2)
    print(f"Here is ${change} in change.")
    return "success"
    

is_over = False
while not is_over:
    # TODO: 1. Prompt user for input
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
    is_make_drink = True

    if user_input == 'off':
        is_over = True
        is_make_drink = False
    elif user_input == 'report':
        report()
        is_make_drink = False

    while is_make_drink:
        drink = MENU[user_input]
        # TODO: 2a. If enough ingredients are available, prepare the beverage and add it to cash register
        check_response = check_resources(user_input, drink)
        if check_response == True:
            if pay(drink) == 'success':
                print(make_drink(user_input, drink))
                is_make_drink = False
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            is_make_drink = False
            print(f"Sorry, not enough {check_response}")