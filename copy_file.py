#!/usr/bin/python3

import os
import shutil
import argparse


def main():
    parser = argparse.ArgumentParser(description='copy file')
    parser.add_argument('source', help='source file')
    parser.add_argument('-o', '--overwrite', type=bool, default=False, required=True, help='overwrite the file')
    parser.add_argument('destination', help='destination file')
    args = parser.parse_args()

    try:
        with open(args.source) as source:
            sourcePath = os.path.abspath(args.source)
    except:
        raise FileNotFoundError

    try:
        with open(args.destination) as destination:
            exists = True
            destPath = os.path.abspath(args.destination)

    except:
        try:
            destination = open(args.destination, 'w+')
            destPath = os.path.abspath(args.destination)
        except IsADirectoryError:
            try:
                with open(args.destination + f'/{source}', 'w+') as destination:
                    destPath = os.path.abspath(args.destination)
            except:
                with open(args.destination + source, 'w+') as destination:
                    destPath = os.path.abspath(args.destination)
            exists = False

    if args.overwrite:
        overwrite = True
    else:
        overwrite = False

    copyFile(sourcePath, overwrite, exists, destPath)


def copyFile(sourceFile, overwriteFile, fileExists, targetFile):
    if overwriteFile:
        shutil.copy2(sourceFile, targetFile)
    else:
        if not fileExists:
            shutil.copy2(sourceFile, targetFile)
        else:
            raise Exception('The file already exists.')


if __name__ == "__main__":
    main()
