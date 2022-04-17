#!/usr/bin/python3


def main():
    while True:
        userInput = input('Please enter a number: ').strip()
        try:
            print(findFactorial(int(userInput)))
        except:
            continue


def findFactorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i

    return factorial


def findFactorial2(num):
    if num == 1:
        return num
    oneLess = num - 1
    return num * findFactorial2(oneLess)


if __name__ == '__main__':
    main()
