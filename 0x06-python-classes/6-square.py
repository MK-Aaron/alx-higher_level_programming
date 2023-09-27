#!/usr/bin/python3
"""Class square"""


class Square:
    """square class with a private attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize instance of square

        Args:
            size (int): Define size of square intialized to 0
            position(int, int): tuple of 2 positive intergers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get size of square

        Returns:
            Private size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set size of a square

        Args:
            Value (init): size of square
        """
        self.__size = value

        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """retrieve the attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """modify the attribute value"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Get area of a square

        Returns:
           the current area - size * size
        """
        return self.__size * self.__size

    def my_print(self):
        """Print in stdout the quare with character #

        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
