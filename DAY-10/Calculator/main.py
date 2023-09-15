from art import logo
from os import name, system


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}

number1 = float(input("Enter a number: "))
for symbol in operations:
    print(symbol, end=" ")
print()

should_continue = True
while should_continue:
    operand = input("Choose an operation: ").strip()
    number2 = float(input("What's the next number? "))

    function = operations[operand]
    result = function(number1, number2)
    should_continue = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation or anything else to exit: ")
    if should_continue == 'y':
        number1  = result
    elif should_continue == 'n':
        clear()
        number1 = float(input("Enter a number: "))
    else:
        should_continue = False
