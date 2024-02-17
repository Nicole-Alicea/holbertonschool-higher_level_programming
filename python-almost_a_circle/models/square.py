#!/usr/bin/python3
"""Creates a class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class representing a square, inheriting from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
            Class constructor - Initializes a Square object

            Parameters:
            - size (int): The size of the square.
            - x (int): The x-coordinate of the square (default is 0).
            - y (int): The y-coordinate of the square (default is 0).
            - id: The identifier of the square (default is None).
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Returns a string representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """gets size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the same value for width and height"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            Updates the attributes of the square.

            Accepts either positional arguments or keyword arguments.

            If positional arguments are used:
            - First argument (optional): id
            - Second argument (optional): size
            - Third argument (optional): x
            - Fourth argument (optional): y

            If keyword arguments are used:
            - id (optional): The identifier of the square.
            - size (optional): The size of the square.
            - x (optional): The x-coordinate of the square.
            - y (optional): The y-coordinate of the square.
        """
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
        dict = {}
        dict["id"] = self.id
        dict["size"] = self.size
        dict["x"] = self.x
        dict["y"] = self.y
        return dict
