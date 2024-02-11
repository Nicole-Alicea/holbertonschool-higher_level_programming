#!/usr/bin/python3
"""This module define the function lookup"""


def lookup(obj):
    """Returns the list of available attribute and
        methods of an object
    """
    if obj:
        return list(dir(obj))
    else:
        return None
