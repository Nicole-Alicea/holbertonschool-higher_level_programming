#!/usr/bin/python3
"""Creates a function"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited
        (directed or indirectly) from the specified class; otherwise False
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
