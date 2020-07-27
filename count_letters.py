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

header = ('Letter', 'Frequency')
template = '{:<10}{:<10}'

letter = template.format(*header)
print(letter)

for i in letterFrequency:
    frequency = template.format(*letterFrequency)
    print(frequency)
