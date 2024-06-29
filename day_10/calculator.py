# Calculator
import os

from art import logo


def clear():
    if "TERM" in os.environ:
        os.system("clear" if os.name != "nt" else "cls")
    else:
        print("\033[H\033[J", end="")


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for operator in operations:
        print(operator)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_func = operations[operation_symbol]
        answer = calculation_func(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        want_to_continue = input(
            f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation or 'q' for exit: "
        )
        if want_to_continue == "y":
            num1 = answer
        elif want_to_continue == "q":
            break
        elif want_to_continue == "n":
            # should_continue = False
            # clear()
            # calculate()
            clear()
            num1 = float(
                input("What's the first number?: ")
            )  # Reset num1 for a new calculation
            for operator in operations:
                print(operator)
        else:
            break


calculate()
