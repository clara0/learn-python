#!/usr/bin/python3


def main():
    result = rotate([1, 2, 3], 1000)
    print(result)


def rotateElement(element, rotateNum, list1):
    if element in list1:
        newELementIndex = list1.index(element) + rotateNum
        finalNewLetterIndex = newELementIndex - (newELementIndex // len(list1)) * len(list1)
        return list1[finalNewLetterIndex]


def rotate(list1, rotateNum):
    newList = []

    for element in list1:
        newList.append(rotateElement(element, rotateNum, list1))

    return newList


if __name__ == '__main__':
    main()
