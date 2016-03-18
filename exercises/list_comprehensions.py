"""
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
"""


def find_even_elements(data):
    result_list = [item for item in data if item % 2 == 0]
    return result_list


def main():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print("result list - {}".format(find_even_elements(a)))


if __name__ == '__main__':
    main()