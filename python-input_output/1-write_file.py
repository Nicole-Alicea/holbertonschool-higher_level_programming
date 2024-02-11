#!/usr/bin/python3
"""Creates a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of
        characters written
    """
    with open(filename, 'w', encoding="utf-8") as f_obj:
        return f_obj.write(text)
