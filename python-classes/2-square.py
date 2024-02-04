#!/usr/bin/python3
"""This will create a class named square that defines a square."""


class Square:
    """Class that defines a square with a private instance attribute."""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
