#!/usr/bin/python3
"""Function that writes a string to

a text file"""

def write_file(filename="", text=""):
    """Writes a string to a text file"""

    with open(filename, "w", encoding="utf-8") as ptr:
        ptr.write(text)

    with open(filename, encoding="utf-8") as ptr:
        line = ptr.read()

    wordList = line.split()

    charCount = 0

    for word in wordList:
        for char in word:
            charCount += 1

    return charCount
