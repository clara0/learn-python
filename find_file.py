import os


def findFile(directory, file, recursive=False):
    result = []
    contents = os.listdir(directory)

    for element in contents:
        fullPath = os.path.join(directory, element)
        if os.path.isdir(fullPath):
            result.extend(findFile(fullPath, file, recursive=True))
        else:
            if element == file:
                result.append(file)

    return result


if __name__ == '__main__':
    result = findFile('/tmp', 'a.txt', recursive=False)
    print(result)