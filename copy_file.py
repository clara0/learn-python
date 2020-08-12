#!/usr/bin/python3

import os
import shutil
import argparse


def copyFile(sourceFile, overwriteFile, fileExists, targetFile):
    if overwriteFile:
        shutil.copy2(sourceFile, targetFile)
    else:
        if not fileExists:
            shutil.copy2(sourceFile, targetFile)
        else:
            raise Exception('The file already exists.')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='copy file')
    parser.add_argument('source', help='source file')
    parser.add_argument('-o', '--overwrite', type=bool, default=False, required=True, help='overwrite the file')
    parser.add_argument('destination', help='destination file')
    args = parser.parse_args()

    try:
        source = open(args.source)
    except:
        raise FileNotFoundError

    try:
        destination = open(args.destination)
        exists = True
    except:
        try:
            destination = open(args.destination, 'w+')
        except IsADirectoryError:
            try:
                destination = open(args.destination + f'/{source}', 'w+')
            except:
                destination = open(args.destination + source, 'w+')
        exists = False

    sourcePath = os.path.abspath(args.source)
    destPath = os.path.abspath(args.destination)

    if args.overwrite:
        overwrite = True
    else:
        overwrite = False

    copyFile(sourcePath, overwrite, exists, destPath)
    source.close()
    destination.close()
