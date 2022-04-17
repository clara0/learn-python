#!/usr/bin/python3


def main():
    while True:
        userInput = input('Enter an equation: ').strip()
        if userInput != '':
            result = matchBrackets(userInput)
            print(f'Are the brackets valid? {result}')


def matchBrackets(equation):
    firstBrackets = '{[(<'
    lastBrackets = '}])>'
    equationBrackets = []
    for i in equation:
        if i in firstBrackets:
            equationBrackets.append(i)
        if i in lastBrackets:
            try:
                if firstBrackets[lastBrackets.index(i)] != equationBrackets.pop():
                    return False
            except:
                return False

    if len(equationBrackets) == 0:
        return True
    return False


if __name__ == '__main__':
    main()
