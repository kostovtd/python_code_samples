import random
import re

_validate_input = re.compile("^[0-9]+$")


def generate_random_list():
    list_length = random.randint(10000, 10001)
    random_list = []

    for x in range(0, list_length):
        number = random.randint(1, 1000000)
        if number not in random_list:
            random_list.append(number)

    return random_list


def validate_input(data):
    if data == "":
        raise ValueError("Empty input is not allowed")
    elif not _validate_input.search(data) or int(data) < 0:
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


def binary_search(generated_list, user_input):
    first_index = 0
    last_index = len(generated_list) - 1
    found = False
    count = 0

    while first_index <= last_index and not found:
        count += 1
        mid_index = (first_index + last_index) // 2
        if generated_list[mid_index] == user_input:
            found = True
        else:
            if generated_list[mid_index] > user_input:
                last_index = mid_index - 1
            else:
                first_index = mid_index + 1

    return found, count


def main():
    generated_list = sorted(generate_random_list())
    print("Generated list: {}".format(generated_list))
    print("List length: {}".format(len(generated_list)))
    user_input = input_with_validation("Please, enter a number: ")

    found, count = binary_search(generated_list, user_input)
    if found:
        print("The element was found.")
    else:
        print("The element was NOT found")

    print("Total number of checks: {}".format(count))

if __name__ == "__main__":
    main()