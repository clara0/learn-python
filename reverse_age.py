#!/usr/bin/python3


def main():
    ages = findAge()
    print(ages)


def reverseNum(num):
    num = str(num)
    return int(num[::-1])


def findAge():
    possibleAges = []
    for num in range(10, 100):
        if str(num)[0] > str(num)[1]:
            possibleAges.append((num, reverseNum(num)))

    for ageTuple in possibleAges:
        countList = []
        ageTupleDiff = ageTuple[0] - ageTuple[1]

        for ageTuple1 in possibleAges:
            ageTuple1Diff = ageTuple1[0] - ageTuple1[1]
            if ageTupleDiff == ageTuple1Diff:
                countList.append(ageTuple1)

        if len(countList) > 6:
            if ageTupleDiff > 20:
                return countList


if __name__ == '__main__':
    main()
