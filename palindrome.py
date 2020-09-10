#!/usr/bin/python3


def palindrome(num):
    if num == num[::-1]:
        return True
    return False


def addOne(num):
    num = int(num) + 1
    return str(num)


def isPalindrome(num):
    num = str(num)

    num = num.zfill(6)
    value = palindrome(num[2:])
    if value:
        num = num.zfill(6)
        value2 = palindrome(num[1:])
        if value2:
            num = num.zfill(6)
            value3 = palindrome(num[1:-2])
            if value3:
                num = num.zfill(6)
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
