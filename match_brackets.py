#!/usr/bin/python3


def matchBrackets(equation):
    firstBrackets = '{[(<'
    lastBrackets = '}])>'
    equationBrackets = []
    for i in equation:
        if i in firstBrackets:
            equationBrackets.append(i)
        if i in lastBrackets:
            try:
                if firstBrackets[lastBrackets.index(i)] == equationBrackets[-1]:
                    equationBrackets.pop()
                else:
                    return False
            except:
                return False

    if len(equationBrackets) == 0:
        return True
    return False


if __name__ == '__main__':
    while True:
        userInput = input('Enter an equation: ').strip()
        if userInput != '':
            result = matchBrackets(userInput)
            print(f'Are the brackets valid? {result}')
