from urllib.request import urlopen
from matplotlib import pyplot as plt


def displayTable(url):
    data = urlopen(url)
    yearList = []
    floodList = []
    for line in data:
        elements = (line.decode('utf-8')).split(', ')
        if elements[0] != '"Year"':
            if int(elements[0]) <= 10:
                yearList.append(elements[0])
                floodList.append(elements[1])

    return plt.plot(yearList, floodList, marker='o', color='b')


plottedData = displayTable('https://people.sc.fsu.edu/~jburkardt/data/csv/nile.csv')
plt.title('Nile River Flood Data')
plt.xlabel('Year')
plt.ylabel('Flood Height')
plt.show()
