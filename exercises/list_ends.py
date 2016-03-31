"""

Generates a list of random numbers and creates a new list

containing only the first and the last entries from the previous list.

"""


import random


def generate_random_list():
    list_length = random.randint(1, 25)
    array = []

    for x in range(1, list_length +1):
        array.append(random.randint(1, 100))

    return array


def get_first_and_last_list(data):
    array = []
    array.append(data[0])
    array.append(data[-1])
    return array


def main():
    data = generate_random_list()
    print("Generated list: {}".format(data))
    print("New list: {}".format(get_first_and_last_list(data)))


if __name__ == "__main__":
    main()