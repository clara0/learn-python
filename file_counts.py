#!/usr/bin/python3
import sys


def count(fHand):
    termInuput = sys.argv
    lineCount = 0
    wordCount = 0
    charCount = 0

    if '-l' in termInuput:
        needLines = True
    if '-w' in termInuput:
        needWords = True
    if '-c' in termInuput:
        needChars = True
    if len(termInuput) == 2:
        needLines = True
        needWords = True
        needChars = True
    if len(termInuput) < 2 and ('-l' or '-w' or '-c' not in termInuput) or \
            (len(termInuput) > 2 and ('-l' or '-w' or '-c' in termInuput)):
        raise Exception('Enter valid files and options, please')

    if needLines:
        for line in fHand:
            lineCount += 1
        fHand.seek(0, 0)
    if needWords:
        for line in fHand:
            words = line.split()
            print(words)
            wordCount = len(words)
        fHand.seek(0, 0)
    if needChars:
        for line in fHand:
            for char in line:
                charCount += 1
        fHand.seek(0, 0)

    total = (lineCount, wordCount, charCount)
    return total


try:
    file = open(sys.argv[len(sys.argv) - 1])
except FileNotFoundError:
    raise Exception('Enter a valid file name')

counts = count(file)

header = ('Lines', 'Words', 'Chars')
template = '{:<10}{:<10}{:<10}'

x = template.format(*header)
print(x)

row = template.format(*counts)
print(row)

file.close()

