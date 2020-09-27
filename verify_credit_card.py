#!/usr/bin/python3


def listNum(num1):
    digitList = []
    while True:
        if num1 != 0:
            digitList.append(num1 % 10)
            num1 = num1 // 10
        else:
            break

    return tuple(digitList[::-1])


def verifyNum(num):
    backwardsNum = num[::-1]
    sum1 = 0
    sum2 = 0
    for index, digit in enumerate(backwardsNum, 1):
        if index % 2 != 0:
            sum1 += int(digit)
        else:
            doubledDigit = int(digit) * 2
            if doubledDigit > 9:
                digits = listNum(doubledDigit)
                sum2 += (digits[0] + digits[1])
            else:
                sum2 += doubledDigit

    total = sum1 + sum2
    if str(total)[-1] == '0':
        return True

    return False


if __name__ == '__main__':
    while True:
        num = input('Enter a number: ').strip()
        if num != '':
            try:
                result = verifyNum(num)
                print(result)
            except:
                continue
