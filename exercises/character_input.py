import re
from datetime import date
_digits = re.compile("\d")  # a simple RegEx to check if the data is a digit
_characters = re.compile("[a-zA-Z]")  # a simple RegEx to check if the data contains characters


def contains_digits(data):
    return bool(_digits.search(data))


def contains_characters(data):
    return bool(_characters.search(data))


def input_name():
    name = input("Enter your name, please: ")

    if name == "":
        raise ValueError("Empty input")

    if contains_digits(name):
        raise ValueError("No digits allowed in the name")

    return name


def input_age():
    age = input("Enter your age, please: ")

    if age == "":
        raise ValueError("Empty input")

    if contains_characters(age):
        raise ValueError("No characters allowed in the age")

    return int(age)


def input_num_of_copies():
    num_of_copies = input("Enter number of copies, please : ")

    if num_of_copies == "":
        raise ValueError("Empty input")

    if contains_characters(num_of_copies):
        raise ValueError("No characters allowed in the number of copies")

    return int(num_of_copies)


def current_year():
    return date.today().year


def one_hundred_years(name, age):
    year = current_year() + 100 - age
    return "{0}, you will be 100 years old in {1}".format(name, year)


def print_copies(message, num_of_copies):
    i = 0
    for i in range(0, num_of_copies):
        print("{0} - {1}".format(i+1, message))


def main():
    name = input_name()
    age = input_age()
    num_of_copies = input_num_of_copies()
    message = one_hundred_years(name, age)
    print(message)
    print_copies(message, num_of_copies)


if __name__ == '__main__':
    main()