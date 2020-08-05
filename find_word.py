#!/usr/bin/python3
import sys


def findWord(word, file):
    arguments = sys.argv
    lineList = []
    if len(arguments) < 3:
        raise Exception('usage: [word] [-i ignore case] [--ignore-case ignore case] [file]')
    if arguments[1] == '-i' or '--ignore-case' and len(arguments) == 4:
        ignoreCase = True
    else:
        ignoreCase = False
    if ignoreCase:
        for line1 in file:
            words = line1.split()
            for w in words:
                if w.lower() == word.lower():
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

x = findWord(sys.argv[(-1) - 1], fhand)
for line in x:
    print(line)
