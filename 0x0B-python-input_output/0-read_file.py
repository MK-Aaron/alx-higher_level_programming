#!/usr/bin/python3
"""Function that reads a text file"""


def read_file(filename=""):
    """read contents of a file"""

    with open(filename, encoding="utf-8") as ptr:
        line = ptr.read()

    return print(line, end="")
