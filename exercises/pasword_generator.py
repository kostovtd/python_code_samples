"""

Generates a random password based on a length given by the user
and a hardcoded set of symbols from which to choose

Input validation included (password's length MUST be more than 8 symbols long)

"""

import random
import re

_symbols = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_"
_validate_input = re.compile("^[0-9]+$")


def validate_input(data):
    if data == "":
        raise ValueError("Empty input is not allowed")
    elif not _validate_input.search(data):
        raise ValueError("Only digits allowed")
    elif int(data) <= 8:
        raise ValueError("The length of the password must be greater than 8")


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


def generate_password(length):
    password = ""

    for x in range(0, length + 1):
        password += random.choice(_symbols)

    return password


def main():
    password_length = input_with_validation("Please, enter a number greater than 8: ")
    password = generate_password(password_length)
    print("Your password is: {}".format(password))


if __name__ == "__main__":
    main()