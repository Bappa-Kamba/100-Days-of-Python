from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


waiter = CoffeeMaker()
menu = Menu()
bank = MoneyMachine()

def report():
    waiter.report()
    bank.report()


is_order_over = False
while not is_order_over:
    user_input = input(
        f"What would you like? {menu.get_items()}: ").lower().strip()
    
    if user_input == 'off':
        is_order_over = True
    elif user_input == 'report':
        report()
    else:
        drink = menu.find_drink(user_input)
        if waiter.is_resource_sufficient(drink):
            if bank.make_payment(drink.cost):
                waiter.make_coffee(drink)
    