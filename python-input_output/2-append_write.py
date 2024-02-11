#!/usr/bin/python3
"""Creates a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file and returns the number
        of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f_obj:
        return f_obj.write(text)
