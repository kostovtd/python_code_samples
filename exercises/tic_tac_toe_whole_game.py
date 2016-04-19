"""

A whole tic tac toe game including drawing a board
and user input

"""

# TODO fix input overriding
# TODO fix drawing of wider boards

import re

_validate_input = re.compile("^[0-9]+$")
x = 0
y = 0


def validate_input(data):
    if data == "":
        raise ValueError("Empty input is not allowed")
    elif not _validate_input.search(data):
        raise ValueError("Only positive numbers allowed")


def input_with_validation(input_message):
    not_valid = True
    data = -1

    while not_valid:
        try:
            data = input(input_message)
            validate_input(data)
            not_valid = False
        except ValueError as err:
            print(err)

    return int(data)


def draw_board(data):
    print("\n")

    for a in range(0, y + 1):
        if x == y:
            print(" ---" * y)
            if a < y:
                row_str = ""
                for m in range(0, len(data[a])):
                    if m == len(data[a]) - 1:
                        if data[a][m] == 0:
                            row_str += "|   |"
                        else:
                            row_str += "| " + str(data[a][m]) + " |"
                    else:
                        if data[a][m] == 0:
                            row_str += "|   "
                        else:
                            row_str += "| " + str(data[a][m]) + " "
                print(row_str)
        else:
            print(" ---" * x)
            if a < y:
                print("|   " * int(x + 1))

    print("\n")


def find_winner(game):
    for q in range(0, len(game)):
        if str(game[q][0]) + str(game[q][1]) + str(game[q][2]) == 'xxx' or str(game[0][q]) + str(game[1][q]) + str(game[2][q]) == 'xxx':
            print("Player one wins")
            return False
        elif str(game[q][0]) + str(game[q][1]) + str(game[q][2]) == 'ooo' or str(game[0][q]) + str(game[1][q]) + str(game[2][q]) == 'ooo':
            print("Player two wins")
            return False

    if str(game[0][0]) + str(game[1][1]) + str(game[2][2]) == 'xxx' or str(game[0][2]) + str(game[1][1]) + str(game[2][0]) == 'xxx':
        print("Player one wins")
        return False
    elif str(game[0][0]) + str(game[1][1]) + str(game[2][2]) == 'ooo' or str(game[0][2]) + str(game[1][1]) + str(game[2][0]) == 'ooo':
        print("Player two wins")
        return False
    # else:
    #     print("No winner")
    return True


def main():
    global x, y
    turn = 1
    x = input_with_validation("Please enter X:")
    y = input_with_validation("Please enter Y:")

    data = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    play = True
    user_input = ""

    while play:
        if turn % 2 == 0:
            user_input = input("-- Player two -- Enter input as X,Y:")
            input_list = user_input.split(",")
            data[int(input_list[0])-1][int(input_list[1])-1] = 'o'
        else:
            user_input = input("-- Player one -- Enter input as X,Y:")
            input_list = user_input.split(",")
            data[int(input_list[0])-1][int(input_list[1])-1] = 'x'

        turn += 1
        draw_board(data)
        play = find_winner(data)


if __name__ == "__main__":
    main()