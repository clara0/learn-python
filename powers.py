#!/usr/bin/python3


def isPower(baseNum, powerNum):
    try:
        if powerNum % baseNum == 0:
            if powerNum == baseNum:
                return True
            else:
                result = isPower(baseNum, powerNum / baseNum)
                return result
        else:
            return False

    except:
        return False


if __name__ == '__main__':
    while True:
        firstNum = input('Enter a base number: ').strip()
        secondNum = input('Enter another number: ').strip()
        result = isPower(float(firstNum), float(secondNum))
        print(f'{secondNum} is a power of {firstNum}? {result}')
