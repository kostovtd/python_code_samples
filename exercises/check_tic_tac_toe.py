"""

Checks the result of a predefined tic tak toe game

"""


def find_winner(game):
    for x in range(0, len(game)):
        sum_list = sum(game[x])
        if sum_list == 3 or game[0][x] + game[1][x] + game[2][x] == 3:
            print("Player one wins")
            return
        elif sum_list == 15 or game[0][x] + game[1][x] + game[2][x] == 15:
            print("Player two wins")
            return

    if game[0][0] + game[1][1] + game[2][2] == 3 or game[0][2] + game[1][1] + game[2][0] == 3:
        print("Player one wins")
        return
    elif game[0][0] + game[1][1] + game[2][2] == 15 or game[0][2] + game[1][1] + game[2][0] == 15:
        print("Player two wins")
        return
    else:
        print("No winner")


def main():
    game = [[1, 1, 5],
            [1, 5, 5],
            [5, 1, 1]]

    find_winner(game)

if __name__ == "__main__":
    main()