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
        word = word.lower()
        for line1 in file:
            if word in line1.lower():
                lineList.append(line1)
    else:
        for line1 in file:
            if word in line1:
                lineList.append(line1)

    return lineList


def getUsage():
    return 'usage: sys.argv[0] [-i | --ignore-case ignore case] <word> <file>'


try:
    fhand = open(sys.argv[-1])
    word = sys.argv[(-1) - 1]
    if word.startswith('-') and len(sys.argv) == 3:
        raise Exception(getUsage())
    elif sys.argv[1] != '-i' and sys.argv[1] != '--ignore-case':
        raise Exception(getUsage())
except:
    raise Exception(getUsage())

x = findWord(word, fhand)
for line in x:
    print(line)
