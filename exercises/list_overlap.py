from random import randint


def generate_random_list():
    list_length = randint(1, 100)
    list_result = []

    for x in range(1, list_length + 1):
        list_result.append(randint(1, 100))

    return list_result


def find_intersection(list_a, list_b):
    return set(list_a).intersection(list_b)


def main():
    list_a = generate_random_list()
    list_b = generate_random_list()
    print("list a {}".format(list_a))
    print("list b {}".format(list_b))

    list_intersection = find_intersection(list_a, list_b)
    print("intersection {}".format(list_intersection))


if __name__ == '__main__':
    main()