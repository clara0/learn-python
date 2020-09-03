#!/usr/bin/python3

from collections import Counter

template = '{:<10}{:<10}'
titles = ('Char', 'Count')

while True:
    sentence = input('Enter a sentence: ').strip()
    counts = Counter(sentence)
    print(template.format(*titles))
    for char in counts:
        charCount = (char, counts[char])
        print(template.format(*charCount))
