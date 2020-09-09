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


if __name__ == '__main__':
    while True:
        userInput = input('Enter three side lengths:').strip()
        sides = userInput.split()
        if len(sides) != 3:
            continue
        try:
            result = isTriangle(float(sides[0]), float(sides[1]), float(sides[2]))
            print(result)
        except:
            continue
