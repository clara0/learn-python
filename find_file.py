import os


def findFile(directory, file, recursive=False):
    fileOccurrences = []
    contents = os.listdir(directory)

    for element in contents:
        fullPath = os.path.join(directory, element)
        if os.path.isdir(fullPath):
            if recursive:
                fileOccurrences.extend(findFile(fullPath, file, recursive=True))
        else:
            if element == file:
                fileOccurrences.append(fullPath)

    return fileOccurrences


if __name__ == '__main__':
    result = findFile('/tmp', 'a.txt', recursive=False)
    print(result)