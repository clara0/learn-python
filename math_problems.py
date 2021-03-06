#!/usr/bin/python3

import random
import argparse
from datetime import datetime


parser = argparse.ArgumentParser(description='Prints out math problems to answer')
parser.add_argument('-n', '--minimum', type=int, metavar='', default=10, help='Minimum number')
parser.add_argument('-m', '--maximum', type=int, metavar='', default=100, help='Maximum number')
parser.add_argument('-c', '--count', type=int, metavar='', default=20, help='Number of questions')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print quiet')
group.add_argument('-v', '--verbose', action='store_true', help='print verbose')
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

    if args.quiet:
        pass
    else:
        header = template.format(*titles)
        print(header)

        row = template.format(*data)
        print(row)


if __name__ == "__main__":
    math()
