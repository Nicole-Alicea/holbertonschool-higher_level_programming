#!/usr/bin/python3
"""Creates a class that defines a student"""


class Student:
    """Class with attributes and method"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        Student_dict = vars(self)
        wanted_data = {}
        if isinstance(attrs, list):
            for key in attrs:
                if isinstance(key, str) and key in Student_dict:
                    wanted_data[key] = Student_dict[key]
            return wanted_data
        return Student_dict
