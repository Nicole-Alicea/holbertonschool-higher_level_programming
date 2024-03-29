#!/usr/bin/python3
"""Creates a class that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ inherits from Rectangle"""
    def __init__(self, size):
        if self.integer_validator('size', size):
            self.__size = size
        super().__init__(size, size)

    def area(self):
        return super().area()
