#!/usr/bin/python3
import sys


def count(fHand):
    lineCount = 0
    wordCount = 0
    charCount = 0

    for line in fHand:
        lineCount += 1
        words = line.split()
        for word in words:
            wordCount += 1
        for char in line:
            charCount += 1

    total = (lineCount, wordCount, charCount)
    return total


counts = count(open(sys.argv[1]))

header = ('Lines', 'Words', 'Chars')
template = '{:<10}{:<10}{:<10}'

x = template.format(*header)
print(x)

row = template.format(*counts)
print(row)

