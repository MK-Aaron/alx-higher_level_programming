#!/usr/bin/python3
"""Module for class base"""
import json
import os


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

    @staticmethod
    def from_json_string(json_string):
        """Convert JSON string to dictionary
    
        Args:
            from_json_string (str): string representing a list of dictionaries
        """
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set

        Args:
            dictionary (dict): dictionary with key/value
        """
        instance = cls(1, 4)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        """
        path = cls.__name__ + ".json"
        if not os.path.exists(path):
            return []
        with open(path, encoding="utf-8") as f:
            json_dict_list = f.read()
        dict_list = cls.from_json_string(json_dict_list)
        instance_list = []
        for obj in dict_list:
            instance = cls.create(**obj)
            instance_list.append(instance)
        return instance_list
