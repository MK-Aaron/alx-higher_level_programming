#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Class rectangle"""
    def __init__(self, width=0, height=0):
        """An instance in a class"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Confirm width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Get height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Find area of the shape"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Finds perimeter of the shape"""
        if self.__height < 0 or self.__width < 0:
            return 0
        return (2 * (self.__height + self.__width))
