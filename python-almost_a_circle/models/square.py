#!/usr/bin/python3
"""Creates a class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class inheriting from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

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
        s = "[{}] ({}) {}/{} - {}".format(
            type(self).__name__, self.id, self.x, self.y, self.width)
        return s

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
