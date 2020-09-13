#!/usr/bin/python3

from urllib.request import urlopen


def reversedWord(word):
    newWord = word[1:] + word[0]
    if newWord[::-1] == word:
        return True
    return False


if __name__ == '__main__':
    file = urlopen('http://www.gutenberg.org/files/3201/files/CROSSWD.TXT')
    for line in file:
        word = line.decode('utf-8').strip()
        if reversedWord(word):
            print(word)
