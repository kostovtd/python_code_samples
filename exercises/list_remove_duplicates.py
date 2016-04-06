"""

The program takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.

Two different methods included for doing that using:
- simple loops
- sets

"""

import random


def generate_random_list():
    list_length = random.randint(1, 25)
    array = []

    for x in range(1, list_length + 1):
        array.append(random.randint(1, 51))

    return array


def remove_duplicates_loop(data):
    current_item = -1
    array = []

    for x in range(0, len(data)):
        current_item = data[x]
        if x == 0:
            array.append(current_item)

        is_added = False

        for y in range(0, len(array)):
            if array[y] == current_item:
                is_added = True
                break

        if not is_added:
            array.append(current_item)

    return array


def remove_duplicates_sets(data):
    data_set = set(data)
    data_list = list(data_set)
    return data_list


def main():
    random_list = generate_random_list()
    print("First list: {}".format(random_list))
    list_no_duplicates = remove_duplicates_loop(random_list)
    print("No duplicates list: {}".format(list_no_duplicates))
    list_no_duplicates_sets = remove_duplicates_sets(random_list)
    print("No duplicates list (sets): {}".format(list_no_duplicates_sets))



if __name__ == "__main__":
    main()