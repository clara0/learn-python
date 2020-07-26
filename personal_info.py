# reads file and separates lines into tuples


def readInfo(file):
    list1 = []
    tupleList = []
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

    finalList = sorted(tupleList, key=lambda x: x[-1])
    return finalList


fileHandle = open('/Users/clara/Downloads/dataJul-26-2020.csv')
people = readInfo(fileHandle)

print('Name\t\t\t\t\t\t\tEmail\t\t\t\t\t\t\t\tPhone\t\t\t\t\t\t\tZip Code')
for person in people:
    for i in person:
        if i == person[-1]:
            print(i[:20], end='\n')
        else:
            print(i[:20], end='\t\t\t\t\t\t')


