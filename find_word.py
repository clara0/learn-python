#!/usr/bin/python3
import sys


def findWord(word, file):
    ignoreCase = False
    arguments = sys.argv
    lineList = []
    if len(arguments) < 3:
        raise Exception('usage: [word] [-i ignore case] [--ignore-case ignore case] [file]')
    if '-i' or '--ignore-case' in arguments:
        ignoreCase = True
    if ignoreCase:
        for line1 in file:
            if (word.lower() or word.title() or word.upper()) in line1:
                lineList.append(line1)
    else:
        for line1 in file:
            if word in line1:
                lineList.append(line)

    return lineList


try:
    fhand = open(sys.argv[-1])
except FileNotFoundError:
    raise Exception('usage: [word] [-i ignore case] [--ignore-case ignore case] [file]')

x = findWord(sys.argv[1], fhand)
for line in x:
    print(line)
