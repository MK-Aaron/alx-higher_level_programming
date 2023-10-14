#!/usr/bin/python3
"""
Module is for a class representing Rectangle

"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """"Initial instance of a rectangle

        Args:
            width (int): width of a rectangle
            height (int): height of a rectangle
            x (int or optional): x value. Default is 0
            y (int or optional): y value. Default is 0
            id (int or None): id value. Default is None
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get width of a rectangle

        Returns:
            private width of a rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of a rectangle

        Args:
            value (int): size of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an interger")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height of rectangle

        Returns:
            Private height of a rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set height of a rectangle.

        Args:
            value (int): height of rectabgle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x of a rectangle

        Returns:
            private x of a rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """set x of a rectangle

        Args:
            value (int): value of x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y of a rectangle

        Returns:
            private y of a rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """set y of the rectangle

        Args:
            value (int): y of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns:
            Area of a rectangle - width * height
        """
        return self.__width * self.__height

    def display(self):
        """print in stdout the rectangle with character '#'
        """
        for i in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """
        Returns:
            String representation of the recatangle dimentions
        """
        xy = "{:d}/{:d}".format(self.x, self.y)
        wh = "{:d}/{:d}".format(self.width, self.height)
        return f"[Rectangle] ({self.id}) {xy} - {wh}"
