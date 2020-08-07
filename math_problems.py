import random
import sys


def math():
    generated = False
    correct = 0
    wrong = 0
    while correct < 20:
        if not generated:
            operations = [sys.argv[1], sys.argv[2]]
            op = random.choice(operations)
            nums = range(1, 101)
            num1 = random.choice(nums)
            num2 = random.choice(nums)
            generated = True
            if op == '+':
                answer = str(num1 + num2)
            elif op == '-':
                answer = str(num1 - num2)
            elif op == '*':
                answer = str(num1 * num2)
            elif op == '/':
                answer = str(num1 / num2)

        question = input(f'{num1} {op} {num2} = ').strip()
        if answer != question:
            wrong += 1
            continue
        else:
            # ready for the next round, reset generated flag to false
            correct += 1
            generated = False

    print(f'Correct\t\tWrong\t\tScore\t\tTotal Retries\n{correct}\t\t{wrong}\t\t\t{correct / (correct + wrong) * 100}%\t\t\t{wrong}')
