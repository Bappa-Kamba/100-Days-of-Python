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


def calculator(num1, operand, num2):
    if operand == '+':
        return add(num1, num2)
    elif operand == '-':
        return sub(num1, num2)
    elif operand == '*':
        return mul(num1, num2)
    elif operand == '/':
        return div(num1, num2)
    else:
        print("Sorry that is beyond my scope :(")


def prompt():
    print(logo)
    number1 = float(input("Enter a number: "))
    operand = input("Choose an operation ['+', '-', '*' or '/']: ").strip()
    number2 = float(input("What's the next number? "))

    return number1, operand, number2


def main():
    number1, operand, number2 = prompt()
    result = calculator(num1=number1, operand=operand, num2=number2)
    print(f"{number1} {operand} {number2} = {result}")

    while True:
        continue_calc = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if continue_calc == 'y':
            operand = input(
                "Choose an operation ['+', '-', '*' or '/']: ").strip()
            number2 = float(input("What's the next number? "))
            result = calculator(num1=result, operand=operand, num2=number2)
            print(f"{number1} {operand} {number2} = {result}")
        elif continue_calc == 'n':
            clear()
            number1, operand, number2 = prompt()
            result = calculator(num1=number1, operand=operand, num2=number2)
            print(f"{number1} {operand} {number2} = {result}")


main()
