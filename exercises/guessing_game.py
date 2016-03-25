"""
A simple guessing game. A random number between 1 and 10 is generated

and the user has to guess it. To exit the game the use has to type 'exit'.

Some simple input validation included and game stats at the end of the game

(number of guess and the time when the game finished)
"""
import random
import re
import datetime

_numbers = re.compile("[0-9]")


def input_with_validation(input_message):
    user_guess = input(input_message)
    user_guess = user_guess.lower()

    if user_guess == "":
        raise ValueError("Empty input is not allowed")
    elif user_guess == "exit":
        return -1
    elif not _numbers.search(user_guess):
        raise ValueError("Input is not a number")

    user_guess = int(user_guess)

    if user_guess < 1 or user_guess > 10:
        raise ValueError("Input is out of the boundaries")

    return user_guess


def make_a_guess(user_input, random_number):
    if user_input < random_number:
        print("Guess is too low")
        return False
    elif user_input > random_number:
        print("Guess is too high")
        return False
    else:
        print("Guess is exactly right!")
        return True


def print_game_stats(guess_tries):
    print("---- Game stats ----")
    print("- Guess tries: {}".format(guess_tries))
    print("- Game finished at: {}".format(datetime.datetime.now()))
    print("--------------------")


def main():
    print("==== START GAME ====")
    print("Game started at: {}".format(datetime.datetime.now()))
    print("This is a simple guess game. The computer will generate a random number\n"
          "between 1 and 10 and you have to guess it.\n")
    random_number = random.randrange(1, 11, 1)

    keep_playing = True
    guess_tries = 0

    while keep_playing:
        try:
            user_guess = input_with_validation("Please, enter a number or enter 'exit' to stop playing: ")

            if user_guess == -1:
                print("==== END GAME ====")
                print_game_stats(guess_tries)
                keep_playing = False
            else:
                is_guess_right = make_a_guess(user_guess, random_number)
                guess_tries += 1
                if is_guess_right:
                    random_number = random.randrange(1, 11, 1)
                    print("A new number generated")
        except ValueError as exp:
            print(exp)


if __name__ == '__main__':
    main()