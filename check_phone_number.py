#!/usr/bin/python3


def main():
    while True:
        userInput = input('Enter a U.S. phone number: ').strip()
        result = checkPhoneNum(userInput)
        print(result)


def checkPhoneNum(phoneNum):
    valid = '-() '
    numbers = 0
    for i in phoneNum:
        if i.isnumeric():
            numbers += 1
    if 9 < numbers < 12:
        tripleNumCount = 0
        for count, i in enumerate(phoneNum):
            if i not in valid and not i.isnumeric():
                print(i)
                return False

            if tripleNumCount == 2 and phoneNum[-4:].isnumeric():
                if numbers == 11:
                    if phoneNum.startswith('1'):
                        return True
                    else:
                        return False
                return True

            elif tripleNumCount < 2 and phoneNum[count:count + 3].isnumeric():
                tripleNumCount += 1
    return False


if __name__ == '__main__':
    main()
