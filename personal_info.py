# reads file and separates lines into tuples


def readInfo(file):
    list1 = []
    tupleList = []
    secondTupleList = []
    finalList = []
    for line in file:
        if line.startswith('name,'):
            pass
        else:
            info = line.split(',')
            for i in info:
                i = i.strip()
                list1.append(i)

            info = tuple(list1)
            tupleList.append(info)
            list1.clear()

    for name, email, phone, zipCode in tupleList:
        secondTupleList.append((zipCode, name, email, phone))

    secondTupleList.sort()

    for zipCode, name, email, phone in secondTupleList:
        finalList.append((name, email, phone, zipCode))

    return finalList


fileHandle = open('/Users/clara/Downloads/dataJul-26-2020.csv')
people = readInfo(fileHandle)

for person in people:
    print(person)
