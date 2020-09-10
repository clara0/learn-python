#!/usr/bin/python3


def palindrome(num):
    if num == num[::-1]:
        return True
    return False


def addZero(num):
    if len(num) < 6:
        num = '0' * (6 - len(str(num))) + str(num)
    return num


def addOne(num):
    num = int(num) + 1
    return str(num)


def isPalindrome(num):
    num = str(num)
    num = addZero(num)

    value = palindrome(num[2:])
    if value:
        num = addZero(addOne(num))
        value2 = palindrome(num[1:])
        if value2:
            num = addZero(addOne(num))
            value3 = palindrome(num[1:-2])
            if value3:
                num = addZero(addOne(num))
                value4 = palindrome(num)
                if value4:
                    return True
    return False


resultList = []

for i in range(1, 999996):
    result = isPalindrome(i)
    if result:
        resultList.append(i)

print(resultList)
