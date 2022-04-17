#!/usr/bin/python3


def main():
    result = rosellaCode("test", "tets")
    print(result)


def rosellaCode(str1, str2):
    sameLetters = ""
    for char in str1:
        for char1 in str2:
            if char == char1:
                sameLetters += char
                str2 = str2[str2.find(char1):]
                break

    return sameLetters


if __name__ == '__main__':
    main()
