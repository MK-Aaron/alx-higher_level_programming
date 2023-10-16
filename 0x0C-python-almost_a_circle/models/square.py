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

    def update(self, *args, **kwargs):
        """update the class square dimentions

        Args:
            args (list): list of arguements
            kwargs (dict): dictionary with key/value
        """
        up = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, up[i], args[i])
        else:
            for j in kwargs:
                setattr(self, j, kwargs[j])

    def to_dictionary(self):
        """Returns the dict representation of a square"""
        return {
                "id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y
            }
