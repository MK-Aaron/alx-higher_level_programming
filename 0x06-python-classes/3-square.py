#!/usr/bin/python3
""" Area of a square"""

class Square:
    """ Square class """
    def __init__(self, size=0):
        """Intialize instance of square"""

        self.__size = size
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Get area of a square

        Returns:
            size * size
        """
        return self.__size * self.__size
