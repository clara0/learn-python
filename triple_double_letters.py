#!/usr/bin/python3
from urllib.request import urlopen


def findTripleDoubles(word):
    prevLetter = None
    pairs = 0
    inbetween = 0

    for letter in word:
        if letter == prevLetter:
            if inbetween < 2:
                pairs += 1
                inbetween = 0
        elif 0 < pairs < 3:
            inbetween += 1
        if pairs == 3:
            return True
        prevLetter = letter
    return False


if __name__ == '__main__':
    file = urlopen('http://www.gutenberg.org/files/3201/files/CROSSWD.TXT')
    resultList = []
    for line in file:
        word = (line.decode('utf-8')).strip()
        result = findTripleDoubles(word)
        if result:
            resultList.append(word)
    print(resultList)
