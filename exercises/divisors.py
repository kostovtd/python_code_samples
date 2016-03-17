import re
import time
_characters_ = re.compile("[a-zA-Z]")
_start_time = 0


def contains_characters(number):
    return bool(_characters_.search(number))


def input_number():
    number = input("Enter a number, please:")

    if number == "":
        raise ValueError("Empty input not allowed")
    elif contains_characters(number):
        raise ValueError("Characters not allowed as input")

    return number


def find_divisors_trivial_division(number):
    global _start_time
    _start_time = time.time()

    number = int(float(number) * 0.5)
    arr = range(1, number + 1)
    divisors = []

    for x in arr:
        if number % x == 0:
            divisors.append(x)

    if number > 1:
        divisors.append(number)

    print("--- %s seconds TRIVIAL DIVISION ---" % (time.time() - _start_time))


def main():
    number = input_number()
    find_divisors_trivial_division(number)


if __name__ == '__main__':
    main()
