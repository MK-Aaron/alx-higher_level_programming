#!/usr/bin/python3
"""CLass that inherits"""


class MyList(list):
    """CLass  MyList sorts numbers"""
    def __init__(self):
        """initialize the object"""
        super().__init__()

    def print_sorted(self):
        """Sort the list"""
        print(sorted(self))
