#!/usr/bin/python3

from urllib.request import urlopen


def isValidWordPair(word1, word2):
    differentLetters = 0
    for letterIndex, letter1 in enumerate(word1):
        if letter1 != word2[letterIndex]:
            differentLetters += 1
        if differentLetters >= 3:
            return False

        if differentLetters == 2:
            return True
    return False


if __name__ == '__main__':
    wordPairList = []
    file = urlopen('http://www.gutenberg.org/files/3201/files/CROSSWD.TXT')
    wordList = sorted([line.decode('utf-8').strip() for line in file], key=len)

    for index, word1 in enumerate(wordList[:3000]):
        len1 = len(word1)
        sorted1 = sorted(word1)
        for word2 in wordList[index + 1: 3000]:
            if len(word2) > len1:
                break
            sorted2 = sorted(word2)
            if sorted1 == sorted2:
                if isValidWordPair(word1, word2):
                    wordPairList.append((word1, word2))

    for a, b in wordPairList:
        print(a, b)
