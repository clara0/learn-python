from urllib.request import urlopen


def readFile(file_url):
    entireDataSet = []
    data = urlopen(file_url)
    for line in data:
        partialDataSet = []
        dataValues = (line.decode('utf-8')).split(',')
        for value in dataValues:
            partialDataSet.append(value.strip())

        entireDataSet.append(partialDataSet)

    return entireDataSet


url = "https://raw.githubusercontent.com/jberet/jberet-support/master/src/test/resources/movies-2012.csv"
result = readFile(url)

template = '{:<10}{:<50}{:<20}{:<15}'
titles = result[0]

header = template.format(*titles)
print(header + '\n' + ('-' * 95))

for movie in result[1:]:
    line = template.format(*movie)
    print(line)
