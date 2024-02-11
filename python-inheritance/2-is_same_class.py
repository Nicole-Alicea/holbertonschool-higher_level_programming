#!/usr/bin/python3
"""Creates a function"""

def is_same_class(obj, a_class):
    """Will return True if object is exactly an instance of the
        specified class; otherwise False
    """
    return type(obj) is a_class
