#!/usr/bin/python3
"""Defines append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing
        a specific string
    """
    with open(filename, "r+") as f_object:
        lines = f_object.readlines()
        changed = []
        for line in range(len(lines)):
            changed.append(lines[line])
            if search_string in lines[line]:
                changed.append(new_string)

        f_object.seek(0)
        f_object.write("".join(changed))
