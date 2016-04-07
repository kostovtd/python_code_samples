"""

Asks for some input and print the same input,
but in reverse order

"""


def reverse_word_order(data):
    data = data.split(" ")
    result = ""

    for x in range(len(data)-1, -1, -1):
        result += data[x] + " "

    return result


def main():
    user_input = input("Please, enter something:")
    reverse_user_input = reverse_word_order(user_input)
    print("Reverse input: {}".format(reverse_user_input))


if __name__ == "__main__":
    main()