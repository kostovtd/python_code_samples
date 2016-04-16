"""

Draws a simple game board by given
X and Y values by the user

Has some simple input validation

"""

import re

_validate_input = re.compile("^[0-9]+$")


def validate_input(data):
    if data == "":
        raise ValueError("Empty input is not allowed")
    elif not _validate_input.search(data):
        raise ValueError("Only positive numbers allowed")


def input_with_validation(input_message):
    not_valid = True
    data = -1

    while not_valid:
        try:
            data = input(input_message)
            validate_input(data)
            not_valid = False
        except ValueError as err:
            print(err)

    return int(data)


def draw_board(x, y):
    print("\n")

    for a in range(0, y + 1):
        if x == y:
            print(" ---" * y)
            if a < y:
                print("|   " * int(y + 1))
        else:
            print(" ---" * x)
            if a < y:
                print("|   " * int(x + 1))


def main():
    x = input_with_validation("Please enter X:")
    y = input_with_validation("Please enter Y:")
    draw_board(x, y)


if __name__ == "__main__":
    main()