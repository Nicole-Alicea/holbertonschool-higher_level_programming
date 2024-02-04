#!/usr/bin/python3
"""This creates a class that defines a square"""


class Square:
    """Class that represents a square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if size == 0:
            print("")
        else:
            print(area)
