#!/usr/bin/python3


def isPower(baseNum, powerNum):
    try:
        if powerNum % baseNum == 0:
            if powerNum == baseNum:
                return True
            else:
                return isPower(baseNum, powerNum / baseNum)
        else:
            return False

    except:
        return False


if __name__ == '__main__':
    while True:
        firstNum = input('Enter a base number: ').strip()
        secondNum = input('Enter another number: ').strip()
        print(f'{secondNum} is a power of {firstNum}? {isPower(float(firstNum), float(secondNum))}')
