#!/usr/bin/python3
"""Module for class base"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string represenation

        Args:
            list_dictionaries (list[dict]): list of dictionaries
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string to a file

        Args:
            list_objs (list): list of instances that inherit from base
        """
        path = cls.__name__ + ".json"
        dict_list = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(dict_list)
        with open(path, "w", encoding="utf-8") as f:
            f.write(json_str)
