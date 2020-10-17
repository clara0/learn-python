#!/usr/bin/python3


def mySort(list1):
    if len(list1) == 1:
        return list1

    lastElement = list1[-1]
    part1 = list1[0:-1]
    sortedPart1 = mySort(part1)

    return mySort0(sortedPart1, lastElement)


def mySort0(part1, part2):
    for index, e in enumerate(part1):
        if part2 <= e:
            part1.insert(index, part2)
            return part1

    part1.append(part2)
    return part1


if __name__ == '__main__':
    print(mySort([10, 20, 15, 5]))
