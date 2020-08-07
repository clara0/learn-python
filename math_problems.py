#!/usr/bin/python3

import random
import sys
from datetime import datetime
import time


minNum = 10
maxNum = 1000
totalQuestions = 20


def math():
    questions = 0
    wrong = 0
    correct = 0
    startTime = datetime.now()

    while questions < totalQuestions:
        operations = ('-', '+')
        op = random.choice(operations)
        nums = range(minNum, maxNum)
        num1 = random.choice(nums)
        num2 = random.choice(nums)
        if op == '+':
            answer = str(num1 + num2)
        elif op == '-':
            answer = str(num1 - num2)

        question = input(f'{num1} {op} {num2} = ').strip()
        if answer != question:
            wrong += 1
        else:
            correct += 1
        questions += 1

    endTime = datetime.now()

    timeTaken = endTime - startTime
    timePerQuestion = timeTaken / totalQuestions
    percentage = (correct / (correct + wrong)) * 100
    titles = ('\nCorrect', 'Wrong', 'Duration', 'Time per Question', 'Percentage')
    data = (correct, wrong, str(timeTaken), str(timePerQuestion), str(percentage) + '%')
    template = '{:<20}{:<20}{:<20}{:<20}{:<20}'

    header = template.format(*titles)
    print(header)

    row = template.format(*data)
    print(row)


def getHelp():
    return f'usage: {sys.argv[0]} [--min=<minimum-number>] [--max=<maximum-number>] [--count=<number-of-questions>]'


if len(sys.argv) > 4:
    raise Exception(getHelp())
elif len(sys.argv) != 1:
    for option in sys.argv[1:]:
        if '--min=' in option:
            value = option[6:]
            if value.isnumeric():
                minNum = int(value)
            else:
                raise Exception(getHelp())
        elif '--max=' in option:
            value = option[6:]
            if value.isnumeric():
                maxNum = int(value)
            else:
                raise Exception(getHelp())
        elif '--count=':
            value = option[8:]
            if value.isnumeric():
                totalQuestions = int(value)
            else:
                raise Exception(getHelp())

if maxNum < minNum:
    raise Exception(getHelp())

if totalQuestions <= 0:
    raise Exception(getHelp())


math()

