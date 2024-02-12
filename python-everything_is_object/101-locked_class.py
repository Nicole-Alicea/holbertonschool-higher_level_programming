#!/usr/bin/python3
"""Creates a class that avoids dynmaically created attributes"""


class LockedClass():
    """ locked class """
    __slots__ = ['first_name']
