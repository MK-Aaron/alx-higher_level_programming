#!usr/bin/python3
"""The module is 10-square.py"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle.py').Rectangle

class Square(Rectangle):
    """A subclass of rectangle"""

    def __init__(self, size):
        """Initialize dimetions of the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns area of a square"""
        return self.__size ** 2
