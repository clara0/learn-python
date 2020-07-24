# count letters in a file
import collections


def countLetters(file):
    letters = dict()

    for line in file:
        line = line.lower()
        for char in line:
            if char.isalpha():
                letters[char] = letters.get(char, 0) + 1

    sortedDict = sorted(letters.items(), key=lambda x: x[1])
    return sortedDict


fileHandle = open('/tmp/wget.rb')
letterFrequency = countLetters(fileHandle)

for i in letterFrequency:
    print(f'{i[0]} => {i[1]}')

