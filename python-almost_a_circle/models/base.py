#!/usr/bin/python3
"""Creates a class that will be the 'base' of all other classes"""


class Base:
    """Class with attributes and constructor"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        self.id = id

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of
            list_dictionaries
        """
        if list_dictionaries == None or list_dictionaries == []:
            return '"[]"'
        return json.dumps(list_dictionaries)
