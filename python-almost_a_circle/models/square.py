#!/usr/bin/python3
"""Creates a class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class inheriting from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """gets size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the same value for width and height"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of Square"""
        s = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)
        return s
