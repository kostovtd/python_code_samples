"""
A simple Rock-Paper-Scissors game which uses

infinite loops and RegEx expressions for input

validation
"""

import re
_valid_player_input = re.compile("[s|S|r|R|p|P]")
_valid_game_input = re.compile("[y|Y|n|N]")


def validate_input(data, is_user_input):
    if data == "":
        raise ValueError("Empty input is not allowed")
    elif is_user_input:
        if not _valid_player_input.search(data):
            raise ValueError("Invalid input")
    elif not _valid_game_input.search(data):
        raise ValueError("Invalid input")


def input_with_validation(input_message, is_user_input):
    not_valid = True
    data = ""

    while not_valid:
        try:
            data = input(input_message)
            validate_input(data, is_user_input)
            not_valid = False
        except ValueError as exp:
            print(exp)

    return data


def compare_input(first_player, second_player):
    first_player = first_player.lower()
    second_player = second_player.lower()

    if first_player == second_player:
        print("==== Equal ====")
        return
    elif first_player == "s" and second_player == "p":
        print("==== First Player Win ====")
        return
    elif first_player == "r" and second_player == "s":
        print("==== First Player Win ====")
        return
    elif first_player == "p" and second_player == "r":
        print("==== First Player Win ====")
        return
    else:
        print("==== Second Player Win ====")
        return


def main():
    print("----- Rock VS Paper VS Scissors ------")
    print("Chose between:")
    print("- (R) for Rock")
    print("- (P) for Paper")
    print("- (S) for Scissors\n")

    keep_playing = True

    while keep_playing:
        first_player = input_with_validation("First player: ", True)
        second_player = input_with_validation("Second player: ", True)
        compare_input(first_player, second_player)
        new_game = input_with_validation("New game? (Y/N): ", False)
        new_game = new_game.lower()
        if new_game == "n":
            print("------ END GAME -----")
            keep_playing = False


if __name__ == '__main__':
    main()