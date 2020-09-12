#!/usr/bin/python3

import string

alphabet = string.ascii_lowercase


def rotateLetter(letter, rotateNum):
    if letter in alphabet:
        newLetterIndex = alphabet.find(letter) + rotateNum
        finalNewLetterIndex = newLetterIndex - (newLetterIndex // len(alphabet)) * len(alphabet)
        return alphabet[finalNewLetterIndex]


def rotate(word, rotateNum):
    newWord = ''

    for letter in word.lower():
        newWord = newWord + (rotateLetter(letter, rotateNum))

    return newWord


if __name__ == '__main__':
    while True:
        string = input('Enter a word: ').strip()
        if string.isalpha():
            num = input('Enter a number: ').strip()
            try:
                result = rotate(string, int(num))
                print(result)
            except:
                continue



