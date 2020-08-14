import os
import shutil


def listFiles(directory, currentResult, recursive=False):
    contents = os.listdir(directory)

    if recursive:
        for subelement in contents:
            fullpath = os.path.join(directory, subelement)
            if os.path.isdir(fullpath):
                currentResult.append(listFiles(fullpath, [subelement]))
            else:
                currentResult.append(subelement)
    else:
        for element in contents:
            currentResult.append(element)

    return currentResult


if __name__ == '__main__':
    fileList = listFiles('/tmp/a', [], recursive=True)
    print(fileList)
