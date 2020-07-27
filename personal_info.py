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

title = ('Name', 'Email', 'Phone', 'Zip Code')
template = '{:<20}{:<50}{:<20}{:<10}'

x = template.format(*title)
print(x)

print('-' * 100)

for person in people:
    x = template.format(*person)
    print(x)




