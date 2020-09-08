#!/usr/bin/python3


def isTriangle(side1, side2, side3):
    if (side1 + side2) < side3:
        triangle = False
    elif (side2 + side3) < side1:
        triangle = False
    elif (side1 + side3) < side2:
        triangle = False
    else:
        triangle = True

    return triangle


while True:
    userInput = input('Enter three side lengths:').strip()
    sides = [side for side in userInput.split()]
    if len(sides) != 3:
        continue
    try:
        result = isTriangle(int(sides[0]), int(sides[1]), int(sides[2]))
        print(result)
    except:
        continue
