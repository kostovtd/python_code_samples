"""
Ask the user for a string and print out whether this string is a palindrome or not.

(A palindrome is a string that reads the same forwards and backwards.)
"""

def is_palindrome(data):
    if data == "":
        raise ValueError("Empty input")

    data_len = len(data)
    half_len =int(data_len / 2)

    for x in range(0, half_len + 1):
        if data[x] != data[data_len - 1 - x]:
            return False

    return True


def main():
    user_input = input("Please add your input here:")
    print("Is '{0}' a palindrome? - {1}".format(user_input, is_palindrome(user_input)))


if __name__ == '__main__':
    main()