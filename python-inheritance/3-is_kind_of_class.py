#!/usr/bin/python3
"""Creates a function"""


def is_kind_of_class(obj, a_class):
    """Will return True if the object is an instance of, or if the object
        is an instance of a class that inherited from, the specified class;
        otherwise False
    """
    return isinstance(obj, a_class)
