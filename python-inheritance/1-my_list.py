#!/usr/bin/python3
"""Creates a class named MyList"""


class MyList:
    """Class that inherits from list"""
    def print_sorted(self):
        one_shot = self.copy()
        one_shot.sort()
        print(one_shot)
