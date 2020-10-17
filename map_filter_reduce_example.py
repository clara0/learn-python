#!/usr/bin/python3

import math
from functools import reduce

list1 = [1, 2, 3, 4, 5, 6]


def findMax(a, b):
    if a > b:
        return a
    return b


def findMin(a, b):
    if a < b:
        return a
    else:
        return b


# MAPPING

resultList = list(map(math.sqrt, list1))
print(resultList)

# FILTERING

resultList5 = list(filter(lambda a: a % 2 == 0, list1))
print(resultList5)

# REDUCING

resultList1 = reduce(findMax, list1)
print(resultList1)

resultList2 = reduce(findMin, list1)
print(resultList2)

resultList3 = reduce(lambda a, b: a + b, list1)
print(resultList3)

resultList4 = reduce(lambda a, b: (a + b) / 2, list1)
print(resultList4)
