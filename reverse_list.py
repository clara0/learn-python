#!/usr/bin/python3


def reverseShallow(list1):
    if len(list1) == 1:
        return list1

    lastElement = list1.pop()
    return [lastElement] + (reverseShallow(list1))


def reverseDeep(list1):
    if len(list1) == 1:
        if type(list1[0]) == list:
            return [reverseDeep(list1[0])]
        return list1

    return reverseDeep([list1.pop()]) + reverseDeep(list1)


if __name__ == '__main__':
    while True:
        userInput = input('Enter a list separated by spaces: ').strip()
        try:
            print(reverseDeep(userInput.split()))
        except:
            continue