"""

A simple cows and bulls game with
some basic statistics

"""


import random
import re

_validate_input = re.compile("^[0-9]+$")
_generated_number = -1


def generate_number():
    global _generated_number
    _generated_number = random.randint(1000, 9999)


def validate_input(data):
    if data == "":
        raise ValueError("Empty input is not allowed")
    elif not _validate_input.search(data):
        raise ValueError("Only digits allowed")
    elif int(data) < 1000 or int(data) > 9999:
        raise ValueError("You must enter a four-digits number")


def input_with_validation(input_message):
    not_valid = True
    data = -1

    while not_valid:
        try:
            data = input(input_message)
            if int(data) == 0:
                not_valid = False
                continue
            validate_input(data)
            not_valid = False
        except ValueError as err:
            print(err)

    return str(data)


def check_cows_bulls(data):
    cows_count = 0
    bulls_count = 0
    data_list = list(data)
    generated_number_list = list(str(_generated_number))

    if data == '0':
        print(_generated_number)
        return "00"

    for x in range(0, len(generated_number_list)):
        if generated_number_list[x] == data_list[x]:
            cows_count += 1
            continue
        if generated_number_list[x] != data_list[x] and data_list[x] in generated_number_list \
                and data_list.count(data_list[x]) == generated_number_list.count(data_list[x]):
            bulls_count += 1
            continue

    return cows_count, bulls_count


def main():
    generate_number()
    print("Welcome to the Cows and Bulls game!")
    number_fount = False
    guesses_count = 0

    while not number_fount:
        guesses_count += 1
        user_input = input_with_validation("Enter a number:")
        cows, bulls = check_cows_bulls(user_input)
        print("{0} cows, {1} bulls".format(cows, bulls))

        if int(user_input) == _generated_number:
            number_fount = True
            print("Total number of guesses: {}".format(guesses_count))


if __name__ == "__main__":
    main()