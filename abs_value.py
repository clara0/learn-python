#!/usr/bin/python3


def main():
    import random

    while True:
        numRange = range(-100, 101)
        randomNum = random.choice(numRange)
        answer = str(abs(randomNum) * 2)
        while True:
            userInput = input(f'Enter double the amount of the absolute value of {randomNum}: ').strip()
            if userInput == answer:
                print('Correct!')
                break
            else:
                print('Try again!')


if __name__ == '__main__':
    main()
