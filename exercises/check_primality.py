"""

Ask the user for a number and determine whether the number is prime or not.

"""


import re
_validate_input = re.compile("^[0-9]+$")


def validate_input(data):
    if data == "":
        raise ValueError("Empty input is not allowed")
    elif not _validate_input.search(data):
        raise ValueError("Only digits allowed")


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


def check_primality(data):
    if data <= 1:
        return False
    elif data <= 3:
        return True
    elif data % 2 == 0 or data % 3 == 0:
        return False

    i = 5

    while i * i <= data:
        if data % i == 0 or data % (i + 2) == 0:
            return False
        i += 6

    return True


def main():
    user_input = input_with_validation("Please, enter a number: ")
    print("Is {0} a prime number? {1}".format(user_input, check_primality(user_input)))


if __name__ == "__main__":
    main()