#!/usr/bin/python3
"""
Model square inherits from rectangle

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class  square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Intialize the square

        Args:
            size (int): width or height are equal in a square
            x (int): x axis
            y (int): y axis
            id (list): identity of the square
        """
        super().__init__(id=id, width=size, height=size, x=x, y=y)

    def __str__(self):
        """returns the string representation of dimentions"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get size of Square.
        Returns:
            size of Square
        """
        return self.width

    @size.setter
    def size(self, value):
        """Set size of Square.
        Args:
           value (int): Size of size
        """
        self.width = value
        self.height = value

