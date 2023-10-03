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
        self.height = height
        self.width = width

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

    def area(self):
        """Returns area of the reectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return representation of a rectangle using '#'"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        loop = []
        for i in range(self.__height):
            [loop.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                loop.append("\n")
        return ("".join(loop))

    def __repr__(self):
        """return a string represantation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Sets the del behaviour of rectangle object"""
        print("Bye rectangle...")
