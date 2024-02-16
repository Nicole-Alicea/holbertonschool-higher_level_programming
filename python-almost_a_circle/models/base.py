#!/usr/bin/python3
"""Creates a class that will be the 'base' of all other classes"""
import json


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
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of
            list_objs to a file
        """
        file_name = "{}.json".format(cls.__name__)

        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dict = []
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())
                jsonfile.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation
            json_string
        """
        if json_string is None or json_string is "[]":
            return []
        else:
            return json.loads(json_string)
