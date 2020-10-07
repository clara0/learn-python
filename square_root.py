#!/usr/bin/python3

import sys


def squareRoot(num):
    guess = num / 2
    while True:
        closerGuess = (guess + (num / guess)) / 2
        if abs(guess - closerGuess) <= sys.float_info.epsilon:
            return closerGuess
        else:
            guess = closerGuess


if __name__ == '__main__':
    while True:
        userInput = input('Enter a number: ').strip()
        try:
            print(f'The square root of {userInput} is {squareRoot(float(userInput))}.')
        except:
            continue
