# count letters in a file


def countLetters(file):
    letters = dict()

    for line in file:
        line = line.lower()
        for char in line:
            if char.isalpha():
                letters[char] = letters.get(char, 0) + 1

    sortedDict = sorted(letters.items(), key=lambda x: x[1])
    return sortedDict


fileHandle = open('/usr/local/Cellar/wget/1.20.3_2/.brew/wget.rb')
letterFrequency = countLetters(fileHandle)

header1 = ('Letter', 'Frequency')
template1 = '{:<10}{:<10}'

letter = template1.format(*header1)
print(letter)

for letter in letterFrequency:
    frequency = template1.format(*letter)
    print(frequency)


def count(file):
    lineCount = 0
    wordCount = 0
    charCount = 0

    for line in file:
        lineCount += 1
        words = line.split()
        for word in words:
            wordCount += 1
        for char in line:
            charCount += 1

    total = (lineCount, wordCount, charCount)
    return total


fHand = open('/Users/clara/.bashrc')
counts = count(fHand)

header2 = ('Lines', 'Words', 'Chars')
template2 = '{:<10}{:<10}{:<10}'

x = template2.format(*header2)
print(x)

row = template2.format(*counts)
print(row)

