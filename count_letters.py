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

header = ('Letter', 'Frequency')
template = '{:<10}{:<10}'

letter = template.format(*header)
print(letter)

for letter in letterFrequency:
    frequency = template.format(*letter)
    print(frequency)
