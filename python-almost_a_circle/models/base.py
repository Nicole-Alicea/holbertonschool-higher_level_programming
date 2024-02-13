#!/usr/bin/python3
"""Creates a class that will be the 'base' of all other classes"""


class Base:
    """Class with attributes and constructor"""
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
