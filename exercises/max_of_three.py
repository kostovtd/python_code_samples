"""

Find the maximum of three positive numbers entered as
user input

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


def max_of_three(numbers_list):
    buff = numbers_list[0]

    for x in range(1, len(numbers_list)):
        if buff < numbers_list[x]:
            buff = numbers_list[x]

    print("The max of the three is: {}".format(buff))


def main():
    numbers_list = []
    first_number = input_with_validation("Enter first number:")
    second_number = input_with_validation("Enter second number:")
    third_number = input_with_validation("Enter third number:")

    numbers_list.append(first_number)
    numbers_list.append(second_number)
    numbers_list.append(third_number)

    max_of_three(numbers_list)


if __name__ == "__main__":
    main()