import os


def main():
    fileList = listFiles('/tmp/a', [], recursive=True)
    print(fileList)


def listFiles(directory, currentResult, recursive=False):
    contents = os.listdir(directory)

    if recursive:
        for subelement in contents:
            fullpath = os.path.join(directory, subelement)
            if os.path.isdir(fullpath):
                currentResult.append(listFiles(fullpath, [subelement], recursive=True))
            else:
                currentResult.append(subelement)
    else:
        for element in contents:
            currentResult.append(element)

    return currentResult


if __name__ == '__main__':
    main()
