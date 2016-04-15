"""

The program reads from files given by their path and
finds the intersection between the lists of the elements from the
two files.

It's using sets

"""

def read_file(file_path):
    lines_list = []

    with open(file_path, 'r') as open_file:
        for line in open_file:
            lines_list.append(int(line.replace("\n", "")))

    return lines_list


def find_overlapping_numbers(first_list, second_list):
    first_set = set(first_list)
    second_set = set(second_list)

    return first_set.intersection(second_set)


def main():
    a = 5
    prime_numbers_list = read_file('C:/Users/Todor/Desktop/primenumbers.txt')
    happy_numbers_list = read_file('C:/Users/Todor/Desktop/happynumbers.txt')
    overlapping_numbers_list = sorted(find_overlapping_numbers(prime_numbers_list, happy_numbers_list))
    print(prime_numbers_list)
    print(happy_numbers_list)
    print(overlapping_numbers_list)


if __name__ == "__main__":
    main()