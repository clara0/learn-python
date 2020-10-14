#!/usr/bin/python3


def convertBase(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        newNum = num // 2
        return int(str(convertBase(newNum)) + str(num % 2))


if __name__ == '__main__':
    while True:
        userInput = input('Enter a number: ').strip()
        try:
            print(convertBase(int(userInput)))
        except:
            continue
