#!/usr/bin/python3

import string
alphabet = string.ascii_lowercase


def main():
    while True:
        userInput = input('Enter some letters: ').strip()
        if userInput.isalpha():
            result = findMissingLetters(userInput)
            print(result)


def findMissingLetters(letterRange):
    missingLetters = []
    letterRange = letterRange.lower()
    if letterRange not in alphabet:
        for count, letter in enumerate(letterRange):
            try:
                for i in alphabet[alphabet.find(letter) + 1:alphabet.find(letterRange[count + 1])]:
                    if i not in missingLetters:
                        missingLetters.append(i)
            except:
                continue
    return tuple(missingLetters)


if __name__ == '__main__':
    main()
