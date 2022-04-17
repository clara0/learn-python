#!/usr/bin/python3


def main():
    while True:
        userInput = input('Enter some DNA letters: ').strip().upper()
        try:
            if userInput != '':
                print(matchLetters(userInput))
        except:
            continue


def matchLetters(letters):
    pairList = []
    for letter in letters:
        if letter == 'A':
            pairList.append((letter, 'T'))
        elif letter == 'T':
            pairList.append((letter, 'A'))
        elif letter == 'G':
            pairList.append((letter, 'C'))
        elif letter == 'C':
            pairList.append((letter, 'G'))
        else:
            raise Exception('Enter a valid set of numbers')

    return pairList


if __name__ == '__main__':
    main()
