#!/usr/bin/python3

import random
import argparse
from datetime import datetime


parser = argparse.ArgumentParser(description='Prints out math problems to answer')
parser.add_argument('-n', '--minimum', type=int, metavar='', help='Minimum number')
parser.add_argument('-m', '--maximum', type=int, metavar='', help='Maximum number')
parser.add_argument('-c', '--count', type=int, metavar='', help='Number of questions')
args = parser.parse_args()


def math():
    minNumChosen = False
    maxNumChosen = False
    countChosen = False
    questionsDone = 0
    wrong = 0
    correct = 0
    startTime = datetime.now()

    if args.minimum:
        minNum = args.minimum
        minNumChosen = True
    if args.maximum:
        maxNum = args.maximum
        maxNumChosen = True
    if args.count:
        totalQuestions = args.count
        countChosen = True

    if not minNumChosen:
        minNum = 10
    if not maxNumChosen:
        maxNum = 1000
    if not countChosen:
        totalQuestions = 20

    while questionsDone < totalQuestions:
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
        questionsDone += 1

    endTime = datetime.now()

    timeTaken = endTime - startTime
    timePerQuestion = timeTaken / totalQuestions
    percentage = (correct / totalQuestions) * 100
    titles = ('\nCorrect', 'Wrong', 'Duration', 'Time per Question', 'Percentage')
    data = (correct, wrong, str(timeTaken), str(timePerQuestion), str(percentage) + '%')
    template = '{:<20}{:<20}{:<20}{:<20}{:<20}'

    header = template.format(*titles)
    print(header)

    row = template.format(*data)
    print(row)


math()
