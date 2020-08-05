#!/usr/bin/python3
import sys


def findWord(word, file):
    arguments = sys.argv
    lineList = []
    if arguments[1] == '-i' or arguments[1] == '--ignore-case':
        ignoreCase = True
    else:
        ignoreCase = False
    if ignoreCase:
        for line1 in file:
            if word.lower() in line1.lower():
                lineList.append(line1)
    else:
        for line1 in file:
            if word in line1:
                lineList.append(line1)

    return lineList

try:
    fhand = open(sys.argv[-1])
    word = sys.argv[(-1) - 1]
    if word.startswith('-') and len(sys.argv) == 3:
        raise Exception('usage: [word] [-i ignore case] [--ignore-case ignore case] [file]')
    elif sys.argv[1] != '-i' and sys.argv[1] != '--ignore-case':
        raise Exception('usage: [word] [-i ignore case] [--ignore-case ignore case] [file]')
except:
    raise Exception('usage: [word] [-i ignore case] [--ignore-case ignore case] [file]')

x = findWord(word, fhand)
for line in x:
    print(line)
