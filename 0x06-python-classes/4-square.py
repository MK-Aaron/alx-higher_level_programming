#!/usr/bin/python3
"""Class name square"""


class Square:
    """A square class"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Retrive the attributes"""
        return self.__size

    @size.setter
    def size(self, value):
        """modify the attribute vale"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """return the current square area"""
        return self.__size * self.__size
