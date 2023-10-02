#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """class Rectangle"""
    def __init__(self, width=0, height=0):
        """Intializing the rectangle

        Args:
            width (int): The width of the new rectangle
            height (int): Height of new rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get/set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Checks if value width is valid"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/Set height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Check if value width is valid"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
