"""

Generates a set of the Fibonacci numbers. It's length is

given by the user.

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


def generate_fibonacci_v2(data):
    a,b = 0,1
    yield a
    yield b
    while data > 0:
        data -= 1
        a, b = b, a + b
        yield b


def main():
    user_input = input_with_validation("Count of Fibonacci numbers: ")
    numbers = generate_fibonacci_v2(user_input)

    for number in numbers:
        print(number)


if __name__ == "__main__":
    main()