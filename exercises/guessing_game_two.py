"""

A simple guessing game. The user has to choose a number
between 1 and 100 and the program has to make guess.

Binary search is being used in the following code

"""


def guess(generated_list):
    first_index = 0
    last_index = len(generated_list) - 1
    found = False
    count = 0

    while first_index <= last_index and not found:
        count += 1
        mid_index = (first_index + last_index) // 2
        print("The mighty computer says: {}".format(generated_list[mid_index]))
        user_input = input("If it's true enter T / If it's lower enter L / If it's higher enter H:")
        if user_input == 'T':
            print("Yeaaah! I'm good! Total guesses: {}".format(count-1))
            found = True
        else:
            if user_input == 'L':
                last_index = mid_index - 1
            elif user_input == 'H':
                first_index = mid_index + 1


def main():
    list_number = range(1, 101)
    guess(list_number)

if __name__ == '__main__':
    main()