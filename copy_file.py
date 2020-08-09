#!/usr/bin/python3

import sys
options = ('-o', '--overwrite', '-h')


def copyFile(sourceFile, targetFile):
    arguments = sys.argv
    if arguments[1] in options:
        if arguments[1] != '-h':
            for line in sourceFile:
                targetFile.write(line)
        else:
            raise Exception(getHelp())
    else:
        if not fileExists:
            for line in sourceFile:
                targetFile.write(line)
        else:
            raise Exception('The target file already exists\n' + getHelp())


def getHelp():
    return f'usage: {sys.argv[0]} [-o | --overwrite] [-h] <source> <target>'


if __name__ == "__main__":
    try:
        source = open(sys.argv[(-1) - 1])
        if sys.argv[1] not in options:
            if len(sys.argv) != 3:
                raise Exception(getHelp())
    except:
        raise Exception(getHelp())

    try:
        destination = open(sys.argv[-1])
        fileExists = True
    except:
        try:
            destination = open(sys.argv[-1], 'w+')
            fileExists = False
        except IsADirectoryError:
            if sys.argv[-1].endswith('/'):
                path = sys.argv[-1] + sys.argv[(-1) - 1]
                try:
                    destination = open(path)
                    fileExists = True
                except:
                    destination = open(path, 'w+')
                    fileExists = False
            else:
                try:
                    path = sys.argv[-1] + '/' + sys.argv[(-1) - 1]
                    destination = open(path)
                    fileExists = True
                except:
                    path = sys.argv[-1] + '/' + sys.argv[(-1) - 1]
                    destination = open(path, 'w+')
                    fileExists = False

    copyFile(source, destination)
    source.close()
    destination.close()
