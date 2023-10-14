#!/usr/bin/python3
"""Module for class base"""


class Base:
    """The base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
