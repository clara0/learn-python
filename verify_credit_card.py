#!/usr/bin/python3


def verifyNum(num):
    backwardsNum = str(num)[::-1]
    sum1 = 0
    sum2 = 0
    for index, digit in enumerate(backwardsNum, 1):
        if index % 2 != 0:
            sum1 += int(digit)
        else:
            doubledDigit = int(digit) * 2
            if doubledDigit > 9:
                sum2 += (int(str(doubledDigit)[0]) + int(str(doubledDigit)[1]))
            else:
                sum2 += doubledDigit

    total = sum1 + sum2
    if str(total)[-1] == '0':
        return True

    return False


if __name__ == '__main__':
    while True:
        num = input('Enter a number: ').strip()
        try:
            result = verifyNum(int(num))
            print(result)
        except:
            continue
