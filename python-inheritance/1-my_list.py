#!/usr/bin/python3
"""Creates a class named MyList"""


class MyList:
    """Class that inherits from list"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
