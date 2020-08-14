import os


def listFiles2(directory, currentResult):
    for subelement in os.listdir(directory):
        fullpath = os.path.join(directory, subelement)
        if os.path.isdir(fullpath):
            currentResult.append(listFiles2(fullpath, [subelement]))
        else:
            currentResult.append(subelement)
    return currentResult


if __name__ == '__main__':
    fileList = listFiles2('/tmp', [])
    for i in fileList:
        print(i)
