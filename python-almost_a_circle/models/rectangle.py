#!/usr/bin/python3
"""Creates a class that will inherit from the 'base' class"""
from models.base import Base


class Rectangle(Base):
    """Derived class with its attributes"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer1(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer1(value, "height")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer2(value, "x")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer2(value, "y")
        self.__y = value

    def validate_integer1(self, value, attribute_name):
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        if value <= 0:
            raise ValueError(f"{attribute_name} must be > 0")

    def validate_integer2(self, value, attribute_name):
        if not isinstance(value, int):
            raise TypeError(f"{attribut_name} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute_name} must be >= 0")
