

def main():
    combos = findAll(('1', '2', '3'), ('a', 'b', 'c'))
    print(combos)


def findAll(tuple1, tuple2):
    possibleCombos = []
    for char1 in tuple1:
        for char2 in tuple2:
            possibleCombos.append(char1 + char2)
            possibleCombos.append(char2 + char1)

    return set(possibleCombos)


if __name__ == "__main__":
    main()
