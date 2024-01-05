#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Class rectangle"""
    def __init__(self, width=0, height=0):
        """An instance in a class"""
        self.__width = width
        self.__height = height

    def width(self, value):
        """Get width value"""
        if width is None or type(width) not in [int]:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        return self.width

    def height(self, value):
        """Get height value"""
        if height is None or type(height) not in [int]:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        return self.height

    def __rpr__(self):
        """Returns dimentions of object"""
        return f"{self.height}, {self.width}"
