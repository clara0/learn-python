#!/usr/bin/python3


def main():
    while True:
        num = input('Enter a number: ').strip()
        if num != '':
            try:
                result = LuhnTest(num)
                print(result)
            except:
                continue


def listDigits(num1):
    digitList = []
    num1 = abs(num1)

    while True:
        if num1 > 9:
            digitList.append(num1 % 10)
            num1 = num1 // 10
        else:
            digitList.append(num1)
            return tuple(digitList[::-1])


def listDigits2(num1):
    num1 = abs(num1)
    if num1 < 10:
        return (num1,)
    else:
        digit1 = num1 % 10
        return listDigits2(num1 // 10) + (digit1,)


def LuhnTest(num):
    backwardsNum = num[::-1]
    sum1 = 0
    sum2 = 0
    for index, digit in enumerate(backwardsNum, 1):
        if index % 2 != 0:
            sum1 += int(digit)
        else:
            doubledDigit = int(digit) * 2
            if doubledDigit > 9:
                digits = listDigits(doubledDigit)
                sum2 += (digits[0] + digits[1])
            else:
                sum2 += doubledDigit

    total = sum1 + sum2
    if str(total)[-1] == '0':
        return True

    return False


if __name__ == '__main__':
    main()
