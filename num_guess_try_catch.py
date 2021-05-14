#!/usr/bin/env python3
# Created by: Jonathan Kene
# Created on: May 11 2021
# This program asks the user to guess a number between 0 to 9
# and tells the user if the guess is right or wrong

import random


def main():

    # generate a number between 0 to 9
    correct_guess = random.randint(0, 9)

    # get the user's guess
    user_guess_string = input("Enter the number between 0 and 9: ")
    print("")

    # make sure if the user types anything but an integer, it's not valid
    try:
        user_guess_int = int(user_guess_string)
        print("You entered an integer correctly")
        print("")
    except ValueError:
        print("{} is not a number" .format(user_guess_string))

    # check to see if the user guess is correct or wrong
    else:
        if user_guess_string == correct_guess:
            print("You are correct!")
        else:
            print("You are wrong! The answer is = {}" .format(correct_guess))


if __name__ == "__main__":
    main()
