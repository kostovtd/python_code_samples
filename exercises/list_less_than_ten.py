import re
_characters = re.compile("[a-zA-Z]")


def get_less_than(a, m):
    b = []
    m = int(m)
    for x in a:
        if x < m:
            b.append(x)

    return b


def contains_characters(data):
    return bool(_characters.search(data))


def input_number():
    number = input("Enter a number, please: ")

    if number == "":
        raise ValueError("Empty input not allowed")
    elif contains_characters(number):
        raise ValueError("Characters not allowed as input")

    return number


def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    m = input_number()
    b = get_less_than(a, m)
    print(b)


if __name__ == '__main__':
    main()