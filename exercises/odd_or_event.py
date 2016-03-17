import re

_characters = re.compile("[a-zA-Z]")  # a simple RegEx to check if the data contains characters


def contains_characters(data):
    return bool(_characters.search(data))


def input_number():
    number = input("Enter a number, please: ")

    if number == "":
        raise ValueError("Empty input not allowed")
    elif contains_characters(number):
        raise ValueError("Characters not allowed as input")

    return number


def odd_or_event(number):
    if int(number) % 2 == 0:
        print("{} is odd".format(number))
    else:
        print("{} is even".format(number))


def multiple_by(number, multiple):
    if int(number) % multiple == 0:
        print("{0} is multiple by {1}".format(number, multiple))
    else:
        print("{0} is not multiple by {1}".format(number, multiple))


def divides_evenly(number, check):
    if int(number) % int(check) == 0:
        print("{0} divides evenly into {1}".format(check, number))
    else:
        print("{0} divides unevenly into {1}".format(check, number))


def main():
    number = input_number()
    odd_or_event(number)
    multiple_by(number, 4)
    number2 = input_number()
    check = input_number()
    divides_evenly(number2, check)


if __name__ == '__main__':
    main()